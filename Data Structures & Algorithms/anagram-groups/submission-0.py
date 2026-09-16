class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = dict()

        for string in strs:
            count = [0] * 26

            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1

            count = tuple(count)

            if count in counts: counts[count].append(string)
            else: counts[count] = [string]

        return list(counts.values())
        
       
        