"""End-to-end software pipeline tests.

Test ID: QK-QTST-0001-FILE-0002
Version: QK.2.0.0
"""

import unittest

from quantum.compiler.model_qk_compiler import linear_route
from quantum.scheduler.model_qk_scheduler import ModelQKScheduler, QuantumJob
from quantum.backend.model_qk_simulator_backend import bell_state


class TestQKPipeline(unittest.TestCase):
    def test_linear_compilation(self):
        self.assertEqual(linear_route([("H", 0), ("CX", 0, 1)], 4)[1], ("CX", 0, 1))

    def test_scheduler_priority(self):
        scheduler = ModelQKScheduler()
        scheduler.submit(QuantumJob(10, "slow"))
        scheduler.submit(QuantumJob(1, "fast"))
        self.assertEqual(scheduler.next_job().job_id, "fast")

    def test_bell_distribution_support(self):
        result = bell_state(128, 7)
        self.assertEqual(result["shots"], 128)
        self.assertEqual(sum(result["counts"].values()), 128)


if __name__ == "__main__":
    unittest.main()
