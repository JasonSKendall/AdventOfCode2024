#!python
# https://adventofcode.com/2024/day/2
# https://adventofcode.com/2024/day/2/input
import re

def monoup(vals):
    for i in range(1, len(vals)):
        if vals[i] < vals[i - 1]:
            return False
    return True

def monodn(vals):
    for i in range(1, len(vals)):
        if vals[i] > vals[i - 1]:
            return False
    return True

def allinit(vals):
    return all(i in (-1, -2, -3, 3, 2, 1) for i in vals)

with open('/Users/jasonkendall/Desktop/input.txt' , mode='r') as fhand:
    for rawline in fhand:
        current_line = rawline.rstrip()
        #print(current_line)
        values = current_line.split(" ")

        intvals = [int(x) for x in values]
        vals = []
        
        for i in range(1, len(intvals)):
            curdiff = intvals[i] - intvals[i-1]
            vals.append(curdiff)

        if allinit(vals):
            if monodn(intvals):
                print(vals)
            if monoup(intvals):
                print(vals)
