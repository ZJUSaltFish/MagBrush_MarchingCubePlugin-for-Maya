# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QStandardPaths(__Shiboken.Object):
    # no doc
    def displayName(self, type): # real signature unknown; restored from __doc__
        """ displayName(type: PySide2.QtCore.QStandardPaths.StandardLocation) -> str """
        return ""

    def enableTestMode(self, testMode): # real signature unknown; restored from __doc__
        """ enableTestMode(testMode: bool) -> None """
        pass

    def findExecutable(self, executableName, paths, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ findExecutable(executableName: str, paths: typing.Sequence[str] = []) -> str """
        pass

    def isTestModeEnabled(self): # real signature unknown; restored from __doc__
        """ isTestModeEnabled() -> bool """
        return False

    def locate(self, type, fileName, options=None): # real signature unknown; restored from __doc__
        """ locate(type: PySide2.QtCore.QStandardPaths.StandardLocation, fileName: str, options: PySide2.QtCore.QStandardPaths.LocateOptions = PySide2.QtCore.QStandardPaths.LocateOption.LocateFile) -> str """
        return ""

    def locateAll(self, type, fileName, options=None): # real signature unknown; restored from __doc__
        """ locateAll(type: PySide2.QtCore.QStandardPaths.StandardLocation, fileName: str, options: PySide2.QtCore.QStandardPaths.LocateOptions = PySide2.QtCore.QStandardPaths.LocateOption.LocateFile) -> typing.List[str] """
        pass

    def setTestModeEnabled(self, testMode): # real signature unknown; restored from __doc__
        """ setTestModeEnabled(testMode: bool) -> None """
        pass

    def standardLocations(self, type): # real signature unknown; restored from __doc__
        """ standardLocations(type: PySide2.QtCore.QStandardPaths.StandardLocation) -> typing.List[str] """
        pass

    def writableLocation(self, type): # real signature unknown; restored from __doc__
        """ writableLocation(type: PySide2.QtCore.QStandardPaths.StandardLocation) -> str """
        return ""

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AppConfigLocation = PySide2.QtCore.QStandardPaths.StandardLocation.AppConfigLocation
    AppDataLocation = PySide2.QtCore.QStandardPaths.StandardLocation.AppDataLocation
    ApplicationsLocation = PySide2.QtCore.QStandardPaths.StandardLocation.ApplicationsLocation
    AppLocalDataLocation = PySide2.QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation
    CacheLocation = PySide2.QtCore.QStandardPaths.StandardLocation.CacheLocation
    ConfigLocation = PySide2.QtCore.QStandardPaths.StandardLocation.ConfigLocation
    DataLocation = PySide2.QtCore.QStandardPaths.StandardLocation.DataLocation
    DesktopLocation = PySide2.QtCore.QStandardPaths.StandardLocation.DesktopLocation
    DocumentsLocation = PySide2.QtCore.QStandardPaths.StandardLocation.DocumentsLocation
    DownloadLocation = PySide2.QtCore.QStandardPaths.StandardLocation.DownloadLocation
    FontsLocation = PySide2.QtCore.QStandardPaths.StandardLocation.FontsLocation
    GenericCacheLocation = PySide2.QtCore.QStandardPaths.StandardLocation.GenericCacheLocation
    GenericConfigLocation = PySide2.QtCore.QStandardPaths.StandardLocation.GenericConfigLocation
    GenericDataLocation = PySide2.QtCore.QStandardPaths.StandardLocation.GenericDataLocation
    HomeLocation = PySide2.QtCore.QStandardPaths.StandardLocation.HomeLocation
    LocateDirectory = PySide2.QtCore.QStandardPaths.LocateOption.LocateDirectory
    LocateFile = PySide2.QtCore.QStandardPaths.LocateOption.LocateFile
    LocateOption = None # (!) real value is "<class 'PySide2.QtCore.QStandardPaths.LocateOption'>"
    LocateOptions = None # (!) real value is "<class 'PySide2.QtCore.QStandardPaths.LocateOptions'>"
    MoviesLocation = PySide2.QtCore.QStandardPaths.StandardLocation.MoviesLocation
    MusicLocation = PySide2.QtCore.QStandardPaths.StandardLocation.MusicLocation
    PicturesLocation = PySide2.QtCore.QStandardPaths.StandardLocation.PicturesLocation
    RuntimeLocation = PySide2.QtCore.QStandardPaths.StandardLocation.RuntimeLocation
    StandardLocation = None # (!) real value is "<class 'PySide2.QtCore.QStandardPaths.StandardLocation'>"
    TempLocation = PySide2.QtCore.QStandardPaths.StandardLocation.TempLocation


