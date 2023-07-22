# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QBackingStore(__Shiboken.Object):
    """ QBackingStore(self, window: PySide2.QtGui.QWindow) -> None """
    def beginPaint(self, arg__1): # real signature unknown; restored from __doc__
        """ beginPaint(self, arg__1: PySide2.QtGui.QRegion) -> None """
        pass

    def endPaint(self): # real signature unknown; restored from __doc__
        """ endPaint(self) -> None """
        pass

    def flush(self, region, window, PySide2_QtGui_QWindow=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ flush(self, region: PySide2.QtGui.QRegion, window: typing.Optional[PySide2.QtGui.QWindow] = None, offset: PySide2.QtCore.QPoint = Default(QPoint)) -> None """
        pass

    def hasStaticContents(self): # real signature unknown; restored from __doc__
        """ hasStaticContents(self) -> bool """
        return False

    def paintDevice(self): # real signature unknown; restored from __doc__
        """ paintDevice(self) -> PySide2.QtGui.QPaintDevice """
        pass

    def resize(self, size): # real signature unknown; restored from __doc__
        """ resize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def scroll(self, area, dx, dy): # real signature unknown; restored from __doc__
        """ scroll(self, area: PySide2.QtGui.QRegion, dx: int, dy: int) -> bool """
        return False

    def setStaticContents(self, region): # real signature unknown; restored from __doc__
        """ setStaticContents(self, region: PySide2.QtGui.QRegion) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def staticContents(self): # real signature unknown; restored from __doc__
        """ staticContents(self) -> PySide2.QtGui.QRegion """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtGui.QWindow """
        pass

    def __init__(self, window): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


