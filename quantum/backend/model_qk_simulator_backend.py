"""QK simulator backend: executes circuits on the Model QK state-vector reference.

Program ID: QK-QBE-0001
File ID: QK-QBE-0001-FILE-0002
Version: QK.2.0.0
"""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from quantum.sim.aethernox_statevector import StateVector


class ModelQKSimulatorBackend:
    name = "QK-STATEVECTOR"

    def __init__(self, qubits: int = 8):
        self.qubits = qubits
        self.state = StateVector(qubits)

    def reset(self) -> None:
        self.state.reset()

    def run_operations(self, operations: list[tuple], shots: int = 1024, seed: int | None = None) -> dict[str, Any]:
        self.reset()
        for op in operations:
            name, *args = op
            if name == "X":
                self.state.x(args[0])
            elif name == "H":
                self.state.h(args[0])
            elif name == "CX":
                self.state.cx(args[0], args[1])
            elif name == "CZ":
                self.state.cz(args[0], args[1])
            elif name == "SWAP":
                self.state.swap(args[0], args[1])
            elif name == "RESET":
                self.state.reset_qubit(args[0])
            else:
                raise ValueError(f"Unsupported simulator operation: {name}")
        counts = self.state.measure_all(shots=shots, seed=seed)
        return {"backend": self.name, "qubits": self.qubits, "shots": shots, "counts": counts}


def bell_state(shots: int = 1024, seed: int = 20261011) -> dict[str, Any]:
    return ModelQKSimulatorBackend(2).run_operations(
        [("H", 0), ("CX", 0, 1)], shots=shots, seed=seed
    )


if __name__ == "__main__":
    print(bell_state())
