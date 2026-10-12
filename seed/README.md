# Model K Seed System

The seed subsystem provides deterministic initialization for Model K software and simulation.

- Master seed: unsigned 64-bit value
- Algorithm identifier: MKSEED64-V1
- Domain-separated streams: MACHINE, MEMORY, RECORD, GRAPH, QUANTUM, APPLICATION
- Seed manifests use the .SEED text format
- Seeds provide reproducibility; they are not cryptographic secrets

Example:
    SEED SET 0x4D4B2026
    SEED SHOW
    SEED STREAM QUANTUM
