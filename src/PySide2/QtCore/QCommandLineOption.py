# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QCommandLineOption(__Shiboken.Object):
    """
    QCommandLineOption(self, name: str) -> None
    QCommandLineOption(self, name: str, description: str, valueName: str = '', defaultValue: str = '') -> None
    QCommandLineOption(self, names: typing.Sequence[str]) -> None
    QCommandLineOption(self, names: typing.Sequence[str], description: str, valueName: str = '', defaultValue: str = '') -> None
    QCommandLineOption(self, other: PySide2.QtCore.QCommandLineOption) -> None
    """
    def defaultValues(self): # real signature unknown; restored from __doc__
        """ defaultValues(self) -> typing.List[str] """
        pass

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtCore.QCommandLineOption.Flags """
        pass

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def names(self): # real signature unknown; restored from __doc__
        """ names(self) -> typing.List[str] """
        pass

    def setDefaultValue(self, defaultValue): # real signature unknown; restored from __doc__
        """ setDefaultValue(self, defaultValue: str) -> None """
        pass

    def setDefaultValues(self, defaultValues, p_str=None): # real signature unknown; restored from __doc__
        """ setDefaultValues(self, defaultValues: typing.Sequence[str]) -> None """
        pass

    def setDescription(self, description): # real signature unknown; restored from __doc__
        """ setDescription(self, description: str) -> None """
        pass

    def setFlags(self, aflags): # real signature unknown; restored from __doc__
        """ setFlags(self, aflags: PySide2.QtCore.QCommandLineOption.Flags) -> None """
        pass

    def setHidden(self, hidden): # real signature unknown; restored from __doc__
        """ setHidden(self, hidden: bool) -> None """
        pass

    def setValueName(self, name): # real signature unknown; restored from __doc__
        """ setValueName(self, name: str) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtCore.QCommandLineOption) -> None """
        pass

    def valueName(self): # real signature unknown; restored from __doc__
        """ valueName(self) -> str """
        return ""

    def __init__(self, name): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Flag = None # (!) real value is "<class 'PySide2.QtCore.QCommandLineOption.Flag'>"
    Flags = None # (!) real value is "<class 'PySide2.QtCore.QCommandLineOption.Flags'>"
    HiddenFromHelp = PySide2.QtCore.QCommandLineOption.Flag.HiddenFromHelp
    ShortOptionStyle = PySide2.QtCore.QCommandLineOption.Flag.ShortOptionStyle


