# Model QK Quantum Subsystem

The quantum subsystem is a software-defined research layer for Model QK. It separates classical control, QISA, circuit generation, compilation, scheduling, virtual hardware, simulation, and future physical backends.

Architecture: Application -> Procedural Generator -> OpenQASM/QISA -> Compiler -> Scheduler -> Backend -> Results

Backends include QK-VQPU virtual hardware, exact state-vector simulation, and future superconducting, trapped-ion, neutral-atom, and photonic adapters.

The virtual hardware is software-only. It models topology, gate/readout error, seeded execution, and capability metadata; it does not claim physical device measurements.

Current applications: quantum/apps/procedural_generator.py and quantum/apps/virtual_hardware.py.

Verification uses Python unittest discovery from the repository root. Physical-device claims require separate laboratory measurements.
