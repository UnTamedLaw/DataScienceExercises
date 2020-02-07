#Stacks LIFO Last In First Out
stack = []
stack.append(25)
stack.append(-12)
tos = stack.pop() #tos will have -12 and stack will have 25

capitals = [("USA", "Washington"), ("India", "Delhi"), ("France", "Paris"), ("UK", "London")]
capitals.sort(key = lambda item : item[1]) # sort by country

#Queue first in first out strategy FIFO
#using pop operation is super slow in python
#instead implement the same queue using the deque data structure

#ipython command %%time
from collections import deque
queue2 = deque()
for i in range(0, 100):
    queue2.append(i)
print("Queue created")

for i in range(0, 100):
    queue2.popleft()
print("Queue emptied")

#numpy array are like mathematical objects called vectors
#
