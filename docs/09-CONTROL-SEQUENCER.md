# Model K Control Sequencer

Conceptual multi-cycle sequence:

FETCH -> DECODE -> OPERAND READ -> EXECUTE -> WRITEBACK -> FLAGS -> NEXT -> FETCH

HALT transitions to a halted state until reset. The reference RTL collapses basic instruction behavior into a single active clock edge.
