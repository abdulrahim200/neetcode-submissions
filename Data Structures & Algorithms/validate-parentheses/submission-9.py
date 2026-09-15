class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
        for ch in s:
            if ch in"{[(":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if pairs[ch]!=stack.pop():
                    return False
        if stack:
            return False
        return True
            

        