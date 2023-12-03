def parseInput(filename):
    file = open(filename)
    return list(file.read().split("\n"))
    
def shouldCount(schematic: list[str], row: int, column: int):
    if column > 0 and schematic[row][column - 1].isdigit(): return False # Partway through a number
    i = column
    length = 0
    while i < len(schematic[row]) and schematic[row][i].isdigit():
        i = i + 1
        length = length + 1
    if row > 0:
        i = max(column - 1, 0)
        while i < len(schematic[row]) and i < column + length + 1:
            if schematic[row - 1][i] != "." and schematic[row - 1][i].isdigit() == False: return True
            i = i + 1
    if column > 0 and schematic[row][column - 1] != "." and schematic[row][column - 1].isdigit() == False: return True
    if column + length < len(schematic[row]) and schematic[row][column + length] != "." and schematic[row][column + length].isdigit() == False: return True
    if row < len(schematic) - 1:
        i = max(column - 1, 0)
        while i < len(schematic[row]) and i < column + length + 1:
            if schematic[row + 1][i] != "." and schematic[row + 1][i].isdigit() == False: return True
            i = i + 1
    return False

def calculateResult(schematic: list[str]):
    total = 0
    for row in range(len(schematic)):
        column = 0
        while column < len(schematic[row]):
            if (schematic[row][column].isdigit()) and shouldCount(schematic, row, column):
                number = ""
                while column < len(schematic[row]) and schematic[row][column].isdigit():
                    number = number + schematic[row][column]
                    column = column + 1
                total = total + int(number)
            column = column + 1
    return total

def getResult(filename):
    input = parseInput(filename)
    print(filename + ": " + str(calculateResult(input)))

getResult("./3/example.txt")
getResult("./3/input.txt")
