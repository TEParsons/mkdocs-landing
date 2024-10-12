import subprocess
from pathlib import Path


def build_site(folder: Path):
    """
    Build a site from its folder dir, and assert that it ran.

    Parameters
    ----------
    folder : Path
        Director to build site from
    """
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