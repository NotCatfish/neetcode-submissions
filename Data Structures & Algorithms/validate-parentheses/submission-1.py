class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        bracket_map = {
            ')': '(', 
            '}': '{', 
            ']': '['
        }
        for x in s:
            if x in bracket_map:
                top_element=stack.pop() if stack else '#'
                if bracket_map[x]!=top_element:
                    return False
            else:
                stack.append(x)
            
        return len(stack)==0