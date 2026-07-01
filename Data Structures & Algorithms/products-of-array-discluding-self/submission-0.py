class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for i in range(1,len(nums),1):
            prefix.append(prefix[i-1]*nums[i-1])
        for i in range(len(nums)-1,0,-1):
            suffix.append(suffix[len(nums)-i-1]*nums[i])
        suffix.reverse()
        result = []
        for i in range(len(prefix)):
            result.append(prefix[i]*suffix[i])
        return result