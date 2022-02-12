# A quick and dirty BSN generator for testing purposes.
# For instance, to fill the Burp Intruder.
# No commandline arguments yet, just run it and send to file.


import random
import string

# Creates an array of length 8
def randomDigit(N=8):
    a = [0] * N
    for x in range (N):
        a[x] = random.randint(0, 9)
    return a

# Accumulate the array content, setup for checknum
def elevenCheck(numArr):
    acc = 0
    for i in range(len(numArr)):
        acc += ( numArr[i] * ((len(numArr)-i)+1))
    return (acc)

# Caclulate the checknum based on the input array
# Module 11 as per 'elf proef'
def calcChecknum(acc):
    checknum = acc % 11
    if checknum == 10:
        checknum = 0
    return checknum

# Get the array and the check and put them together.
def BSNgen(test):
    part1 = randomDigit()
    
    # If we want only test BSNs
    if test:
        part1[0] = 9

    part2 = calcChecknum(elevenCheck(part1))
    part1.append(part2)
    string_ints = [str(int) for int in part1]
    return ("".join(string_ints))


# Set False to True to generate only 'test' BSNs starting with 9.
for i in range (20000):
    print(BSNgen(False))
