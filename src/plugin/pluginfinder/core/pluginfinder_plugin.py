import mobase
from ....base.base_plugin import BasePlugin
from .pluginfinder import PluginFinder
from ....common.common_qt import *

class PluginFinderPlugin(BasePlugin):
    """Base Plugin Finder plugin, to be inherited by all other plugins."""

    def __init__(self):
        super().__init__("PluginFinder", "Plugin Finder", mobase.VersionInfo(2, 0, 1))

    def init(self, organiser:mobase.IOrganizer):
        self._pluginFinder = PluginFinder(organiser)
        return super().init(organiser)

    def __tr(self, trstr):
        return QCoreApplication.translate(self._pluginName, trstr)
    
    def settings(self):
        """ Current list of game settings for Mod Organizer. """
        baseSettings = super().settings()
        customSettings = [
            mobase.PluginSetting("priority", self.__tr("The priority of the installer module for installing plugins."), 120)
            ]
        for setting in customSettings:
            baseSettings.append(setting)
        return baseSettings
        