from collections import deque
class Traversal:
    def __init__(self,vertices):
        self.V = vertices
        self.adj = {i:[] for i in range(vertices)}

    def add_edge(self,u, v, directed = False):
        self.adj[u].append(v)
        if not directed:
            self.adj[v].append(u)
    
    def bfs(self,start):
        visited = [False] * self.V
        q = deque()
        result = []

        #start
        visited[start] = True
        q.append(start)
        while q:
            node = q.popleft()
            result.append(node)
            for neighbour in self.adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)
        return result
    
    def display(self):
        print("\nAdjacency List:")
        print("-" * 30)
        for node in self.adj:
            print(f"  {node} → {self.adj[node]}")
        print("-" * 30)

class traversal:
    def __init__(self,vertices):
        self.V = vertices
        self.adj = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u,v,directed = False):
        self.adj[u][v] = 1
        if not directed:
            self.adj[v][u] = 1
    
    def bfs(self, start):
        visited = [False] * self.V
        q = deque()
        result = []

        visited[start] = True
        q.append(start)
        while q:
            node = q.popleft()
            result.append(node)

            for neighbor in range(self.V):
                if self.adj[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)
        return result
    
    def display_matrix(self):
        print("\nAdjacency Matrix:")
        print("-" * (self.V * 4 + 5))
        print("    ", end="")
        for i in range(self.V):
            print(f"{i:3}", end="")
        print()
        print("   +" + "---" * self.V)
        for i in range(self.V):
            print(f" {i} |", end="")
            for j in range(self.V):
                print(f"  {self.adj[i][j]}", end="")
            print()
        print("-" * (self.V * 4 + 5))
    
if __name__ == "__main__":
    # g1 = Traversal(5)
    # g1.add_edge(0, 1)
    # g1.add_edge(0, 2)
    # g1.add_edge(1, 3)
    # g1.add_edge(1, 4)
    # g1.add_edge(2, 4)

    # g1.display()

    # print("\nBFS from node 0:")
    # print(f"  Order : {g1.bfs(0)}")


    print("=" * 45)
    print("   Example 1 — Undirected Graph")
    print("=" * 45)
    #
    #   0 ── 1 ── 3
    #   |    |
    #   2 ── 4
    #
 
    g1 = traversal(5)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    g1.add_edge(1, 4)
    g1.add_edge(2, 4)
 
    g1.display_matrix()
 
    print("\nBFS from node 0:")
    print(f"  Order      : {g1.bfs(0)}")