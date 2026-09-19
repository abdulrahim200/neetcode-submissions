class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens.reverse()
        operations = {
            "+":lambda a,b:a+b,
            "-":lambda a,b:b-a,
            "*":lambda a,b:a*b,
            "/":lambda a,b:b/a,
        }
        l = []  
        while tokens:
            top = tokens.pop()
            if top in "+*-/":
                op1 = l.pop()
                op2 = l.pop()
                res = operations[top](int(op1),int(op2))
                l.append(int(res))
            else:
                l.append(int(top))
        if not tokens:
            return l[-1]

