# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLDebugMessage(__Shiboken.Object):
    """
    QOpenGLDebugMessage(self) -> None
    QOpenGLDebugMessage(self, debugMessage: PySide2.QtGui.QOpenGLDebugMessage) -> None
    """
    def createApplicationMessage(self, text, id=0, severity=None, type=None): # real signature unknown; restored from __doc__
        """ createApplicationMessage(text: str, id: int = 0, severity: PySide2.QtGui.QOpenGLDebugMessage.Severity = PySide2.QtGui.QOpenGLDebugMessage.Severity.NotificationSeverity, type: PySide2.QtGui.QOpenGLDebugMessage.Type = PySide2.QtGui.QOpenGLDebugMessage.Type.OtherType) -> PySide2.QtGui.QOpenGLDebugMessage """
        pass

    def createThirdPartyMessage(self, text, id=0, severity=None, type=None): # real signature unknown; restored from __doc__
        """ createThirdPartyMessage(text: str, id: int = 0, severity: PySide2.QtGui.QOpenGLDebugMessage.Severity = PySide2.QtGui.QOpenGLDebugMessage.Severity.NotificationSeverity, type: PySide2.QtGui.QOpenGLDebugMessage.Type = PySide2.QtGui.QOpenGLDebugMessage.Type.OtherType) -> PySide2.QtGui.QOpenGLDebugMessage """
        pass

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def message(self): # real signature unknown; restored from __doc__
        """ message(self) -> str """
        return ""

    def severity(self): # real signature unknown; restored from __doc__
        """ severity(self) -> PySide2.QtGui.QOpenGLDebugMessage.Severity """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> PySide2.QtGui.QOpenGLDebugMessage.Source """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QOpenGLDebugMessage) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtGui.QOpenGLDebugMessage.Type """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    AnySeverity = PySide2.QtGui.QOpenGLDebugMessage.Severity.AnySeverity
    AnySource = PySide2.QtGui.QOpenGLDebugMessage.Source.AnySource
    AnyType = PySide2.QtGui.QOpenGLDebugMessage.Type.AnyType
    APISource = PySide2.QtGui.QOpenGLDebugMessage.Source.APISource
    ApplicationSource = PySide2.QtGui.QOpenGLDebugMessage.Source.ApplicationSource
    DeprecatedBehaviorType = PySide2.QtGui.QOpenGLDebugMessage.Type.DeprecatedBehaviorType
    ErrorType = PySide2.QtGui.QOpenGLDebugMessage.Type.ErrorType
    GroupPopType = PySide2.QtGui.QOpenGLDebugMessage.Type.GroupPopType
    GroupPushType = PySide2.QtGui.QOpenGLDebugMessage.Type.GroupPushType
    HighSeverity = PySide2.QtGui.QOpenGLDebugMessage.Severity.HighSeverity
    InvalidSeverity = PySide2.QtGui.QOpenGLDebugMessage.Severity.InvalidSeverity
    InvalidSource = PySide2.QtGui.QOpenGLDebugMessage.Source.InvalidSource
    InvalidType = PySide2.QtGui.QOpenGLDebugMessage.Type.InvalidType
    LastSeverity = PySide2.QtGui.QOpenGLDebugMessage.Severity.LastSeverity
    LastSource = PySide2.QtGui.QOpenGLDebugMessage.Source.LastSource
    LastType = PySide2.QtGui.QOpenGLDebugMessage.Type.LastType
    LowSeverity = PySide2.QtGui.QOpenGLDebugMessage.Severity.LowSeverity
    MarkerType = PySide2.QtGui.QOpenGLDebugMessage.Type.MarkerType
    MediumSeverity = PySide2.QtGui.QOpenGLDebugMessage.Severity.MediumSeverity
    NotificationSeverity = PySide2.QtGui.QOpenGLDebugMessage.Severity.NotificationSeverity
    OtherSource = PySide2.QtGui.QOpenGLDebugMessage.Source.OtherSource
    OtherType = PySide2.QtGui.QOpenGLDebugMessage.Type.OtherType
    PerformanceType = PySide2.QtGui.QOpenGLDebugMessage.Type.PerformanceType
    PortabilityType = PySide2.QtGui.QOpenGLDebugMessage.Type.PortabilityType
    Severities = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLDebugMessage.Severities'>"
    Severity = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLDebugMessage.Severity'>"
    ShaderCompilerSource = PySide2.QtGui.QOpenGLDebugMessage.Source.ShaderCompilerSource
    Source = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLDebugMessage.Source'>"
    Sources = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLDebugMessage.Sources'>"
    ThirdPartySource = PySide2.QtGui.QOpenGLDebugMessage.Source.ThirdPartySource
    Type = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLDebugMessage.Type'>"
    Types = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLDebugMessage.Types'>"
    UndefinedBehaviorType = PySide2.QtGui.QOpenGLDebugMessage.Type.UndefinedBehaviorType
    WindowSystemSource = PySide2.QtGui.QOpenGLDebugMessage.Source.WindowSystemSource
    __hash__ = None


