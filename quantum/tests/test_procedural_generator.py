import unittest
from quantum.apps.procedural_generator import Config, Generator

class TestProceduralGenerator(unittest.TestCase):
    def test_reproducible(self):
        c=Config(42,4,5,"random")
        self.assertEqual(Generator(c).generate(),Generator(c).generate())
    def test_seed_changes_random(self):
        self.assertNotEqual(Generator(Config(1,4,5,"random")).generate(),
                            Generator(Config(2,4,5,"random")).generate())
    def test_qft(self):
        s=Generator(Config(1,3,1,"qft")).generate()
        self.assertIn("cp(",s); self.assertIn("swap q[0], q[2];",s)
    def test_variational(self):
        s=Generator(Config(7,3,2,"variational")).generate()
        self.assertIn("ry(",s); self.assertIn("cx q[0], q[1];",s)
    def test_grover_requires_two(self):
        with self.assertRaises(ValueError): Generator(Config(1,1,1,"grover")).generate()

if __name__=="__main__": unittest.main()
