"""Minimal QISA/OpenQASM operation compiler for Model QK.

Program ID: QK-QCMP-0001
File ID: QK-QCMP-0001-FILE-0001
Version: QK.2.0.0
"""

from __future__ import annotations


SUPPORTED = {"X", "H", "CX", "CZ", "SWAP", "RESET"}


def compile_operations(operations: list[tuple], qubits: int) -> list[tuple]:
    if qubits < 1:
        raise ValueError("qubits must be positive")
    compiled = []
    for op in operations:
        if not op:
            raise ValueError("empty operation")
        name, *args = op
        if name not in SUPPORTED:
            raise ValueError(f"unsupported gate: {name}")
        if any(not isinstance(q, int) or q < 0 or q >= qubits for q in args):
            raise ValueError(f"invalid qubit in {op}")
        if name in {"CX", "CZ", "SWAP"} and len(args) != 2:
            raise ValueError(f"{name} requires two qubits")
        if name in {"X", "H", "RESET"} and len(args) != 1:
            raise ValueError(f"{name} requires one qubit")
        compiled.append(op)
    return compiled


def linear_route(operations: list[tuple], qubits: int) -> list[tuple]:
    """Validate operations for a linear QK-VQPU topology."""
    out = compile_operations(operations, qubits)
    for name, *args in out:
        if name in {"CX", "CZ", "SWAP"} and abs(args[0] - args[1]) != 1:
            raise ValueError(f"{name} requires adjacent qubits on the linear target")
    return out
