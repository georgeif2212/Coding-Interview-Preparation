
def romanToInt( s):
    res=0
    romanMap={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    for i in range(len(s)-1):
        if romanMap[s[i]] < romanMap[s[i+1]]:
            res=res-romanMap[s[i]]
        else:
            res=res+romanMap[s[i]]
    return res +romanMap[s[-1]]
        
# to distinguish "VI"=6, but "IV"=4, you need to see if the numeric 
# value of the next character is greater than the numeric value of the current character

s = "DCXC"
print(romanToInt(s))