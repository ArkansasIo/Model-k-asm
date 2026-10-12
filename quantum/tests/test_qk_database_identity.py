"""Identity and data-format regression tests."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class TestRepositoryIdentity(unittest.TestCase):
    def test_registry_exists(self):
        self.assertTrue((ROOT / "docs" / "PROJECT_ID_REGISTRY.md").exists())

    def test_source_manifest_exists(self):
        self.assertTrue((ROOT / "docs" / "SOURCE_FILE_MANIFEST.md").exists())

    def test_quantum_tree_exists(self):
        self.assertTrue((ROOT / "quantum" / "apps").exists())
        self.assertTrue((ROOT / "quantum" / "hardware" / "virtual").exists())

if __name__ == "__main__":
    unittest.main()
