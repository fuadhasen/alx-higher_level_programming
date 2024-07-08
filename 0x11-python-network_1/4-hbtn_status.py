#!/usr/bin/python3
"""python script fetch url using requests package """

import requests

if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
