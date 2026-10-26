# Cluster 23 Invariants: Graph BFS & Topological Sorting

## 1. Bidirectional Breadth-First Search (LC 127 Word Ladder)
* **Invariant:** When searching shortest paths between two known vertices in an unweighted state space, advancing the smaller frontier set $\min(|F_{\text{begin}}|, |F_{\text{end}}|)$ reduces the exponential branching factor from $b^d$ to $2b^{d/2}$.
* **Wildcard Bucketing:** Hashing generic wildcard masks ($w[:i] + * + w[i+1:]$) prevents an $O(N)$ pairwise string distance scan, bounding discovery to $O(M \times 26) \approx O(M)$ neighbors per node.

## 2. Kahn's Topological Sort & Cycle Invariant (LC 207 Course Schedule)
* **Invariant:** Every Directed Acyclic Graph (DAG) contains at least one vertex with in-degree 0.
* **Removal Step:** Removing in-degree 0 nodes preserves the DAG property for remaining subgraphs. If total processed vertices $< V$, at least one directed cycle prevented in-degree reduction to zero.
* **Complexity:** Time $O(V + E)$ where each edge and vertex is inspected exactly once; auxiliary queue and in-degree array require $O(V + E)$ space.
