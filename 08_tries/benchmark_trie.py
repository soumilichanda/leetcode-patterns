"""
Benchmark comparison: Trie prefix matching vs. Linear scan on synthetic dictionaries.
"""
import time
from importlib import import_module

trie_mod = import_module("08_tries.0208_implement_trie")

def benchmark_prefix_matching():
    words = [f"word_{i}" for i in range(10_000)]
    trie = trie_mod.Trie()
    for w in words:
        trie.insert(w)

    start = time.perf_counter()
    for _ in range(1_000):
        trie.startsWith("word_999")
    trie_elapsed = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(1_000):
        any(w.startswith("word_999") for w in words)
    linear_elapsed = time.perf_counter() - start

    print(f"Trie Search Time:   {trie_elapsed * 1000:.3f} ms")
    print(f"Linear Search Time: {linear_elapsed * 1000:.3f} ms")
    assert trie_elapsed < linear_elapsed

if __name__ == "__main__":
    benchmark_prefix_matching()
