# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QPaintDevice import QPaintDevice

class QPicture(QPaintDevice):
    """
    QPicture(self, arg__1: PySide2.QtGui.QPicture) -> None
    QPicture(self, formatVersion: int = -1) -> None
    """
    def boundingRect(self): # real signature unknown; restored from __doc__
        """ boundingRect(self) -> PySide2.QtCore.QRect """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> bytes """
        return b""

    def devType(self): # real signature unknown; restored from __doc__
        """ devType(self) -> int """
        return 0

    def inputFormatList(self): # real signature unknown; restored from __doc__
        """ inputFormatList() -> typing.List[str] """
        pass

    def inputFormats(self): # real signature unknown; restored from __doc__
        """ inputFormats() -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def load(self, dev, format, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        load(self, dev: PySide2.QtCore.QIODevice, format: typing.Optional[bytes] = None) -> bool
        load(self, fileName: str, format: typing.Optional[bytes] = None) -> bool
        """
        pass

    def metric(self, m): # real signature unknown; restored from __doc__
        """ metric(self, m: PySide2.QtGui.QPaintDevice.PaintDeviceMetric) -> int """
        return 0

    def outputFormatList(self): # real signature unknown; restored from __doc__
        """ outputFormatList() -> typing.List[str] """
        pass

    def outputFormats(self): # real signature unknown; restored from __doc__
        """ outputFormats() -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def paintEngine(self): # real signature unknown; restored from __doc__
        """ paintEngine(self) -> PySide2.QtGui.QPaintEngine """
        pass

    def pictureFormat(self, fileName): # real signature unknown; restored from __doc__
        """ pictureFormat(fileName: str) -> bytes """
        return b""

    def play(self, p): # real signature unknown; restored from __doc__
        """ play(self, p: PySide2.QtGui.QPainter) -> bool """
        return False

    def save(self, dev, format, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        save(self, dev: PySide2.QtCore.QIODevice, format: typing.Optional[bytes] = None) -> bool
        save(self, fileName: str, format: typing.Optional[bytes] = None) -> bool
        """
        pass

    def setBoundingRect(self, r): # real signature unknown; restored from __doc__
        """ setBoundingRect(self, r: PySide2.QtCore.QRect) -> None """
        pass

    def setData(self, data, size): # real signature unknown; restored from __doc__
        """ setData(self, data: bytes, size: int) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QPicture) -> None """
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

    def __init__(self, arg__1): # real signature unknown; restored from __doc__
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


