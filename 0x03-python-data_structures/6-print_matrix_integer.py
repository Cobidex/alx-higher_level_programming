#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        n = 0
        for j in i:
            print("{:d}". format(j), end="")
            if n < (len(i) - 1):
                print(" ", end="")
            n = n + 1
        print()
