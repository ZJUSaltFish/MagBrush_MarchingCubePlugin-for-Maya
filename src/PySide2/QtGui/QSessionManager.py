# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSessionManager(__PySide2_QtCore.QObject):
    # no doc
    def allowsErrorInteraction(self): # real signature unknown; restored from __doc__
        """ allowsErrorInteraction(self) -> bool """
        return False

    def allowsInteraction(self): # real signature unknown; restored from __doc__
        """ allowsInteraction(self) -> bool """
        return False

    def cancel(self): # real signature unknown; restored from __doc__
        """ cancel(self) -> None """
        pass

    def discardCommand(self): # real signature unknown; restored from __doc__
        """ discardCommand(self) -> typing.List[str] """
        pass

    def isPhase2(self): # real signature unknown; restored from __doc__
        """ isPhase2(self) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> None """
        pass

    def requestPhase2(self): # real signature unknown; restored from __doc__
        """ requestPhase2(self) -> None """
        pass

    def restartCommand(self): # real signature unknown; restored from __doc__
        """ restartCommand(self) -> typing.List[str] """
        pass

    def restartHint(self): # real signature unknown; restored from __doc__
        """ restartHint(self) -> PySide2.QtGui.QSessionManager.RestartHint """
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ sessionId(self) -> str """
        return ""

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ sessionKey(self) -> str """
        return ""

    def setDiscardCommand(self, arg__1, p_str=None): # real signature unknown; restored from __doc__
        """ setDiscardCommand(self, arg__1: typing.Sequence[str]) -> None """
        pass

    def setManagerProperty(self, name, value): # real signature unknown; restored from __doc__
        """
        setManagerProperty(self, name: str, value: str) -> None
        setManagerProperty(self, name: str, value: typing.Sequence[str]) -> None
        """
        pass

    def setRestartCommand(self, arg__1, p_str=None): # real signature unknown; restored from __doc__
        """ setRestartCommand(self, arg__1: typing.Sequence[str]) -> None """
        pass

    def setRestartHint(self, arg__1): # real signature unknown; restored from __doc__
        """ setRestartHint(self, arg__1: PySide2.QtGui.QSessionManager.RestartHint) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    RestartAnyway = PySide2.QtGui.QSessionManager.RestartHint.RestartAnyway
    RestartHint = None # (!) real value is "<class 'PySide2.QtGui.QSessionManager.RestartHint'>"
    RestartIfRunning = PySide2.QtGui.QSessionManager.RestartHint.RestartIfRunning
    RestartImmediately = PySide2.QtGui.QSessionManager.RestartHint.RestartImmediately
    RestartNever = PySide2.QtGui.QSessionManager.RestartHint.RestartNever
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00831380>'


