# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAudio(__Shiboken.Object):
    # no doc
    def convertVolume(self, volume, from_, to): # real signature unknown; restored from __doc__
        """ convertVolume(volume: float, from_: PySide2.QtMultimedia.QAudio.VolumeScale, to: PySide2.QtMultimedia.QAudio.VolumeScale) -> float """
        return 0.0

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AccessibilityRole = PySide2.QtMultimedia.QAudio.Role.AccessibilityRole
    ActiveState = PySide2.QtMultimedia.QAudio.State.ActiveState
    AlarmRole = PySide2.QtMultimedia.QAudio.Role.AlarmRole
    AudioInput = PySide2.QtMultimedia.QAudio.Mode.AudioInput
    AudioOutput = PySide2.QtMultimedia.QAudio.Mode.AudioOutput
    CubicVolumeScale = PySide2.QtMultimedia.QAudio.VolumeScale.CubicVolumeScale
    CustomRole = PySide2.QtMultimedia.QAudio.Role.CustomRole
    DecibelVolumeScale = PySide2.QtMultimedia.QAudio.VolumeScale.DecibelVolumeScale
    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudio.Error'>"
    FatalError = PySide2.QtMultimedia.QAudio.Error.FatalError
    GameRole = PySide2.QtMultimedia.QAudio.Role.GameRole
    IdleState = PySide2.QtMultimedia.QAudio.State.IdleState
    InterruptedState = PySide2.QtMultimedia.QAudio.State.InterruptedState
    IOError = PySide2.QtMultimedia.QAudio.Error.IOError
    LinearVolumeScale = PySide2.QtMultimedia.QAudio.VolumeScale.LinearVolumeScale
    LogarithmicVolumeScale = PySide2.QtMultimedia.QAudio.VolumeScale.LogarithmicVolumeScale
    Mode = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudio.Mode'>"
    MusicRole = PySide2.QtMultimedia.QAudio.Role.MusicRole
    NoError = PySide2.QtMultimedia.QAudio.Error.NoError
    NotificationRole = PySide2.QtMultimedia.QAudio.Role.NotificationRole
    OpenError = PySide2.QtMultimedia.QAudio.Error.OpenError
    RingtoneRole = PySide2.QtMultimedia.QAudio.Role.RingtoneRole
    Role = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudio.Role'>"
    SonificationRole = PySide2.QtMultimedia.QAudio.Role.SonificationRole
    State = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudio.State'>"
    StoppedState = PySide2.QtMultimedia.QAudio.State.StoppedState
    SuspendedState = PySide2.QtMultimedia.QAudio.State.SuspendedState
    UnderrunError = PySide2.QtMultimedia.QAudio.Error.UnderrunError
    UnknownRole = PySide2.QtMultimedia.QAudio.Role.UnknownRole
    VideoRole = PySide2.QtMultimedia.QAudio.Role.VideoRole
    VoiceCommunicationRole = PySide2.QtMultimedia.QAudio.Role.VoiceCommunicationRole
    VolumeScale = None # (!) real value is "<class 'PySide2.QtMultimedia.QAudio.VolumeScale'>"


