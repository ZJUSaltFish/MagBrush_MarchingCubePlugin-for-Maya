# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaBindableInterface import QMediaBindableInterface

class QMediaPlaylist(__PySide2_QtCore.QObject, QMediaBindableInterface):
    """ QMediaPlaylist(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addMedia(self, content): # real signature unknown; restored from __doc__
        """
        addMedia(self, content: PySide2.QtMultimedia.QMediaContent) -> bool
        addMedia(self, items: typing.Sequence[PySide2.QtMultimedia.QMediaContent]) -> bool
        """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> bool """
        return False

    def currentIndex(self): # real signature unknown; restored from __doc__
        """ currentIndex(self) -> int """
        return 0

    def currentIndexChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentMedia(self): # real signature unknown; restored from __doc__
        """ currentMedia(self) -> PySide2.QtMultimedia.QMediaContent """
        pass

    def currentMediaChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtMultimedia.QMediaPlaylist.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def insertMedia(self, index, content): # real signature unknown; restored from __doc__
        """
        insertMedia(self, index: int, content: PySide2.QtMultimedia.QMediaContent) -> bool
        insertMedia(self, index: int, items: typing.Sequence[PySide2.QtMultimedia.QMediaContent]) -> bool
        """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def load(self, device, format, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        load(self, device: PySide2.QtCore.QIODevice, format: typing.Optional[bytes] = None) -> None
        load(self, location: PySide2.QtCore.QUrl, format: typing.Optional[bytes] = None) -> None
        load(self, request: PySide2.QtNetwork.QNetworkRequest, format: typing.Optional[bytes] = None) -> None
        """
        pass

    def loaded(self, *args, **kwargs): # real signature unknown
        pass

    def loadFailed(self, *args, **kwargs): # real signature unknown
        pass

    def media(self, index): # real signature unknown; restored from __doc__
        """ media(self, index: int) -> PySide2.QtMultimedia.QMediaContent """
        pass

    def mediaAboutToBeInserted(self, *args, **kwargs): # real signature unknown
        pass

    def mediaAboutToBeRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def mediaChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mediaCount(self): # real signature unknown; restored from __doc__
        """ mediaCount(self) -> int """
        return 0

    def mediaInserted(self, *args, **kwargs): # real signature unknown
        pass

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> PySide2.QtMultimedia.QMediaObject """
        pass

    def mediaRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def moveMedia(self, from_, to): # real signature unknown; restored from __doc__
        """ moveMedia(self, from_: int, to: int) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> None """
        pass

    def nextIndex(self, steps=1): # real signature unknown; restored from __doc__
        """ nextIndex(self, steps: int = 1) -> int """
        return 0

    def playbackMode(self): # real signature unknown; restored from __doc__
        """ playbackMode(self) -> PySide2.QtMultimedia.QMediaPlaylist.PlaybackMode """
        pass

    def playbackModeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def previous(self): # real signature unknown; restored from __doc__
        """ previous(self) -> None """
        pass

    def previousIndex(self, steps=1): # real signature unknown; restored from __doc__
        """ previousIndex(self, steps: int = 1) -> int """
        return 0

    def removeMedia(self, pos): # real signature unknown; restored from __doc__
        """
        removeMedia(self, pos: int) -> bool
        removeMedia(self, start: int, end: int) -> bool
        """
        return False

    def save(self, device, format): # real signature unknown; restored from __doc__
        """
        save(self, device: PySide2.QtCore.QIODevice, format: bytes) -> bool
        save(self, location: PySide2.QtCore.QUrl, format: typing.Optional[bytes] = None) -> bool
        """
        return False

    def setCurrentIndex(self, index): # real signature unknown; restored from __doc__
        """ setCurrentIndex(self, index: int) -> None """
        pass

    def setMediaObject(self, p_object): # real signature unknown; restored from __doc__
        """ setMediaObject(self, object: PySide2.QtMultimedia.QMediaObject) -> bool """
        return False

    def setPlaybackMode(self, mode): # real signature unknown; restored from __doc__
        """ setPlaybackMode(self, mode: PySide2.QtMultimedia.QMediaPlaylist.PlaybackMode) -> None """
        pass

    def shuffle(self): # real signature unknown; restored from __doc__
        """ shuffle(self) -> None """
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

    AccessDeniedError = PySide2.QtMultimedia.QMediaPlaylist.Error.AccessDeniedError
    CurrentItemInLoop = PySide2.QtMultimedia.QMediaPlaylist.PlaybackMode.CurrentItemInLoop
    CurrentItemOnce = PySide2.QtMultimedia.QMediaPlaylist.PlaybackMode.CurrentItemOnce
    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaPlaylist.Error'>"
    FormatError = PySide2.QtMultimedia.QMediaPlaylist.Error.FormatError
    FormatNotSupportedError = PySide2.QtMultimedia.QMediaPlaylist.Error.FormatNotSupportedError
    Loop = PySide2.QtMultimedia.QMediaPlaylist.PlaybackMode.Loop
    NetworkError = PySide2.QtMultimedia.QMediaPlaylist.Error.NetworkError
    NoError = PySide2.QtMultimedia.QMediaPlaylist.Error.NoError
    PlaybackMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaPlaylist.PlaybackMode'>"
    Random = PySide2.QtMultimedia.QMediaPlaylist.PlaybackMode.Random
    Sequential = PySide2.QtMultimedia.QMediaPlaylist.PlaybackMode.Sequential
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887465D400>'


