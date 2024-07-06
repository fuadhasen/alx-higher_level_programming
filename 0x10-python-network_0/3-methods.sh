#!/bin/bash
#script to cURL only methods
curl -sI "$1" | grep -i "Allow: .*" | awk '{print $2}'
