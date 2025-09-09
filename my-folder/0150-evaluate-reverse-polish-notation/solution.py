class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # def eval_operator(i):
        #     operator = tokens[i]
        #     operand_one, next_operand = eval_operand(i - 1)
        #     operand_two, next = eval_operand(next_operand)
        #     if operator == '*':
        #         return (operand_two * operand_one, next)
        #     elif operator == '/':
        #         return (math.floor(operand_two / operand_one), next)
        #     elif operator == '+':
        #         return (operand_two + operand_one, next)
        #     else:
        #         return (operand_two - operand_one, next)
            
        # def eval_operand(i):
        #     if i < 0:
        #         return (0, 0)
        #     if tokens[i] not in '+-*/':
        #         return (int(tokens[i]), i-1)
        #     else:
        #         return eval_operator(i)

        # return eval_operator(len(tokens) - 1)[0]
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in tokens:
            if i not in '+-/*':
                stack.append(i)
            else:
                operand_b = int(stack.pop())
                operand_a = int(stack.pop())
                if i == '+':
                    stack.append(operand_a + operand_b)
                elif i == '-':
                    stack.append(operand_a - operand_b)
                elif i == '/':
                    # int function rounds towards 0 as required
                    stack.append(int(operand_a / operand_b))
                else:
                    stack.append(operand_a * operand_b)
        return stack.pop()
        

        
