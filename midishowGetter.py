#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @Date    : 2018-05-21 00:57:32
# @Author  : Xingfan Xia (xingfanxia@gmail.com)
# @Link    : http://xiax.ai
# @Version : 1.0
This script downloads midi song from midishow.com
Usage:
    python3 midishowGetter.py <url>
'''

import wget, sys, os
import requests, re
import cgi

outPath ="midishowDownloads/"

def parse_url(url):
    out = url.replace("/midi", "/midi/file")
    out = out.replace("html", "mid")
    return out

def main():
    url = parse_url(sys.argv[1])
    r = requests.get(url)
    con_disp = r.headers.get('Content-Disposition').encode('ISO-8859-1').decode('utf-8')
    v, p = cgi.parse_header(con_disp)
    fname = p['filename*'].replace("\'", "").replace('\"', "").replace("UTF-8", "")
    if not os.path.exists(outPath):
        os.mkdir(outPath)
    open(outPath+fname, "wb").write(r.content)
    print("{} downloaded!".format(fname))

if __name__ == '__main__':
    main()
