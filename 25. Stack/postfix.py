a = input("Enter the postfix expression: ")

stack = []

for char in a:
    # if operand (digit), push to stack
    if char.isdigit():
        stack.append(int(char))
    
    # if operator, pop two operands and evaluate
    else:
        b = stack.pop()  # second operand
        a2 = stack.pop() # first operand
        
        if char == '+':
            stack.append(a2 + b)
        elif char == '-':
            stack.append(a2 - b)
        elif char == '*':
            stack.append(a2 * b)
        elif char == '/':
            stack.append(a2 // b)  # integer division

print("Result:", stack[0])