from collections import deque

d = deque([1, 2, 3,])
d.append(4) 
d.appendleft(0)
print(d.pop())
print(d.popleft())

d2 = deque([1,2,3,4,5])
d2.rotate(2)
print(d2)
d2.rotate(-1)
print