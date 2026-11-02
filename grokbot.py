#!/usr/bin/env python3
import sys
import json
from fleet_core import GrokBotWorkspaceFleet, AgentCue

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 grokbot.py [run-cue|status|health]")
        sys.exit(0)

    cmd = sys.argv[1]
    fleet = GrokBotWorkspaceFleet()

    if cmd == "run-cue":
        name = sys.argv[2] if len(sys.argv) > 2 else "ManualCue"
        target = sys.argv[3] if len(sys.argv) > 3 else "/home/aizatfir/projects/Eden-Dominion"
        cue = AgentCue(name=name, target_repo=target, action_type="code", instruction="Autonomous code sprint via GrokBot-Cue")
        res = fleet.run_sprint([cue])
        print(json.dumps(res, indent=2))
    elif cmd == "status":
        print(json.dumps({"status": "ready", "engine": "GrokBot-Cue-Fleet", "version": "1.0.0"}, indent=2))
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
