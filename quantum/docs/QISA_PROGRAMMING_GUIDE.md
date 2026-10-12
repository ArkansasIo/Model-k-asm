# Model K QISA Programming Guide

## Scope
Model K QISA is a project-specific educational instruction notation. It is not a standardized ISA and is not directly executable on a commercial QPU. OpenQASM 3 is used for portable circuit examples; QISA sketches require a project assembler/simulator or backend lowering.

## Control-plane split
The classical Model K CPU handles files, job metadata, 20-bit values, scheduling, result storage, and error handling. A quantum backend or simulator executes gates and returns measurement samples. Magnetic-core memory remains classical storage; it does not store qubits or quantum amplitudes physically.

## Instruction families
- Allocation/lifetime: QALLOC, QFREE, RESET
- Gates: X, Y, Z, H, S, T, RX, RY, RZ
- Two-qubit gates: CX, CZ, SWAP
- Results/control: MEASURE, IF, HOST_CALLBACK, HALT
- Proposed backend-specific placeholders: CONTROLLED_U, CONTROLLED_PHASE, PARAM

## Compilation pipeline
1. Parse source and resolve symbols.
2. Check qubit allocation and gate operand ranges.
3. Verify classical/quantum type boundaries.
4. Lower project QISA into OpenQASM 3 or backend IR.
5. Run simulator or submit to a supported backend.
6. Record backend, seed, shots, calibration metadata, and measurement counts.

## Semantics warning
Instructions such as CONTROLLED_U, HOST_CALLBACK, and PARAM are illustrative extensions, not standard OpenQASM instructions. Their exact syntax and hardware mapping must be defined by a backend profile.
