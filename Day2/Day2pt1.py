testFile = open("c:/coding-projects/AdventOfCode24/Day2/day2.txt", "r")

for line in testFile:
    seperatedLine = line.split()
    numArray = list(map(int, seperatedLine))
    
    i = 0

    while i < len(numArray):
        if numArray[i] < numArray[i+1]:
            print("true asc")
        elif numArray[i] > numArray[i+1]:
            print("true desc")
        else:
            print("false")
        i += 1
        
    