#QUEUE
from collections import deque

queue = deque()

#enqueue
queue.append(10)
queue.append(20)

#dequeue
queue.popleft()

print(queue)
