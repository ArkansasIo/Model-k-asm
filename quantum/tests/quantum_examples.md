# Quantum Example Test Plan

## Bell state
Expected ideal probabilities: P(00)=0.5, P(11)=0.5, P(01)=P(10)=0. Repeated finite-shot runs fluctuate around these values.

## Grover 2-qubit
For the supplied oracle marking |11>, verify the circuit's output convention and simulator probabilities. Check whether one Grover iteration is appropriate for N=4 and the exact phase-oracle/diffusion definitions.

## Teleportation
Prepare a known input state, run the Bell measurement and conditional corrections, then compare Bob's output state to the input state in a simulator. Test both classical feed-forward bits across all four outcomes.

## Phase estimation
Use a backend that implements controlled-U and inverse-QFT lowering. Compare the measured bitstring distribution against the chosen eigenphase and counting-register precision.

## Reproducibility metadata
Record QISA version, OpenQASM version, simulator/backend name, random seed when applicable, shots, transpiler options, and date.
