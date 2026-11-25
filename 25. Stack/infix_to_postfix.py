a = input("Enter the infix expression: ")
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(':3, ')':3}
c = []
d = []

for char in a:
    # operand - directly add to output
    if char not in ['+', '-', '*', '/', '(', ')']:
        c.append(char)

    # open bracket - push to stack
    elif char == '(':
        d.append(char)

    # close bracket - pop until matching (
    elif char == ')':
        while d and d[-1] != '(':
            c.append(d.pop())
        d.pop()  # remove the '('

    # operator
    else:
        while (d and d[-1] != '(' and d[-1] in precedence and precedence[d[-1]] >= precedence[char]):
            c.append(d.pop())
        d.append(char)

# pop remaining operators
while d:
    c.append(d.pop())

print("Postfix:", ''.join(c))