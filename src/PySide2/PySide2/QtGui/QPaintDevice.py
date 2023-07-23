# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPaintDevice(__Shiboken.Object):
    """ QPaintDevice(self) -> None """
    def colorCount(self): # real signature unknown; restored from __doc__
        """ colorCount(self) -> int """
        return 0

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> int """
        return 0

    def devicePixelRatioF(self): # real signature unknown; restored from __doc__
        """ devicePixelRatioF(self) -> float """
        return 0.0

    def devicePixelRatioFScale(self): # real signature unknown; restored from __doc__
        """ devicePixelRatioFScale() -> float """
        return 0.0

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def heightMM(self): # real signature unknown; restored from __doc__
        """ heightMM(self) -> int """
        return 0

    def initPainter(self, painter): # real signature unknown; restored from __doc__
        """ initPainter(self, painter: PySide2.QtGui.QPainter) -> None """
        pass

    def logicalDpiX(self): # real signature unknown; restored from __doc__
        """ logicalDpiX(self) -> int """
        return 0

    def logicalDpiY(self): # real signature unknown; restored from __doc__
        """ logicalDpiY(self) -> int """
        return 0

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def paintingActive(self): # real signature unknown; restored from __doc__
        """ paintingActive(self) -> bool """
        return False

    def physicalDpiX(self): # real signature unknown; restored from __doc__
        """ physicalDpiX(self) -> int """
        return 0

    def physicalDpiY(self): # real signature unknown; restored from __doc__
        """ physicalDpiY(self) -> int """
        return 0

    def redirected(self, offset): # real signature unknown; restored from __doc__
        """ redirected(self, offset: PySide2.QtCore.QPoint) -> PySide2.QtGui.QPaintDevice """
        pass

    def sharedPainter(self): # real signature unknown; restored from __doc__
        """ sharedPainter(self) -> PySide2.QtGui.QPainter """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def widthMM(self): # real signature unknown; restored from __doc__
        """ widthMM(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    painters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    PaintDeviceMetric = None # (!) real value is "<class 'PySide2.QtGui.QPaintDevice.PaintDeviceMetric'>"
    PdmDepth = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmDepth
    PdmDevicePixelRatio = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmDevicePixelRatio
    PdmDevicePixelRatioScaled = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmDevicePixelRatioScaled
    PdmDpiX = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmDpiX
    PdmDpiY = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmDpiY
    PdmHeight = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmHeight
    PdmHeightMM = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmHeightMM
    PdmNumColors = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmNumColors
    PdmPhysicalDpiX = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmPhysicalDpiX
    PdmPhysicalDpiY = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmPhysicalDpiY
    PdmWidth = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmWidth
    PdmWidthMM = PySide2.QtGui.QPaintDevice.PaintDeviceMetric.PdmWidthMM


