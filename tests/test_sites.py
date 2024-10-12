from pathlib import Path
from . import util


def test_all_sites():
    # iterate through subfolders from root
    root = Path(__file__).parent / "test_sites"
    for folder in root.glob("*"):
        # skip non-folders
        if not folder.is_dir():
            continue
        # build
        util.build_site(folder)