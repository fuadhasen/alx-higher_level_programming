#!/bin/bash
#script to cURL only methods
curl -sI -X OPTIONS "$1" | grep 'Allow' | cut -d ' ' -f 2-
