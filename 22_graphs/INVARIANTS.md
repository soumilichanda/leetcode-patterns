# Cluster 22: Graph Traversals & Disjoint Components

### Algorithmic Invariants & Complexity Analysis

#### 1. LeetCode 200: Number of Islands
- **In-Place Grid Sinking:** Mutating visited cells from `'1'` to `'0'` guarantees each cell is traversed a constant number of times ($4 \cdot M \cdot N$ boundary checks), eliminating auxiliary hash set allocation overhead.
- **Complexity Bound:** $\mathcal{O}(M \times N)$ time; $\mathcal{O}(M \times N)$ auxiliary call stack worst-case for fully contiguous grids.

#### 2. LeetCode 133: Clone Graph
- **Deep Reference Virtualization:** Storing visited mappings (`original_node -> cloned_node`) before recursing into adjacency lists breaks cyclic recursion loops and preserves arbitrary graph topology.
- **Complexity Bound:** $\mathcal{O}(V + E)$ time traversing every vertex and edge; $\mathcal{O}(V)$ memory allocation for node mappings.
