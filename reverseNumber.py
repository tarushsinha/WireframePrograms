def reverseNumber(inp):
    ret = list(str(inp))
    ret.reverse()
    v = ""
    for i in ret:
        v = v + i
    return int(v)