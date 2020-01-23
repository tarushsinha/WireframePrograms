## program to return numbers within a larger range that satisfy a specific rule
## also employs Python List Comprehensions for practice

def valid(num):
    if not(num%2 == 0 or num%3 == 0):
        return num

def subList(maxRange):
    sList = [valid(i) for i in range(maxRange) if valid(i) != None]
    return sList

print(subList(50))