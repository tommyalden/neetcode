class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for num in nums:
            if num - 1 in numSet:
                continue  

            x = num
            while x in numSet: x += 1
            
            length = x - num
            if length > longest: longest = length

        return longest

        
            