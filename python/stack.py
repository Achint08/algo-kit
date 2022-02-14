# We assume we don't have any stack capacity
stack = []
# Push to stack
stack.append(12)
stack.append(23)
stack.append(43)
stack.append(63)
stack.append(15)
# Stack order from right to left
print(stack)

# Check the top element
top = stack[-1]
print(top)

# General way to pop
if(stack):
    print(stack.pop())

print(stack)

# Empty the stack
while(stack):
    stack.pop()

print(stack)

if(stack):
    print(stack.pop())
