# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLDebugLogger(__PySide2_QtCore.QObject):
    """ QOpenGLDebugLogger(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def disableMessages(self, ids, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        disableMessages(self, ids: typing.List[int], sources: PySide2.QtGui.QOpenGLDebugMessage.Sources = PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types: PySide2.QtGui.QOpenGLDebugMessage.Types = PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType) -> None
        disableMessages(self, sources: PySide2.QtGui.QOpenGLDebugMessage.Sources = PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types: PySide2.QtGui.QOpenGLDebugMessage.Types = PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType, severities: PySide2.QtGui.QOpenGLDebugMessage.Severities = PySide2.QtGui.QOpenGLDebugMessage.Severity.AnySeverity) -> None
        """
        pass

    def enableMessages(self, ids, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        enableMessages(self, ids: typing.List[int], sources: PySide2.QtGui.QOpenGLDebugMessage.Sources = PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types: PySide2.QtGui.QOpenGLDebugMessage.Types = PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType) -> None
        enableMessages(self, sources: PySide2.QtGui.QOpenGLDebugMessage.Sources = PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource, types: PySide2.QtGui.QOpenGLDebugMessage.Types = PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType, severities: PySide2.QtGui.QOpenGLDebugMessage.Severities = PySide2.QtGui.QOpenGLDebugMessage.Severity.AnySeverity) -> None
        """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) -> bool """
        return False

    def isLogging(self): # real signature unknown; restored from __doc__
        """ isLogging(self) -> bool """
        return False

    def loggedMessages(self): # real signature unknown; restored from __doc__
        """ loggedMessages(self) -> typing.List[PySide2.QtGui.QOpenGLDebugMessage] """
        pass

    def loggingMode(self): # real signature unknown; restored from __doc__
        """ loggingMode(self) -> PySide2.QtGui.QOpenGLDebugLogger.LoggingMode """
        pass

    def logMessage(self, debugMessage): # real signature unknown; restored from __doc__
        """ logMessage(self, debugMessage: PySide2.QtGui.QOpenGLDebugMessage) -> None """
        pass

    def maximumMessageLength(self): # real signature unknown; restored from __doc__
        """ maximumMessageLength(self) -> int """
        return 0

    def messageLogged(self, *args, **kwargs): # real signature unknown
        pass

    def popGroup(self): # real signature unknown; restored from __doc__
        """ popGroup(self) -> None """
        pass

    def pushGroup(self, name, id=0, source=None): # real signature unknown; restored from __doc__
        """ pushGroup(self, name: str, id: int = 0, source: PySide2.QtGui.QOpenGLDebugMessage.Source = PySide2.QtGui.QOpenGLDebugMessage.Source.ApplicationSource) -> None """
        pass

    def startLogging(self, loggingMode=None): # real signature unknown; restored from __doc__
        """ startLogging(self, loggingMode: PySide2.QtGui.QOpenGLDebugLogger.LoggingMode = PySide2.QtGui.QOpenGLDebugLogger.LoggingMode.AsynchronousLogging) -> None """
        pass

    def stopLogging(self): # real signature unknown; restored from __doc__
        """ stopLogging(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AsynchronousLogging = PySide2.QtGui.QOpenGLDebugLogger.LoggingMode.AsynchronousLogging
    LoggingMode = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLDebugLogger.LoggingMode'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00854EC0>'
    SynchronousLogging = PySide2.QtGui.QOpenGLDebugLogger.LoggingMode.SynchronousLogging


