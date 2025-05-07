#!/usr/bin/python3
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # ESTA línea es la importante
    return result

import sys
f = factorial(int(sys.argv[1]))
print(f)
