from pathlib import Path
import subprocess


def test_all_sites():
    # iterate through subfolders from root
    root = Path(__file__).parent / "test_sites"
    for folder in root.glob("*"):
        # skip non-folders
        if not folder.is_dir():
            continue
        # skip artefacts
        # run mkdocs build in that folder
        proc = subprocess.Popen(
            args=["mkdocs", "build"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=folder.absolute()
        )
        stdout, stderr = proc.communicate()
        # print stdout
        print(stdout)
        # make sure it ran
        assert proc.returncode == 0, (
            f"Build failed in folder {folder}, reason: {stderr}"
        )