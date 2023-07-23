# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QFrame import QFrame

class QLCDNumber(QFrame):
    """
    QLCDNumber(self, numDigits: int, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QLCDNumber(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    """
    def checkOverflow(self, num): # real signature unknown; restored from __doc__
        """
        checkOverflow(self, num: float) -> bool
        checkOverflow(self, num: int) -> bool
        """
        return False

    def digitCount(self): # real signature unknown; restored from __doc__
        """ digitCount(self) -> int """
        return 0

    def display(self, num): # real signature unknown; restored from __doc__
        """
        display(self, num: float) -> None
        display(self, num: int) -> None
        display(self, str: str) -> None
        """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def intValue(self): # real signature unknown; restored from __doc__
        """ intValue(self) -> int """
        return 0

    def mode(self): # real signature unknown; restored from __doc__
        """ mode(self) -> PySide2.QtWidgets.QLCDNumber.Mode """
        pass

    def overflow(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def segmentStyle(self): # real signature unknown; restored from __doc__
        """ segmentStyle(self) -> PySide2.QtWidgets.QLCDNumber.SegmentStyle """
        pass

    def setBinMode(self): # real signature unknown; restored from __doc__
        """ setBinMode(self) -> None """
        pass

    def setDecMode(self): # real signature unknown; restored from __doc__
        """ setDecMode(self) -> None """
        pass

    def setDigitCount(self, nDigits): # real signature unknown; restored from __doc__
        """ setDigitCount(self, nDigits: int) -> None """
        pass

    def setHexMode(self): # real signature unknown; restored from __doc__
        """ setHexMode(self) -> None """
        pass

    def setMode(self, arg__1): # real signature unknown; restored from __doc__
        """ setMode(self, arg__1: PySide2.QtWidgets.QLCDNumber.Mode) -> None """
        pass

    def setOctMode(self): # real signature unknown; restored from __doc__
        """ setOctMode(self) -> None """
        pass

    def setSegmentStyle(self, arg__1): # real signature unknown; restored from __doc__
        """ setSegmentStyle(self, arg__1: PySide2.QtWidgets.QLCDNumber.SegmentStyle) -> None """
        pass

    def setSmallDecimalPoint(self, arg__1): # real signature unknown; restored from __doc__
        """ setSmallDecimalPoint(self, arg__1: bool) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def smallDecimalPoint(self): # real signature unknown; restored from __doc__
        """ smallDecimalPoint(self) -> bool """
        return False

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, numDigits, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Bin = PySide2.QtWidgets.QLCDNumber.Mode.Bin
    Dec = PySide2.QtWidgets.QLCDNumber.Mode.Dec
    Filled = PySide2.QtWidgets.QLCDNumber.SegmentStyle.Filled
    Flat = PySide2.QtWidgets.QLCDNumber.SegmentStyle.Flat
    Hex = PySide2.QtWidgets.QLCDNumber.Mode.Hex
    Mode = None # (!) real value is "<class 'PySide2.QtWidgets.QLCDNumber.Mode'>"
    Oct = PySide2.QtWidgets.QLCDNumber.Mode.Oct
    Outline = PySide2.QtWidgets.QLCDNumber.SegmentStyle.Outline
    SegmentStyle = None # (!) real value is "<class 'PySide2.QtWidgets.QLCDNumber.SegmentStyle'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507E4D00>'


