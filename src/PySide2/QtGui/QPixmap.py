# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QPaintDevice import QPaintDevice

class QPixmap(QPaintDevice):
    """
    QPixmap(self) -> None
    QPixmap(self, arg__1: PySide2.QtCore.QSize) -> None
    QPixmap(self, arg__1: PySide2.QtGui.QPixmap) -> None
    QPixmap(self, fileName: str, format: typing.Optional[bytes] = None, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> None
    QPixmap(self, image: PySide2.QtGui.QImage) -> None
    QPixmap(self, w: int, h: int) -> None
    QPixmap(self, xpm: typing.Sequence[str]) -> None
    """
    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def convertFromImage(self, img, flags=None): # real signature unknown; restored from __doc__
        """ convertFromImage(self, img: PySide2.QtGui.QImage, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> bool """
        return False

    def copy(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        copy(self, rect: PySide2.QtCore.QRect = Default(QRect)) -> PySide2.QtGui.QPixmap
        copy(self, x: int, y: int, width: int, height: int) -> PySide2.QtGui.QPixmap
        """
        pass

    def createHeuristicMask(self, clipTight=True): # real signature unknown; restored from __doc__
        """ createHeuristicMask(self, clipTight: bool = True) -> PySide2.QtGui.QBitmap """
        pass

    def createMaskFromColor(self, maskColor, mode=None): # real signature unknown; restored from __doc__
        """ createMaskFromColor(self, maskColor: PySide2.QtGui.QColor, mode: PySide2.QtCore.Qt.MaskMode = PySide2.QtCore.Qt.MaskMode.MaskInColor) -> PySide2.QtGui.QBitmap """
        pass

    def defaultDepth(self): # real signature unknown; restored from __doc__
        """ defaultDepth() -> int """
        return 0

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def fill(self, device, ofs): # real signature unknown; restored from __doc__
        """
        fill(self, device: PySide2.QtGui.QPaintDevice, ofs: PySide2.QtCore.QPoint) -> None
        fill(self, device: PySide2.QtGui.QPaintDevice, xofs: int, yofs: int) -> None
        fill(self, fillColor: PySide2.QtGui.QColor = PySide2.QtCore.Qt.GlobalColor.white) -> None
        """
        pass

    def fromImage(self, image, flags=None): # real signature unknown; restored from __doc__
        """ fromImage(image: PySide2.QtGui.QImage, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QPixmap """
        pass

    def fromImageInPlace(self, image, flags=None): # real signature unknown; restored from __doc__
        """ fromImageInPlace(image: PySide2.QtGui.QImage, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QPixmap """
        pass

    def fromImageReader(self, imageReader, flags=None): # real signature unknown; restored from __doc__
        """ fromImageReader(imageReader: PySide2.QtGui.QImageReader, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QPixmap """
        pass

    def grabWidget(self, widget, rect): # real signature unknown; restored from __doc__
        """
        grabWidget(widget: PySide2.QtCore.QObject, rect: PySide2.QtCore.QRect) -> PySide2.QtGui.QPixmap
        grabWidget(widget: PySide2.QtCore.QObject, x: int = 0, y: int = 0, w: int = -1, h: int = -1) -> PySide2.QtGui.QPixmap
        """
        pass

    def grabWindow(self, arg__1, x=0, y=0, w=-1, h=-1): # real signature unknown; restored from __doc__
        """ grabWindow(arg__1: int, x: int = 0, y: int = 0, w: int = -1, h: int = -1) -> PySide2.QtGui.QPixmap """
        pass

    def hasAlpha(self): # real signature unknown; restored from __doc__
        """ hasAlpha(self) -> bool """
        return False

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ hasAlphaChannel(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isQBitmap(self): # real signature unknown; restored from __doc__
        """ isQBitmap(self) -> bool """
        return False

    def load(self, fileName, format, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ load(self, fileName: str, format: typing.Optional[bytes] = None, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> bool """
        pass

    def loadFromData(self, buf, len, format, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        loadFromData(self, buf: bytes, len: int, format: typing.Optional[bytes] = None, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> bool
        loadFromData(self, data: PySide2.QtCore.QByteArray, format: typing.Optional[bytes] = None, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> bool
        """
        pass

    def mask(self): # real signature unknown; restored from __doc__
        """ mask(self) -> PySide2.QtGui.QBitmap """
        pass

    def metric(self, arg__1): # real signature unknown; restored from __doc__
        """ metric(self, arg__1: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> PySide2.QtCore.QRect """
        pass

    def save(self, device, format, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        save(self, device: PySide2.QtCore.QIODevice, format: typing.Optional[bytes] = None, quality: int = -1) -> bool
        save(self, fileName: str, format: typing.Optional[bytes] = None, quality: int = -1) -> bool
        """
        pass

    def scaled(self, s, aspectMode=None, mode=None): # real signature unknown; restored from __doc__
        """
        scaled(self, s: PySide2.QtCore.QSize, aspectMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap
        scaled(self, w: int, h: int, aspectMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap
        """
        pass

    def scaledToHeight(self, h, mode=None): # real signature unknown; restored from __doc__
        """ scaledToHeight(self, h: int, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap """
        pass

    def scaledToWidth(self, w, mode=None): # real signature unknown; restored from __doc__
        """ scaledToWidth(self, w: int, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap """
        pass

    def scroll(self, dx, dy, rect, exposed, PySide2_QtGui_QRegion=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        scroll(self, dx: int, dy: int, rect: PySide2.QtCore.QRect, exposed: typing.Optional[PySide2.QtGui.QRegion] = None) -> None
        scroll(self, dx: int, dy: int, x: int, y: int, width: int, height: int, exposed: typing.Optional[PySide2.QtGui.QRegion] = None) -> None
        """
        pass

    def setDevicePixelRatio(self, scaleFactor): # real signature unknown; restored from __doc__
        """ setDevicePixelRatio(self, scaleFactor: float) -> None """
        pass

    def setMask(self, arg__1): # real signature unknown; restored from __doc__
        """ setMask(self, arg__1: PySide2.QtGui.QBitmap) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QPixmap) -> None """
        pass

    def toImage(self): # real signature unknown; restored from __doc__
        """ toImage(self) -> PySide2.QtGui.QImage """
        pass

    def transformed(self, arg__1, mode=None): # real signature unknown; restored from __doc__
        """
        transformed(self, arg__1: PySide2.QtGui.QMatrix, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap
        transformed(self, arg__1: PySide2.QtGui.QTransform, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap
        """
        pass

    def trueMatrix(self, m, w, h): # real signature unknown; restored from __doc__
        """
        trueMatrix(m: PySide2.QtGui.QMatrix, w: int, h: int) -> PySide2.QtGui.QMatrix
        trueMatrix(m: PySide2.QtGui.QTransform, w: int, h: int) -> PySide2.QtGui.QTransform
        """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


