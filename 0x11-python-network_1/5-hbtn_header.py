#!/usr/bin/python3
"""python script that fetch header using requests package """

import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
