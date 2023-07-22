# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaObject import QMediaObject

class QAudioDecoder(QMediaObject):
    """ QAudioDecoder(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def audioFormat(self): # real signature unknown; restored from __doc__
        """ audioFormat(self) -> PySide2.QtMultimedia.QAudioFormat """
        pass

    def bind(self, arg__1): # real signature unknown; restored from __doc__
        """ bind(self, arg__1: PySide2.QtCore.QObject) -> bool """
        return False

    def bufferAvailable(self): # real signature unknown; restored from __doc__
        """ bufferAvailable(self) -> bool """
        return False

    def bufferAvailableChanged(self, *args, **kwargs): # real signature unknown
        pass

    def bufferReady(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def durationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtMultimedia.QAudioDecoder.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def formatChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hasSupport(self, mimeType, codecs, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasSupport(mimeType: str, codecs: typing.Sequence[str] = []) -> PySide2.QtMultimedia.QMultimedia.SupportEstimate """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def read(self): # real signature unknown; restored from __doc__
        """ read(self) -> PySide2.QtMultimedia.QAudioBuffer """
        pass

    def setAudioFormat(self, format): # real signature unknown; restored from __doc__
        """ setAudioFormat(self, format: PySide2.QtMultimedia.QAudioFormat) -> None """
        pass

    def setSourceDevice(self, device): # real signature unknown; restored from __doc__
        """ setSourceDevice(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def setSourceFilename(self, fileName): # real signature unknown; restored from __doc__
        """ setSourceFilename(self, fileName: str) -> None """
        pass

    def sourceChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sourceDevice(self): # real signature unknown; restored from __doc__
        """ sourceDevice(self) -> PySide2.QtCore.QIODevice """
        pass

    def sourceFilename(self): # real signature unknown; restored from __doc__
        """ sourceFilename(self) -> str """
        return ""

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtMultimedia.QAudioDecoder.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def unbind(self, arg__1): # real signature unknown; restored from __doc__
        """ unbind(self, arg__1: PySide2.QtCore.QObject) -> None """
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

    AccessDeniedError = PySide2.QtMultimedia.QAudioDecoder.Error.AccessDeniedError
    DecodingState = PySide2.QtMultimedia.QAudioDecoder.State.DecodingState
    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudioDecoder.Error'>"
    FormatError = PySide2.QtMultimedia.QAudioDecoder.Error.FormatError
    NoError = PySide2.QtMultimedia.QAudioDecoder.Error.NoError
    ResourceError = PySide2.QtMultimedia.QAudioDecoder.Error.ResourceError
    ServiceMissingError = PySide2.QtMultimedia.QAudioDecoder.Error.ServiceMissingError
    State = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudioDecoder.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887465DD80>'
    StoppedState = PySide2.QtMultimedia.QAudioDecoder.State.StoppedState


