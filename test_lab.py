"""Independent observable assertions for the synthetic ledger example."""
import unittest
from lab import run

class RecoveryTests(unittest.TestCase):
    def test_guarded_retry_commits_once(self):
        event = run(True)
        self.assertEqual(event["commits"], 1)
        self.assertTrue(event["exactly_once"])
        self.assertEqual(event["first_receipt"], event["retry_receipt"])

    def test_broken_retry_is_caught(self):
        event = run(False)
        self.assertEqual(event["commits"], 2)
        self.assertFalse(event["exactly_once"])

if __name__ == "__main__":
    unittest.main()
