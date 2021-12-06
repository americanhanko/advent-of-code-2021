import glob
import os
import sys

import pytest


dirs = [os.path.abspath(os.path.dirname(path)) for path in sorted(glob.glob("*/tests"))]
scripts = [
    os.path.abspath(os.path.dirname(path)) for path in sorted(glob.glob("*/*.py"))
]

sys.path += dirs

for d in dirs:
    os.chdir(d)
    script = glob.glob("*.py")[0]
    # print(f"=== Day {os.path.basename(d)} ===")
    # with open(script) as fp:
    #     print(f"{script} ", end="")
    #     exec(fp.read())

    pytest.main(["--quiet", "-v"])
    print("")
