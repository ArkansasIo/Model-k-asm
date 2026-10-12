from __future__ import annotations
from dataclasses import dataclass, field
import random
from quantum.sim.aethernox_statevector import StateVector

@dataclass
class VirtualHardwareConfig:
    name: str = "QK-VQPU-4"
    qubits: int = 4
    topology: str = "linear"
    gate_error: float = 0.0
    readout_error: float = 0.0
    seed: int = 20261011

@dataclass
class VirtualHardware:
    config: VirtualHardwareConfig
    rng: random.Random = field(init=False)
    q: StateVector = field(init=False)

    def __post_init__(self):
        if not 1 <= self.config.qubits <= 24: raise ValueError("qubits must be 1..24")
        if not 0 <= self.config.gate_error <= 1: raise ValueError("gate_error must be 0..1")
        if not 0 <= self.config.readout_error <= 1: raise ValueError("readout_error must be 0..1")
        self.rng = random.Random(self.config.seed)
        self.reset()

    def reset(self):
        self.q = StateVector(self.config.qubits, seed=self.config.seed)

    def _noise(self):
        return self.rng.random() < self.config.gate_error

    def x(self, q):
        if not self._noise(): self.q.x(q)
        else: self.q.x(q); self.q.z(q)

    def h(self, q):
        if not self._noise(): self.q.h(q)
        else: self.q.h(q); self.q.x(q)

    def cx(self, a, b):
        if self.config.topology == "linear" and abs(a-b) != 1:
            raise ValueError("linear topology permits CX only between adjacent qubits")
        if not self._noise(): self.q.cx(a,b)
        else: self.q.cx(a,b); self.q.z(b)

    def measure_all(self):
        bits = self.q.measure_all()
        out=[]
        for bit in bits:
            if self.rng.random() < self.config.readout_error:
                bit = "1" if bit == "0" else "0"
            out.append(bit)
        return "".join(out)

    def run_bell(self, shots=1024):
        counts={"00":0,"01":0,"10":0,"11":0}
        for _ in range(shots):
            self.reset(); self.h(0); self.cx(0,1)
            key=self.measure_all()[-2:]
            counts[key]+=1
        return counts

    def capabilities(self):
        return {"name":self.config.name,"qubits":self.config.qubits,
                "topology":self.config.topology,
                "gate_error":self.config.gate_error,
                "readout_error":self.config.readout_error,
                "supported_gates":["X","H","CX","MEASURE","RESET"],
                "software_only":True}
