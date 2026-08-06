class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        curr = 0
        length = 0
        maxlen = 0
        for num in nums_set:
            if num-1 not in nums_set:
                curr = num
                length = 1
                while curr+1 in nums_set:
                    curr+=1
                    length+=1
                    maxlen = max(maxlen,length)
                maxlen = max(maxlen,length)
        return maxlen

            

                

            
        

            
            