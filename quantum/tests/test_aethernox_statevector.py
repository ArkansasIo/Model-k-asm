import math
import unittest
from quantum.sim.aethernox_statevector import StateVector, bell_state


class StateVectorTests(unittest.TestCase):
    def test_initial_state(self):
        q = StateVector(3)
        self.assertEqual(q.probabilities(), [1.0] + [0.0] * 7)
        self.assertAlmostEqual(q.norm(), 1.0)

    def test_x_gate(self):
        q = StateVector(1)
        q.x(0)
        self.assertAlmostEqual(q.probabilities()[1], 1.0)

    def test_h_then_h_is_identity(self):
        q = StateVector(1)
        q.h(0)
        q.h(0)
        self.assertAlmostEqual(q.probabilities()[0], 1.0)
        self.assertAlmostEqual(q.probabilities()[1], 0.0)

    def test_bell_state(self):
        q = bell_state(seed=2)
        p = q.probabilities()
        self.assertAlmostEqual(p[0], 0.5)
        self.assertAlmostEqual(p[3], 0.5)
        self.assertAlmostEqual(p[1], 0.0)
        self.assertAlmostEqual(p[2], 0.0)

    def test_cx_flips_target_when_control_one(self):
        q = StateVector(2)
        q.x(0)
        q.cx(0, 1)
        self.assertAlmostEqual(q.probabilities()[3], 1.0)

    def test_measurement_collapse(self):
        q = StateVector(1, seed=1)
        q.h(0)
        result = q.measure(0)
        self.assertIn(result, (0, 1))
        self.assertAlmostEqual(q.norm(), 1.0)
        self.assertAlmostEqual(q.probabilities()[result], 1.0)

    def test_invalid_qubit(self):
        q = StateVector(2)
        with self.assertRaises(ValueError):
            q.x(2)

    def test_normalized_custom_state(self):
        q = StateVector(1)
        q.set_state([1/math.sqrt(2), 1j/math.sqrt(2)])
        self.assertAlmostEqual(q.norm(), 1.0)


if __name__ == "__main__":
    unittest.main()
