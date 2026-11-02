class Solution:
    def isValid(self, s: str) -> bool:
        """
        walk through elements and push to stack
        walk through elements again and pop from stack. if element != stack pop element, return false
        """
        stack = []
        mapping = {
            '[' : ']', 
            '(' : ')',
            '{' : '}'  
        }

        for c in s:
            if c in mapping:
                stack.append(c)
            elif not stack or mapping[stack.pop()] != c:
                return False
        if stack:
            return False
        return True
        
