# Model QK Virtual Hardware Design

Pipeline:

Circuit/QISA -> compiler -> virtual device -> topology -> noise model -> measurement -> classical result

The simulator separates logical circuit semantics from topology constraints,
stochastic gate errors, readout errors, and result provenance.

The virtual device is deterministic when a seed is supplied and provides a
capability contract that future physical adapters can implement.

Research uses include compiler regression, topology routing, scheduling,
noise sensitivity, algorithm comparison, and error-correction experiments.

Virtual results must never be presented as measured physical-hardware results.
