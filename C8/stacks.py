#The stack variable is initialized as an empty list
stack = []
n = int(input('Enter how many elements you want inside the stack: '))

#Input loop to add elements to the stack
for i in range (n):
    element = input('Enter the element: ')
    stack.append(element)

print('Initial stack')
print(stack)

print('\nElements popped from stack')
print(stack.pop(1))
#removes element at index 1
print(stack.pop(2))
#removes element at index 2
print(stack.pop(3))
#removes element at index 3

print('\nStack after elements are popped:')
print(stack)