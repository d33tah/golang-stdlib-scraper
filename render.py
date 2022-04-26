#!/usr/bin/env python3

import sys

import lxml.etree
import lxml.html

fname = sys.argv[1]
try:
    modname = fname.split('/')[-1].replace('_', '/')
    with open(fname) as f:
        orig = f.read()
        if not orig.strip():
            sys.exit()
        raw = orig.replace((' ' * 6) + 'Documentation',
                          f'Documentation for {modname}')
        if orig == raw:
            raise RuntimeError('Documentation header not fixed!')
        h = lxml.html.fromstring(raw)

    docs = h.xpath('//div [@data-test-id="UnitDetails-content"]').pop()
    html = lxml.etree.tostring(docs).decode()
    print(html)
except:
    sys.stderr.write(f'filename was: {fname}\n')
    raise
