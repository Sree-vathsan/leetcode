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
h = []
t = (a,b)
heapq.heappush(h,t) # first element of the iterable is used as key to heapify. default-smallest element on the top
heapq.heappop(h)
# nsmallest and nlargest is suggested only for smaller val of n
heapq.nlargest(k, h)
heapq.nsmallest(k, h)

arr = [4,2,3,1]
heapq.heapify(arr)
```

DisjointUnionFind
```
def find(node: int) -> int:
	if parent[node] == node:
  		return node
	parent[node] = find(parent[node])            
	return parent[node]

def union(u: int, v: int):
	v_parent = find(v)
	u_parent = find(u)
	parent[v_parent] = u_parent
```
