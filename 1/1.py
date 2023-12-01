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

def getFirstDigit(input: str):
    index = 0
    while True:
        if input[index].isdigit():
            return int(input[index])
        index = index + 1

def getLastDigit(input: str):
    index = len(input) - 1
    while True:
        if input[index].isdigit():
            return int(input[index])
        index = index - 1
    

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

def calculate(inputFile, getFirstNumber, getLastNumber):
    directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    inputLines = parseInput(directory + '/' + inputFile)
    total = 0
    for inputLine in inputLines:
        total = total + int(str(getFirstNumber(inputLine)) + str(getLastNumber(inputLine)))
    print(inputFile + ": " + str(total))

calculate("example.txt", getFirstDigit, getLastDigit)
calculate("input.txt", getFirstDigit, getLastDigit)
calculate("example2.txt", getFirstNumber, getLastNumber)
calculate("input.txt", getFirstNumber, getLastNumber)
