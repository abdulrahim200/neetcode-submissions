class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        ans = set()
        for i in range(len(nums)):
            hashset = set()
            for j in range(i+1,len(nums),1):
                third  = -(nums[i]+nums[j])
                if third in hashset:
                    triplet = []
                    triplet.append(nums[i])
                    triplet.append(nums[j])
                    triplet.append(third)
                    triplet = tuple(sorted(triplet))
                    ans.add(triplet)
                hashset.add(nums[j])
        return list(ans)