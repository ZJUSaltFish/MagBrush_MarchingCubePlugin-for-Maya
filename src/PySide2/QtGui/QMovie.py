# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QMovie(__PySide2_QtCore.QObject):
    """
    QMovie(self, device: PySide2.QtCore.QIODevice, format: PySide2.QtCore.QByteArray = Default(QByteArray), parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QMovie(self, fileName: str, format: PySide2.QtCore.QByteArray = Default(QByteArray), parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QMovie(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def backgroundColor(self): # real signature unknown; restored from __doc__
        """ backgroundColor(self) -> PySide2.QtGui.QColor """
        pass

    def cacheMode(self): # real signature unknown; restored from __doc__
        """ cacheMode(self) -> PySide2.QtGui.QMovie.CacheMode """
        pass

    def currentFrameNumber(self): # real signature unknown; restored from __doc__
        """ currentFrameNumber(self) -> int """
        return 0

    def currentImage(self): # real signature unknown; restored from __doc__
        """ currentImage(self) -> PySide2.QtGui.QImage """
        pass

    def currentPixmap(self): # real signature unknown; restored from __doc__
        """ currentPixmap(self) -> PySide2.QtGui.QPixmap """
        pass

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtCore.QByteArray """
        pass

    def frameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def frameCount(self): # real signature unknown; restored from __doc__
        """ frameCount(self) -> int """
        return 0

    def frameRect(self): # real signature unknown; restored from __doc__
        """ frameRect(self) -> PySide2.QtCore.QRect """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def jumpToFrame(self, frameNumber): # real signature unknown; restored from __doc__
        """ jumpToFrame(self, frameNumber: int) -> bool """
        return False

    def jumpToNextFrame(self): # real signature unknown; restored from __doc__
        """ jumpToNextFrame(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> PySide2.QtGui.QImageReader.ImageReaderError """
        pass

    def lastErrorString(self): # real signature unknown; restored from __doc__
        """ lastErrorString(self) -> str """
        return ""

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def nextFrameDelay(self): # real signature unknown; restored from __doc__
        """ nextFrameDelay(self) -> int """
        return 0

    def resized(self, *args, **kwargs): # real signature unknown
        pass

    def scaledSize(self): # real signature unknown; restored from __doc__
        """ scaledSize(self) -> PySide2.QtCore.QSize """
        pass

    def setBackgroundColor(self, color): # real signature unknown; restored from __doc__
        """ setBackgroundColor(self, color: PySide2.QtGui.QColor) -> None """
        pass

    def setCacheMode(self, mode): # real signature unknown; restored from __doc__
        """ setCacheMode(self, mode: PySide2.QtGui.QMovie.CacheMode) -> None """
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

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) -> None """
        pass

    def setScaledSize(self, size): # real signature unknown; restored from __doc__
        """ setScaledSize(self, size: PySide2.QtCore.QSize) -> None """
        pass

    def setSpeed(self, percentSpeed): # real signature unknown; restored from __doc__
        """ setSpeed(self, percentSpeed: int) -> None """
        pass

    def speed(self): # real signature unknown; restored from __doc__
        """ speed(self) -> int """
        return 0

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def started(self, *args, **kwargs): # real signature unknown
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtGui.QMovie.MovieState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def supportedFormats(self): # real signature unknown; restored from __doc__
        """ supportedFormats() -> typing.List[PySide2.QtCore.QByteArray] """
        pass

    def updated(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, device, format=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    CacheAll = PySide2.QtGui.QMovie.CacheMode.CacheAll
    CacheMode = None # (!) real value is "<class 'PySide2.QtGui.QMovie.CacheMode'>"
    CacheNone = PySide2.QtGui.QMovie.CacheMode.CacheNone
    MovieState = None # (!) real value is "<class 'PySide2.QtGui.QMovie.MovieState'>"
    NotRunning = PySide2.QtGui.QMovie.MovieState.NotRunning
    Paused = PySide2.QtGui.QMovie.MovieState.Paused
    Running = PySide2.QtGui.QMovie.MovieState.Running
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00870C80>'


