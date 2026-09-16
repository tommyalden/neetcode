class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [set() for _ in range(len(nums) + 1)]
        counts = dict()
        
        for num in nums:
            if num in counts: counts[num] += 1
            else: counts[num] = 1
            
        for num in nums: buckets[counts[num]].add(num)
        
        output = []

        for i in range(len(nums), -1, -1):
            if buckets[i] == set(): continue
            output += list(buckets[i])

            if len(output) == k: break

        return output
