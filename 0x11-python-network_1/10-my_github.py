#!/usr/bin/python3
"""python script search my github api using requests package """

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    usr_name = sys.argv[1]
    usr_token = sys.argv[2]
    auth = HTTPBasicAuth(usr_name, usr_token)
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    res = requests.get('https://api.github.com/user', auth=auth, headers=headers)
    # parse the json response and return python dict
    response = res.json()
    print("{}".format(response.get('id')))
