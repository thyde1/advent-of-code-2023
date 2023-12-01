import os
import sys

def parseInput(filename):
    file = open(filename)
    lines = file.read().splitlines()
    return lines

numbersAsText = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def getFirstNumber(input: str):
    numbersFound = {}
    for number in numbersAsText.items():
        index = input.find(number[0])
        numbersFound[number[1]] = index
    for number in numbersAsText.values():
        index = input.find(str(number))
        if (numbersFound[number] == -1 or (numbersFound[number] > index and index != -1)):
            numbersFound[number] = index

    sortedIndexes = sorted(numbersFound.items(), key = lambda item: item[1])
    sortedFilteredIndexes = list(filter(lambda i : i[1] != - 1, sortedIndexes))
    return sortedFilteredIndexes[0][0]


def getLastNumber(input: str):
    numbersFound = {}
    for number in numbersAsText.items():
        index = input.rfind(number[0])
        numbersFound[number[1]] = index
    for number in numbersAsText.values():
        index = input.rfind(str(number))
        if (numbersFound[number] == -1 or numbersFound[number] < index):
            numbersFound[number] = index

    sortedIndexes = sorted(numbersFound.items(), key = lambda item: item[1], reverse = True)
    sortedFilteredIndexes = list(filter(lambda i : i[1] != - 1, sortedIndexes))
    return sortedFilteredIndexes[0][0]

def calculate(inputFile):
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    inputLines = parseInput(directory + '/' + inputFile)
    total = 0
    for inputLine in inputLines:
        numberFound = False
        firstValue = 0
        index = 0
        while numberFound == False:
            if inputLine[index].isdigit():
                firstValue = int(inputLine[index])
                numberFound = True
            index = index + 1
        numberFound = False
        lastValue = 0
        index = len(inputLine) - 1
        while numberFound == False:
            if inputLine[index].isdigit():
                lastValue = int(inputLine[index])
                numberFound = True
            index = index - 1
        total = total + int(str(firstValue) + str(lastValue))
    print(inputFile + ": " + str(total))

def calculate2(inputFile):
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    inputLines = parseInput(directory + '/' + inputFile)
    total = 0
    for inputLine in inputLines:
        total = total + int(str(getFirstNumber(inputLine)) + str(getLastNumber(inputLine)))
    print(inputFile + ": " + str(total))

calculate("example.txt")
calculate("input.txt")
calculate2("example2.txt")
calculate2("input.txt")
