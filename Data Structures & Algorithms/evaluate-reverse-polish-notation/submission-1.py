class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        walk through list
        until you hit an operator, append to stack.
        then pop twice do operation and append answer to stack
        pop answer from stack
        """

        stack = []
        operations = set(['+', '-', '*', '/'])

        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(tokens[i])
                continue
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(left + right)
                elif tokens[i] == '-':
                    stack.append(left - right)
                elif tokens[i] == '*':
                    stack.append(left * right)
                else:
                    stack.append(left/right)
        
        answer = int(stack.pop())
        return answer