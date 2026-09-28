class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        i = 0

        found = -1
        while found == -1:
            if i == 5: break
            i += 1
            if high == low: break

            midpoint = (high - low) // 2 + low
            print(midpoint, high, low)

            if target == nums[midpoint]: found = midpoint
            elif target < nums[midpoint]: high = midpoint
            else: low = midpoint

        return found