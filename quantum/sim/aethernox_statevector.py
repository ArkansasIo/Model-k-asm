#!/usr/bin/env python3
"""Small exact state-vector simulator for Aethernox quantum experiments.

This is a software simulator, not a physical quantum processor. Qubit q0 is
the least-significant bit of the computational-basis index.
"""
from __future__ import annotations
import cmath
import math
import random
from typing import Iterable, Sequence


class StateVector:
    def __init__(self, n_qubits: int, seed: int | None = None):
        if not isinstance(n_qubits, int) or n_qubits < 1 or n_qubits > 24:
            raise ValueError("n_qubits must be an integer from 1 to 24")
        self.n = n_qubits
        self.rng = random.Random(seed)
        self.state = [0j] * (1 << n_qubits)
        self.state[0] = 1 + 0j

    def _check_q(self, q: int) -> None:
        if not isinstance(q, int) or not 0 <= q < self.n:
            raise ValueError(f"qubit index out of range: {q}")

    def probabilities(self) -> list[float]:
        return [abs(a) ** 2 for a in self.state]

    def norm(self) -> float:
        return sum(self.probabilities())

    def apply_single(self, q: int, matrix: Sequence[Sequence[complex]]) -> None:
        self._check_q(q)
        if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
            raise ValueError("single-qubit gate must be a 2x2 matrix")
        bit = 1 << q
        for base in range(len(self.state)):
            if base & bit:
                continue
            other = base | bit
            a0, a1 = self.state[base], self.state[other]
            self.state[base] = matrix[0][0] * a0 + matrix[0][1] * a1
            self.state[other] = matrix[1][0] * a0 + matrix[1][1] * a1

    def x(self, q: int) -> None:
        self.apply_single(q, ((0, 1), (1, 0)))

    def y(self, q: int) -> None:
        self.apply_single(q, ((0, -1j), (1j, 0)))

    def z(self, q: int) -> None:
        self.apply_single(q, ((1, 0), (0, -1)))

    def h(self, q: int) -> None:
        s = 1 / math.sqrt(2)
        self.apply_single(q, ((s, s), (s, -s)))

    def s(self, q: int) -> None:
        self.apply_single(q, ((1, 0), (0, 1j)))

    def t(self, q: int) -> None:
        self.apply_single(q, ((1, 0), (0, cmath.exp(1j * math.pi / 4))))

    def rx(self, q: int, theta: float) -> None:
        c, s = math.cos(theta / 2), -1j * math.sin(theta / 2)
        self.apply_single(q, ((c, s), (s, c)))

    def ry(self, q: int, theta: float) -> None:
        c, s = math.cos(theta / 2), math.sin(theta / 2)
        self.apply_single(q, ((c, -s), (s, c)))

    def rz(self, q: int, theta: float) -> None:
        self.apply_single(q, ((cmath.exp(-1j * theta / 2), 0),
                              (0, cmath.exp(1j * theta / 2))))

    def cx(self, control: int, target: int) -> None:
        self._check_q(control)
        self._check_q(target)
        if control == target:
            raise ValueError("control and target must differ")
        cbit, tbit = 1 << control, 1 << target
        for i in range(len(self.state)):
            if (i & cbit) and not (i & tbit):
                j = i | tbit
                self.state[i], self.state[j] = self.state[j], self.state[i]

    def cz(self, control: int, target: int) -> None:
        self._check_q(control)
        self._check_q(target)
        if control == target:
            raise ValueError("control and target must differ")
        cb, tb = 1 << control, 1 << target
        for i in range(len(self.state)):
            if (i & cb) and (i & tb):
                self.state[i] = -self.state[i]

    def swap(self, q0: int, q1: int) -> None:
        self._check_q(q0)
        self._check_q(q1)
        if q0 == q1:
            return
        b0, b1 = 1 << q0, 1 << q1
        for i in range(len(self.state)):
            v0, v1 = bool(i & b0), bool(i & b1)
            if not v0 and v1:
                j = i ^ b0 ^ b1
                self.state[i], self.state[j] = self.state[j], self.state[i]

    def measure(self, q: int) -> int:
        self._check_q(q)
        bit = 1 << q
        p1 = sum(abs(a) ** 2 for i, a in enumerate(self.state) if i & bit)
        p1 = min(1.0, max(0.0, p1))
        result = 1 if self.rng.random() < p1 else 0
        keep_prob = p1 if result else 1.0 - p1
        if keep_prob < 1e-15:
            raise ArithmeticError("sampled a zero-probability measurement outcome")
        scale = 1 / math.sqrt(keep_prob)
        for i, amp in enumerate(self.state):
            if bool(i & bit) != bool(result):
                self.state[i] = 0j
            else:
                self.state[i] *= scale
        return result

    def measure_all(self) -> str:
        # Display most-significant qubit first; q0 remains the least-significant bit.
        return "".join(str(self.measure(q)) for q in reversed(range(self.n)))

    def sample(self, shots: int) -> dict[str, int]:
        if shots < 1:
            raise ValueError("shots must be >= 1")
        counts: dict[str, int] = {}
        original = self.state[:]
        for _ in range(shots):
            self.state = original[:]
            key = self.measure_all()
            counts[key] = counts.get(key, 0) + 1
        self.state = original
        return counts

    def set_state(self, amplitudes: Iterable[complex]) -> None:
        values = [complex(a) for a in amplitudes]
        if len(values) != len(self.state):
            raise ValueError("amplitude count must equal 2**n_qubits")
        norm = sum(abs(a) ** 2 for a in values)
        if not math.isclose(norm, 1.0, rel_tol=1e-9, abs_tol=1e-9):
            raise ValueError(f"state must be normalized; norm squared is {norm}")
        self.state = values


def bell_state(seed: int | None = 1) -> StateVector:
    q = StateVector(2, seed=seed)
    q.h(0)
    q.cx(0, 1)
    return q


if __name__ == "__main__":
    q = bell_state()
    print("Aethernox state-vector simulator (software only)")
    print("Bell-state probabilities:", [round(p, 6) for p in q.probabilities()])
    print("1000-shot sample:", q.sample(1000))
