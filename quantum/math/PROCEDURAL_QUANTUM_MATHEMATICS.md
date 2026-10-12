# Procedural Quantum Mathematics

Configuration:
G = (s,n,d,a,theta)

Seeded generation:
r_k = PRNG(s,k)

Variational parameter:
theta_(l,q) = theta * sin((l+1)(q+1))

Ideal state evolution:
|psi_(k+1)> = U_k |psi_k>

Normalization:
<psi|psi> = 1

Measurement:
P(x) = |<x|psi>|^2
sum_x P(x) = 1

QFT:
|x> -> 1/sqrt(2^n) sum_y exp(2*pi*i*x*y/2^n)|y>

Future optimizer objective:
J = w_d D + w_2 N_2 + w_e E + w_c C

D = circuit depth
N_2 = two-qubit gate count
E = estimated error cost
C = classical-control cost
