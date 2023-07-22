# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSoundEffect(__PySide2_QtCore.QObject):
    """
    QSoundEffect(self, audioDevice: PySide2.QtMultimedia.QAudioDeviceInfo, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSoundEffect(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def category(self): # real signature unknown; restored from __doc__
        """ category(self) -> str """
        return ""

    def categoryChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ isLoaded(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isPlaying(self): # real signature unknown; restored from __doc__
        """ isPlaying(self) -> bool """
        return False

    def loadedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self): # real signature unknown; restored from __doc__
        """ loopCount(self) -> int """
        return 0

    def loopCountChanged(self, *args, **kwargs): # real signature unknown
        pass

    def loopsRemaining(self): # real signature unknown; restored from __doc__
        """ loopsRemaining(self) -> int """
        return 0

    def loopsRemainingChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mutedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ play(self) -> None """
        pass

    def playingChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setCategory(self, category): # real signature unknown; restored from __doc__
        """ setCategory(self, category: str) -> None """
        pass

    def setLoopCount(self, loopCount): # real signature unknown; restored from __doc__
        """ setLoopCount(self, loopCount: int) -> None """
        pass

    def setMuted(self, muted): # real signature unknown; restored from __doc__
        """ setMuted(self, muted: bool) -> None """
        pass

    def setSource(self, url): # real signature unknown; restored from __doc__
        """ setSource(self, url: PySide2.QtCore.QUrl) -> None """
        pass

    def setVolume(self, volume): # real signature unknown; restored from __doc__
        """ setVolume(self, volume: float) -> None """
        pass

    def source(self): # real signature unknown; restored from __doc__
        """ source(self) -> PySide2.QtCore.QUrl """
        pass

    def sourceChanged(self, *args, **kwargs): # real signature unknown
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtMultimedia.QSoundEffect.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def supportedMimeTypes(self): # real signature unknown; restored from __doc__
        """ supportedMimeTypes() -> typing.List[str] """
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def volumeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, audioDevice, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Error = PySide2.QtMultimedia.QSoundEffect.Status.Error
    Infinite = PySide2.QtMultimedia.QSoundEffect.Loop.Infinite
    Loading = PySide2.QtMultimedia.QSoundEffect.Status.Loading
    Loop = None # (!) real value is "<class 'PySide2.QtMultimedia.QSoundEffect.Loop'>"
    Null = PySide2.QtMultimedia.QSoundEffect.Status.Null
    Ready = PySide2.QtMultimedia.QSoundEffect.Status.Ready
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887464E600>'
    Status = None # (!) real value is "<class 'PySide2.QtMultimedia.QSoundEffect.Status'>"


