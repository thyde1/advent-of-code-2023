import os
import sys

class Game:
    id: int
    draws: dict[str, int]

def parseInput(filename):
    file = open(filename)
    lines = file.read().splitlines()
    for line in lines:
        id, rest = line.split(": ")
        gameId = int(id.split(" ")[1])
        draws = rest.split(";")
        def getDrawsInGame(draws: list[str]):
            for draw in draws:
                def getDrawColors(draw: str):
                    colorDict = {}
                    drawColors = draw.split(", ")
                    for drawColor in drawColors:
                        number, color = drawColor.strip().split(" ")
                        colorDict[color] = int(number)
                    return colorDict
                drawColors = getDrawColors(draw)
                yield drawColors
        thisGame = Game()
        thisGame.id = gameId
        thisGame.draws = getDrawsInGame(draws)
        yield thisGame

maximums = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def isPossible(colors: dict[str, int]) -> bool:
    return any(maximums[color[0]] < color[1] for color in colors.items()) == False

def calculateValue(games: list[Game]):
    total = 0
    for game in games:
        possible = True
        for draw in game.draws:
            if isPossible(draw) == False:
                possible = False
                break
        if possible: total = total + game.id
    return total

def getValueForInput(filename: str):
    games = parseInput(filename)
    value = calculateValue(games)
    print(filename + ": " + str(value))
    return value

def getMinCubesForGame(game: Game):
    mins: dict[str, int] = {}
    draws = list(game.draws)
    for color in maximums.keys():
        min = 0
        for draw in draws:
            if (draw.get(color) or 0) > min:
                min = draw[color]
            else:
                x = 9
        mins[color] = min
    return mins

def calculateTotalPower(games: list[Game]):
    totalPowers = 0
    for game in games:
        minColors = getMinCubesForGame(game)
        power = 1
        for color in minColors:
            power = power * minColors[color]
        totalPowers = totalPowers + power
    return totalPowers
            

def getPowerForInput(filename: str):
    games = parseInput(filename)
    value = calculateTotalPower(games)
    print(filename + ": " + str(value))
    return value 

getValueForInput("./2/example.txt")
getValueForInput("./2/input.txt")
getPowerForInput("./2/example.txt")
getPowerForInput("./2/input.txt")
