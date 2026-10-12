# Quantum Assembly Research Notes

Research basis: OpenQASM 3 is an imperative, machine-independent representation of quantum circuits with gate operations, measurement, reset, and classical feed-forward. Quantum instruction-set research such as eQASM focuses on expressing control flow and timing constraints in a form suitable for quantum-control microarchitecture.

Model K design implications:
1. Keep a portable circuit interchange format (OpenQASM 3) separate from project-specific QISA.
2. Make backend-specific timing and pulse details profile-controlled rather than pretending every device shares one instruction set.
3. Treat measurement as a probabilistic classical output and store shot counts plus run metadata.
4. Keep host CPU scheduling, file I/O, patching, and database work in the classical control plane.
5. Validate circuits with a simulator before backend submission; note that simulator success is not proof of hardware execution.

Sources:
- IBM Quantum, Introduction to OpenQASM: https://quantum.cloud.ibm.com/docs/en/guides/introduction-to-qasm
- IBM Quantum, OpenQASM 3 and Qiskit: https://quantum.cloud.ibm.com/docs/en/guides/interoperate-qiskit-qasm3
- Fu et al., eQASM: An Executable Quantum Instruction Set Architecture: https://arxiv.org/abs/1808.02449
