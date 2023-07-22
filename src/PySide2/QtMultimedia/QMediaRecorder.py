# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaBindableInterface import QMediaBindableInterface

class QMediaRecorder(__PySide2_QtCore.QObject, QMediaBindableInterface):
    """ QMediaRecorder(self, mediaObject: PySide2.QtMultimedia.QMediaObject, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def actualLocation(self): # real signature unknown; restored from __doc__
        """ actualLocation(self) -> PySide2.QtCore.QUrl """
        pass

    def actualLocationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def audioCodecDescription(self, codecName): # real signature unknown; restored from __doc__
        """ audioCodecDescription(self, codecName: str) -> str """
        return ""

    def audioSettings(self): # real signature unknown; restored from __doc__
        """ audioSettings(self) -> PySide2.QtMultimedia.QAudioEncoderSettings """
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> PySide2.QtMultimedia.QMultimedia.AvailabilityStatus """
        pass

    def availabilityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def availableMetaData(self): # real signature unknown; restored from __doc__
        """ availableMetaData(self) -> typing.List[str] """
        pass

    def containerDescription(self, format): # real signature unknown; restored from __doc__
        """ containerDescription(self, format: str) -> str """
        return ""

    def containerFormat(self): # real signature unknown; restored from __doc__
        """ containerFormat(self) -> str """
        return ""

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def durationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtMultimedia.QMediaRecorder.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isMetaDataAvailable(self): # real signature unknown; restored from __doc__
        """ isMetaDataAvailable(self) -> bool """
        return False

    def isMetaDataWritable(self): # real signature unknown; restored from __doc__
        """ isMetaDataWritable(self) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> PySide2.QtMultimedia.QMediaObject """
        pass

    def metaData(self, key): # real signature unknown; restored from __doc__
        """ metaData(self, key: str) -> typing.Any """
        pass

    def metaDataAvailableChanged(self, *args, **kwargs): # real signature unknown
        pass

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def metaDataWritableChanged(self, *args, **kwargs): # real signature unknown
        pass

    def mutedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def outputLocation(self): # real signature unknown; restored from __doc__
        """ outputLocation(self) -> PySide2.QtCore.QUrl """
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) -> None """
        pass

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> None """
        pass

    def setAudioSettings(self, audioSettings): # real signature unknown; restored from __doc__
        """ setAudioSettings(self, audioSettings: PySide2.QtMultimedia.QAudioEncoderSettings) -> None """
        pass

    def setContainerFormat(self, container): # real signature unknown; restored from __doc__
        """ setContainerFormat(self, container: str) -> None """
        pass

    def setEncodingSettings(self, audioSettings, videoSettings=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setEncodingSettings(self, audioSettings: PySide2.QtMultimedia.QAudioEncoderSettings, videoSettings: PySide2.QtMultimedia.QVideoEncoderSettings = Default(QVideoEncoderSettings), containerMimeType: str = '') -> None """
        pass

    def setMediaObject(self, p_object): # real signature unknown; restored from __doc__
        """ setMediaObject(self, object: PySide2.QtMultimedia.QMediaObject) -> bool """
        return False

    def setMetaData(self, key, value): # real signature unknown; restored from __doc__
        """ setMetaData(self, key: str, value: typing.Any) -> None """
        pass

    def setMuted(self, muted): # real signature unknown; restored from __doc__
        """ setMuted(self, muted: bool) -> None """
        pass

    def setOutputLocation(self, location): # real signature unknown; restored from __doc__
        """ setOutputLocation(self, location: PySide2.QtCore.QUrl) -> bool """
        return False

    def setVideoSettings(self, videoSettings): # real signature unknown; restored from __doc__
        """ setVideoSettings(self, videoSettings: PySide2.QtMultimedia.QVideoEncoderSettings) -> None """
        pass

    def setVolume(self, volume): # real signature unknown; restored from __doc__
        """ setVolume(self, volume: float) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtMultimedia.QMediaRecorder.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtMultimedia.QMediaRecorder.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def supportedAudioCodecs(self): # real signature unknown; restored from __doc__
        """ supportedAudioCodecs(self) -> typing.List[str] """
        pass

    def supportedContainers(self): # real signature unknown; restored from __doc__
        """ supportedContainers(self) -> typing.List[str] """
        pass

    def supportedVideoCodecs(self): # real signature unknown; restored from __doc__
        """ supportedVideoCodecs(self) -> typing.List[str] """
        pass

    def videoCodecDescription(self, codecName): # real signature unknown; restored from __doc__
        """ videoCodecDescription(self, codecName: str) -> str """
        return ""

    def videoSettings(self): # real signature unknown; restored from __doc__
        """ videoSettings(self) -> PySide2.QtMultimedia.QVideoEncoderSettings """
        pass

    def volume(self): # real signature unknown; restored from __doc__
        """ volume(self) -> float """
        return 0.0

    def volumeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, mediaObject, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaRecorder.Error'>"
    FinalizingStatus = PySide2.QtMultimedia.QMediaRecorder.Status.FinalizingStatus
    FormatError = PySide2.QtMultimedia.QMediaRecorder.Error.FormatError
    LoadedStatus = PySide2.QtMultimedia.QMediaRecorder.Status.LoadedStatus
    LoadingStatus = PySide2.QtMultimedia.QMediaRecorder.Status.LoadingStatus
    NoError = PySide2.QtMultimedia.QMediaRecorder.Error.NoError
    OutOfSpaceError = PySide2.QtMultimedia.QMediaRecorder.Error.OutOfSpaceError
    PausedState = PySide2.QtMultimedia.QMediaRecorder.State.PausedState
    PausedStatus = PySide2.QtMultimedia.QMediaRecorder.Status.PausedStatus
    RecordingState = PySide2.QtMultimedia.QMediaRecorder.State.RecordingState
    RecordingStatus = PySide2.QtMultimedia.QMediaRecorder.Status.RecordingStatus
    ResourceError = PySide2.QtMultimedia.QMediaRecorder.Error.ResourceError
    StartingStatus = PySide2.QtMultimedia.QMediaRecorder.Status.StartingStatus
    State = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaRecorder.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887465C7C0>'
    Status = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaRecorder.Status'>"
    StoppedState = PySide2.QtMultimedia.QMediaRecorder.State.StoppedState
    UnavailableStatus = PySide2.QtMultimedia.QMediaRecorder.Status.UnavailableStatus
    UnloadedStatus = PySide2.QtMultimedia.QMediaRecorder.Status.UnloadedStatus


