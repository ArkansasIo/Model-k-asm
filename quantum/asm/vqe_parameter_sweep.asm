; Model K QISA variational-circuit control sketch
; Host supplies theta parameters and evaluates measured energy classically.
QALLOC Q0, 2
PARAM theta0
PARAM theta1
RY Q0[0], theta0
CX Q0[0], Q0[1]
RZ Q0[1], theta1
MEASURE Q0[0], C0[0]
MEASURE Q0[1], C0[1]
HOST_CALLBACK ENERGY_ESTIMATE, C0, theta0, theta1
HALT
