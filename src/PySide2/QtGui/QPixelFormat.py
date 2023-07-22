# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPixelFormat(__Shiboken.Object):
    """
    QPixelFormat(self) -> None
    QPixelFormat(self, QPixelFormat: PySide2.QtGui.QPixelFormat) -> None
    QPixelFormat(self, colorModel: PySide2.QtGui.QPixelFormat.ColorModel, firstSize: int, secondSize: int, thirdSize: int, fourthSize: int, fifthSize: int, alphaSize: int, alphaUsage: PySide2.QtGui.QPixelFormat.AlphaUsage, alphaPosition: PySide2.QtGui.QPixelFormat.AlphaPosition, premultiplied: PySide2.QtGui.QPixelFormat.AlphaPremultiplied, typeInterpretation: PySide2.QtGui.QPixelFormat.TypeInterpretation, byteOrder: PySide2.QtGui.QPixelFormat.ByteOrder = PySide2.QtGui.QPixelFormat.ByteOrder.CurrentSystemEndian, subEnum: int = 0) -> None
    """
    def alphaPosition(self): # real signature unknown; restored from __doc__
        """ alphaPosition(self) -> PySide2.QtGui.QPixelFormat.AlphaPosition """
        pass

    def alphaSize(self): # real signature unknown; restored from __doc__
        """ alphaSize(self) -> int """
        return 0

    def alphaUsage(self): # real signature unknown; restored from __doc__
        """ alphaUsage(self) -> PySide2.QtGui.QPixelFormat.AlphaUsage """
        pass

    def bitsPerPixel(self): # real signature unknown; restored from __doc__
        """ bitsPerPixel(self) -> int """
        return 0

    def blackSize(self): # real signature unknown; restored from __doc__
        """ blackSize(self) -> int """
        return 0

    def blueSize(self): # real signature unknown; restored from __doc__
        """ blueSize(self) -> int """
        return 0

    def brightnessSize(self): # real signature unknown; restored from __doc__
        """ brightnessSize(self) -> int """
        return 0

    def byteOrder(self): # real signature unknown; restored from __doc__
        """ byteOrder(self) -> PySide2.QtGui.QPixelFormat.ByteOrder """
        pass

    def channelCount(self): # real signature unknown; restored from __doc__
        """ channelCount(self) -> int """
        return 0

    def colorModel(self): # real signature unknown; restored from __doc__
        """ colorModel(self) -> PySide2.QtGui.QPixelFormat.ColorModel """
        pass

    def cyanSize(self): # real signature unknown; restored from __doc__
        """ cyanSize(self) -> int """
        return 0

    def greenSize(self): # real signature unknown; restored from __doc__
        """ greenSize(self) -> int """
        return 0

    def hueSize(self): # real signature unknown; restored from __doc__
        """ hueSize(self) -> int """
        return 0

    def lightnessSize(self): # real signature unknown; restored from __doc__
        """ lightnessSize(self) -> int """
        return 0

    def magentaSize(self): # real signature unknown; restored from __doc__
        """ magentaSize(self) -> int """
        return 0

    def premultiplied(self): # real signature unknown; restored from __doc__
        """ premultiplied(self) -> PySide2.QtGui.QPixelFormat.AlphaPremultiplied """
        pass

    def redSize(self): # real signature unknown; restored from __doc__
        """ redSize(self) -> int """
        return 0

    def saturationSize(self): # real signature unknown; restored from __doc__
        """ saturationSize(self) -> int """
        return 0

    def subEnum(self): # real signature unknown; restored from __doc__
        """ subEnum(self) -> int """
        return 0

    def typeInterpretation(self): # real signature unknown; restored from __doc__
        """ typeInterpretation(self) -> PySide2.QtGui.QPixelFormat.TypeInterpretation """
        pass

    def yellowSize(self): # real signature unknown; restored from __doc__
        """ yellowSize(self) -> int """
        return 0

    def yuvLayout(self): # real signature unknown; restored from __doc__
        """ yuvLayout(self) -> PySide2.QtGui.QPixelFormat.YUVLayout """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Alpha = PySide2.QtGui.QPixelFormat.ColorModel.Alpha
    AlphaPosition = None # (!) real value is "<class 'PySide2.QtGui.QPixelFormat.AlphaPosition'>"
    AlphaPremultiplied = None # (!) real value is "<class 'PySide2.QtGui.QPixelFormat.AlphaPremultiplied'>"
    AlphaUsage = None # (!) real value is "<class 'PySide2.QtGui.QPixelFormat.AlphaUsage'>"
    AtBeginning = PySide2.QtGui.QPixelFormat.AlphaPosition.AtBeginning
    AtEnd = PySide2.QtGui.QPixelFormat.AlphaPosition.AtEnd
    BGR = PySide2.QtGui.QPixelFormat.ColorModel.BGR
    BigEndian = PySide2.QtGui.QPixelFormat.ByteOrder.BigEndian
    ByteOrder = None # (!) real value is "<class 'PySide2.QtGui.QPixelFormat.ByteOrder'>"
    CMYK = PySide2.QtGui.QPixelFormat.ColorModel.CMYK
    ColorModel = None # (!) real value is "<class 'PySide2.QtGui.QPixelFormat.ColorModel'>"
    CurrentSystemEndian = PySide2.QtGui.QPixelFormat.ByteOrder.CurrentSystemEndian
    FloatingPoint = PySide2.QtGui.QPixelFormat.TypeInterpretation.FloatingPoint
    Grayscale = PySide2.QtGui.QPixelFormat.ColorModel.Grayscale
    HSL = PySide2.QtGui.QPixelFormat.ColorModel.HSL
    HSV = PySide2.QtGui.QPixelFormat.ColorModel.HSV
    IgnoresAlpha = PySide2.QtGui.QPixelFormat.AlphaUsage.IgnoresAlpha
    IMC1 = PySide2.QtGui.QPixelFormat.YUVLayout.IMC1
    IMC2 = PySide2.QtGui.QPixelFormat.YUVLayout.IMC2
    IMC3 = PySide2.QtGui.QPixelFormat.YUVLayout.IMC3
    IMC4 = PySide2.QtGui.QPixelFormat.YUVLayout.IMC4
    Indexed = PySide2.QtGui.QPixelFormat.ColorModel.Indexed
    LittleEndian = PySide2.QtGui.QPixelFormat.ByteOrder.LittleEndian
    NotPremultiplied = PySide2.QtGui.QPixelFormat.AlphaPremultiplied.NotPremultiplied
    NV12 = PySide2.QtGui.QPixelFormat.YUVLayout.NV12
    NV21 = PySide2.QtGui.QPixelFormat.YUVLayout.NV21
    Premultiplied = PySide2.QtGui.QPixelFormat.AlphaPremultiplied.Premultiplied
    RGB = PySide2.QtGui.QPixelFormat.ColorModel.RGB
    TypeInterpretation = None # (!) real value is "<class 'PySide2.QtGui.QPixelFormat.TypeInterpretation'>"
    UnsignedByte = PySide2.QtGui.QPixelFormat.TypeInterpretation.UnsignedByte
    UnsignedInteger = PySide2.QtGui.QPixelFormat.TypeInterpretation.UnsignedInteger
    UnsignedShort = PySide2.QtGui.QPixelFormat.TypeInterpretation.UnsignedShort
    UsesAlpha = PySide2.QtGui.QPixelFormat.AlphaUsage.UsesAlpha
    UYVY = PySide2.QtGui.QPixelFormat.YUVLayout.UYVY
    Y16 = PySide2.QtGui.QPixelFormat.YUVLayout.Y16
    Y8 = PySide2.QtGui.QPixelFormat.YUVLayout.Y8
    YUV = PySide2.QtGui.QPixelFormat.ColorModel.YUV
    YUV411 = PySide2.QtGui.QPixelFormat.YUVLayout.YUV411
    YUV420P = PySide2.QtGui.QPixelFormat.YUVLayout.YUV420P
    YUV420SP = PySide2.QtGui.QPixelFormat.YUVLayout.YUV420SP
    YUV422 = PySide2.QtGui.QPixelFormat.YUVLayout.YUV422
    YUV444 = PySide2.QtGui.QPixelFormat.YUVLayout.YUV444
    YUVLayout = None # (!) real value is "<class 'PySide2.QtGui.QPixelFormat.YUVLayout'>"
    YUYV = PySide2.QtGui.QPixelFormat.YUVLayout.YUYV
    YV12 = PySide2.QtGui.QPixelFormat.YUVLayout.YV12


