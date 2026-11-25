import heapq

class prims:
    def __init__(self,vertices):
        self.V = vertices
        self.adj = {i:[] for i in range(vertices)}
    
    def add_edge(self,u,v,weight):
        self.adj[u].append((weight, v))
        self.adj[v].append((weight, u))
    
    def prims_algo(self, start = 0):
        visited = [False]*self.V
        min_heap   = [(0, start, -1)]   # (weight, node, parent)
        mst_edges  = []
        total_cost = 0

        while min_heap:
            weight,u,parent = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True

            if parent != -1:
                mst_edges.append((parent,u,weight))
                total_cost+=weight
            
            for edge_weight,v in self.adj[u]:
                if not visited[v]:
                    heapq.heappush(min_heap,(edge_weight,v,u))
        return mst_edges, total_cost
    
    def display(self):
        print("\nAdjacency List (weight, neighbor):")
        print("-" * 35)
        for node in self.adj:
            edges = [(w, v) for w, v in self.adj[node]]
            print(f"  {node} → {edges}")
        print("-" * 35)

def print_mst(mst_edges, total_cost):
    print("\nMST Edges:")
    print("-" * 35)
    print(f"  {'Edge':10} {'Weight':>6}")
    print("-" * 35)
    for u, v, w in mst_edges:
        print(f"  {u} ── {v}  :  {w:>4}")
        print("-" * 35)
    print(f"  Total Cost : {total_cost}")
    print("-" * 35)
    
if __name__ == "__main__":
    print("\n--- Adjacency LIST version ---")
    pl = prims(6)
    pl.add_edge(0, 1, 2)
    pl.add_edge(0, 3, 6)
    pl.add_edge(1, 2, 3)
    pl.add_edge(1, 3, 8)
    pl.add_edge(1, 4, 5)
    pl.add_edge(2, 4, 7)
    pl.add_edge(3, 4, 9)
    pl.add_edge(4, 5, 1)
    pl.add_edge(2, 5, 7)
 
    pl.display()

    mst, cost = pl.prims_algo(start=0)
    print_mst(mst, cost)