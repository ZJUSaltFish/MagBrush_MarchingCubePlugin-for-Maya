# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QWidget import QWidget

class QProgressBar(QWidget):
    """ QProgressBar(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def alignment(self): # real signature unknown; restored from __doc__
        """ alignment(self) -> PySide2.QtCore.Qt.Alignment """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> str """
        return ""

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionProgressBar) -> None """
        pass

    def invertedAppearance(self): # real signature unknown; restored from __doc__
        """ invertedAppearance(self) -> bool """
        return False

    def isTextVisible(self): # real signature unknown; restored from __doc__
        """ isTextVisible(self) -> bool """
        return False

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resetFormat(self): # real signature unknown; restored from __doc__
        """ resetFormat(self) -> None """
        pass

    def setAlignment(self, alignment): # real signature unknown; restored from __doc__
        """ setAlignment(self, alignment: PySide2.QtCore.Qt.Alignment) -> None """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: str) -> None """
        pass

    def setInvertedAppearance(self, invert): # real signature unknown; restored from __doc__
        """ setInvertedAppearance(self, invert: bool) -> None """
        pass

    def setMaximum(self, maximum): # real signature unknown; restored from __doc__
        """ setMaximum(self, maximum: int) -> None """
        pass

    def setMinimum(self, minimum): # real signature unknown; restored from __doc__
        """ setMinimum(self, minimum: int) -> None """
        pass

    def setOrientation(self, arg__1): # real signature unknown; restored from __doc__
        """ setOrientation(self, arg__1: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def setRange(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setRange(self, minimum: int, maximum: int) -> None """
        pass

    def setTextDirection(self, textDirection): # real signature unknown; restored from __doc__
        """ setTextDirection(self, textDirection: PySide2.QtWidgets.QProgressBar.Direction) -> None """
        pass

    def setTextVisible(self, visible): # real signature unknown; restored from __doc__
        """ setTextVisible(self, visible: bool) -> None """
        pass

    def setValue(self, value): # real signature unknown; restored from __doc__
        """ setValue(self, value: int) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def textDirection(self): # real signature unknown; restored from __doc__
        """ textDirection(self) -> PySide2.QtWidgets.QProgressBar.Direction """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    BottomToTop = PySide2.QtWidgets.QProgressBar.Direction.BottomToTop
    Direction = None # (!) real value is "<class 'PySide2.QtWidgets.QProgressBar.Direction'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50817440>'
    TopToBottom = PySide2.QtWidgets.QProgressBar.Direction.TopToBottom


