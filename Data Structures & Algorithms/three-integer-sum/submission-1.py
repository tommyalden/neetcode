class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()

        for i, target in enumerate(nums):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                summed = nums[left] + nums[right]
            
                if summed == -target: 
                    triplets.add(tuple(sorted([target, nums[left],nums[right]])))
                    left += 1
                    right -= 1
                if summed > -target: right -= 1
                if summed < -target: left += 1
        
        return list(triplets)




        