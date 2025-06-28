def count_characters(s):
    freq = {}
    for c in s:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    return freq


dictionary = count_characters("hola")
print(dictionary.values()!=[1,1,1,1])
