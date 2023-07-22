# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QWindow import QWindow

from .QPaintDevice import QPaintDevice

class QPaintDeviceWindow(QWindow, QPaintDevice):
    # no doc
    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def exposeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ exposeEvent(self, arg__1: PySide2.QtGui.QExposeEvent) -> None """
        pass

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def paintEvent(self, event): # real signature unknown; restored from __doc__
        """ paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None """
        pass

    def update(self): # real signature unknown; restored from __doc__
        """
        update(self) -> None
        update(self, rect: PySide2.QtCore.QRect) -> None
        update(self, region: PySide2.QtGui.QRegion) -> None
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00844500>'


