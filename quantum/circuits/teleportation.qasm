OPENQASM 3.0;
include "stdgates.inc";
qubit[3] q;
bit[2] mid;
bit out;
// For a runnable test, prepare a known input state instead of an unknown state.
ry(pi/3) q[0];
h q[1];
cx q[1], q[2];
cx q[0], q[1];
h q[0];
mid[0] = measure q[0];
mid[1] = measure q[1];
if (mid[1]) { x q[2]; }
if (mid[0]) { z q[2]; }
out = measure q[2];
