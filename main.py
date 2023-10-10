#Creating an empty queue
queue = []

#Inserting a few items
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)


print(f"Queues: {queue}")

#Dequeuing
print("Removing items from the queue: ")
print(queue.pop())
print(queue.pop())
print(queue.pop(0))

#Remaining queue
print(f"Remaining queue: {queue}")
