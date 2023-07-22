# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaObject import QMediaObject

class QMediaPlayer(QMediaObject):
    """ QMediaPlayer(self, parent: typing.Optional[PySide2.QtCore.QObject] = None, flags: PySide2.QtMultimedia.QMediaPlayer.Flags = Default(QMediaPlayer.Flags)) -> None """
    def audioAvailableChanged(self, *args, **kwargs): # real signature unknown
        pass

    def audioRole(self): # real signature unknown; restored from __doc__
        """ audioRole(self) -> PySide2.QtMultimedia.QAudio.Role """
        pass

    def audioRoleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> PySide2.QtMultimedia.QMultimedia.AvailabilityStatus """
        pass

    def bind(self, arg__1): # real signature unknown; restored from __doc__
        """ bind(self, arg__1: PySide2.QtCore.QObject) -> bool """
        return False

    def bufferStatus(self): # real signature unknown; restored from __doc__
        """ bufferStatus(self) -> int """
        return 0

    def bufferStatusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentMedia(self): # real signature unknown; restored from __doc__
        """ currentMedia(self) -> PySide2.QtMultimedia.QMediaContent """
        pass

    def currentMediaChanged(self, *args, **kwargs): # real signature unknown
        pass

    def currentNetworkConfiguration(self): # real signature unknown; restored from __doc__
        """ currentNetworkConfiguration(self) -> PySide2.QtNetwork.QNetworkConfiguration """
        pass

    def customAudioRole(self): # real signature unknown; restored from __doc__
        """ customAudioRole(self) -> str """
        return ""

    def customAudioRoleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def durationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtMultimedia.QMediaPlayer.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def hasSupport(self, mimeType, codecs, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasSupport(mimeType: str, codecs: typing.Sequence[str] = [], flags: PySide2.QtMultimedia.QMediaPlayer.Flags = Default(QMediaPlayer.Flags)) -> PySide2.QtMultimedia.QMultimedia.SupportEstimate """
        pass

    def isAudioAvailable(self): # real signature unknown; restored from __doc__
        """ isAudioAvailable(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSeekable(self): # real signature unknown; restored from __doc__
        """ isSeekable(self) -> bool """
        return False

    def isVideoAvailable(self): # real signature unknown; restored from __doc__
        """ isVideoAvailable(self) -> bool """
        return False

    def media(self): # real signature unknown; restored from __doc__
        """ media(self) -> PySide2.QtMultimedia.QMediaContent """
        pass

    def mediaChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mediaStatus(self): # real signature unknown; restored from __doc__
        """ mediaStatus(self) -> PySide2.QtMultimedia.QMediaPlayer.MediaStatus """
        pass

    def mediaStatusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mediaStream(self): # real signature unknown; restored from __doc__
        """ mediaStream(self) -> PySide2.QtCore.QIODevice """
        pass

    def mutedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def networkConfigurationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) -> None """
        pass

    def play(self): # real signature unknown; restored from __doc__
        """ play(self) -> None """
        pass

    def playbackRate(self): # real signature unknown; restored from __doc__
        """ playbackRate(self) -> float """
        return 0.0

    def playbackRateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def playlist(self): # real signature unknown; restored from __doc__
        """ playlist(self) -> PySide2.QtMultimedia.QMediaPlaylist """
        pass

    def position(self): # real signature unknown; restored from __doc__
        """ position(self) -> int """
        return 0

    def positionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def seekableChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setAudioRole(self, audioRole): # real signature unknown; restored from __doc__
        """ setAudioRole(self, audioRole: PySide2.QtMultimedia.QAudio.Role) -> None """
        pass

    def setCustomAudioRole(self, audioRole): # real signature unknown; restored from __doc__
        """ setCustomAudioRole(self, audioRole: str) -> None """
        pass

    def setMedia(self, media, stream, PySide2_QtCore_QIODevice=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setMedia(self, media: PySide2.QtMultimedia.QMediaContent, stream: typing.Optional[PySide2.QtCore.QIODevice] = None) -> None """
        pass

    def setMuted(self, muted): # real signature unknown; restored from __doc__
        """ setMuted(self, muted: bool) -> None """
        pass

    def setNetworkConfigurations(self, configurations, PySide2_QtNetwork_QNetworkConfiguration=None): # real signature unknown; restored from __doc__
        """ setNetworkConfigurations(self, configurations: typing.Sequence[PySide2.QtNetwork.QNetworkConfiguration]) -> None """
        pass

    def setPlaybackRate(self, rate): # real signature unknown; restored from __doc__
        """ setPlaybackRate(self, rate: float) -> None """
        pass

    def setPlaylist(self, playlist): # real signature unknown; restored from __doc__
        """ setPlaylist(self, playlist: PySide2.QtMultimedia.QMediaPlaylist) -> None """
        pass

    def setPosition(self, position): # real signature unknown; restored from __doc__
        """ setPosition(self, position: int) -> None """
        pass

    def setVideoOutput(self, arg__1): # real signature unknown; restored from __doc__
        """
        setVideoOutput(self, arg__1: PySide2.QtMultimediaWidgets.QGraphicsVideoItem) -> None
        setVideoOutput(self, arg__1: PySide2.QtMultimediaWidgets.QVideoWidget) -> None
        setVideoOutput(self, surface: PySide2.QtMultimedia.QAbstractVideoSurface) -> None
        setVideoOutput(self, surfaces: typing.List[PySide2.QtMultimedia.QAbstractVideoSurface]) -> None
        """
        pass

    def setVolume(self, volume): # real signature unknown; restored from __doc__
        """ setVolume(self, volume: int) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtMultimedia.QMediaPlayer.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def supportedAudioRoles(self): # real signature unknown; restored from __doc__
        """ supportedAudioRoles(self) -> typing.List[PySide2.QtMultimedia.QAudio.Role] """
        pass

    def supportedCustomAudioRoles(self): # real signature unknown; restored from __doc__
        """ supportedCustomAudioRoles(self) -> typing.List[str] """
        pass

    def supportedMimeTypes(self, flags=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ supportedMimeTypes(flags: PySide2.QtMultimedia.QMediaPlayer.Flags = Default(QMediaPlayer.Flags)) -> typing.List[str] """
        pass

    def unbind(self, arg__1): # real signature unknown; restored from __doc__
        """ unbind(self, arg__1: PySide2.QtCore.QObject) -> None """
        pass

    def videoAvailableChanged(self, *args, **kwargs): # real signature unknown
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> int """
        return 0

    def volumeChanged(self, *args, **kwargs): # real signature unknown
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

    AccessDeniedError = PySide2.QtMultimedia.QMediaPlayer.Error.AccessDeniedError
    BufferedMedia = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.BufferedMedia
    BufferingMedia = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.BufferingMedia
    EndOfMedia = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.EndOfMedia
    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaPlayer.Error'>"
    Flag = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaPlayer.Flag'>"
    Flags = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaPlayer.Flags'>"
    FormatError = PySide2.QtMultimedia.QMediaPlayer.Error.FormatError
    InvalidMedia = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.InvalidMedia
    LoadedMedia = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.LoadedMedia
    LoadingMedia = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.LoadingMedia
    LowLatency = PySide2.QtMultimedia.QMediaPlayer.Flag.LowLatency
    MediaIsPlaylist = PySide2.QtMultimedia.QMediaPlayer.Error.MediaIsPlaylist
    MediaStatus = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaPlayer.MediaStatus'>"
    NetworkError = PySide2.QtMultimedia.QMediaPlayer.Error.NetworkError
    NoError = PySide2.QtMultimedia.QMediaPlayer.Error.NoError
    NoMedia = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.NoMedia
    PausedState = PySide2.QtMultimedia.QMediaPlayer.State.PausedState
    PlayingState = PySide2.QtMultimedia.QMediaPlayer.State.PlayingState
    ResourceError = PySide2.QtMultimedia.QMediaPlayer.Error.ResourceError
    ServiceMissingError = PySide2.QtMultimedia.QMediaPlayer.Error.ServiceMissingError
    StalledMedia = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.StalledMedia
    State = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaPlayer.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887465EC40>'
    StoppedState = PySide2.QtMultimedia.QMediaPlayer.State.StoppedState
    StreamPlayback = PySide2.QtMultimedia.QMediaPlayer.Flag.StreamPlayback
    UnknownMediaStatus = PySide2.QtMultimedia.QMediaPlayer.MediaStatus.UnknownMediaStatus
    VideoSurface = PySide2.QtMultimedia.QMediaPlayer.Flag.VideoSurface


