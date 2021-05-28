# try out the Python queue functions
from collections import deque
# create a new empty deque object that will function as a queue
queue= deque()

# add some items to the queue
queue.append(1)
queue.append(12)
queue.append(123)
queue.append(1234)


# print the queue contents
print(queue)

# pop an item off the front of the queue
x = queue.popleft()
print(x)
print(queue)