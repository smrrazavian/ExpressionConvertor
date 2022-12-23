"""Convert infix, postfix and prefix expressions"""
from structures.stack import Stack


def precedence(operand):
    """Return precedence of operator"""
    first_level = ['+', '-']
    second_level = ['*', '/']
    third_level = ['^']
    if operand in first_level:
        return 1
    elif operand in second_level:
        return 2
    elif operand in third_level:
        return 3
    else:
        return 0


def infix_to_postfix(infix:str) -> str:
    """Convert infix to postfix"""
    stack = Stack()
    postfix = Stack()
    for i in infix:
        if i.isalpha():
            postfix.push(i)
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while stack.peek() != '(':
                postfix.push(stack.pop())
            stack.pop()
        else:
            while stack and stack.peek() != '(' and precedence(i) <= precedence(stack.peek()):
                postfix.push(stack.pop())
            stack.push(i)
    while stack:
        postfix.push(stack.pop())
    return postfix.get_string()


def infix_to_prefix(infix:str) -> str:
    """Convert infix to prefix"""
    stack = Stack()
    prefix = Stack()
    for i in infix[::-1]:
        if i.isalpha():
            prefix.push(i)
        elif i == ')':
            stack.push(i)
        elif i == '(':
            while stack.peek() != ')':
                prefix.push(stack.pop())
            stack.pop()
        else:
            while stack and stack.peek() != ')' and precedence(i) < precedence(stack.peek()):
                prefix.push(stack.pop())
            stack.push(i)
    while stack:
        prefix.push(stack.pop())
    return (prefix.get_string())[::-1]


def postfix_to_infix(postfix:str) -> str:
    """Convert postfix to infix"""
    stack = Stack()
    for char in postfix:
        if char.isalpha():
            stack.push(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push('(' + op2 + char + op1 + ')')
    return stack.pop()


def prefix_to_infix(prefix:str) -> str:
    """Convert prefix to infix"""
    stack = Stack()
    for i in prefix[::-1]:
        if i.isalpha():
            stack.push(i)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push('(' + op1 + i + op2 + ')')
    return stack.pop()


def detect_type(expression:str) -> str:
    """Detect type of expression"""
    operators = ['+', '-', '*', '/', '^']
    if (expression[0].isalpha() and expression[-1].isalpha()) or (expression[0] == '(' and expression[-1] == ')'):
        return 'infix'
    elif expression[0] in operators:
        return 'prefix'
    elif expression[-1] in operators:
        return 'postfix'
    else:
        return 'invalid'
