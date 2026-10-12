# Aethernox Quantum Roadmap — 2026

## Milestones and exit criteria

### Q0 — Reproducible software baseline
- State-vector simulator supports X/Y/Z/H/S/T, rotations, CX/CZ/SWAP, measurement, normalization, and seeded sampling.
- Unit tests cover gate semantics and measurement collapse.
- Exit: tests pass locally and a sample Bell circuit produces only 00/11 with approximately equal frequencies.

### Q1 — Circuit and backend contract
- Define a versioned circuit IR and backend interface.
- Add capability negotiation: gate set, qubit count, topology, shot limits, measurement model, queue/job states.
- Exit: same circuit runs through local simulator adapter and a mock backend.

### Q2 — Compiler
- Validate qubit indices and circuit parameters.
- Lower high-level operations to backend-native gates.
- Route two-qubit gates to the target connectivity graph.
- Track circuit depth, two-qubit gate count, and estimated error budget.
- Exit: compiler output and resource estimate are deterministic and tested.

### Q3 — Noise models and benchmarking
- Add configurable depolarizing, readout, amplitude-damping, and phase-damping models with clearly stated assumptions.
- Add repeatable benchmark suites and statistical confidence intervals.
- Exit: seeded tests validate distributions; benchmark reports include shots, seed, circuit, and model parameters.

### Q4 — Error correction
- Implement stabilizer/syndrome representations and at least one small-code simulation.
- Add decoder interface and tests for injected bit/phase errors.
- Exit: recovery succeeds for the code's designed correctable error cases in simulation.

### Q5 — Physical platform decision
- Compare superconducting, trapped-ion, neutral-atom, and photonic platforms for one selected workload.
- Obtain vendor/platform specifications, total-cost estimates, lab requirements, maintenance requirements, and safety review.
- Exit: approved platform decision record with explicit assumptions.

### Q6 — Hardware integration
- Implement vendor-specific control and readout adapters only after hardware selection.
- Validate calibration, reset, measurement, timing, and feed-forward.
- Exit: a documented circuit executes on actual hardware; data is tagged as hardware-derived.

### Q7 — Logical-qubit demonstration
- Perform repeated syndrome extraction and decoding.
- Report physical vs logical error rate with confidence intervals and full methodology.
- Exit: independently reproducible result; do not infer fault tolerance merely from a successful circuit.

## 2026 research notes

Fault-tolerant design is increasingly shaped by error correction, qubit loss/leakage, mid-circuit measurement and reuse, control overhead, and logical rather than raw physical-qubit metrics. Neutral-atom research reported key fault-tolerant architecture components using arrays up to 448 atoms; trapped-ion research in July 2026 reported a single-ion encoded logical-qubit correction experiment. These results illustrate different approaches and should not be conflated into a single assumed hardware design.

References:
- https://www.nature.com/articles/s41586-025-09848-5
- https://www.nature.com/articles/s41567-026-03315-2
- https://arxiv.org/abs/2607.21554
- https://arxiv.org/abs/2609.10079
