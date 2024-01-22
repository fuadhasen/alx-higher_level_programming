#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        first = None
    else:
        first = sentence[:1]
    tuples = len(sentence), first
    return tuples
