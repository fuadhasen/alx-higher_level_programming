#!/usr/bin/python3
"""python script search api using requests package """

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}
    res = requests.post('http://0.0.0.0:5000/search_user', data=data)
    if res.headers['Content-Type'] == 'application/json':
        # parse the json response and return python dict
        response = res.json()
        if response:
            # check empty json or not
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
