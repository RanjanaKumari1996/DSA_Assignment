s = "*-A/BC-/AKL"
 
stack = []
 
operators = set(['+', '-', '*', '/', '^'])
 
s = s[::-1]
 

for i in s:
 
    # if token is operator
    if i in operators:
 
        
        a = stack.pop()
        b = stack.pop()
 
        
        temp = a+b+i
        stack.append(temp)
 
    # else if operand
    else:
        stack.append(i)
 

print(*stack)