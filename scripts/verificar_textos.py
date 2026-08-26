#!/usr/bin/env python3
"""Punto 2 de la revisión final: que TODOS los textos del artboard estén en la página.

No basta con que la pantalla «se parezca»: el modo de fallo real es saltarse un bloque entero
—un slider, una lista— y no enterarse, porque lo que falta no deja hueco visible. Esta
comprobación lo caza contando.

Lo que NO cuenta como falta, y por qué:
  · el rótulo de plantilla del XD («Manual de Componentes…»), que no es contenido del curso;
  · los textos que van DENTRO de una figura (son parte de la imagen);
  · los de una pestaña o un acordeón cerrados, que `innerText` no ve.
Por eso imprime lo que falta, uno a uno: el número solo no decide nada.

Uso: verificar_textos.py            (todas las pantallas del mapa)
     verificar_textos.py <ruta> <artboard>
"""
import glob
import json
import os
import re
import subprocess
import sys
import unicodedata

import config as C

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
RUTAS = [('introduccion', 'Introduccion'), ('curso/tema1', 'Tema 1'), ('curso/tema2', 'Tema 2'),
         ('curso/tema3', 'Tema 3'), ('curso/tema4', 'Tema 4')]


def norm(s):
    s = unicodedata.normalize('NFKD', s)
    return re.sub(r'[^a-z0-9]', '', s.lower())


def textos_xd(ab):
    d = json.load(open(glob.glob(
        f'{C.XDDIR}/artwork/artboard-{ab}*/graphics/graphicContent.agc')[0], encoding='utf8'))
    fuera = []

    def walk(n):
        if n.get('type') == 'text':
            for t in ((n.get('text') or {}).get('rawText', '') or '').split('\n'):
                if len(t.strip()) > 25:
                    fuera.append(t.strip())
        for c in (n.get('children') or (n.get('group') or {}).get('children') or []):
            walk(c)
    walk(d['children'][0]['artboard'])
    return fuera


def revisa(ruta, ab):
    xd = textos_xd(ab)
    out = subprocess.run(
        ['python3', os.path.join(SCRIPTS, 'cdp.py'), ruta, '--eval',
         "document.querySelector('.curso-main-container').innerText"],
        capture_output=True, text=True, cwd=SCRIPTS).stdout
    pagina = norm(out)
    if not pagina:
        print(f'  ❌ {ruta}: la página no devolvió NADA de texto — no se ha medido nada')
        return 1
    faltan = [t for t in xd if norm(t)[:45] not in pagina]
    print(f'  {ruta}: {len(xd) - len(faltan)}/{len(xd)} textos del artboard en la página')
    for t in faltan:
        print(f'     falta: {t[:95]!r}')
    return len(faltan)


if __name__ == '__main__':
    mapa = {f['nombre']: f['id'][:8] for f in json.load(open(f'{C.ENTREGABLE}/docs/mapa-artboards.json'))}
    if len(sys.argv) > 2:
        revisa(sys.argv[1], sys.argv[2])
    else:
        for ruta, nombre in RUTAS:
            revisa(ruta, mapa[nombre])
