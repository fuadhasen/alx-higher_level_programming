#!/usr/bin/python3
""" python script that fetch url """

import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        content = response.read()

    print("Body response:")
    print("\t- type: {}".format(content.__class__))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode(encoding='utf-8')))
