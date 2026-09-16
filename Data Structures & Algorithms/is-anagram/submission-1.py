class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        letter_counts = dict()

        for char in s:
            if char in letter_counts: 
                letter_counts[char] += 1
            else: letter_counts[char] = 1

        for char in t:
            if char not in letter_counts:
                return False
            letter_counts[char] -= 1
            if letter_counts[char] < 0:
                return False

        return True