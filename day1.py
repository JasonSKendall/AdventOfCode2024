#!python
# https://adventofcode.com/2024/day/1
import re

numr = []
numl = []

with open('/Users/jasonkendall/Desktop/Advent_of_code/day1_input.txt' , mode='r') as fhand:
    for rawline in fhand:
        current_line = rawline.rstrip()
        #print(current_line)
        values = current_line.split("   ")
        #print(f"{values[0]} { values[1]}")
        numl.append(int(values[0]))
        numr.append(int(values[1]))

numlsort = sorted(numl)
numrsort = sorted(numr)
runsum = 0

for i, item in enumerate(numlsort):
	thing = abs(item - numrsort[i])
	runsum += thing
	print(f"{i} {item} {numrsort[i]} {thing} {runsum}")
	
