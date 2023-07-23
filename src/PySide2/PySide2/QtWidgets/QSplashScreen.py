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

class QSplashScreen(QWidget):
    """
    QSplashScreen(self, parent: PySide2.QtWidgets.QWidget, pixmap: PySide2.QtGui.QPixmap = Default(PySide2.QtGui.QPixmap), f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QSplashScreen(self, pixmap: PySide2.QtGui.QPixmap = Default(PySide2.QtGui.QPixmap), f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QSplashScreen(self, screen: PySide2.QtGui.QScreen, pixmap: PySide2.QtGui.QPixmap = Default(PySide2.QtGui.QPixmap), f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    """
    def clearMessage(self): # real signature unknown; restored from __doc__
        """ clearMessage(self) -> None """
        pass

    def drawContents(self, painter): # real signature unknown; restored from __doc__
        """ drawContents(self, painter: PySide2.QtGui.QPainter) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def finish(self, w): # real signature unknown; restored from __doc__
        """ finish(self, w: PySide2.QtWidgets.QWidget) -> None """
        pass

    def message(self): # real signature unknown; restored from __doc__
        """ message(self) -> str """
        return ""

    def messageChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mousePressEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ mousePressEvent(self, arg__1: PySide2.QtGui.QMouseEvent) -> None """
        pass

    def pixmap(self): # real signature unknown; restored from __doc__
        """ pixmap(self) -> PySide2.QtGui.QPixmap """
        pass

    def setPixmap(self, pixmap): # real signature unknown; restored from __doc__
        """ setPixmap(self, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def showMessage(self, message, alignment=None, color=None): # real signature unknown; restored from __doc__
        """ showMessage(self, message: str, alignment: int = PySide2.QtCore.Qt.AlignmentFlag.AlignLeft, color: PySide2.QtGui.QColor = PySide2.QtCore.Qt.GlobalColor.black) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, pixmap=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507BC500>'


