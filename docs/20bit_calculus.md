# Model K Calculus / Physical Timing Model

Digital Boolean state is discrete, while a physical implementation has continuous voltage, current, propagation delay, and power.

For node voltage V(t):
I(t)=C dV/dt
V(t)=V(t0)+(1/C) integral[t0..t] I(tau) dt

First-order RC transition:
V(t)=V_final+(V_initial-V_final)e^(-t/(RC))
tau=RC
t_r(10%-90%) ~= 2.2RC

Dynamic power:
P_dynamic ~= alpha C V^2 f

Synchronous timing:
T_clock >= t_clk-q + t_comb + t_setup + t_skew
f_max <= 1/T_clock

These equations form the continuous-time layer around the Model K gate, RTL, and assembly model.