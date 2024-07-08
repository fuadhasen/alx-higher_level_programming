#!/usr/bin/python3
"""python script that print Error_code using requests package """

import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
