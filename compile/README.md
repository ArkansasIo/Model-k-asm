# Model K Compiled Reference Build

Portable native C reference implementation of the Model K logical semantics.

Build:
    make

Test:
    make test

This executable is a **reference build**, not a claim that the host binary is
the physical Model K CPU image. The RTL and assembly remain authoritative for
hardware implementation.

Architecture covered by this build:
- 8-bit reference CPU model
- 20-bit logical arithmetic
- 20-byte record model
- magnetic-core memory abstraction
- quantum QISA boundary identification
