"""Grava characters/<nome>/model.svg a partir da saída de tools/engine-test.html."""
import html, re, sys, xml.dom.minidom

dom = open(sys.argv[1], encoding='utf-8', errors='replace').read()
root = sys.argv[2]
pre = re.search(r'<pre id="out">(.*?)</pre>', dom, re.S)
print(html.unescape(pre.group(1)) if pre else 'NO RESULT BLOCK')
for name in ['dan', 'mia', 'leo', 'bea', 'biscuit']:
    m = re.search(r'<textarea id="model-%s">(.*?)</textarea>' % name, dom, re.S)
    if not m:
        print('sem modelo', name)
        continue
    svg = html.unescape(m.group(1))
    head = ('<title>%s - modelo-base de Survive the Headline</title>'
            '<desc>Partes alternativas e acessorios existem com display=none. Cada parte tem id e data-part; '
            'data-pivot marca o ponto de articulacao. A animacao vem do rig em engine/rigs.</desc>' % name.capitalize())
    svg = re.sub(r'(<svg[^>]*>)', lambda g: g.group(1) + head, svg, count=1)
    svg = re.sub(r'><', '>\n<', svg)
    xml.dom.minidom.parseString(svg.encode('utf-8'))
    open('%s/characters/%s/model.svg' % (root, name), 'w', encoding='utf-8', newline='\n').write('<?xml version="1.0" encoding="UTF-8"?>\n' + svg + '\n')
    print('model', name, len(svg))
