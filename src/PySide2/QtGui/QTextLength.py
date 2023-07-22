# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTextLength(__Shiboken.Object):
    """
    QTextLength(self) -> None
    QTextLength(self, QTextLength: PySide2.QtGui.QTextLength) -> None
    QTextLength(self, type: PySide2.QtGui.QTextLength.Type, value: float) -> None
    """
    def rawValue(self): # real signature unknown; restored from __doc__
        """ rawValue(self) -> float """
        return 0.0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtGui.QTextLength.Type """
        pass

    def value(self, maximumLength): # real signature unknown; restored from __doc__
        """ value(self, maximumLength: float) -> float """
        return 0.0

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

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    FixedLength = PySide2.QtGui.QTextLength.Type.FixedLength
    PercentageLength = PySide2.QtGui.QTextLength.Type.PercentageLength
    Type = None # (!) real value is "<class 'PySide2.QtGui.QTextLength.Type'>"
    VariableLength = PySide2.QtGui.QTextLength.Type.VariableLength
    __hash__ = None


