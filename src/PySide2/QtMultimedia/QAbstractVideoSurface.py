# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAbstractVideoSurface(__PySide2_QtCore.QObject):
    """ QAbstractVideoSurface(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def activeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtMultimedia.QAbstractVideoSurface.Error """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isFormatSupported(self, format): # real signature unknown; restored from __doc__
        """ isFormatSupported(self, format: PySide2.QtMultimedia.QVideoSurfaceFormat) -> bool """
        return False

    def nativeResolution(self): # real signature unknown; restored from __doc__
        """ nativeResolution(self) -> PySide2.QtCore.QSize """
        pass

    def nativeResolutionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def nearestFormat(self, format): # real signature unknown; restored from __doc__
        """ nearestFormat(self, format: PySide2.QtMultimedia.QVideoSurfaceFormat) -> PySide2.QtMultimedia.QVideoSurfaceFormat """
        pass

    def present(self, frame): # real signature unknown; restored from __doc__
        """ present(self, frame: PySide2.QtMultimedia.QVideoFrame) -> bool """
        return False

    def setError(self, error): # real signature unknown; restored from __doc__
        """ setError(self, error: PySide2.QtMultimedia.QAbstractVideoSurface.Error) -> None """
        pass

    def setNativeResolution(self, resolution): # real signature unknown; restored from __doc__
        """ setNativeResolution(self, resolution: PySide2.QtCore.QSize) -> None """
        pass

    def start(self, format): # real signature unknown; restored from __doc__
        """ start(self, format: PySide2.QtMultimedia.QVideoSurfaceFormat) -> bool """
        return False

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def supportedFormatsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def supportedPixelFormats(self, type=None): # real signature unknown; restored from __doc__
        """ supportedPixelFormats(self, type: PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType = PySide2.QtMultimedia.QAbstractVideoBuffer.HandleType.NoHandle) -> typing.List[PySide2.QtMultimedia.QVideoFrame.PixelFormat] """
        pass

    def surfaceFormat(self): # real signature unknown; restored from __doc__
        """ surfaceFormat(self) -> PySide2.QtMultimedia.QVideoSurfaceFormat """
        pass

    def surfaceFormatChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QAbstractVideoSurface.Error'>"
    IncorrectFormatError = PySide2.QtMultimedia.QAbstractVideoSurface.Error.IncorrectFormatError
    NoError = PySide2.QtMultimedia.QAbstractVideoSurface.Error.NoError
    ResourceError = PySide2.QtMultimedia.QAbstractVideoSurface.Error.ResourceError
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887464D6C0>'
    StoppedError = PySide2.QtMultimedia.QAbstractVideoSurface.Error.StoppedError
    UnsupportedFormatError = PySide2.QtMultimedia.QAbstractVideoSurface.Error.UnsupportedFormatError


