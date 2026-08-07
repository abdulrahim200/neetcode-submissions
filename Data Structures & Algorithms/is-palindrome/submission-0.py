class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        start = 0
        end = 0
        count = 0
        for i in range(len(s)):
            start = i
            end = len(s)-i-1
            if s[start] == s[end]:
                count+=1
        return count == len(s)



        