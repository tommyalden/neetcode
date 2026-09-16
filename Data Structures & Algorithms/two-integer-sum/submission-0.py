class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                j = seen[difference]

                if i < j: return [i, j]
                else: return [j, i]

            seen[num] = i