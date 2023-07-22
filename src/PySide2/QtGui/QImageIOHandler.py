# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QImageIOHandler(__Shiboken.Object):
    """ QImageIOHandler(self) -> None """
    def canRead(self): # real signature unknown; restored from __doc__
        """ canRead(self) -> bool """
        return False

    def currentImageNumber(self): # real signature unknown; restored from __doc__
        """ currentImageNumber(self) -> int """
        return 0

    def currentImageRect(self): # real signature unknown; restored from __doc__
        """ currentImageRect(self) -> PySide2.QtCore.QRect """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtCore.QByteArray """
        pass

    def imageCount(self): # real signature unknown; restored from __doc__
        """ imageCount(self) -> int """
        return 0

    def jumpToImage(self, imageNumber): # real signature unknown; restored from __doc__
        """ jumpToImage(self, imageNumber: int) -> bool """
        return False

    def jumpToNextImage(self): # real signature unknown; restored from __doc__
        """ jumpToNextImage(self) -> bool """
        return False

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> PySide2.QtCore.QByteArray """
        pass

    def nextImageDelay(self): # real signature unknown; restored from __doc__
        """ nextImageDelay(self) -> int """
        return 0

    def option(self, option): # real signature unknown; restored from __doc__
        """ option(self, option: PySide2.QtGui.QImageIOHandler.ImageOption) -> typing.Any """
        pass

    def read(self, image): # real signature unknown; restored from __doc__
        """ read(self, image: PySide2.QtGui.QImage) -> bool """
        return False

    def setDevice(self, device): # real signature unknown; restored from __doc__
        """ setDevice(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtCore.QByteArray) -> None """
        pass

    def setOption(self, option, value): # real signature unknown; restored from __doc__
        """ setOption(self, option: PySide2.QtGui.QImageIOHandler.ImageOption, value: typing.Any) -> None """
        pass

    def supportsOption(self, option): # real signature unknown; restored from __doc__
        """ supportsOption(self, option: PySide2.QtGui.QImageIOHandler.ImageOption) -> bool """
        return False

    def write(self, image): # real signature unknown; restored from __doc__
        """ write(self, image: PySide2.QtGui.QImage) -> bool """
        return False

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

    Animation = PySide2.QtGui.QImageIOHandler.ImageOption.Animation
    BackgroundColor = PySide2.QtGui.QImageIOHandler.ImageOption.BackgroundColor
    ClipRect = PySide2.QtGui.QImageIOHandler.ImageOption.ClipRect
    CompressionRatio = PySide2.QtGui.QImageIOHandler.ImageOption.CompressionRatio
    Description = PySide2.QtGui.QImageIOHandler.ImageOption.Description
    Endianness = PySide2.QtGui.QImageIOHandler.ImageOption.Endianness
    Gamma = PySide2.QtGui.QImageIOHandler.ImageOption.Gamma
    ImageFormat = PySide2.QtGui.QImageIOHandler.ImageOption.ImageFormat
    ImageOption = None # (!) real value is "<class 'PySide2.QtGui.QImageIOHandler.ImageOption'>"
    ImageTransformation = PySide2.QtGui.QImageIOHandler.ImageOption.ImageTransformation
    IncrementalReading = PySide2.QtGui.QImageIOHandler.ImageOption.IncrementalReading
    Name = PySide2.QtGui.QImageIOHandler.ImageOption.Name
    OptimizedWrite = PySide2.QtGui.QImageIOHandler.ImageOption.OptimizedWrite
    ProgressiveScanWrite = PySide2.QtGui.QImageIOHandler.ImageOption.ProgressiveScanWrite
    Quality = PySide2.QtGui.QImageIOHandler.ImageOption.Quality
    ScaledClipRect = PySide2.QtGui.QImageIOHandler.ImageOption.ScaledClipRect
    ScaledSize = PySide2.QtGui.QImageIOHandler.ImageOption.ScaledSize
    Size = PySide2.QtGui.QImageIOHandler.ImageOption.Size
    SubType = PySide2.QtGui.QImageIOHandler.ImageOption.SubType
    SupportedSubTypes = PySide2.QtGui.QImageIOHandler.ImageOption.SupportedSubTypes
    Transformation = None # (!) real value is "<class 'PySide2.QtGui.QImageIOHandler.Transformation'>"
    TransformationFlip = PySide2.QtGui.QImageIOHandler.Transformation.TransformationFlip
    TransformationFlipAndRotate90 = PySide2.QtGui.QImageIOHandler.Transformation.TransformationFlipAndRotate90
    TransformationMirror = PySide2.QtGui.QImageIOHandler.Transformation.TransformationMirror
    TransformationMirrorAndRotate90 = PySide2.QtGui.QImageIOHandler.Transformation.TransformationMirrorAndRotate90
    TransformationNone = PySide2.QtGui.QImageIOHandler.Transformation.TransformationNone
    TransformationRotate180 = PySide2.QtGui.QImageIOHandler.Transformation.TransformationRotate180
    TransformationRotate270 = PySide2.QtGui.QImageIOHandler.Transformation.TransformationRotate270
    TransformationRotate90 = PySide2.QtGui.QImageIOHandler.Transformation.TransformationRotate90
    Transformations = None # (!) real value is "<class 'PySide2.QtGui.QImageIOHandler.Transformations'>"
    TransformedByDefault = PySide2.QtGui.QImageIOHandler.ImageOption.TransformedByDefault


