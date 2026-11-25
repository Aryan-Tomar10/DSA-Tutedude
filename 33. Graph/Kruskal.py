
# ─────────────────────────────────────────────
#  Kruskal's Algorithm — Minimum Spanning Tree
#  Using Union-Find (Disjoint Set Union)
# ─────────────────────────────────────────────
 
 
# ══════════════════════════════════════════════
#  UNION-FIND (Disjoint Set Union)
#  used to detect cycle in Kruskal's
# ══════════════════════════════════════════════
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # each node is its own parent
        self.rank   = [0] * n         # rank for union by rank
 
    def find(self, x):
        """find root of x with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
 
    def union(self, x, y):
        """union two sets by rank"""
        rx = self.find(x)
        ry = self.find(y)
 
        if rx == ry:
            return False             # already in same set → cycle!
 
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx]  += 1
 
        return True                  # successfully united
 
 
# ══════════════════════════════════════════════
#  KRUSKAL'S ALGORITHM
# ══════════════════════════════════════════════
class Kruskal:
    def __init__(self, vertices):
        self.V     = vertices
        self.edges = []              # list of (weight, u, v)
 
    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))
 
    # ══════════════════════════════════════════
    #   KRUSKAL'S — Main
    # ══════════════════════════════════════════
    def kruskal(self):
        """
        1. sort all edges by weight
        2. pick smallest edge
        3. if it doesn't form cycle → add to MST
        4. repeat until V-1 edges added
        """
        # step 1: sort edges by weight
        self.edges.sort()
        print(f"\nSorted Edges:")
        print("-" * 35)
        for w, u, v in self.edges:
            print(f"  {u} ── {v}  :  weight = {w}")
 
        uf         = UnionFind(self.V)
        mst_edges  = []
        total_cost = 0
 
        print(f"\nProcessing Edges:")
        print("-" * 45)
 
        # step 2: process each edge
        for weight, u, v in self.edges:
            if len(mst_edges) == self.V - 1:  # MST complete
                break
 
            # step 3: check if adding this edge forms a cycle
            if uf.union(u, v):
                mst_edges.append((u, v, weight))
                total_cost += weight
                print(f"  Added  : {u} ── {v} (weight={weight}) ✅")
            else:
                print(f"  Skipped: {u} ── {v} (weight={weight}) ❌ forms cycle")
 
        return mst_edges, total_cost
 
    def display_edges(self):
        print("\nAll Edges:")
        print("-" * 35)
        for w, u, v in self.edges:
            print(f"  {u} ── {v}  :  weight = {w}")
        print("-" * 35)
 
 
# ── Helper: print MST ──────────────────────────
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
 
 
# ── Main ───────────────────────────────────────
if __name__ == "__main__":
 
    # ── Example 1 ─────────────────────────────
    print("=" * 45)
    print("   Example 1 — Basic Graph")
    print("=" * 45)
    #
    #       2       3
    #   0 ──── 1 ──── 2
    #   |    / |    / |
    # 6 |  8/  |5 /   | 7
    #   | /    | /    |
    #   3 ──── 4 ──── 5
    #       9       1
    #
 
    g1 = Kruskal(6)
    g1.add_edge(0, 1, 2)
    g1.add_edge(0, 3, 6)
    g1.add_edge(1, 2, 3)
    g1.add_edge(1, 3, 8)
    g1.add_edge(1, 4, 5)
    g1.add_edge(2, 4, 7)
    g1.add_edge(3, 4, 9)
    g1.add_edge(4, 5, 1)
    g1.add_edge(2, 5, 7)
 
    g1.display_edges()
    mst, cost = g1.kruskal()
    print_mst(mst, cost)