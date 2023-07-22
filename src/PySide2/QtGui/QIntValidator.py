# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QValidator import QValidator

class QIntValidator(QValidator):
    """
    QIntValidator(self, bottom: int, top: int, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QIntValidator(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def bottom(self): # real signature unknown; restored from __doc__
        """ bottom(self) -> int """
        return 0

    def bottomChanged(self, *args, **kwargs): # real signature unknown
        pass

    def fixup(self, input): # real signature unknown; restored from __doc__
        """ fixup(self, input: str) -> None """
        pass

    def setBottom(self, arg__1): # real signature unknown; restored from __doc__
        """ setBottom(self, arg__1: int) -> None """
        pass

    def setRange(self, bottom, top): # real signature unknown; restored from __doc__
        """ setRange(self, bottom: int, top: int) -> None """
        pass

    def setTop(self, arg__1): # real signature unknown; restored from __doc__
        """ setTop(self, arg__1: int) -> None """
        pass

    def top(self): # real signature unknown; restored from __doc__
        """ top(self) -> int """
        return 0

    def topChanged(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ validate(self, arg__1: str, arg__2: int) -> PySide2.QtGui.QValidator.State """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, bottom, top, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00845D00>'


