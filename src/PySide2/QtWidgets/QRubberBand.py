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

class QRubberBand(QWidget):
    """ QRubberBand(self, arg__1: PySide2.QtWidgets.QRubberBand.Shape, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionRubberBand) -> None """
        pass

    def move(self, p): # real signature unknown; restored from __doc__
        """
        move(self, p: PySide2.QtCore.QPoint) -> None
        move(self, x: int, y: int) -> None
        """
        pass

    def moveEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ moveEvent(self, arg__1: PySide2.QtGui.QMoveEvent) -> None """
        pass

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def resize(self, s): # real signature unknown; restored from __doc__
        """
        resize(self, s: PySide2.QtCore.QSize) -> None
        resize(self, w: int, h: int) -> None
        """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def setGeometry(self, r): # real signature unknown; restored from __doc__
        """
        setGeometry(self, r: PySide2.QtCore.QRect) -> None
        setGeometry(self, x: int, y: int, w: int, h: int) -> None
        """
        pass

    def shape(self): # real signature unknown; restored from __doc__
        """ shape(self) -> PySide2.QtWidgets.QRubberBand.Shape """
        pass

    def showEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ showEvent(self, arg__1: PySide2.QtGui.QShowEvent) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Line = PySide2.QtWidgets.QRubberBand.Shape.Line
    Rectangle = PySide2.QtWidgets.QRubberBand.Shape.Rectangle
    Shape = None # (!) real value is "<class 'PySide2.QtWidgets.QRubberBand.Shape'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507D4340>'


