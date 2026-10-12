"""QK-VQPU capability and device descriptor.

Program ID: QK-QVHW-0001
File ID: QK-QVHW-0001-FILE-0002
Version: QK.2.0.0
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class VQPUConfig:
    device_id: str = "QK-VQPU-4"
    qubits: int = 4
    topology: str = "linear"
    gate_error: float = 0.0
    readout_error: float = 0.0
    software_only: bool = True

    def capabilities(self):
        return {
            "device_id": self.device_id,
            "qubits": self.qubits,
            "topology": self.topology,
            "supported_gates": ["X","H","CX","CZ","SWAP","RESET","MEASURE"],
            "gate_error": self.gate_error,
            "readout_error": self.readout_error,
            "software_only": self.software_only,
        }
