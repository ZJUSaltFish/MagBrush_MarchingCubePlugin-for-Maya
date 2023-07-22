# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QCommandLineOption(__sip.simplewrapper):
    """
    QCommandLineOption(name: str)
    QCommandLineOption(names: Iterable[str])
    QCommandLineOption(name: str, description: str, valueName: str = '', defaultValue: str = '')
    QCommandLineOption(names: Iterable[str], description: str, valueName: str = '', defaultValue: str = '')
    QCommandLineOption(other: QCommandLineOption)
    """
    def defaultValues(self): # real signature unknown; restored from __doc__
        """ defaultValues(self) -> List[str] """
        return []

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QCommandLineOption.Flags """
        pass

    def isHidden(self): # real signature unknown; restored from __doc__
        """ isHidden(self) -> bool """
        return False

    def names(self): # real signature unknown; restored from __doc__
        """ names(self) -> List[str] """
        return []

    def setDefaultValue(self, defaultValue): # real signature unknown; restored from __doc__
        """ setDefaultValue(self, defaultValue: str) """
        pass

    def setDefaultValues(self, defaultValues, p_str=None): # real signature unknown; restored from __doc__
        """ setDefaultValues(self, defaultValues: Iterable[str]) """
        pass

    def setDescription(self, description): # real signature unknown; restored from __doc__
        """ setDescription(self, description: str) """
        pass

    def setFlags(self, aflags, QCommandLineOption_Flags=None, QCommandLineOption_Flag=None): # real signature unknown; restored from __doc__
        """ setFlags(self, aflags: Union[QCommandLineOption.Flags, QCommandLineOption.Flag]) """
        pass

    def setHidden(self, hidden): # real signature unknown; restored from __doc__
        """ setHidden(self, hidden: bool) """
        pass

    def setValueName(self, name): # real signature unknown; restored from __doc__
        """ setValueName(self, name: str) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QCommandLineOption) """
        pass

    def valueName(self): # real signature unknown; restored from __doc__
        """ valueName(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    HiddenFromHelp = 1
    ShortOptionStyle = 2


