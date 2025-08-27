class Solution:
    def isValid(self, s: str) -> bool:
        # you can use a hashmap for faster runtime and cleaner code
        if len(s) % 2 != 0:
            return False

        open = '({['
        close = ')}]'
        stack = []

        for paren in s:
            if paren in open:
                stack.append(paren)

            if paren in close:
                if len(stack) == 0:
                    return False
                pair = stack[-1] #stack.peep()
                if paren == ')' and pair != '(':
                    return False
                elif paren == '}' and pair != '{':
                    return False
                elif paren == ']' and pair != '[':
                    return False
                else:
                    stack.pop()

        if len(stack) != 0:
            return False
        else:
            return True
