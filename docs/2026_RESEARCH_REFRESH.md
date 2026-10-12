# Aethernox / Model K — 2026 Research Refresh

**Research snapshot:** 11 October 2026  
**Scope:** Classical architecture, memory, records, storage interfaces, hardware roadmap.  
**Quantum scope:** The quantum tree is included as a separate software/hardware-interface research layer; it remains decoupled from the classical memory and CPU specifications.

## Executive summary

The repository began as an educational Model K design: an 8-bit reference CPU, Boolean gates, K2 adder, ALU, registers, RTL, assembly routines, 20-bit logical values, 20-byte records, and a separate quantum instruction interface. For a current 2026 research direction, retain that baseline as **Model K v1** and introduce **Aethernox v2** as a versioned 64-bit logical-data and modern-memory architecture. Do not silently reinterpret existing record bytes or claim the old CPU is natively 64-bit.

## Current technology position

- **SRAM / FPGA block RAM:** appropriate for low-latency working storage, register files, caches, queues, and small buffers.
- **DDR5 / LPDDR5-family DRAM:** appropriate for general-purpose main memory where capacity and bandwidth matter; select an actual interface based on the chosen FPGA/SoC and board.
- **HBM:** specialized high-bandwidth memory for suitable accelerator-class platforms, not a default requirement for this small experimental CPU.
- **NAND flash with NVMe:** appropriate for persistent bulk storage and program images. The project should specify a standard storage interface rather than inventing a flash protocol.
- **MRAM:** relevant as a modern non-volatile magnetic-memory research option. It is physically and electrically distinct from historical ferrite magnetic-core memory.
- **CXL / memory expansion:** a future research extension for platforms that support coherent memory expansion/pooling; not a requirement for the first prototype.
- **Ferrite magnetic-core memory:** retain as a historical experimental subsystem for characterizing destructive read, rewrite, addressing, sense circuitry, retention, and reliability. It is not the recommended mainstream memory for the 2026 prototype.

These are architecture-level choices. Actual part selection, bandwidth, latency, endurance, and cost must be measured from current vendor datasheets and the chosen board's capabilities.

## Current research references

1. NVMe Express, *NVM Express Base Specification*, Revision 2.4, ratified 31 July 2026: https://nvmexpress.org/specification/nvm-express-base-specification/
2. PCI-SIG, *PCI Express Base Specification Revision 7.1*, dated 17 September 2026: https://pcisig.com/specification-overview/pci-express-base
3. AMD, *Memory technologies for adaptive SoCs and FPGAs* (on-chip RAM, HBM, DDR5/LPDDR interfaces): https://www.amd.com/en/products/adaptive-socs-and-fpgas/technologies/memory.html
4. SNIA, *The Rebirth of Persistent Memory*, 23 September 2026, discussing CXL-enabled memory expansion and pooling: https://www.snia.org/blog/2026/rebirth-persistent-memory
5. *Next-generation MRAM technologies and their emerging roles in artificial intelligence*, Journal of Magnetism and Magnetic Materials, volume 655, 1 October 2026: https://www.sciencedirect.com/science/article/abs/pii/S0304885326005007
6. *Interface-Engineered STT-MRAM for Device-to-Device Variation-Aware, Energy-Efficient, and Reliable Computing-in-Memory Arrays*, IEEE Transactions on Electron Devices, July 2026: https://doi.org/10.1109/TED.2026.3692177

Research references establish the state of the field; they do not mean the corresponding technologies are implemented in this repository.

## Migration rules

1. Preserve current behavior and schemas under the **Model K v1** compatibility label.
2. Define a separate **Aethernox v2** record schema with a 64-bit logical value.
3. Use explicit schema identifiers and version fields; never infer a schema solely from a record's contents.
4. Define byte order explicitly for all multi-byte fields.
5. Add golden test vectors for serialization, deserialization, checksums, range checks, and corruption cases.
6. Keep logical word width distinct from CPU datapath width and physical record length.
7. Treat SRAM/BRAM, DRAM, NAND/NVMe, MRAM, and ferrite core as distinct backends with a common abstract memory interface.
8. Keep the quantum subsystem separate; this refresh does not modify files under `quantum/`.

## Required engineering work still outstanding

This document is a research refresh and migration policy. It does not certify that every legacy ASM routine, RTL module, or C implementation has been converted to 64-bit. Each implementation must be changed and tested against the v2 specification before it is labelled 64-bit compatible.


## Quantum architecture refresh

Model QK now treats quantum execution as a layered subsystem: procedural application generation, OpenQASM/QISA representation, compiler, topology mapping, scheduler, backend contract, virtual hardware, state-vector simulation, and future physical platform adapters. The reference virtual device is QK-VQPU. Virtual results are software-model results and must not be presented as laboratory measurements.
