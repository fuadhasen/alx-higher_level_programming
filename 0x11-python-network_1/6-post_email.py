#!/usr/bin/python3
"""python script POST email using requests package """

import sys
import requests

if __name__ == "__main__":
    data = {'email': sys.argv[2])
    res = requests.post(sys.argv[1], data=data)
    print(res.text)
