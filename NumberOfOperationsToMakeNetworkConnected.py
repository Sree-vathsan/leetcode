class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]

    def union(self, s: int, d: int) -> int:
        s_parent, d_parent = self.find(self.parent[s]), self.find(self.parent[d])
        if s_parent == d_parent:
            return 1
        self.parent[d_parent] = self.parent[s] = self.parent[d] = s_parent
        return 0

    def find(self, s: int) -> int:
        if self.parent[s] != s:
            self.parent[s] = self.find(self.parent[s])
        return self.parent[s]

    def getUnique(self) -> int:
        return len({self.find(p) for p in self.parent})
        
class Solution:
    def stefanPochman(self, n: int, connections: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/number-of-operations-to-make-network-connected/discuss/477835/6-lines-clean-Unicode-Find
        """
        if len(connections) < n-1:
            return -1
        string: List[str] = "".join(map(chr, range(n)))
        for s,d in connections:
            string = string.replace(string[s], string[d])
        return len(set(string)) - 1
            
    def makeConnectedUF(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        num_redundant: int = 0  #this is not needed, If I am interviewer, I would also ask for number of redundant connections
        uf = UnionFind(n)
        for s,d in connections:
            num_redundant += uf.union(s,d)
        num_dis_connected_components: int = uf.getUnique()
        return num_dis_connected_components - 1
        
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        return self.makeConnectedUF(n, connections)
        # return self.stefanPochman(n, connections)
