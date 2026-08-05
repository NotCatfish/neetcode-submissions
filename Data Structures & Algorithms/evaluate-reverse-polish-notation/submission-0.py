class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={
            '+':lambda a,b:a+b,
            '-':lambda a,b:a-b,
            '*':lambda a,b:a*b,
            '/':lambda a,b:int(a/b)
        }
        for x in tokens:
            if x in operations:
                right=stack.pop()
                left=stack.pop()
                result=operations[x](left,right)
                stack.append(result)
            else:
                stack.append(int(x))

            
        return stack.pop()