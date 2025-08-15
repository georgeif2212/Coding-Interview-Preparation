class Solution:
    def reverseVowels(self, s: str) -> str:
        
        def isVowel(character):
            return character in "aeiouAEIOU"

        string=list(s)
        left = 0
        right = len(string)-1

        while left < right:
            if not isVowel(string[left]):
                left+=1
            if not isVowel(string[right]):
                right-=1
            
            if isVowel(string[right]) and isVowel(string[left]):
                string[left], string[right] = string[right], string[left]
                left+=1
                right-=1
        
        return "".join(string)



# Optimized solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        def isVowel(c):
            return c in "aeiouAEIOU"
        
        string = list(s)
        left, right = 0, len(string) - 1
        
        while left < right:
            if not isVowel(string[left]):
                left += 1
                continue
            if not isVowel(string[right]):
                right -= 1
                continue
            
            # Aquí ambos son vocales
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        
        return "".join(string)
