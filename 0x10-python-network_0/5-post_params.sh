#!/bin/bash
# script to cURL post
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
