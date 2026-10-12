# Aethernox 2026 Hardware and Memory Implementation Plan

## Goal

Move from the Model K reference design toward a reproducible experimental system using modern memory interfaces while retaining a separate historical magnetic-core experiment.

## Recommended prototype hierarchy

1. FPGA block RAM or SRAM for initial deterministic working memory.
2. DDR5/LPDDR-compatible controller only if supported by the selected FPGA/SoC board and required by capacity/bandwidth.
3. NVMe SSD for persistent bulk storage through an existing host interface.
4. Optional MRAM research board/device to investigate non-volatile memory behavior.
5. Separate ferrite magnetic-core bench experiment, with safe current-limited drivers and sense-amplifier characterization.
6. Optional CXL/memory-fabric research only after a platform and use case justify it.

## Measurement plan

For each backend, measure:
- read/write latency distribution
- sustained throughput
- energy per operation if instrumentation supports it
- error rate and checksum failures
- persistence after power interruption where relevant
- endurance/write limits from vendor specifications and testing
- temperature and supply-voltage conditions
- controller overhead and queue depth

Report test conditions, board/device model, firmware, toolchain version, sample size, and raw data. Do not copy headline figures from vendor pages as measured Aethernox results.

## Milestones

- H0: select FPGA/SoC platform and freeze interfaces.
- H1: implement memory abstraction and BRAM backend.
- H2: pass randomized and boundary memory tests.
- H3: implement a storage adapter for the host/NVMe layer.
- H4: create 64-byte record serializer and v1-to-v2 converter.
- H5: characterize optional MRAM or ferrite-core hardware.
- H6: publish benchmark scripts, raw measurements, and reproducibility notes.

## Research basis as of 11 October 2026

NVMe 2.4 was ratified on 31 July 2026. PCI-SIG lists PCI Express Base Specification 7.1 dated 17 September 2026. FPGA vendors document on-chip block RAM, external DDR/LPDDR, and HBM options. 2026 MRAM literature studies STT/SOT and other magnetic memory mechanisms for non-volatile and compute-in-memory use. These technologies are distinct and should not be represented as interchangeable at the physical level.

References:
- https://nvmexpress.org/specification/nvm-express-base-specification/
- https://pcisig.com/specification-overview/pci-express-base
- https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/memory.html
- https://www.snia.org/blog/2026/rebirth-persistent-memory
- https://www.sciencedirect.com/science/article/abs/pii/S0304885326005007
