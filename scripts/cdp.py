#!/usr/bin/env python3
"""Abre una ruta del curso en Chrome por CDP y evalúa una expresión JS, o la captura.

Existe porque las comprobaciones de la revisión final (cobertura de textos, geometría de los
botones, animaciones de la portada) necesitan leer el DOM YA renderizado, y hacerlo a mano en
el scratchpad significa perderlas en cuanto la sesión se limpia.

Dos cosas que salieron de fallos reales y están resueltas aquí dentro:

- **AOS deja un `transform` puesto hasta que anima**: sin forzar `aos-animate` la captura sale
  con los bloques a medio opacar y se acaba revisando un render que el usuario nunca ve.
- **`captureBeyondViewport` no pinta el contenido de un `overflow:hidden` posicionado por
  transform**: el slider salía vacío y parecía un fallo de maqueta. Para eso está `--zona`,
  que captura con la ventana normal desplazada al elemento.

Uso:
  cdp.py <ruta> --eval "<expresión JS>"          # imprime el valor, entero
  cdp.py <ruta> --captura salida.png [--ancho N]
  cdp.py <ruta> --zona <selector> salida.png
"""
import base64
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request

import websocket  # noqa: E402

import config as C  # noqa: E402

PUERTO_CDP = 9350


def base_url():
    m = re.search(r"base:.*?'(/[^']+/)'", open(f'{C.ENTREGABLE}/vite.config.js').read())
    ruta = m.group(1) if m else '/'
    puertos = ([int(os.environ['VITE_PORT'])] if os.environ.get('VITE_PORT') else []) + \
        list(range(5173, 5200))
    for p in puertos:
        try:
            url = f'http://localhost:{p}{ruta}'
            urllib.request.urlopen(url, timeout=1).read(1)
            return url
        except Exception:
            continue
    raise SystemExit('no hay servidor de vite escuchando')


def abre(ruta, ancho=1600, alto=1200):
    """El router va por HASH: sin el `#/` delante se sirve siempre la portada."""
    destino = base_url() + (f'#/{ruta.lstrip("/")}' if ruta else '')
    perfil = f'/tmp/cdp-perfil-{os.getpid()}'
    shutil.rmtree(perfil, ignore_errors=True)
    proc = subprocess.Popen(
        ['google-chrome', '--headless=new', '--disable-gpu', '--hide-scrollbars',
         f'--remote-debugging-port={PUERTO_CDP}', '--remote-allow-origins=*',
         f'--user-data-dir={perfil}', f'--window-size={ancho},{alto}', destino],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    ws_url = None
    for _ in range(120):
        try:
            for t in json.load(urllib.request.urlopen(f'http://localhost:{PUERTO_CDP}/json')):
                if t['type'] == 'page' and 'localhost' in t['url']:
                    ws_url = t['webSocketDebuggerUrl']
            if ws_url:
                break
        except Exception:
            pass
        time.sleep(0.25)
    if not ws_url:
        proc.terminate()
        raise SystemExit('Chrome no respondió por CDP')
    ws = websocket.create_connection(ws_url, timeout=120)
    n = [0]

    def cmd(metodo, params=None):
        n[0] += 1
        ws.send(json.dumps({'id': n[0], 'method': metodo, 'params': params or {}}))
        while True:
            m = json.loads(ws.recv())
            if m.get('id') == n[0]:
                return m
    time.sleep(4)
    cmd('Runtime.evaluate', {'expression': """
document.querySelectorAll('[data-aos]').forEach(e => {
  e.classList.add('aos-animate'); e.style.transform = 'none'; e.style.opacity = '1';
}); 'ok'"""})
    time.sleep(1)
    return proc, ws, cmd


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else ''
    ancho = int(sys.argv[sys.argv.index('--ancho') + 1]) if '--ancho' in sys.argv else 1600
    proc, ws, cmd = abre(ruta, ancho)
    try:
        if '--eval' in sys.argv:
            expr = sys.argv[sys.argv.index('--eval') + 1]
            r = cmd('Runtime.evaluate', {'expression': expr, 'returnByValue': True})
            print(json.dumps(r['result'].get('result', {}).get('value'), ensure_ascii=False))
        elif '--zona' in sys.argv:
            i = sys.argv.index('--zona')
            sel, salida = sys.argv[i + 1], sys.argv[i + 2]
            cmd('Runtime.evaluate', {'expression':
                f"document.querySelector('{sel}').scrollIntoView({{block:'center'}}); 'ok'"})
            time.sleep(1.5)
            r = cmd('Page.captureScreenshot', {})
            open(salida, 'wb').write(base64.b64decode(r['result']['data']))
            print(salida)
        elif '--captura' in sys.argv:
            salida = sys.argv[sys.argv.index('--captura') + 1]
            alto = cmd('Runtime.evaluate',
                       {'expression': 'document.documentElement.scrollHeight'})['result']['result']['value']
            cmd('Emulation.setDeviceMetricsOverride',
                {'width': ancho, 'height': min(alto, 30000), 'deviceScaleFactor': 1, 'mobile': False})
            # Los sliders miden sus diapositivas al montar: si se redimensiona y nadie avisa,
            # se quedan posicionadas fuera y la captura sale con la tarjeta vacía.
            cmd('Runtime.evaluate', {'expression': "window.dispatchEvent(new Event('resize')); 'ok'"})
            time.sleep(2)
            r = cmd('Page.captureScreenshot', {'captureBeyondViewport': True})
            open(salida, 'wb').write(base64.b64decode(r['result']['data']))
            print(salida, alto)
    finally:
        ws.close()
        proc.terminate()


if __name__ == '__main__':
    main()
