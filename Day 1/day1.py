import math

testFile = open("c:/coding-projects/AdventOfCode24/Day 1/day1.txt", "r")

leftList = []
rightList = []
total = 0
i = 0

for line in testFile:
    splitLine = line.split()
    leftList.append(int(splitLine[0]))
    rightList.append(int(splitLine[1]))

leftList.sort()
rightList.sort()



for num in leftList:
    total += abs(num - rightList[i])
    i += 1

print(total)