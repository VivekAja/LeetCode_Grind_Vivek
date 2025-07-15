class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiouAEIOU'
        has_vowels = False
        has_consonants = False
        if len(word)<3:
            return False
        for char in word:
            if not char.isalnum():
                return False
            if char in vowels:
                has_vowels = True
            elif char.isalpha():
                has_consonants = True
        return has_vowels and has_consonants 
                