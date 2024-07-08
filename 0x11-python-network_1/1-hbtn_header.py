#!/usr/bin/python3
""" python script that fetch url  header"""

from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    req = Request(sys.argv[1])
    with urlopen(req) as response:
        header_value = response.getheader('X-Request-Id')
    print(header_value)

