# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QPaintDevice import QPaintDevice

class QImage(QPaintDevice):
    """
    QImage(self) -> None
    QImage(self, arg__1: PySide2.QtGui.QImage) -> None
    QImage(self, arg__1: str, arg__2: int, arg__3: int, arg__4: PySide2.QtGui.QImage.Format) -> None
    QImage(self, arg__1: str, arg__2: int, arg__3: int, arg__4: int, arg__5: PySide2.QtGui.QImage.Format) -> None
    QImage(self, data: bytes, width: int, height: int, bytesPerLine: int, format: PySide2.QtGui.QImage.Format, cleanupFunction: typing.Optional[typing.Callable] = None, cleanupInfo: typing.Optional[int] = None) -> None
    QImage(self, data: bytes, width: int, height: int, format: PySide2.QtGui.QImage.Format, cleanupFunction: typing.Optional[typing.Callable] = None, cleanupInfo: typing.Optional[int] = None) -> None
    QImage(self, fileName: str, format: typing.Optional[bytes] = None) -> None
    QImage(self, size: PySide2.QtCore.QSize, format: PySide2.QtGui.QImage.Format) -> None
    QImage(self, width: int, height: int, format: PySide2.QtGui.QImage.Format) -> None
    QImage(self, xpm: typing.Sequence[str]) -> None
    """
    def allGray(self): # real signature unknown; restored from __doc__
        """ allGray(self) -> bool """
        return False

    def alphaChannel(self): # real signature unknown; restored from __doc__
        """ alphaChannel(self) -> PySide2.QtGui.QImage """
        pass

    def bitPlaneCount(self): # real signature unknown; restored from __doc__
        """ bitPlaneCount(self) -> int """
        return 0

    def bits(self): # real signature unknown; restored from __doc__
        """ bits(self) -> bytes """
        return b""

    def byteCount(self): # real signature unknown; restored from __doc__
        """ byteCount(self) -> int """
        return 0

    def bytesPerLine(self): # real signature unknown; restored from __doc__
        """ bytesPerLine(self) -> int """
        return 0

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def color(self, i): # real signature unknown; restored from __doc__
        """ color(self, i: int) -> int """
        return 0

    def colorCount(self): # real signature unknown; restored from __doc__
        """ colorCount(self) -> int """
        return 0

    def colorSpace(self): # real signature unknown; restored from __doc__
        """ colorSpace(self) -> PySide2.QtGui.QColorSpace """
        pass

    def colorTable(self): # real signature unknown; restored from __doc__
        """ colorTable(self) -> typing.List[int] """
        pass

    def constBits(self): # real signature unknown; restored from __doc__
        """ constBits(self) -> bytes """
        return b""

    def constScanLine(self, arg__1): # real signature unknown; restored from __doc__
        """ constScanLine(self, arg__1: int) -> bytes """
        return b""

    def convertedToColorSpace(self, arg__1): # real signature unknown; restored from __doc__
        """ convertedToColorSpace(self, arg__1: PySide2.QtGui.QColorSpace) -> PySide2.QtGui.QImage """
        pass

    def convertTo(self, f, flags=None): # real signature unknown; restored from __doc__
        """ convertTo(self, f: PySide2.QtGui.QImage.Format, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> None """
        pass

    def convertToColorSpace(self, arg__1): # real signature unknown; restored from __doc__
        """ convertToColorSpace(self, arg__1: PySide2.QtGui.QColorSpace) -> None """
        pass

    def convertToFormat(self, f, colorTable, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        convertToFormat(self, f: PySide2.QtGui.QImage.Format, colorTable: typing.List[int], flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QImage
        convertToFormat(self, f: PySide2.QtGui.QImage.Format, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QImage
        """
        pass

    def convertToFormat_helper(self, format, flags): # real signature unknown; restored from __doc__
        """ convertToFormat_helper(self, format: PySide2.QtGui.QImage.Format, flags: PySide2.QtCore.Qt.ImageConversionFlags) -> PySide2.QtGui.QImage """
        pass

    def convertToFormat_inplace(self, format, flags): # real signature unknown; restored from __doc__
        """ convertToFormat_inplace(self, format: PySide2.QtGui.QImage.Format, flags: PySide2.QtCore.Qt.ImageConversionFlags) -> bool """
        return False

    def copy(self, rect=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        copy(self, rect: PySide2.QtCore.QRect = Default(QRect)) -> PySide2.QtGui.QImage
        copy(self, x: int, y: int, w: int, h: int) -> PySide2.QtGui.QImage
        """
        pass

    def createAlphaMask(self, flags=None): # real signature unknown; restored from __doc__
        """ createAlphaMask(self, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QImage """
        pass

    def createHeuristicMask(self, clipTight=True): # real signature unknown; restored from __doc__
        """ createHeuristicMask(self, clipTight: bool = True) -> PySide2.QtGui.QImage """
        pass

    def createMaskFromColor(self, color, mode=None): # real signature unknown; restored from __doc__
        """ createMaskFromColor(self, color: int, mode: PySide2.QtCore.Qt.MaskMode = PySide2.QtCore.Qt.MaskMode.MaskInColor) -> PySide2.QtGui.QImage """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def dotsPerMeterX(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterX(self) -> int """
        return 0

    def dotsPerMeterY(self): # real signature unknown; restored from __doc__
        """ dotsPerMeterY(self) -> int """
        return 0

    def fill(self, color): # real signature unknown; restored from __doc__
        """
        fill(self, color: PySide2.QtCore.Qt.GlobalColor) -> None
        fill(self, color: PySide2.QtGui.QColor) -> None
        fill(self, pixel: int) -> None
        """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QImage.Format """
        pass

    def fromData(self, data, format, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fromData(data: PySide2.QtCore.QByteArray, format: typing.Optional[bytes] = None) -> PySide2.QtGui.QImage """
        pass

    def hasAlphaChannel(self): # real signature unknown; restored from __doc__
        """ hasAlphaChannel(self) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def invertPixels(self, mode=None): # real signature unknown; restored from __doc__
        """ invertPixels(self, mode: PySide2.QtGui.QImage.InvertMode = PySide2.QtGui.QImage.InvertMode.InvertRgb) -> None """
        pass

    def isGrayscale(self): # real signature unknown; restored from __doc__
        """ isGrayscale(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def load(self, device, format): # real signature unknown; restored from __doc__
        """
        load(self, device: PySide2.QtCore.QIODevice, format: bytes) -> bool
        load(self, fileName: str, format: typing.Optional[bytes] = None) -> bool
        """
        return False

    def loadFromData(self, data, aformat, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ loadFromData(self, data: PySide2.QtCore.QByteArray, aformat: typing.Optional[bytes] = None) -> bool """
        pass

    def metric(self, metric): # real signature unknown; restored from __doc__
        """ metric(self, metric: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def mirrored(self, horizontally=False, vertically=True): # real signature unknown; restored from __doc__
        """ mirrored(self, horizontally: bool = False, vertically: bool = True) -> PySide2.QtGui.QImage """
        pass

    def mirrored_helper(self, horizontal, vertical): # real signature unknown; restored from __doc__
        """ mirrored_helper(self, horizontal: bool, vertical: bool) -> PySide2.QtGui.QImage """
        pass

    def mirrored_inplace(self, horizontal, vertical): # real signature unknown; restored from __doc__
        """ mirrored_inplace(self, horizontal: bool, vertical: bool) -> None """
        pass

    def offset(self): # real signature unknown; restored from __doc__
        """ offset(self) -> PySide2.QtCore.QPoint """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def pixel(self, pt): # real signature unknown; restored from __doc__
        """
        pixel(self, pt: PySide2.QtCore.QPoint) -> int
        pixel(self, x: int, y: int) -> int
        """
        return 0

    def pixelColor(self, pt): # real signature unknown; restored from __doc__
        """
        pixelColor(self, pt: PySide2.QtCore.QPoint) -> PySide2.QtGui.QColor
        pixelColor(self, x: int, y: int) -> PySide2.QtGui.QColor
        """
        pass

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> PySide2.QtGui.QPixelFormat """
        pass

    def pixelIndex(self, pt): # real signature unknown; restored from __doc__
        """
        pixelIndex(self, pt: PySide2.QtCore.QPoint) -> int
        pixelIndex(self, x: int, y: int) -> int
        """
        return 0

    def rect(self): # real signature unknown; restored from __doc__
        """ rect(self) -> PySide2.QtCore.QRect """
        pass

    def reinterpretAsFormat(self, f): # real signature unknown; restored from __doc__
        """ reinterpretAsFormat(self, f: PySide2.QtGui.QImage.Format) -> bool """
        return False

    def rgbSwapped(self): # real signature unknown; restored from __doc__
        """ rgbSwapped(self) -> PySide2.QtGui.QImage """
        pass

    def rgbSwapped_helper(self): # real signature unknown; restored from __doc__
        """ rgbSwapped_helper(self) -> PySide2.QtGui.QImage """
        pass

    def rgbSwapped_inplace(self): # real signature unknown; restored from __doc__
        """ rgbSwapped_inplace(self) -> None """
        pass

    def save(self, device, format, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        save(self, device: PySide2.QtCore.QIODevice, format: typing.Optional[bytes] = None, quality: int = -1) -> bool
        save(self, fileName: str, format: typing.Optional[bytes] = None, quality: int = -1) -> bool
        """
        pass

    def scaled(self, s, aspectMode=None, mode=None): # real signature unknown; restored from __doc__
        """
        scaled(self, s: PySide2.QtCore.QSize, aspectMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage
        scaled(self, w: int, h: int, aspectMode: PySide2.QtCore.Qt.AspectRatioMode = PySide2.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage
        """
        pass

    def scaledToHeight(self, h, mode=None): # real signature unknown; restored from __doc__
        """ scaledToHeight(self, h: int, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage """
        pass

    def scaledToWidth(self, w, mode=None): # real signature unknown; restored from __doc__
        """ scaledToWidth(self, w: int, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage """
        pass

    def scanLine(self, arg__1): # real signature unknown; restored from __doc__
        """ scanLine(self, arg__1: int) -> bytes """
        return b""

    def setAlphaChannel(self, alphaChannel): # real signature unknown; restored from __doc__
        """ setAlphaChannel(self, alphaChannel: PySide2.QtGui.QImage) -> None """
        pass

    def setColor(self, i, c): # real signature unknown; restored from __doc__
        """ setColor(self, i: int, c: int) -> None """
        pass

    def setColorCount(self, arg__1): # real signature unknown; restored from __doc__
        """ setColorCount(self, arg__1: int) -> None """
        pass

    def setColorSpace(self, arg__1): # real signature unknown; restored from __doc__
        """ setColorSpace(self, arg__1: PySide2.QtGui.QColorSpace) -> None """
        pass

    def setColorTable(self, colors, p_int=None): # real signature unknown; restored from __doc__
        """ setColorTable(self, colors: typing.List[int]) -> None """
        pass

    def setDevicePixelRatio(self, scaleFactor): # real signature unknown; restored from __doc__
        """ setDevicePixelRatio(self, scaleFactor: float) -> None """
        pass

    def setDotsPerMeterX(self, arg__1): # real signature unknown; restored from __doc__
        """ setDotsPerMeterX(self, arg__1: int) -> None """
        pass

    def setDotsPerMeterY(self, arg__1): # real signature unknown; restored from __doc__
        """ setDotsPerMeterY(self, arg__1: int) -> None """
        pass

    def setOffset(self, arg__1): # real signature unknown; restored from __doc__
        """ setOffset(self, arg__1: PySide2.QtCore.QPoint) -> None """
        pass

    def setPixel(self, pt, index_or_rgb): # real signature unknown; restored from __doc__
        """
        setPixel(self, pt: PySide2.QtCore.QPoint, index_or_rgb: int) -> None
        setPixel(self, x: int, y: int, index_or_rgb: int) -> None
        """
        pass

    def setPixelColor(self, pt, c): # real signature unknown; restored from __doc__
        """
        setPixelColor(self, pt: PySide2.QtCore.QPoint, c: PySide2.QtGui.QColor) -> None
        setPixelColor(self, x: int, y: int, c: PySide2.QtGui.QColor) -> None
        """
        pass

    def setText(self, key, value): # real signature unknown; restored from __doc__
        """ setText(self, key: str, value: str) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def sizeInBytes(self): # real signature unknown; restored from __doc__
        """ sizeInBytes(self) -> int """
        return 0

    def smoothScaled(self, w, h): # real signature unknown; restored from __doc__
        """ smoothScaled(self, w: int, h: int) -> PySide2.QtGui.QImage """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QImage) -> None """
        pass

    def text(self, key=''): # real signature unknown; restored from __doc__
        """ text(self, key: str = '') -> str """
        return ""

    def textKeys(self): # real signature unknown; restored from __doc__
        """ textKeys(self) -> typing.List[str] """
        pass

    def toImageFormat(self, format): # real signature unknown; restored from __doc__
        """ toImageFormat(format: PySide2.QtGui.QPixelFormat) -> PySide2.QtGui.QImage.Format """
        pass

    def toPixelFormat(self, format): # real signature unknown; restored from __doc__
        """ toPixelFormat(format: PySide2.QtGui.QImage.Format) -> PySide2.QtGui.QPixelFormat """
        pass

    def transformed(self, matrix, mode=None): # real signature unknown; restored from __doc__
        """
        transformed(self, matrix: PySide2.QtGui.QMatrix, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage
        transformed(self, matrix: PySide2.QtGui.QTransform, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QImage
        """
        pass

    def trueMatrix(self, arg__1, w, h): # real signature unknown; restored from __doc__
        """
        trueMatrix(arg__1: PySide2.QtGui.QMatrix, w: int, h: int) -> PySide2.QtGui.QMatrix
        trueMatrix(arg__1: PySide2.QtGui.QTransform, w: int, h: int) -> PySide2.QtGui.QTransform
        """
        pass

    def valid(self, pt): # real signature unknown; restored from __doc__
        """
        valid(self, pt: PySide2.QtCore.QPoint) -> bool
        valid(self, x: int, y: int) -> bool
        """
        return False

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

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
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

    Format = None # (!) real value is "<class 'PySide2.QtGui.QImage.Format'>"
    Format_A2BGR30_Premultiplied = PySide2.QtGui.QImage.Format.Format_A2BGR30_Premultiplied
    Format_A2RGB30_Premultiplied = PySide2.QtGui.QImage.Format.Format_A2RGB30_Premultiplied
    Format_Alpha8 = PySide2.QtGui.QImage.Format.Format_Alpha8
    Format_ARGB32 = PySide2.QtGui.QImage.Format.Format_ARGB32
    Format_ARGB32_Premultiplied = PySide2.QtGui.QImage.Format.Format_ARGB32_Premultiplied
    Format_ARGB4444_Premultiplied = PySide2.QtGui.QImage.Format.Format_ARGB4444_Premultiplied
    Format_ARGB6666_Premultiplied = PySide2.QtGui.QImage.Format.Format_ARGB6666_Premultiplied
    Format_ARGB8555_Premultiplied = PySide2.QtGui.QImage.Format.Format_ARGB8555_Premultiplied
    Format_ARGB8565_Premultiplied = PySide2.QtGui.QImage.Format.Format_ARGB8565_Premultiplied
    Format_BGR30 = PySide2.QtGui.QImage.Format.Format_BGR30
    Format_BGR888 = PySide2.QtGui.QImage.Format.Format_BGR888
    Format_Grayscale16 = PySide2.QtGui.QImage.Format.Format_Grayscale16
    Format_Grayscale8 = PySide2.QtGui.QImage.Format.Format_Grayscale8
    Format_Indexed8 = PySide2.QtGui.QImage.Format.Format_Indexed8
    Format_Invalid = PySide2.QtGui.QImage.Format.Format_Invalid
    Format_Mono = PySide2.QtGui.QImage.Format.Format_Mono
    Format_MonoLSB = PySide2.QtGui.QImage.Format.Format_MonoLSB
    Format_RGB16 = PySide2.QtGui.QImage.Format.Format_RGB16
    Format_RGB30 = PySide2.QtGui.QImage.Format.Format_RGB30
    Format_RGB32 = PySide2.QtGui.QImage.Format.Format_RGB32
    Format_RGB444 = PySide2.QtGui.QImage.Format.Format_RGB444
    Format_RGB555 = PySide2.QtGui.QImage.Format.Format_RGB555
    Format_RGB666 = PySide2.QtGui.QImage.Format.Format_RGB666
    Format_RGB888 = PySide2.QtGui.QImage.Format.Format_RGB888
    Format_RGBA64 = PySide2.QtGui.QImage.Format.Format_RGBA64
    Format_RGBA64_Premultiplied = PySide2.QtGui.QImage.Format.Format_RGBA64_Premultiplied
    Format_RGBA8888 = PySide2.QtGui.QImage.Format.Format_RGBA8888
    Format_RGBA8888_Premultiplied = PySide2.QtGui.QImage.Format.Format_RGBA8888_Premultiplied
    Format_RGBX64 = PySide2.QtGui.QImage.Format.Format_RGBX64
    Format_RGBX8888 = PySide2.QtGui.QImage.Format.Format_RGBX8888
    InvertMode = None # (!) real value is "<class 'PySide2.QtGui.QImage.InvertMode'>"
    InvertRgb = PySide2.QtGui.QImage.InvertMode.InvertRgb
    InvertRgba = PySide2.QtGui.QImage.InvertMode.InvertRgba
    NImageFormats = PySide2.QtGui.QImage.Format.NImageFormats
    __hash__ = None


