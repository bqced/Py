queue = []
queue.append('a')  
# Enqueue 'a' to the back of the queue
queue.append('b') 
queue.append('c')  
queue.append('d')  

print('Initial queue:')
print(queue)

print('\nElements dequeued from the queue:')

while len(queue) > 0:
# If the queue is not empty, continue dequeuing
# If the queue is empty, exit the loop
    if len(queue) > 0:
        # Remove and print the element at the front of the queue
        # Since pop(0) is used, it removes the element at index 0
        print(queue.pop(0))

print('\nQueue after elements are dequeued:')
print(queue)