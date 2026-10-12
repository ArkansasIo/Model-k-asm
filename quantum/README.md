# Model K Quantum Assembly

Optional quantum coprocessor/programming subsystem. The classical CPU and magnetic-core memory remain classical; QASM/QISA commands are submitted to a simulator or quantum backend.

Subsystems: QISA, QASM assembly, algorithms, circuits, simulator, RTL interface, equations, tests.


## Expanded examples

Additional research notes and examples are in `docs/RESEARCH_NOTES.md`, `docs/QISA_PROGRAMMING_GUIDE.md`, and `docs/ALGORITHM_CATALOG.md`. New QISA sketches cover Grover search, teleportation, phase estimation, and a VQE parameter sweep. OpenQASM 3 circuit examples are provided separately under `circuits/`. QISA-specific instructions are project-defined and require a compatible assembler/backend; they are not directly executable on arbitrary quantum hardware.
