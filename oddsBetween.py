## function that returns all odd values within specified range, inclusive of endIndex

def printOdds(startIndex, EndIndex):
    pList = []
    for num in range(startIndex, EndIndex + 1):
        if num%2 == 1:
            pList.append(num)
    print(pList)

printOdds(0, 100)