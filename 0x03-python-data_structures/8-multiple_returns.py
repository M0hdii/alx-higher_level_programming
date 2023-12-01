#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        first = None
        tup = len(sentence), first
        return tup

    tup = len(sentence), sentence[0]
    return tup
