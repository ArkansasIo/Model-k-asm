"""QISA runtime reference for Model QK.

Program ID: QK-QISA-0001
File ID: QK-QISA-0001-FILE-0002
Version: QK.2.0.0
"""

class QISARuntime:
    def __init__(self, backend):
        self.backend = backend
        self.qubits = set()

    def execute(self, program, shots=1024, seed=None):
        for instruction in program:
            op, *args = instruction
            if op == "QALLOC":
                self.qubits.add(args[0])
            elif op == "QFREE":
                self.qubits.discard(args[0])
            elif op == "RESET":
                self.backend.reset_qubit(args[0])
            elif op in {"X", "H"}:
                getattr(self.backend, op.lower())(args[0])
            elif op in {"CX", "CZ", "SWAP"}:
                getattr(self.backend, op.lower())(*args)
            elif op == "MEASURE":
                return self.backend.measure_all(shots=shots, seed=seed)
            elif op == "HALT":
                break
            else:
                raise ValueError(f"Unknown QISA instruction: {op}")
        return self.backend.measure_all(shots=shots, seed=seed)
