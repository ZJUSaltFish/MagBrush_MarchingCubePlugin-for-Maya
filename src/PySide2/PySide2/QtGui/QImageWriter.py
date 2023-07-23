# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QImageWriter(__Shiboken.Object):
    """
    QImageWriter(self) -> None
    QImageWriter(self, device: PySide2.QtCore.QIODevice, format: PySide2.QtCore.QByteArray) -> None
    QImageWriter(self, fileName: str, format: PySide2.QtCore.QByteArray = Default(QByteArray)) -> None
    """
    def canWrite(self): # real signature unknown; restored from __doc__
        """ canWrite(self) -> bool """
        return False

    def compression(self): # real signature unknown; restored from __doc__
        """ compression(self) -> int """
        return 0

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtGui.QImageWriter.ImageWriterError """
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

    def imageFormatsForMimeType(self, mimeType): # real signature unknown; restored from __doc__
        """ imageFormatsForMimeType(mimeType: PySide2.QtCore.QByteArray) -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def optimizedWrite(self): # real signature unknown; restored from __doc__
        """ optimizedWrite(self) -> bool """
        return False

    def progressiveScanWrite(self): # real signature unknown; restored from __doc__
        """ progressiveScanWrite(self) -> bool """
        return False

    def quality(self): # real signature unknown; restored from __doc__
        """ quality(self) -> int """
        return 0

    def setCompression(self, compression): # real signature unknown; restored from __doc__
        """ setCompression(self, compression: int) -> None """
        pass

    def setDescription(self, description): # real signature unknown; restored from __doc__
        """ setDescription(self, description: str) -> None """
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

    def setOptimizedWrite(self, optimize): # real signature unknown; restored from __doc__
        """ setOptimizedWrite(self, optimize: bool) -> None """
        pass

    def setProgressiveScanWrite(self, progressive): # real signature unknown; restored from __doc__
        """ setProgressiveScanWrite(self, progressive: bool) -> None """
        pass

    def setQuality(self, quality): # real signature unknown; restored from __doc__
        """ setQuality(self, quality: int) -> None """
        pass

    def setSubType(self, type): # real signature unknown; restored from __doc__
        """ setSubType(self, type: PySide2.QtCore.QByteArray) -> None """
        pass

    def setText(self, key, text): # real signature unknown; restored from __doc__
        """ setText(self, key: str, text: str) -> None """
        pass

    def setTransformation(self, orientation): # real signature unknown; restored from __doc__
        """ setTransformation(self, orientation: PySide2.QtGui.QImageIOHandler.Transformations) -> None """
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

    def supportsOption(self, option): # real signature unknown; restored from __doc__
        """ supportsOption(self, option: PySide2.QtGui.QImageIOHandler.ImageOption) -> bool """
        return False

    def transformation(self): # real signature unknown; restored from __doc__
        """ transformation(self) -> PySide2.QtGui.QImageIOHandler.Transformations """
        pass

    def write(self, image): # real signature unknown; restored from __doc__
        """ write(self, image: PySide2.QtGui.QImage) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DeviceError = PySide2.QtGui.QImageWriter.ImageWriterError.DeviceError
    ImageWriterError = None # (!) real value is "<class 'PySide2.QtGui.QImageWriter.ImageWriterError'>"
    InvalidImageError = PySide2.QtGui.QImageWriter.ImageWriterError.InvalidImageError
    UnknownError = PySide2.QtGui.QImageWriter.ImageWriterError.UnknownError
    UnsupportedFormatError = PySide2.QtGui.QImageWriter.ImageWriterError.UnsupportedFormatError


