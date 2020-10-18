# This is a Python solution for the Minion problem I got on foo.bar form google.

# !/bin/python

import math
import os
import random
import re
import sys
from itertools import permutations

# Complete the solve function below.
from pip._vendor.distlib.compat import raw_input

def solution(data,n):
    # Your code here
    if (len(data)<=100):
        current = 0
        duplicate_count = -1
        item_dict = {}
        final_list = data.copy()
        k = 0
        #print(data)
        while current < len(data):
            for item in data:
                if data[current] == item :
                    duplicate_count += 1
                    if duplicate_count >= 0:
                        item_dict[data[current]] = duplicate_count+1
            duplicate_count = -1
            current += 1
        #print(item_dict)
        for x, y in item_dict.items():
            if y > int(n) :
                while k < y:
                    data.remove(x)
                    k += 1
                k = 0
        return data
    else:
        print("Too Many Tasks!")








if __name__ == '__main__':
    print(solution([5, 10, 15, 10, 7],1))
    print(solution([1, 2, 3], 0))
    print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))
    print(solution([1,3,1,3,2,9,9,2,5,5],6))