import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalised = re.sub("[^a-z0-9]", "", s.lower())
        
        for i in range(len(normalised)):
            start = normalised[i]
            end = normalised[-1 - i]

            if start != end: return False
        return True