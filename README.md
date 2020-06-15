# leetcode
My solutions to the leetcode problems


Notes:

Graph: 
For shortest path - prefer bfs

Queue:
```
from collections import deque
q = deque([])
q.append(e), q.appendleft()
q.pop(), q.popleft()
```

Priority Queue:
```
import heapq
t = (a,b)
heapq.heappush(t) # first element of the iterable is used as key to heapify. default-smallest element on the top
heapq.heappop()
```
