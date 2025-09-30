
scores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def characterScore(char):
    score = 0
    for i in range(26):
        if not char.isalpha():
            return -1
        elif ord(char.lower()) == 97+i:
            score += scores[i]
    return score

def scrabbleScore(string):
    score = 0
    for i in range(len(string)):
        score += characterScore(string[i])
    return score

def lstScrabbleScore(sList):
    score = 0
    for i in range(len(sList)):
        score += scrabbleScore(sList[i])
        sList[i] = score
    return sList

print(characterScore("a"))
print(scrabbleScore("APPles"))
print(lstScrabbleScore(["cat", "hat", "APPles"]))
