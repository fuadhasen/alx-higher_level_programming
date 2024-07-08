#!/usr/bin/python3
""" python script that fetch url """

from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        content = response.read()

    print("Body response:")
    print("\t- type: {}".format(content.__class__))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode(encoding='utf-8')))
