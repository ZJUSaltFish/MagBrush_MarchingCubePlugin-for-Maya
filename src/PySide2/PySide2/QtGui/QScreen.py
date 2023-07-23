# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QScreen(__PySide2_QtCore.QObject):
    # no doc
    def angleBetween(self, a, b): # real signature unknown; restored from __doc__
        """ angleBetween(self, a: PySide2.QtCore.Qt.ScreenOrientation, b: PySide2.QtCore.Qt.ScreenOrientation) -> int """
        return 0

    def availableGeometry(self): # real signature unknown; restored from __doc__
        """ availableGeometry(self) -> PySide2.QtCore.QRect """
        pass

    def availableGeometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def availableSize(self): # real signature unknown; restored from __doc__
        """ availableSize(self) -> PySide2.QtCore.QSize """
        pass

    def availableVirtualGeometry(self): # real signature unknown; restored from __doc__
        """ availableVirtualGeometry(self) -> PySide2.QtCore.QRect """
        pass

    def availableVirtualSize(self): # real signature unknown; restored from __doc__
        """ availableVirtualSize(self) -> PySide2.QtCore.QSize """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> PySide2.QtCore.QRect """
        pass

    def geometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def grabWindow(self, window, x=0, y=0, w=-1, h=-1): # real signature unknown; restored from __doc__
        """ grabWindow(self, window: int, x: int = 0, y: int = 0, w: int = -1, h: int = -1) -> PySide2.QtGui.QPixmap """
        pass

    def isLandscape(self, orientation): # real signature unknown; restored from __doc__
        """ isLandscape(self, orientation: PySide2.QtCore.Qt.ScreenOrientation) -> bool """
        return False

    def isPortrait(self, orientation): # real signature unknown; restored from __doc__
        """ isPortrait(self, orientation: PySide2.QtCore.Qt.ScreenOrientation) -> bool """
        return False

    def logicalDotsPerInch(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInch(self) -> float """
        return 0.0

    def logicalDotsPerInchChanged(self, *args, **kwargs): # real signature unknown
        pass

    def logicalDotsPerInchX(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInchX(self) -> float """
        return 0.0

    def logicalDotsPerInchY(self): # real signature unknown; restored from __doc__
        """ logicalDotsPerInchY(self) -> float """
        return 0.0

    def manufacturer(self): # real signature unknown; restored from __doc__
        """ manufacturer(self) -> str """
        return ""

    def mapBetween(self, a, b, rect): # real signature unknown; restored from __doc__
        """ mapBetween(self, a: PySide2.QtCore.Qt.ScreenOrientation, b: PySide2.QtCore.Qt.ScreenOrientation, rect: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect """
        pass

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def nativeOrientation(self): # real signature unknown; restored from __doc__
        """ nativeOrientation(self) -> PySide2.QtCore.Qt.ScreenOrientation """
        pass

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.ScreenOrientation """
        pass

    def orientationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def orientationUpdateMask(self): # real signature unknown; restored from __doc__
        """ orientationUpdateMask(self) -> PySide2.QtCore.Qt.ScreenOrientations """
        pass

    def physicalDotsPerInch(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInch(self) -> float """
        return 0.0

    def physicalDotsPerInchChanged(self, *args, **kwargs): # real signature unknown
        pass

    def physicalDotsPerInchX(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInchX(self) -> float """
        return 0.0

    def physicalDotsPerInchY(self): # real signature unknown; restored from __doc__
        """ physicalDotsPerInchY(self) -> float """
        return 0.0

    def physicalSize(self): # real signature unknown; restored from __doc__
        """ physicalSize(self) -> PySide2.QtCore.QSizeF """
        pass

    def physicalSizeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def primaryOrientation(self): # real signature unknown; restored from __doc__
        """ primaryOrientation(self) -> PySide2.QtCore.Qt.ScreenOrientation """
        pass

    def primaryOrientationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def refreshRate(self): # real signature unknown; restored from __doc__
        """ refreshRate(self) -> float """
        return 0.0

    def refreshRateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ serialNumber(self) -> str """
        return ""

    def setOrientationUpdateMask(self, mask): # real signature unknown; restored from __doc__
        """ setOrientationUpdateMask(self, mask: PySide2.QtCore.Qt.ScreenOrientations) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def transformBetween(self, a, b, target): # real signature unknown; restored from __doc__
        """ transformBetween(self, a: PySide2.QtCore.Qt.ScreenOrientation, b: PySide2.QtCore.Qt.ScreenOrientation, target: PySide2.QtCore.QRect) -> PySide2.QtGui.QTransform """
        pass

    def virtualGeometry(self): # real signature unknown; restored from __doc__
        """ virtualGeometry(self) -> PySide2.QtCore.QRect """
        pass

    def virtualGeometryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def virtualSiblingAt(self, point): # real signature unknown; restored from __doc__
        """ virtualSiblingAt(self, point: PySide2.QtCore.QPoint) -> PySide2.QtGui.QScreen """
        pass

    def virtualSiblings(self): # real signature unknown; restored from __doc__
        """ virtualSiblings(self) -> typing.List[PySide2.QtGui.QScreen] """
        pass

    def virtualSize(self): # real signature unknown; restored from __doc__
        """ virtualSize(self) -> PySide2.QtCore.QSize """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00832140>'


