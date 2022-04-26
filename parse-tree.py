#!/usr/bin/env python3

import sys
import lxml.html


def find_subentries(entry, pkgname):
    xpath = f'../../../../tr[contains(@data-id, "{pkgname}-")]//a/text()'
    elements = entry.xpath(xpath)
    if elements:
        for element in elements:
            yield pkgname + '/' + element
    else:
        raise RuntimeError('find_subentries: no elements')


def parse_entry(entry):
    if entry.xpath('.//button'):
        vals = entry.xpath('.//span/text()')
        if not vals:
            vals = entry.xpath('.//a/text()')
            print(vals[0])
        if not vals:
            raise RuntimeError(entry)
        val = vals.pop()
        if vals:
            raise RuntimeError("len(vals) > 1, no button")
        yield from find_subentries(entry, val)
    else:
        vals = entry.xpath('.//a/text()')
#        print(entry.xpath('.//*/text()'))
        val = vals.pop()
        if vals:
            raise RuntimeError("len(vals) > 1, no button")
        yield val


def main():
    fname = sys.argv[1]
    try:
        with open(fname) as f:
            h = lxml.html.fromstring(f.read())

        XPATH = '//div [@class="UnitDirectories-pathCell"]/div [not(@class)]'
        for entry in h.xpath(XPATH):
            for pkgname in parse_entry(entry):
                print(pkgname)
    except:
        sys.stderr.write('filename was: ' + fname + '\n')
        raise


if __name__ == '__main__':
    main()
