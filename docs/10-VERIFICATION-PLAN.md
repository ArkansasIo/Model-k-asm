# Model K Verification Plan

- Exhaustively test all four input combinations for each 2-input gate.
- Exhaustively test K2 sums and carry-in values.
- Test 8-bit add/subtract/multiply across boundary values and randomized pairs.
- Check divide-by-zero behavior (reference ALU returns 0xFF).
- Check Zero=(Y==0), Negative=Y[7], and signed overflow equations.
- Verify memory writes at record boundaries do not corrupt adjacent records.
