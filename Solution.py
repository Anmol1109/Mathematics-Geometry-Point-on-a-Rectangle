#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    px, py = zip(*coordinates)
    x0 = min(px)
    x1 = max(px)
    y0 = min(py)
    y1 = max(py)
    result = all(x in (x0, x1) or y in(y0,y1) for x,y in coordinates)
    if result:
        return "YES"
    else:
        return "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        coordinates = []

        for _ in range(n):
            coordinates.append(list(map(int, input().rstrip().split())))

        result = solve(coordinates)

        fptr.write(result + '\n')

    fptr.close()
