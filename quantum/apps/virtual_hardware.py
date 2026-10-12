import argparse, json
from quantum.sim.model_qk_virtual_hardware import VirtualHardware, VirtualHardwareConfig

p=argparse.ArgumentParser(description="Model QK virtual quantum hardware")
p.add_argument("--qubits",type=int,default=4)
p.add_argument("--shots",type=int,default=1024)
p.add_argument("--gate-error",type=float,default=0.0)
p.add_argument("--readout-error",type=float,default=0.0)
p.add_argument("--seed",type=int,default=20261011)
a=p.parse_args()
hw=VirtualHardware(VirtualHardwareConfig(qubits=a.qubits,gate_error=a.gate_error,
    readout_error=a.readout_error,seed=a.seed))
print(json.dumps({"capabilities":hw.capabilities(),"bell_counts":hw.run_bell(a.shots)},indent=2))
