# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTextOption(__Shiboken.Object):
    """
    QTextOption(self) -> None
    QTextOption(self, alignment: PySide2.QtCore.Qt.Alignment) -> None
    QTextOption(self, o: PySide2.QtGui.QTextOption) -> None
    """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtGui.QTextOption.Flags """
        pass

    def setAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setAlignment(self, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setFlags(self, flags): # real signature unknown; restored from __doc__
        """ setFlags(self, flags: PySide2.QtGui.QTextOption.Flags) -> None """
        pass

    def setTabArray(self, tabStops, p_float=None): # real signature unknown; restored from __doc__
        """ setTabArray(self, tabStops: typing.Sequence[float]) -> None """
        pass

    def setTabs(self, tabStops, PySide2_QtGui_QTextOption_Tab=None): # real signature unknown; restored from __doc__
        """ setTabs(self, tabStops: typing.Sequence[PySide2.QtGui.QTextOption.Tab]) -> None """
        pass

    def setTabStop(self, tabStop): # real signature unknown; restored from __doc__
        """ setTabStop(self, tabStop: float) -> None """
        pass

    def setTabStopDistance(self, tabStopDistance): # real signature unknown; restored from __doc__
        """ setTabStopDistance(self, tabStopDistance: float) -> None """
        pass

    def setTextDirection(self, aDirection): # real signature unknown; restored from __doc__
        """ setTextDirection(self, aDirection: PySide2.QtCore.Qt.LayoutDirection) -> None """
        pass

    def setUseDesignMetrics(self, b): # real signature unknown; restored from __doc__
        """ setUseDesignMetrics(self, b: bool) -> None """
        pass

    def setWrapMode(self, wrap): # real signature unknown; restored from __doc__
        """ setWrapMode(self, wrap: PySide2.QtGui.QTextOption.WrapMode) -> None """
        pass

    def tabArray(self): # real signature unknown; restored from __doc__
        """ tabArray(self) -> typing.List[float] """
        pass

    def tabs(self): # real signature unknown; restored from __doc__
        """ tabs(self) -> typing.List[PySide2.QtGui.QTextOption.Tab] """
        pass

    def tabStop(self): # real signature unknown; restored from __doc__
        """ tabStop(self) -> float """
        return 0.0

    def tabStopDistance(self): # real signature unknown; restored from __doc__
        """ tabStopDistance(self) -> float """
        return 0.0

    def textDirection(self): # real signature unknown; restored from __doc__
        """ textDirection(self) -> PySide2.QtCore.Qt.LayoutDirection """
        pass

    def useDesignMetrics(self): # real signature unknown; restored from __doc__
        """ useDesignMetrics(self) -> bool """
        return False

    def wrapMode(self): # real signature unknown; restored from __doc__
        """ wrapMode(self) -> PySide2.QtGui.QTextOption.WrapMode """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AddSpaceForLineAndParagraphSeparators = PySide2.QtGui.QTextOption.Flag.AddSpaceForLineAndParagraphSeparators
    CenterTab = PySide2.QtGui.QTextOption.TabType.CenterTab
    DelimiterTab = PySide2.QtGui.QTextOption.TabType.DelimiterTab
    Flag = None # (!) real value is "<class 'PySide2.QtGui.QTextOption.Flag'>"
    Flags = None # (!) real value is "<class 'PySide2.QtGui.QTextOption.Flags'>"
    IncludeTrailingSpaces = PySide2.QtGui.QTextOption.Flag.IncludeTrailingSpaces
    LeftTab = PySide2.QtGui.QTextOption.TabType.LeftTab
    ManualWrap = PySide2.QtGui.QTextOption.WrapMode.ManualWrap
    NoWrap = PySide2.QtGui.QTextOption.WrapMode.NoWrap
    RightTab = PySide2.QtGui.QTextOption.TabType.RightTab
    ShowDocumentTerminator = PySide2.QtGui.QTextOption.Flag.ShowDocumentTerminator
    ShowLineAndParagraphSeparators = PySide2.QtGui.QTextOption.Flag.ShowLineAndParagraphSeparators
    ShowTabsAndSpaces = PySide2.QtGui.QTextOption.Flag.ShowTabsAndSpaces
    SuppressColors = PySide2.QtGui.QTextOption.Flag.SuppressColors
    Tab = None # (!) real value is "<class 'PySide2.QtGui.QTextOption.Tab'>"
    TabType = None # (!) real value is "<class 'PySide2.QtGui.QTextOption.TabType'>"
    WordWrap = PySide2.QtGui.QTextOption.WrapMode.WordWrap
    WrapAnywhere = PySide2.QtGui.QTextOption.WrapMode.WrapAnywhere
    WrapAtWordBoundaryOrAnywhere = PySide2.QtGui.QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere
    WrapMode = None # (!) real value is "<class 'PySide2.QtGui.QTextOption.WrapMode'>"


