import json
import os
import re
from pathlib import Path
pins = json.loads(Path("dependencies.json").read_text())["source_revisions"]
with open(os.environ["GITHUB_OUTPUT"], "a") as output:
    for owner, revision in pins.items():
        if not isinstance(revision, str) or not re.fullmatch("[0-9a-f]{40}", revision):
            raise SystemExit("Missing accepted source revision: " + owner)
        output.write(owner.lower() + "=" + revision + "\n")
