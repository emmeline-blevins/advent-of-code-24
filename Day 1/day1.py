import os

print("Advent of Code 2024 - Day 1")

leftlist = []
rightlist = []

with open(os.getcwd() + "\\Day 1\\input1.txt", "r") as input:
    for line in input:
        lr = line.split()
        leftlist = leftlist + [int(lr[0])]
        rightlist = rightlist + [int(lr[1])]

leftlist.sort()
rightlist.sort()

diffsum = 0
for i in range(len(leftlist)):
    diffsum = diffsum + abs(leftlist[i] - rightlist[i])

print("Part 1:", diffsum)

l = 0
r = 0

simsum = 0
counter = 0

while(l < len(leftlist) and r < len(rightlist)):
    if (leftlist[l] == rightlist[r]):
        counter = counter + 1
        r = r + 1
    elif (rightlist[r] > leftlist[l]):
        simsum = simsum + (counter * leftlist[l])
        counter = 0
        l = l + 1
    elif (leftlist[l] > rightlist[r]):
        r = r + 1

simsum = simsum + (counter * leftlist[l])

print("Part 2:", simsum)