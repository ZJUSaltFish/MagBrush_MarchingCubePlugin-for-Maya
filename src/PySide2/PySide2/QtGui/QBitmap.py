# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QPixmap import QPixmap

class QBitmap(QPixmap):
    """
    QBitmap(self) -> None
    QBitmap(self, arg__1: PySide2.QtCore.QSize) -> None
    QBitmap(self, arg__1: PySide2.QtGui.QPixmap) -> None
    QBitmap(self, fileName: str, format: typing.Optional[bytes] = None) -> None
    QBitmap(self, other: PySide2.QtGui.QBitmap) -> None
    QBitmap(self, w: int, h: int) -> None
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def fromData(self, size, bits, monoFormat=None): # real signature unknown; restored from __doc__
        """ fromData(size: PySide2.QtCore.QSize, bits: bytes, monoFormat: PySide2.QtGui.QImage.Format = PySide2.QtGui.QImage.Format.Format_MonoLSB) -> PySide2.QtGui.QBitmap """
        pass

    def fromImage(self, image, flags=None): # real signature unknown; restored from __doc__
        """
        fromImage(image: PySide2.QtGui.QImage, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QBitmap
        fromImage(image: PySide2.QtGui.QImage, flags: PySide2.QtCore.Qt.ImageConversionFlags = PySide2.QtCore.Qt.ImageConversionFlag.AutoColor) -> PySide2.QtGui.QPixmap
        """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """
        swap(self, other: PySide2.QtGui.QBitmap) -> None
        swap(self, other: PySide2.QtGui.QPixmap) -> None
        """
        pass

    def transformed(self, arg__1): # real signature unknown; restored from __doc__
        """
        transformed(self, arg__1: PySide2.QtGui.QMatrix) -> PySide2.QtGui.QBitmap
        transformed(self, arg__1: PySide2.QtGui.QMatrix, mode: PySide2.QtCore.Qt.TransformationMode = PySide2.QtCore.Qt.TransformationMode.FastTransformation) -> PySide2.QtGui.QPixmap
        transformed(self, matrix: PySide2.QtGui.QTransform) -> PySide2.QtGui.QBitmap
        """
        pass

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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


