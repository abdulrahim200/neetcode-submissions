class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]]= hashmap.get(nums[i],0)+1
        for y in hashmap.values():
            if y>1:
                return True
        else : return False

        