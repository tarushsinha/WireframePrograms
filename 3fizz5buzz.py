## program that returns multiples of 3 as fizz, multiples of 5 as buzz, and multiples of both as fizzbuzz within a range
def fizzBuzz(rng):
    retList = []
    for i in range(rng):
        if i % 3 == 0 and i % 5 == 0:
            retList.append("fizzbuzz")
        elif i%3 == 0:
            retList.append("fizz")
        elif i%5 == 0:
            retList.append("buzz")
        else:
            retList.append(i)
    print(retList)

fizzBuzz(100)