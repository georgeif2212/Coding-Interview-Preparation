def findContentChildren(g, s):
    g.sort()
    s.sort()
    i = j = 0

    counter = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
            counter += 1
        j += 1

    return counter
