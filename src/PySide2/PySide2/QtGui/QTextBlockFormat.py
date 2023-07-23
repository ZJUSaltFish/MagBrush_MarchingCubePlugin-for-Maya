# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QTextFormat import QTextFormat

class QTextBlockFormat(QTextFormat):
    """
    QTextBlockFormat(self) -> None
    QTextBlockFormat(self, QTextBlockFormat: PySide2.QtGui.QTextBlockFormat) -> None
    QTextBlockFormat(self, fmt: PySide2.QtGui.QTextFormat) -> None
    """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def bottomMargin(self): # real signature unknown; restored from __doc__
        """ bottomMargin(self) -> float """
        return 0.0

    def headingLevel(self): # real signature unknown; restored from __doc__
        """ headingLevel(self) -> int """
        return 0

    def indent(self): # real signature unknown; restored from __doc__
        """ indent(self) -> int """
        return 0

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def leftMargin(self): # real signature unknown; restored from __doc__
        """ leftMargin(self) -> float """
        return 0.0

    def lineHeight(self): # real signature unknown; restored from __doc__
        """
        lineHeight(self) -> float
        lineHeight(self, scriptLineHeight: float, scaling: float) -> float
        """
        return 0.0

    def lineHeightType(self): # real signature unknown; restored from __doc__
        """ lineHeightType(self) -> int """
        return 0

    def marker(self): # real signature unknown; restored from __doc__
        """ marker(self) -> PySide2.QtGui.QTextBlockFormat.MarkerType """
        pass

    def nonBreakableLines(self): # real signature unknown; restored from __doc__
        """ nonBreakableLines(self) -> bool """
        return False

    def pageBreakPolicy(self): # real signature unknown; restored from __doc__
        """ pageBreakPolicy(self) -> PySide2.QtGui.QTextFormat.PageBreakFlags """
        pass

    def rightMargin(self): # real signature unknown; restored from __doc__
        """ rightMargin(self) -> float """
        return 0.0

    def setAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setAlignment(self, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setBottomMargin(self, margin): # real signature unknown; restored from __doc__
        """ setBottomMargin(self, margin: float) -> None """
        pass

    def setHeadingLevel(self, alevel): # real signature unknown; restored from __doc__
        """ setHeadingLevel(self, alevel: int) -> None """
        pass

    def setIndent(self, indent): # real signature unknown; restored from __doc__
        """ setIndent(self, indent: int) -> None """
        pass

    def setLeftMargin(self, margin): # real signature unknown; restored from __doc__
        """ setLeftMargin(self, margin: float) -> None """
        pass

    def setLineHeight(self, height, heightType): # real signature unknown; restored from __doc__
        """ setLineHeight(self, height: float, heightType: int) -> None """
        pass

    def setMarker(self, marker): # real signature unknown; restored from __doc__
        """ setMarker(self, marker: PySide2.QtGui.QTextBlockFormat.MarkerType) -> None """
        pass

    def setNonBreakableLines(self, b): # real signature unknown; restored from __doc__
        """ setNonBreakableLines(self, b: bool) -> None """
        pass

    def setPageBreakPolicy(self, flags): # real signature unknown; restored from __doc__
        """ setPageBreakPolicy(self, flags: PySide2.QtGui.QTextFormat.PageBreakFlags) -> None """
        pass

    def setRightMargin(self, margin): # real signature unknown; restored from __doc__
        """ setRightMargin(self, margin: float) -> None """
        pass

    def setTabPositions(self, tabs, PySide2_QtGui_QTextOption_Tab=None): # real signature unknown; restored from __doc__
        """ setTabPositions(self, tabs: typing.Sequence[PySide2.QtGui.QTextOption.Tab]) -> None """
        pass

    def setTextIndent(self, aindent): # real signature unknown; restored from __doc__
        """ setTextIndent(self, aindent: float) -> None """
        pass

    def setTopMargin(self, margin): # real signature unknown; restored from __doc__
        """ setTopMargin(self, margin: float) -> None """
        pass

    def tabPositions(self): # real signature unknown; restored from __doc__
        """ tabPositions(self) -> typing.List[PySide2.QtGui.QTextOption.Tab] """
        pass

    def textIndent(self): # real signature unknown; restored from __doc__
        """ textIndent(self) -> float """
        return 0.0

    def topMargin(self): # real signature unknown; restored from __doc__
        """ topMargin(self) -> float """
        return 0.0

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    FixedHeight = PySide2.QtGui.QTextBlockFormat.LineHeightTypes.FixedHeight
    LineDistanceHeight = PySide2.QtGui.QTextBlockFormat.LineHeightTypes.LineDistanceHeight
    LineHeightTypes = None # (!) real value is "<class 'PySide2.QtGui.QTextBlockFormat.LineHeightTypes'>"
    MarkerType = None # (!) real value is "<class 'PySide2.QtGui.QTextBlockFormat.MarkerType'>"
    MinimumHeight = PySide2.QtGui.QTextBlockFormat.LineHeightTypes.MinimumHeight
    ProportionalHeight = PySide2.QtGui.QTextBlockFormat.LineHeightTypes.ProportionalHeight
    SingleHeight = PySide2.QtGui.QTextBlockFormat.LineHeightTypes.SingleHeight


