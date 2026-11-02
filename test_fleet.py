import unittest
import os
import shutil
from fleet_core import GrokBotWorkspaceFleet, AgentCue, CueDispatcher

class TestGrokBotFleet(unittest.TestCase):
    def setUp(self):
        self.test_dir = "/tmp/test_grokbot_cue_workspace"
        os.makedirs(self.test_dir, exist_ok=True)
        self.dispatcher = CueDispatcher(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_cue_dispatch_execution(self):
        cue = AgentCue(
            name="TestCue",
            target_repo=self.test_dir,
            action_type="test",
            instruction="Validate test execution flow"
        )
        res = self.dispatcher.dispatch(cue)
        self.assertEqual(res["status"], "completed")
        self.assertEqual(res["cue"], "TestCue")
        self.assertIn("duration_s", res)

    def test_fleet_sprint(self):
        fleet = GrokBotWorkspaceFleet()
        cues = [
            AgentCue("Cue1", self.test_dir, "audit", "Check memory limits"),
            AgentCue("Cue2", self.test_dir, "code", "Generate baseline worker")
        ]
        results = fleet.run_sprint(cues)
        self.assertEqual(len(results), 2)
        self.assertTrue(all(r["status"] == "completed" for r in results))

if __name__ == "__main__":
    unittest.main()
