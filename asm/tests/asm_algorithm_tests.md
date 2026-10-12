# ASM Algorithm Test Plan

1. ADD20: verify (0xFFFFF + 1) mod 2^20 = 0.
2. SUB20: define and test the target underflow policy.
3. CHECKSUM8: compare against a host-language reference.
4. BINARY_SEARCH: test empty, singleton, first, middle, last, and absent keys.
5. GCD: test (48,18)=6, coprime values, and zero operands.
6. RECORD_READ/WRITE: enforce exactly 20-byte records and validate checksum before commit.
7. TREE_SEARCH: test balanced, skewed, missing, and duplicate-key policies.
8. GRAPH_BFS: test disconnected graphs and visited-set behavior.
9. UPDATE_INSTALL: inject failed hash/dependency/test stages and verify rollback.
