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

getValueForInput("./2/example.txt")
getValueForInput("./2/input.txt")