testFile = open("c:/coding-projects/AdventOfCode24/Day 1/day1.txt", "r")

leftList = []
rightList = []

for line in testFile:
    splitLine = line.split()
    leftList.append(int(splitLine[0]))
    rightList.append(int(splitLine[1]))

