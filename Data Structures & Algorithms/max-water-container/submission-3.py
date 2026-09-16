class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(heights)-1
        while i<=j:
                width = j-i
                height = min(heights[j],heights[i])
                currArea = width*height
                maxArea = max(maxArea,currArea)
                if heights[i]<heights[j]:
                    i = i+1
                elif heights[i]==heights[j]:
                    i = i+1
                else:
                    j = j-1

        return maxArea
        