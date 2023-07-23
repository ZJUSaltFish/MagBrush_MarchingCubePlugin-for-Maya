# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaObject import QMediaObject

class QRadioTuner(QMediaObject):
    """ QRadioTuner(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def antennaConnectedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> PySide2.QtMultimedia.QMultimedia.AvailabilityStatus """
        pass

    def band(self): # real signature unknown; restored from __doc__
        """ band(self) -> PySide2.QtMultimedia.QRadioTuner.Band """
        pass

    def bandChanged(self, *args, **kwargs): # real signature unknown
        pass

    def cancelSearch(self): # real signature unknown; restored from __doc__
        """ cancelSearch(self) -> None """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtMultimedia.QRadioTuner.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def frequency(self): # real signature unknown; restored from __doc__
        """ frequency(self) -> int """
        return 0

    def frequencyChanged(self, *args, **kwargs): # real signature unknown
        pass

    def frequencyRange(self, band): # real signature unknown; restored from __doc__
        """ frequencyRange(self, band: PySide2.QtMultimedia.QRadioTuner.Band) -> typing.Tuple[int, int] """
        pass

    def frequencyStep(self, band): # real signature unknown; restored from __doc__
        """ frequencyStep(self, band: PySide2.QtMultimedia.QRadioTuner.Band) -> int """
        return 0

    def isAntennaConnected(self): # real signature unknown; restored from __doc__
        """ isAntennaConnected(self) -> bool """
        return False

    def isBandSupported(self, b): # real signature unknown; restored from __doc__
        """ isBandSupported(self, b: PySide2.QtMultimedia.QRadioTuner.Band) -> bool """
        return False

    def isMuted(self): # real signature unknown; restored from __doc__
        """ isMuted(self) -> bool """
        return False

    def isSearching(self): # real signature unknown; restored from __doc__
        """ isSearching(self) -> bool """
        return False

    def isStereo(self): # real signature unknown; restored from __doc__
        """ isStereo(self) -> bool """
        return False

    def mutedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def radioData(self): # real signature unknown; restored from __doc__
        """ radioData(self) -> PySide2.QtMultimedia.QRadioData """
        pass

    def searchAllStations(self, searchMode=None): # real signature unknown; restored from __doc__
        """ searchAllStations(self, searchMode: PySide2.QtMultimedia.QRadioTuner.SearchMode = PySide2.QtMultimedia.QRadioTuner.SearchMode.SearchFast) -> None """
        pass

    def searchBackward(self): # real signature unknown; restored from __doc__
        """ searchBackward(self) -> None """
        pass

    def searchForward(self): # real signature unknown; restored from __doc__
        """ searchForward(self) -> None """
        pass

    def searchingChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setBand(self, band): # real signature unknown; restored from __doc__
        """ setBand(self, band: PySide2.QtMultimedia.QRadioTuner.Band) -> None """
        pass

    def setFrequency(self, frequency): # real signature unknown; restored from __doc__
        """ setFrequency(self, frequency: int) -> None """
        pass

    def setMuted(self, muted): # real signature unknown; restored from __doc__
        """ setMuted(self, muted: bool) -> None """
        pass

    def setStereoMode(self, mode): # real signature unknown; restored from __doc__
        """ setStereoMode(self, mode: PySide2.QtMultimedia.QRadioTuner.StereoMode) -> None """
        pass

    def setVolume(self, volume): # real signature unknown; restored from __doc__
        """ setVolume(self, volume: int) -> None """
        pass

    def signalStrength(self): # real signature unknown; restored from __doc__
        """ signalStrength(self) -> int """
        return 0

    def signalStrengthChanged(self, *args, **kwargs): # real signature unknown
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtMultimedia.QRadioTuner.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stationFound(self, *args, **kwargs): # real signature unknown
        pass

    def stereoMode(self): # real signature unknown; restored from __doc__
        """ stereoMode(self) -> PySide2.QtMultimedia.QRadioTuner.StereoMode """
        pass

    def stereoStatusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
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

    ActiveState = PySide2.QtMultimedia.QRadioTuner.State.ActiveState
    AM = PySide2.QtMultimedia.QRadioTuner.Band.AM
    Auto = PySide2.QtMultimedia.QRadioTuner.StereoMode.Auto
    Band = None # (!) real value is "<class 'PySide2.QtMultimedia.QRadioTuner.Band'>"
    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QRadioTuner.Error'>"
    FM = PySide2.QtMultimedia.QRadioTuner.Band.FM
    FM2 = PySide2.QtMultimedia.QRadioTuner.Band.FM2
    ForceMono = PySide2.QtMultimedia.QRadioTuner.StereoMode.ForceMono
    ForceStereo = PySide2.QtMultimedia.QRadioTuner.StereoMode.ForceStereo
    LW = PySide2.QtMultimedia.QRadioTuner.Band.LW
    NoError = PySide2.QtMultimedia.QRadioTuner.Error.NoError
    OpenError = PySide2.QtMultimedia.QRadioTuner.Error.OpenError
    OutOfRangeError = PySide2.QtMultimedia.QRadioTuner.Error.OutOfRangeError
    ResourceError = PySide2.QtMultimedia.QRadioTuner.Error.ResourceError
    SearchFast = PySide2.QtMultimedia.QRadioTuner.SearchMode.SearchFast
    SearchGetStationId = PySide2.QtMultimedia.QRadioTuner.SearchMode.SearchGetStationId
    SearchMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QRadioTuner.SearchMode'>"
    State = None # (!) real value is "<class 'PySide2.QtMultimedia.QRadioTuner.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000018874679640>'
    StereoMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QRadioTuner.StereoMode'>"
    StoppedState = PySide2.QtMultimedia.QRadioTuner.State.StoppedState
    SW = PySide2.QtMultimedia.QRadioTuner.Band.SW


