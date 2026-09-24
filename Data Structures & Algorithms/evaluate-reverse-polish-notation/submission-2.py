class Solution:
    def operation(self, left: int, right: int, op: str) -> int:
        match op:
            case '+': return left + right
            case '-': return left - right
            case '*': return left * right
            case '/': return int(left / right)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                right = stack.pop()
                left = stack.pop()
                stack.append(self.operation(left, right, token))
            else:
                stack.append(int(token))
                
        return stack[0]