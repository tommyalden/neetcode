class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if len(stack) == 0: 
                stack.append(char)
                continue

            top = stack[-1]

            if top == '(' and char == ')': stack.pop()
            elif top == '[' and char == ']': stack.pop()
            elif top == '{' and char == '}': stack.pop()
            else: stack.append(char)

        if len(stack) != 0: return False
        return True
        