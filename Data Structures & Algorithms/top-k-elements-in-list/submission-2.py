class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        elem = []
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        freq = dict(sorted(freq.items(),key = lambda x : x[1],reverse = True))
        for x,y in freq.items():
            elem.append(x)
        result = []
        for i in range(k):
            result.append(elem[i])
        return result
        