# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QImageReader(__Shiboken.Object):
    """
    QImageReader(self) -> None
    QImageReader(self, device: PySide2.QtCore.QIODevice, format: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None
    QImageReader(self, fileName: str, format: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None
    """
    def autoDetectImageFormat(self): # real signature unknown; restored from __doc__
        """ autoDetectImageFormat(self) -> bool """
        return False

    def autoTransform(self): # real signature unknown; restored from __doc__
        """ autoTransform(self) -> bool """
        return False

    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> PySide2.QtGui.QColor """
        pass

    def canRead(self): # real signature unknown; restored from __doc__
        """ canRead(self) -> bool """
        return False

    def clipRect(self): # real signature unknown; restored from __doc__
        """ clipRect(self) -> PySide2.QtCore.QRect """
        pass

    def currentImageNumber(self): # real signature unknown; restored from __doc__
        """ currentImageNumber(self) -> int """
        return 0

    def currentImageRect(self): # real signature unknown; restored from __doc__
        """ currentImageRect(self) -> PySide2.QtCore.QRect """
        pass

    def decideFormatFromContent(self): # real signature unknown; restored from __doc__
        """ decideFormatFromContent(self) -> bool """
        return False

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtGui.QImageReader.ImageReaderError """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtCore.QByteArray """
        pass

    def gamma(self): # real signature unknown; restored from __doc__
        """ gamma(self) -> float """
        return 0.0

    def imageCount(self): # real signature unknown; restored from __doc__
        """ imageCount(self) -> int """
        return 0

    def imageFormat(self, device): # real signature unknown; restored from __doc__
        """
        imageFormat(device: PySide2.QtCore.QIODevice) -> PySide2.QtCore.QByteArray
        imageFormat(fileName: str) -> PySide2.QtCore.QByteArray
        imageFormat(self) -> PySide2.QtGui.QImage.Format
        """
        pass

    def imageFormatsForMimeType(self, mimeType): # real signature unknown; restored from __doc__
        """ imageFormatsForMimeType(mimeType: PySide2.QtCore.QByteArray) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def jumpToImage(self, imageNumber): # real signature unknown; restored from __doc__
        """ jumpToImage(self, imageNumber: int) -> bool """
        return False

    def jumpToNextImage(self): # real signature unknown; restored from __doc__
        """ jumpToNextImage(self) -> bool """
        return False

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def nextImageDelay(self): # real signature unknown; restored from __doc__
        """ nextImageDelay(self) -> int """
        return 0

    def quality(self): # real signature unknown; restored from __doc__
        """ quality(self) -> int """
        return 0

    def read(self): # real signature unknown; restored from __doc__
        """ read(self) -> PySide2.QtGui.QImage """
        pass

    def scaledClipRect(self): # real signature unknown; restored from __doc__
        """ scaledClipRect(self) -> PySide2.QtCore.QRect """
        pass

    def scaledSize(self): # real signature unknown; restored from __doc__
        """ scaledSize(self) -> PySide2.QtCore.QSize """
        pass

    def setAutoDetectImageFormat(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoDetectImageFormat(self, enabled: bool) -> None """
        pass

    def setAutoTransform(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoTransform(self, enabled: bool) -> None """
        pass

    def setBackgroundColor(self, color): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setClipRect(self, rect): # real signature unknown; restored from __doc__
        """ setClipRect(self, rect: PySide2.QtCore.QRect) -> None """
        pass

    def setDecideFormatFromContent(self, ignored): # real signature unknown; restored from __doc__
        """ setDecideFormatFromContent(self, ignored: bool) -> None """
        pass

    def setDevice(self, device): # real signature unknown; restored from __doc__
        """ setDevice(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def setFileName(self, fileName): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: str) -> None """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtCore.QByteArray) -> None """
        pass

    def setGamma(self, gamma): # real signature unknown; restored from __doc__
        """ setGamma(self, gamma: float) -> None """
        pass

    def setQuality(self, quality): # real signature unknown; restored from __doc__
        """ setQuality(self, quality: int) -> None """
        pass

    def setScaledClipRect(self, rect): # real signature unknown; restored from __doc__
        """ setScaledClipRect(self, rect: PySide2.QtCore.QRect) -> None """
        pass

    def setScaledSize(self, size): # real signature unknown; restored from __doc__
        """ setScaledSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> PySide2.QtCore.QSize """
        pass

    def subType(self): # real signature unknown; restored from __doc__
        """ subType(self) -> PySide2.QtCore.QByteArray """
        pass

    def supportedImageFormats(self): # real signature unknown; restored from __doc__
        """ supportedImageFormats() -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def supportedMimeTypes(self): # real signature unknown; restored from __doc__
        """ supportedMimeTypes() -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def supportedSubTypes(self): # real signature unknown; restored from __doc__
        """ supportedSubTypes(self) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def supportsAnimation(self): # real signature unknown; restored from __doc__
        """ supportsAnimation(self) -> bool """
        return False

    def supportsOption(self, option): # real signature unknown; restored from __doc__
        """ supportsOption(self, option: PySide2.QtGui.QImageIOHandler.ImageOption) -> bool """
        return False

    def text(self, key): # real signature unknown; restored from __doc__
        """ text(self, key: str) -> str """
        return ""

    def textKeys(self): # real signature unknown; restored from __doc__
        """ textKeys(self) -> typing.List[str] """
        pass

    def transformation(self): # real signature unknown; restored from __doc__
        """ transformation(self) -> PySide2.QtGui.QImageIOHandler.Transformations """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DeviceError = PySide2.QtGui.QImageReader.ImageReaderError.DeviceError
    FileNotFoundError = PySide2.QtGui.QImageReader.ImageReaderError.FileNotFoundError
    ImageReaderError = None # (!) real value is "<class 'PySide2.QtGui.QImageReader.ImageReaderError'>"
    InvalidDataError = PySide2.QtGui.QImageReader.ImageReaderError.InvalidDataError
    UnknownError = PySide2.QtGui.QImageReader.ImageReaderError.UnknownError
    UnsupportedFormatError = PySide2.QtGui.QImageReader.ImageReaderError.UnsupportedFormatError


