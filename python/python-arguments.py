#!/usr/bin/env python3

import sys

def usage():
    print(__file__ + ": script for demonstrating handling arguments in Python.")
    return True

print('You provided', len(sys.argv), 'arguments.')

print(sys.argv[0])
