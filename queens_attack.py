#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(bn, obs, qr, qc, arr):
    arr[qr-1][qc-1] = 7
    #right
    for i in range(bn):
        m = qr - 1
        n = qc + i
        if n == bn:
            break
        elif arr[m][n] == 2:
            break
        arr[m][n] = 1

    #right-down
    for i in range(bn):
        m = qr + i
        n = qc + i
        if n == bn or m == bn:
            break
        elif arr[m][n] == 2:
            break
        arr[m][n] = 1

    #down
    for i in range(bn):
        m = qr + i
        n = qc - 1
        if m == bn:
            break
        elif arr[m][n] == 2:
            break
        arr[m][n] = 1

    #down-left
    for i in range(bn):
        m = qr + i
        n = qc - i - 2
        if n == -1 or m == bn:
            break
        elif arr[m][n] == 2:
            break
        arr[m][n] = 1

    #left
    for i in range(bn):
        m = qr - 1
        n = qc - i - 2
        if n == -1:
            break
        elif arr[m][n] == 2:
            break
        arr[m][n] = 1
  
    #up-left
    for i in range(bn):
        m = qr - i - 2
        n = qc - i - 2
        if n == -1 or m == -1:
            break
        elif arr[m][n] == 2:
            break
        arr[m][n] = 1
  
    #up
    for i in range(bn):
        m = qr - i - 2
        n = qc - 1
        if m == -1:
            break
        elif arr[m][n] == 2:
            break
        arr[m][n] = 1

    #up-right
    for i in range(bn):
        m = qr - i - 2
        n = qc + i
        if m == -1 or n == bn:
            break
        elif arr[m][n] == 2:
            break
        arr[m][n] = 1

    count=0

    for i in range(bn):
        for j in range(bn):
            if arr[i][j] == 1:
                count += 1
      
    return(count)

if __name__ == '__main__':
    bn= int(input("Board length: "))
    obs= int(input("Obstacle amount: "))

    arr = [[0 for x in range(bn)] for y in range(bn)]

    qr = int(input("Queen's row: "))
    qc = int(input("Queen's column: "))

    for i in range(obs):
        k1 = int(input("Obstacle row: "))
        k2 = int(input("Obstacle column: "))
        arr[k1-1][k2-1] = 2

    

    result = queensAttack(bn, obs, qr, qc, arr)

    print(result)




