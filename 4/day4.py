class Card:
    def __init__(self, id: int, winningNumbers: list[int], yourNumbers: list[int]):
        self.id = id
        self.winningNumbers = winningNumbers
        self.yourNumbers = yourNumbers

def parseInput(filename):
    file = open(filename)
    lines = list(file.read().split("\n"))
    cards = []
    for line in lines:
        id = int(line.split("Card ")[1].lstrip().split(":")[0])
        winningNumbersString, yourNumbersString = line.split(": ")[1].split(" | ")
        winningNumbers = []
        for number in winningNumbersString.split(" "):
            if number.isspace() or number == "": continue
            winningNumbers.append(int(number))
            yourNumbers = []
        for number in yourNumbersString.split(" "):
            if number.isspace() or number == "": continue
            yourNumbers.append(int(number))
        cards.append(Card(id, winningNumbers, yourNumbers))
    return cards

def countMatchesOnCard(card: Card):
    matches = 0
    for yourNumber in card.yourNumbers:
        if yourNumber in card.winningNumbers: matches += 1
    return matches

def calculateScore(cards: list[Card]):
    total = 0
    for card in cards:
        matches = countMatchesOnCard(card)
        if matches > 0 : total += 2 ** (matches - 1)
    return total

def calculateCards(cards: list[Card]):
    cardWins = {}
    for card in cards:
        previouslyCalculatedWins = cardWins.get(card.id)
        wins = []
        if previouslyCalculatedWins == None:
            matches = countMatchesOnCard(card)
            wins = cards[slice(card.id, card.id + matches)]
            cardWins[card.id] = wins
        else: wins = previouslyCalculatedWins
        for wonCard in wins: cards.append(wonCard)
    return len(cards)

def calculateScoreForFile(filename, scorer):
    cards = parseInput(filename)
    print(filename + ": " + str(scorer(cards)))

calculateScoreForFile("./4/example.txt", calculateScore)
calculateScoreForFile("./4/input.txt", calculateScore)
calculateScoreForFile("./4/example.txt", calculateCards)
calculateScoreForFile("./4/input.txt", calculateCards)
