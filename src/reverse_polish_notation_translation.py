#!/usr/bin/env python
'''
Reverse polish notation translation.
This solution works only for equations with brackets, and no functions (sin, cos, etc/)
'''


operators = ['+', '-', '*', '/', '^']
open_br = '('
close_br = ')'


def transform_expression(input_expression):
    expression = list(input_expression)
    stack = []
    output = []

    while len(expression):
        if expression[0].isalpha():
            output.append(expression.pop(0))
        elif expression[0] in operators:
            while stack[-1] != open_br:
                output.append(stack.pop(-1))

            stack.append(expression.pop(0))
        elif expression[0] == open_br:
            stack.append(expression.pop(0))
        elif expression[0] == close_br:
            while len(stack):
                if stack[-1] != open_br:
                    operator = stack.pop(-1)
                    output.append(operator)
                else:
                    stack.pop(-1)
                    break
            expression.pop(0)

    while len(stack):
        if stack[-1] != open_br:
            output.append(stack.pop(-1))
        else:
            stack.pop(-1)

    return ''.join(output)
