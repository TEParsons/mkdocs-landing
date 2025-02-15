import yaml
from pathlib import Path
from inspect import getfile
from mkdocs.config import defaults, config_options


class BaseLandingPreset:
    """
    Base class for a Landing configuration. To add a configuration, create a subclass and overwrite 
    the attribute `file` with the path (relative to the file your subclass is defined in) of a 
    `.yml` file containing the configuration of your preset. This can be a string or a 
    `pathlib.Path` object.

    The `.yml` file should contain the same stuff you'd put under `theme` in an `mkdocs.yaml` file.
    """
    file = None

    def __init_subclass__(cls):
        # make sure we have a file
        assert cls.file is not None, "LandingPreset must have a yml file defined with its config."
        # make sure config file is a Path
        cls.file = Path(cls.file)
        # make file attribute absolute (relative to class def file)
        if not cls.file.is_absolute():
            cls.file = Path(getfile(cls)).parent / cls.file
        # load config file
        with cls.file.open("r") as f:
            cls.config = yaml.load(f, yaml.SafeLoader)
        # initalize as normal
        super().__init_subclass__()
