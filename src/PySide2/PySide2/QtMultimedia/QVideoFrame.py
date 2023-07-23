# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QVideoFrame(__Shiboken.Object):
    """
    QVideoFrame(self) -> None
    QVideoFrame(self, buffer: PySide2.QtMultimedia.QAbstractVideoBuffer, size: PySide2.QtCore.QSize, format: PySide2.QtMultimedia.QVideoFrame.PixelFormat) -> None
    QVideoFrame(self, bytes: int, size: PySide2.QtCore.QSize, bytesPerLine: int, format: PySide2.QtMultimedia.QVideoFrame.PixelFormat) -> None
    QVideoFrame(self, image: PySide2.QtGui.QImage) -> None
    QVideoFrame(self, other: PySide2.QtMultimedia.QVideoFrame) -> None
    """
    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> typing.Dict[str, typing.Any] """
        pass

    def bits(self): # real signature unknown; restored from __doc__
        """ bits(self) -> bytes """
        return b""

    def buffer(self): # real signature unknown; restored from __doc__
        """ buffer(self) -> PySide2.QtMultimedia.QAbstractVideoBuffer """
        pass

    def bytesPerLine(self): # real signature unknown; restored from __doc__
        """
        bytesPerLine(self) -> int
        bytesPerLine(self, plane: int) -> int
        """
        return 0

    def endTime(self): # real signature unknown; restored from __doc__
        """ endTime(self) -> int """
        return 0

    def fieldType(self): # real signature unknown; restored from __doc__
        """ fieldType(self) -> PySide2.QtMultimedia.QVideoFrame.FieldType """
        pass

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> typing.Any """
        pass

    def handleType(self): # real signature unknown; restored from __doc__
        """ handleType(self) -> PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType """
        pass

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def image(self): # real signature unknown; restored from __doc__
        """ image(self) -> PySide2.QtGui.QImage """
        pass

    def imageFormatFromPixelFormat(self, format): # real signature unknown; restored from __doc__
        """ imageFormatFromPixelFormat(format: PySide2.QtMultimedia.QVideoFrame.PixelFormat) -> PySide2.QtGui.QImage.Format """
        pass

    def isMapped(self): # real signature unknown; restored from __doc__
        """ isMapped(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def map(self, mode): # real signature unknown; restored from __doc__
        """ map(self, mode: PySide2.QtMultimedia.QAbstractVideoBuffer.MapMode) -> bool """
        return False

    def mapMode(self): # real signature unknown; restored from __doc__
        """ mapMode(self) -> PySide2.QtMultimedia.QAbstractVideoBuffer.MapMode """
        pass

    def mappedBytes(self): # real signature unknown; restored from __doc__
        """ mappedBytes(self) -> int """
        return 0

    def metaData(self, key): # real signature unknown; restored from __doc__
        """ metaData(self, key: str) -> typing.Any """
        pass

    def pixelFormat(self): # real signature unknown; restored from __doc__
        """ pixelFormat(self) -> PySide2.QtMultimedia.QVideoFrame.PixelFormat """
        pass

    def pixelFormatFromImageFormat(self, format): # real signature unknown; restored from __doc__
        """ pixelFormatFromImageFormat(format: PySide2.QtGui.QImage.Format) -> PySide2.QtMultimedia.QVideoFrame.PixelFormat """
        pass

    def planeCount(self): # real signature unknown; restored from __doc__
        """ planeCount(self) -> int """
        return 0

    def setEndTime(self, time): # real signature unknown; restored from __doc__
        """ setEndTime(self, time: int) -> None """
        pass

    def setFieldType(self, arg__1): # real signature unknown; restored from __doc__
        """ setFieldType(self, arg__1: PySide2.QtMultimedia.QVideoFrame.FieldType) -> None """
        pass

    def setMetaData(self, key, value): # real signature unknown; restored from __doc__
        """ setMetaData(self, key: str, value: typing.Any) -> None """
        pass

    def setStartTime(self, time): # real signature unknown; restored from __doc__
        """ setStartTime(self, time: int) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def startTime(self): # real signature unknown; restored from __doc__
        """ startTime(self) -> int """
        return 0

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) -> None """
        pass

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

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

    BottomField = PySide2.QtMultimedia.QVideoFrame.FieldType.BottomField
    FieldType = None # (!) real value is "<class 'PySide2.QtMultimedia.QVideoFrame.FieldType'>"
    Format_ABGR32 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_ABGR32
    Format_AdobeDng = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_AdobeDng
    Format_ARGB32 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_ARGB32
    Format_ARGB32_Premultiplied = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_ARGB32_Premultiplied
    Format_ARGB8565_Premultiplied = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_ARGB8565_Premultiplied
    Format_AYUV444 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_AYUV444
    Format_AYUV444_Premultiplied = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_AYUV444_Premultiplied
    Format_BGR24 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_BGR24
    Format_BGR32 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_BGR32
    Format_BGR555 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_BGR555
    Format_BGR565 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_BGR565
    Format_BGRA32 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_BGRA32
    Format_BGRA32_Premultiplied = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_BGRA32_Premultiplied
    Format_BGRA5658_Premultiplied = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_BGRA5658_Premultiplied
    Format_CameraRaw = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_CameraRaw
    Format_IMC1 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_IMC1
    Format_IMC2 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_IMC2
    Format_IMC3 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_IMC3
    Format_IMC4 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_IMC4
    Format_Invalid = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_Invalid
    Format_Jpeg = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_Jpeg
    Format_NV12 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_NV12
    Format_NV21 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_NV21
    Format_RGB24 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_RGB24
    Format_RGB32 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_RGB32
    Format_RGB555 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_RGB555
    Format_RGB565 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_RGB565
    Format_User = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_User
    Format_UYVY = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_UYVY
    Format_Y16 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_Y16
    Format_Y8 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_Y8
    Format_YUV420P = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_YUV420P
    Format_YUV422P = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_YUV422P
    Format_YUV444 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_YUV444
    Format_YUYV = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_YUYV
    Format_YV12 = PySide2.QtMultimedia.QVideoFrame.PixelFormat.Format_YV12
    InterlacedFrame = PySide2.QtMultimedia.QVideoFrame.FieldType.InterlacedFrame
    NPixelFormats = PySide2.QtMultimedia.QVideoFrame.PixelFormat.NPixelFormats
    PixelFormat = None # (!) real value is "<class 'PySide2.QtMultimedia.QVideoFrame.PixelFormat'>"
    ProgressiveFrame = PySide2.QtMultimedia.QVideoFrame.FieldType.ProgressiveFrame
    TopField = PySide2.QtMultimedia.QVideoFrame.FieldType.TopField
    __hash__ = None


