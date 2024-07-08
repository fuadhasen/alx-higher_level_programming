#!/usr/bin/python3
""" python script that manage HTTPError """

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib import parse

if __name__ == "__main__":
    req = Request(sys.argv[1])

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
