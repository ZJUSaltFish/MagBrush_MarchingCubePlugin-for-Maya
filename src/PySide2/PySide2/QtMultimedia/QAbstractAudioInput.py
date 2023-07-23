# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAbstractAudioInput(__PySide2_QtCore.QObject):
    """ QAbstractAudioInput(self) -> None """
    def bufferSize(self): # real signature unknown; restored from __doc__
        """ bufferSize(self) -> int """
        return 0

    def bytesReady(self): # real signature unknown; restored from __doc__
        """ bytesReady(self) -> int """
        return 0

    def elapsedUSecs(self): # real signature unknown; restored from __doc__
        """ elapsedUSecs(self) -> int """
        return 0

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtMultimedia.QAudio.Error """
        pass

    def errorChanged(self, *args, **kwargs): # real signature unknown
        pass

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtMultimedia.QAudioFormat """
        pass

    def notify(self, *args, **kwargs): # real signature unknown
        pass

    def notifyInterval(self): # real signature unknown; restored from __doc__
        """ notifyInterval(self) -> int """
        return 0

    def periodSize(self): # real signature unknown; restored from __doc__
        """ periodSize(self) -> int """
        return 0

    def processedUSecs(self): # real signature unknown; restored from __doc__
        """ processedUSecs(self) -> int """
        return 0

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def setBufferSize(self, value): # real signature unknown; restored from __doc__
        """ setBufferSize(self, value: int) -> None """
        pass

    def setFormat(self, fmt): # real signature unknown; restored from __doc__
        """ setFormat(self, fmt: PySide2.QtMultimedia.QAudioFormat) -> None """
        pass

    def setNotifyInterval(self, milliSeconds): # real signature unknown; restored from __doc__
        """ setNotifyInterval(self, milliSeconds: int) -> None """
        pass

    def setVolume(self, arg__1): # real signature unknown; restored from __doc__
        """ setVolume(self, arg__1: float) -> None """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """
        start(self) -> PySide2.QtCore.QIODevice
        start(self, device: PySide2.QtCore.QIODevice) -> None
        """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtMultimedia.QAudio.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def suspend(self): # real signature unknown; restored from __doc__
        """ suspend(self) -> None """
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887464DBC0>'


