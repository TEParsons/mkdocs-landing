from mkdocs.plugins import BasePlugin
from mkdocs.config import Config
from mkdocs.config import config_options
from importlib.metadata import entry_points


class LandingPresetsPluginConfig(Config):
    """
    Config subclass for LandingPresetsPlugin.
    """
    name = config_options.Choice(choices=["default"])


class LandingPresetsPlugin(BasePlugin[LandingPresetsPluginConfig]):
    """
    Plugin which allows the user to specify a preset configuration for the Landing theme by name 
    alone.
    """
    # dictionary mapping names to preset objects
    presets = {}

    def __init__(self):
        # load presets
        for ep in entry_points(group="mkdocs_landing.presets"):
            # get this preset
            cls = ep.load()
            # add this preset to the list of available names
            LandingPresetsPluginConfig.name.choices.append(ep.name)
            # map this preset against its name
            LandingPresetsPlugin.presets[ep.name] = cls    

    def on_config(self, config):
        # if default chosen, do nothing
        if self.config.name == "default":
            return config
        # get chosen preset
        print(self.config)
        preset = self.presets[self.config.name]
        # apply preset to config
        for key in preset.config:
            config['theme'][key] = preset.config[key]

        return config



