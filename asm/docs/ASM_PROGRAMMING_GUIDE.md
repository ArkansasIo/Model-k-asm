# Model K Conventional ASM Programming Guide

Conventional ASM is the classical control language for the 8-bit reference CPU. It is separate from QISA: conventional ASM handles memory, files, records, graphs, updates, and quantum-job scheduling, while QISA describes optional quantum execution.

A 20-bit logical value occupies three registers/fields; only four bits of the high field are significant. A physical Model K record is 20 bytes. Magnetic-core memory remains classical storage.

Program flow: INIT -> INPUT -> COMPUTE -> STORE -> OUTPUT -> HALT.

Validate addresses, record lengths, 20-bit bounds, file handles, stack depth, and update hashes before mutating persistent state. Symbolic calls are interface contracts until a concrete opcode/ABI is finalized.
