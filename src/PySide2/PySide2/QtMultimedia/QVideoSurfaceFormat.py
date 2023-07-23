# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QVideoSurfaceFormat(__Shiboken.Object):
    """
    QVideoSurfaceFormat(self) -> None
    QVideoSurfaceFormat(self, format: PySide2.QtMultimedia.QVideoSurfaceFormat) -> None
    QVideoSurfaceFormat(self, size: PySide2.QtCore.QSize, pixelFormat: PySide2.QtMultimedia.QVideoFrame.PixelFormat, handleType: PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.NoHandle) -> None
    """
    def frameHeight(self): # real signature unknown; restored from __doc__
        """ frameHeight(self) -> int """
        return 0

    def frameRate(self): # real signature unknown; restored from __doc__
        """ frameRate(self) -> float """
        return 0.0

    def frameSize(self): # real signature unknown; restored from __doc__
        """ frameSize(self) -> PySide2.QtCore.QSize """
        pass

    def frameWidth(self): # real signature unknown; restored from __doc__
        """ frameWidth(self) -> int """
        return 0

    def handleType(self): # real signature unknown; restored from __doc__
        """ handleType(self) -> PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType """
        pass

    def isMirrored(self): # real signature unknown; restored from __doc__
        """ isMirrored(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def pixelAspectRatio(self): # real signature unknown; restored from __doc__
        """ pixelAspectRatio(self) -> PySide2.QtCore.QSize """
        pass

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> PySide2.QtMultimedia.QVideoFrame.PixelFormat """
        pass

    def property(self, name): # real signature unknown; restored from __doc__
        """ property(self, name: bytes) -> typing.Any """
        pass

    def propertyNames(self): # real signature unknown; restored from __doc__
        """ propertyNames(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def scanLineDirection(self): # real signature unknown; restored from __doc__
        """ scanLineDirection(self) -> PySide2.QtMultimedia.QVideoSurfaceFormat.Direction """
        pass

    def setFrameRate(self, rate): # real signature unknown; restored from __doc__
        """ setFrameRate(self, rate: float) -> None """
        pass

    def setFrameSize(self, size): # real signature unknown; restored from __doc__
        """
        setFrameSize(self, size: PySide2.QtCore.QSize) -> None
        setFrameSize(self, width: int, height: int) -> None
        """
        pass

    def setMirrored(self, mirrored): # real signature unknown; restored from __doc__
        """ setMirrored(self, mirrored: bool) -> None """
        pass

    def setPixelAspectRatio(self, ratio): # real signature unknown; restored from __doc__
        """
        setPixelAspectRatio(self, ratio: PySide2.QtCore.QSize) -> None
        setPixelAspectRatio(self, width: int, height: int) -> None
        """
        pass

    def setProperty(self, name, value): # real signature unknown; restored from __doc__
        """ setProperty(self, name: bytes, value: typing.Any) -> None """
        pass

    def setScanLineDirection(self, direction): # real signature unknown; restored from __doc__
        """ setScanLineDirection(self, direction: PySide2.QtMultimedia.QVideoSurfaceFormat.Direction) -> None """
        pass

    def setViewport(self, viewport): # real signature unknown; restored from __doc__
        """ setViewport(self, viewport: PySide2.QtCore.QRect) -> None """
        pass

    def setYCbCrColorSpace(self, colorSpace): # real signature unknown; restored from __doc__
        """ setYCbCrColorSpace(self, colorSpace: PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace) -> None """
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def viewport(self): # real signature unknown; restored from __doc__
        """ viewport(self) -> PySide2.QtCore.QRect """
        pass

    def yCbCrColorSpace(self): # real signature unknown; restored from __doc__
        """ yCbCrColorSpace(self) -> PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
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

    BottomToTop = PySide2.QtMultimedia.QVideoSurfaceFormat.Direction.BottomToTop
    Direction = None # (!) real value is "<class 'PySide2.QtMultimedia.QVideoSurfaceFormat.Direction'>"
    TopToBottom = PySide2.QtMultimedia.QVideoSurfaceFormat.Direction.TopToBottom
    YCbCrColorSpace = None # (!) real value is "<class 'PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace'>"
    YCbCr_BT601 = PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_BT601
    YCbCr_BT709 = PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_BT709
    YCbCr_CustomMatrix = PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_CustomMatrix
    YCbCr_JPEG = PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_JPEG
    YCbCr_Undefined = PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_Undefined
    YCbCr_xvYCC601 = PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_xvYCC601
    YCbCr_xvYCC709 = PySide2.QtMultimedia.QVideoSurfaceFormat.YCbCrColorSpace.YCbCr_xvYCC709
    __hash__ = None


