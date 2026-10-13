# Architectural Specification — Retrieval-Augmented Generation Engine

## 1. Vector Space & Hypersphere Normalization
Candidate chunks are projected onto a unit hypersphere via $L_2$ Euclidean normalization:
$$\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|_2}$$
Cosine similarity dot products $\langle \hat{\mathbf{q}}, \hat{\mathbf{d}}_i \rangle$ run in deterministic $\mathcal{O}(N \cdot D)$ time.

## 2. Reciprocal Rank Fusion (RRF) Invariants
To prevent lexical or semantic bias, rank fusion evaluates candidate ranks across both sparse and dense channels:
$$RRF(d) = \sum_{m \in M} \frac{1}{k + r_m(d)} \quad \text{with } k = 60$$

## 3. Telemetry & Guardrail Boundaries
- **Vector Dimension:** $D = 384$ (all-MiniLM-L6-v2 compatible)
- **Minimum Semantic Groundedness Cutoff:** $\tau = 0.35$
- **Lexical Overlap Weight:** $\alpha = 0.35$
