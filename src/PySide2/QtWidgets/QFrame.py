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

class QFrame(QWidget):
    """ QFrame(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def changeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ changeEvent(self, arg__1: PySide2.QtCore.QEvent) -> None """
        pass

    def drawFrame(self, arg__1): # real signature unknown; restored from __doc__
        """ drawFrame(self, arg__1: PySide2.QtGui.QPainter) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def frameRect(self): # real signature unknown; restored from __doc__
        """ frameRect(self) -> PySide2.QtCore.QRect """
        pass

    def frameShadow(self): # real signature unknown; restored from __doc__
        """ frameShadow(self) -> PySide2.QtWidgets.QFrame.Shadow """
        pass

    def frameShape(self): # real signature unknown; restored from __doc__
        """ frameShape(self) -> PySide2.QtWidgets.QFrame.Shape """
        pass

    def frameStyle(self): # real signature unknown; restored from __doc__
        """ frameStyle(self) -> int """
        return 0

    def frameWidth(self): # real signature unknown; restored from __doc__
        """ frameWidth(self) -> int """
        return 0

    def initStyleOption(self, option): # real signature unknown; restored from __doc__
        """ initStyleOption(self, option: PySide2.QtWidgets.QStyleOptionFrame) -> None """
        pass

    def lineWidth(self): # real signature unknown; restored from __doc__
        """ lineWidth(self) -> int """
        return 0

    def midLineWidth(self): # real signature unknown; restored from __doc__
        """ midLineWidth(self) -> int """
        return 0

    def paintEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def setFrameRect(self, arg__1): # real signature unknown; restored from __doc__
        """ setFrameRect(self, arg__1: PySide2.QtCore.QRect) -> None """
        pass

    def setFrameShadow(self, arg__1): # real signature unknown; restored from __doc__
        """ setFrameShadow(self, arg__1: PySide2.QtWidgets.QFrame.Shadow) -> None """
        pass

    def setFrameShape(self, arg__1): # real signature unknown; restored from __doc__
        """ setFrameShape(self, arg__1: PySide2.QtWidgets.QFrame.Shape) -> None """
        pass

    def setFrameStyle(self, arg__1): # real signature unknown; restored from __doc__
        """ setFrameStyle(self, arg__1: int) -> None """
        pass

    def setLineWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ setLineWidth(self, arg__1: int) -> None """
        pass

    def setMidLineWidth(self, arg__1): # real signature unknown; restored from __doc__
        """ setMidLineWidth(self, arg__1: int) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
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

    Box = PySide2.QtWidgets.QFrame.Shape.Box
    HLine = PySide2.QtWidgets.QFrame.Shape.HLine
    NoFrame = PySide2.QtWidgets.QFrame.Shape.NoFrame
    Panel = PySide2.QtWidgets.QFrame.Shape.Panel
    Plain = PySide2.QtWidgets.QFrame.Shadow.Plain
    Raised = PySide2.QtWidgets.QFrame.Shadow.Raised
    Shadow = None # (!) real value is "<class 'PySide2.QtWidgets.QFrame.Shadow'>"
    Shadow_Mask = PySide2.QtWidgets.QFrame.StyleMask.Shadow_Mask
    Shape = None # (!) real value is "<class 'PySide2.QtWidgets.QFrame.Shape'>"
    Shape_Mask = PySide2.QtWidgets.QFrame.StyleMask.Shape_Mask
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507E43C0>'
    StyledPanel = PySide2.QtWidgets.QFrame.Shape.StyledPanel
    StyleMask = None # (!) real value is "<class 'PySide2.QtWidgets.QFrame.StyleMask'>"
    Sunken = PySide2.QtWidgets.QFrame.Shadow.Sunken
    VLine = PySide2.QtWidgets.QFrame.Shape.VLine
    WinPanel = PySide2.QtWidgets.QFrame.Shape.WinPanel


