def getCalVal(text):
    firstNum = ""
    lastNum = ""
    for letter in text:
        if letter.isnumeric():
            if firstNum == "":
                firstNum = letter
            lastNum = letter
    return int(firstNum + lastNum)

result = 0

f = open("AdventOfCode/Day1/input.txt", "r")
for x in f:
    result += getCalVal(x)

print(result)