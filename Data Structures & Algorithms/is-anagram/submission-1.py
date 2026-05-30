class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for s1,s2 in zip_longest(s,t):
            freq1[s1] = freq1.get(s1,0)+1
            freq2[s2] = freq2.get(s2,0)+1
        print(freq1,freq2)
        if freq1==freq2:
            return True
        return False 


        