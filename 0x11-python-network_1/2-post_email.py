#!/usr/bin/python3
""" python script that post an email """

from urllib.request import Request, urlopen
from urllib import parse
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = Request(sys.argv[1], data=data)

    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
