class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0

        left = 0
        right =  len(heights) - 1

        while left < right:
            width = right - left

            if heights[left] < heights[right]:
                height = heights[left]
                left += 1
            else: 
                height = heights[right]
                right -= 1

            area = width * height
            if area > maximum: maximum = area

        return maximum

        # left = 0
        # maximum = 0

        # while left != len(heights):
        #     right = len(heights) - 1

        #     while right != left:
        #         if heights[left] <= heights[right]:
        #             height = heights[left]
        #         else: height = heights[right]

        #         width = right - left
        #         if width * height > maximum: maximum = width * height

        #         right -= 1
        #     left += 1

        # return maximum