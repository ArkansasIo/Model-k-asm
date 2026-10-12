# Quantum Assembly Algorithm Catalog

| Example | Purpose | Key concept | Status |
|---|---|---|---|
| Bell state | Correlated two-qubit state | H + CX | OpenQASM 3 example |
| Grover 2-qubit | Search one marked basis state | Oracle + diffusion | Circuit example; validate oracle conventions |
| Teleportation | Transfer a prepared state using entanglement and classical bits | Bell pair + feed-forward | Educational example |
| Phase estimation | Estimate an eigenphase | Controlled powers + inverse QFT | QISA sketch; controlled-U backend required |
| VQE sweep | Variational energy estimation loop | Parameterized circuit + classical optimizer | Host/simulator integration sketch |

Quantum results are probabilistic. Record shot count and histogram, not only a single measurement. Gate noise, readout error, transpilation, and backend constraints can change observed distributions.
