class Traversal:
    def __init__(self,vertices):
        self.V = vertices
        self.adj = {i:[] for i in range(vertices)}

    def add_edge(self,u,v,directed = False):
        self.adj[u].append(v)
        if(not directed):
            self.adj[v].append(u)

    def _dfs(self,node,visited,result):
        visited[node] = True
        result.append(node)
        for neighbour in self.adj[node]:
            if not visited[neighbour]:
                self._dfs(neighbour,visited,result)
    
    def dfs(self,start):
        visited = [False] * self.V
        result = []
        self._dfs(start,visited,result)
        return result
    
    def display(self):
        print("\nAdjacency List:")
        print("-" * 30)
        for node in self.adj:
            print(f"  {node} → {self.adj[node]}")
        print("-" * 30)

if __name__ == "__main__":
    print("=" * 45)
    print("   DFS using Adjacency LIST")
    print("=" * 45)
    #
    #   0 ── 1 ── 3
    #   |    |
    #   2 ── 4
    #
 
    g1 = Traversal(5)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    g1.add_edge(1, 4)
    g1.add_edge(2, 4)
 
    g1.display()
 
    print(f"\nDFS Recursive  from 0 : {g1.dfs(0)}")