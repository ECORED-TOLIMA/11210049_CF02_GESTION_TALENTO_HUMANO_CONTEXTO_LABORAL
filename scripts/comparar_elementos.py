#!/usr/bin/env python3
"""Compara ELEMENTO A ELEMENTO mi render contra los rects del artboard: color, ancho y alto.

Por qué no basta `comparar_bloques.py`: aquel mide franjas horizontales de ancho completo y en
estas pantallas casi todo es una tarjeta blanca con cajas de color de 916 o 1020 px dentro. El
color dominante de la franja sigue siendo el blanco, así que colapsa la pantalla en una sola
banda y no ve ni una caja. Esto va al revés: coge cada caja con fondo del render y busca en el
XD un rect del MISMO color y ancho parecido.

Qué reporta, por pantalla:
  1. COLORES INVENTADOS  -> un `background-color` del render que no existe como `fill` en el .xd
  2. ANCHOS SIN PAREJA   -> una caja cuyo color sí está en el XD, pero con un ancho que no
                            corresponde a ningún rect de ese color (fuera de tolerancia)
  3. RECTS SIN MAQUETAR  -> un rect del XD de tamaño relevante que no tiene ninguna caja del
                            mismo color y ancho en el render

Los anchos del render se normalizan al ancho de la tarjeta del XD (1328) antes de comparar, que
es lo que hace comparables las dos medidas sin depender del viewport.

Uso:  comparar_elementos.py <ruta> <prefijo_artboard> [--tol 12] [--min 60]
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config as C  # noqa: E402

RUTA = sys.argv[1]
ARTBOARD = sys.argv[2]
TOL = int(sys.argv[sys.argv.index('--tol') + 1]) if '--tol' in sys.argv else 12
MIN = int(sys.argv[sys.argv.index('--min') + 1]) if '--min' in sys.argv else 60
ANCHO_XD = 1328.0


def base_url():
    m = re.search(r"base:.*?'(/[^']+/)'", open(f'{C.ENTREGABLE}/vite.config.js').read())
    ruta = m.group(1) if m else '/'
    # El puerto NO se escribe a fuego: `npm run serve -- --port N` es habitual cuando hay
    # otro curso levantado, y con la lista corta la herramienta abortaba con «no hay servidor»
    # o, peor, medía el curso equivocado. Se respeta `$VITE_PORT` y se barre un rango amplio.
    puertos = ([int(os.environ['VITE_PORT'])] if os.environ.get('VITE_PORT') else []) + \
        list(range(5173, 5200))
    for puerto in puertos:
        try:
            url = f'http://localhost:{puerto}{ruta}'
            urllib.request.urlopen(url, timeout=1).read(1)
            return url
        except Exception:
            continue
    raise SystemExit('no hay servidor de vite escuchando')


def rects_xd():
    """Los rects del artboard: (hex, ancho, alto). Reutiliza el mapa de bloques."""
    ent = dict(os.environ)
    m = json.load(open(f'{C.ENTREGABLE}/docs/mapa-artboards.json'))
    fila = next(f for f in m if f['id'].startswith(ARTBOARD[:8]))
    ent['XD_DX'], ent['XD_DY'] = str(fila['dx']), str(fila['dy'])
    out = subprocess.run(['python3', f'{os.path.dirname(os.path.abspath(__file__))}/mapa_bloques.py',
                          ARTBOARD], capture_output=True, text=True, env=ent).stdout
    # formato de `mapa_bloques.py`:  (  185,   413)   916x140    rect fill=solid #FEDDB4 ...
    rects = []
    for ln in out.splitlines():
        mm = re.search(r'\)\s+(\d+)x(\d+)\s+.*?fill=solid\s+(#[0-9A-Fa-f]{6})', ln)
        if mm:
            rects.append((mm.group(3).upper(), int(mm.group(1)), int(mm.group(2))))
    return rects


def cajas_render():
    import websocket
    proc = subprocess.Popen(['google-chrome', '--headless', '--disable-gpu', '--hide-scrollbars',
                             '--remote-debugging-port=9337', '--window-size=1600,1200',
                             base_url() + '#/' + RUTA],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(40):
            try:
                tg = [t for t in json.loads(urllib.request.urlopen(
                    'http://localhost:9337/json', timeout=1).read()) if t['type'] == 'page']
                if tg:
                    break
            except Exception:
                pass
            time.sleep(0.5)
        ws = websocket.create_connection(tg[0]['webSocketDebuggerUrl'], suppress_origin=True,
                                         timeout=60)
        i = [0]

        def ev(e):
            i[0] += 1
            ws.send(json.dumps({'id': i[0], 'method': 'Runtime.evaluate',
                                'params': {'expression': e, 'returnByValue': True}}))
            while True:
                m = json.loads(ws.recv())
                if m.get('id') == i[0]:
                    return m['result'].get('result', {}).get('value')
        time.sleep(6)
        ev("document.querySelectorAll('[data-aos]').forEach(e=>{e.classList.add('aos-animate');"
           "e.style.transform='none';e.style.opacity=1})")
        time.sleep(1)
        return json.loads(ev(r'''(()=>{
          const card=document.querySelector('.container.tarjeta');
          if(!card) return '[]';
          const esc = 1328 / card.getBoundingClientRect().width;
          const hex = c => { const m=c.match(/\d+/g); return m&&m.length>=3 && (m[3]===undefined||+m[3]>0.05)
              ? '#'+[0,1,2].map(i=>(+m[i]).toString(16).padStart(2,'0')).join('').toUpperCase() : null };
          const out=[];
          [card, ...card.querySelectorAll('*')].forEach(e=>{
            const cs=getComputedStyle(e), b=e.getBoundingClientRect();
            if(b.width<10||b.height<6) return;
            const h=hex(cs.backgroundColor);
            if(h) out.push({hex:h, w:Math.round(b.width*esc), h:Math.round(b.height*esc),
                            cls:String(e.getAttribute('class')||'').slice(0,38)});
          });
          return JSON.stringify(out)})()''') or '[]')
    finally:
        proc.terminate()


def main():
    xd = rects_xd()
    porhex = {}
    for h, w, al in xd:
        porhex.setdefault(h, []).append((w, al))
    cajas = cajas_render()

    # ⚠️ Sin esto la herramienta MIENTE. Con una ruta que no existe el router pinta la portada,
    # no hay ninguna caja que medir y los tres apartados salen «ninguno»: un visto bueno de una
    # medición que no midió nada. Pasó al cerrar CF01 —se invocó `tema-1` cuando la ruta es
    # `curso/tema1`— y las cuatro pantallas dieron limpio con 0 cajas.
    if not cajas:
        print(f'=== {RUTA or "portada"}  ·  artboard {ARTBOARD}')
        print('\n  ❌ CERO cajas con fondo en el render: no se ha medido NADA.')
        print(f'     Comprueba que la ruta «{RUTA}» existe en src/router/index.js (los temas '
              'cuelgan de /curso: `curso/tema1`, no `tema-1`) y que el servidor está levantado.')
        sys.exit(2)

    inventados, sin_pareja, usados = {}, [], set()
    for c in cajas:
        if c['w'] < MIN:
            continue
        anchos = porhex.get(c['hex'])
        if anchos is None:
            inventados.setdefault(c['hex'], []).append(c)
            continue
        par = [a for a in anchos if abs(a[0] - c['w']) <= TOL]
        if par:
            usados.add((c['hex'], par[0][0]))
        else:
            sin_pareja.append((c, sorted({a[0] for a in anchos})))

    print(f'=== {RUTA or "portada"}  ·  artboard {ARTBOARD}')
    print(f'  rects del XD: {len(xd)}   ·   cajas con fondo en el render: {len(cajas)}')

    print('\n  1. COLORES QUE NO ESTAN EN EL XD')
    if inventados:
        for h, cs in sorted(inventados.items()):
            print(f'     {h}  x{len(cs)}   p.ej. {cs[0]["w"]}x{cs[0]["h"]}  .{cs[0]["cls"]}')
    else:
        print('     ninguno')

    print('\n  2. ANCHOS SIN PAREJA EN EL XD (mismo color, ancho distinto)')
    if sin_pareja:
        for c, anchos in sin_pareja[:14]:
            print(f'     {c["hex"]}  render {c["w"]}   XD {anchos}   .{c["cls"]}')
        if len(sin_pareja) > 14:
            print(f'     ... y {len(sin_pareja)-14} mas')
    else:
        print('     ninguno')

    print('\n  3. RECTS DEL XD SIN NINGUNA CAJA EQUIVALENTE')
    # Fuera: lo que no cabe en la tarjeta (sombras del pasteboard que se salen del artboard)
    # y la barra superior de 1600, que es el header de la plantilla y no parte de la tarjeta.
    faltan = [(h, w, al) for h, w, al in xd
              if 240 <= w <= 1340 and al >= 40 and not any(
                  abs(w - uw) <= TOL for uh, uw in usados if uh == h)]
    vistos = set()
    faltan = [f for f in faltan if not (f[:2] in vistos or vistos.add(f[:2]))]
    if faltan:
        for h, w, al in faltan[:14]:
            print(f'     {h}  {w}x{al}')
        if len(faltan) > 14:
            print(f'     ... y {len(faltan)-14} mas')
    else:
        print('     ninguno')


main()
