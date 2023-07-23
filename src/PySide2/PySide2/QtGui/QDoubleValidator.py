# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QValidator import QValidator

class QDoubleValidator(QValidator):
    """
    QDoubleValidator(self, bottom: float, top: float, decimals: int, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QDoubleValidator(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> float """
        return 0.0

    def bottomChanged(self, *args, **kwargs): # real signature unknown
        pass

    def decimals(self): # real signature unknown; restored from __doc__
        """ decimals(self) -> int """
        return 0

    def decimalsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def notation(self): # real signature unknown; restored from __doc__
        """ notation(self) -> PySide2.QtGui.QDoubleValidator.Notation """
        pass

    def notationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setBottom(self, arg__1): # real signature unknown; restored from __doc__
        """ setBottom(self, arg__1: float) -> None """
        pass

    def setDecimals(self, arg__1): # real signature unknown; restored from __doc__
        """ setDecimals(self, arg__1: int) -> None """
        pass

    def setNotation(self, arg__1): # real signature unknown; restored from __doc__
        """ setNotation(self, arg__1: PySide2.QtGui.QDoubleValidator.Notation) -> None """
        pass

    def setRange(self, bottom, top, decimals=0): # real signature unknown; restored from __doc__
        """ setRange(self, bottom: float, top: float, decimals: int = 0) -> None """
        pass

    def setTop(self, arg__1): # real signature unknown; restored from __doc__
        """ setTop(self, arg__1: float) -> None """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> float """
        return 0.0

    def topChanged(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ validate(self, arg__1: str, arg__2: int) -> PySide2.QtGui.QValidator.State """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, bottom, top, decimals, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Notation = None # (!) real value is "<class 'PySide2.QtGui.QDoubleValidator.Notation'>"
    ScientificNotation = PySide2.QtGui.QDoubleValidator.Notation.ScientificNotation
    StandardNotation = PySide2.QtGui.QDoubleValidator.Notation.StandardNotation
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00845B40>'


