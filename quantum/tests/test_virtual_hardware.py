import unittest
from quantum.sim.model_qk_virtual_hardware import VirtualHardware, VirtualHardwareConfig

class TestVirtualHardware(unittest.TestCase):
    def test_ideal_bell_only_00_11(self):
        h=VirtualHardware(VirtualHardwareConfig(qubits=2,seed=1))
        c=h.run_bell(200)
        self.assertEqual(c["01"],0); self.assertEqual(c["10"],0)
        self.assertEqual(c["00"]+c["11"],200)
    def test_linear_topology(self):
        h=VirtualHardware(VirtualHardwareConfig(qubits=4))
        h.reset()
        with self.assertRaises(ValueError): h.cx(0,2)
    def test_capabilities(self):
        self.assertTrue(VirtualHardware(VirtualHardwareConfig()).capabilities()["software_only"])
    def test_reproducible(self):
        c=VirtualHardwareConfig(qubits=2,seed=7)
        self.assertEqual(VirtualHardware(c).run_bell(50),VirtualHardware(c).run_bell(50))

if __name__=="__main__": unittest.main()
