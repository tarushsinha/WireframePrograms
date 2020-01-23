def reverseNumber(inp):
    ret = list(str(inp))
    ret.reverse()
    v = ""
    for i in ret:
        v = v + i
    return int(v)

## same as above method, works without relying on List.reverse()
def independentReverse(inp):
    ret = list(str(inp))
    v = ""
    for i in ret[::-1]:
        v = v + i
    return int(v)

print(reverseNumber(81))
print(independentReverse(81))