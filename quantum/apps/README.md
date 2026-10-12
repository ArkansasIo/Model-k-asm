# Model QK Procedural Quantum Application

The procedural generator creates reproducible OpenQASM 3 circuits from a seed, qubit count, depth, algorithm family, and rotation parameter.

Algorithms:
- random: seeded pseudo-random layers
- qft: quantum Fourier transform structure
- grover: small search experiment
- variational: parameterized RY plus entangling layers

Examples:
python quantum/apps/procedural_generator.py --seed 42 --qubits 4 --depth 8 --algorithm random --output circuit.qasm
python quantum/apps/procedural_generator.py --qubits 3 --algorithm qft
python quantum/apps/procedural_generator.py --qubits 4 --algorithm variational --depth 6

Generated circuits must pass QISA/compiler validation before backend submission.
