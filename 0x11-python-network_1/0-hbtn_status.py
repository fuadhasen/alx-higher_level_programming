#!/usr/bin/python3
""" python script that fetch url """

import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        content = response.read()

    utf8_content = content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(content.__class__))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(utf8_content))
