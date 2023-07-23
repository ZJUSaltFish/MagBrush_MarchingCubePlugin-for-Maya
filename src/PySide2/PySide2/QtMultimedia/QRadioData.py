# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaBindableInterface import QMediaBindableInterface

class QRadioData(__PySide2_QtCore.QObject, QMediaBindableInterface):
    """ QRadioData(self, mediaObject: PySide2.QtMultimedia.QMediaObject, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def alternativeFrequenciesEnabledChanged(self, *args, **kwargs): # real signature unknown
        pass

    def availability(self): # real signature unknown; restored from __doc__
        """ availability(self) -> PySide2.QtMultimedia.QMultimedia.AvailabilityStatus """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtMultimedia.QRadioData.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def isAlternativeFrequenciesEnabled(self): # real signature unknown; restored from __doc__
        """ isAlternativeFrequenciesEnabled(self) -> bool """
        return False

    def mediaObject(self): # real signature unknown; restored from __doc__
        """ mediaObject(self) -> PySide2.QtMultimedia.QMediaObject """
        pass

    def programType(self): # real signature unknown; restored from __doc__
        """ programType(self) -> PySide2.QtMultimedia.QRadioData.ProgramType """
        pass

    def programTypeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def programTypeName(self): # real signature unknown; restored from __doc__
        """ programTypeName(self) -> str """
        return ""

    def programTypeNameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def radioText(self): # real signature unknown; restored from __doc__
        """ radioText(self) -> str """
        return ""

    def radioTextChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setAlternativeFrequenciesEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setAlternativeFrequenciesEnabled(self, enabled: bool) -> None """
        pass

    def setMediaObject(self, arg__1): # real signature unknown; restored from __doc__
        """ setMediaObject(self, arg__1: PySide2.QtMultimedia.QMediaObject) -> bool """
        return False

    def stationId(self): # real signature unknown; restored from __doc__
        """ stationId(self) -> str """
        return ""

    def stationIdChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stationName(self): # real signature unknown; restored from __doc__
        """ stationName(self) -> str """
        return ""

    def stationNameChanged(self, *args, **kwargs): # real signature unknown
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

    AdultHits = PySide2.QtMultimedia.QRadioData.ProgramType.AdultHits
    Alarm = PySide2.QtMultimedia.QRadioData.ProgramType.Alarm
    AlarmTest = PySide2.QtMultimedia.QRadioData.ProgramType.AlarmTest
    ChildrensProgrammes = PySide2.QtMultimedia.QRadioData.ProgramType.ChildrensProgrammes
    Classical = PySide2.QtMultimedia.QRadioData.ProgramType.Classical
    ClassicRock = PySide2.QtMultimedia.QRadioData.ProgramType.ClassicRock
    College = PySide2.QtMultimedia.QRadioData.ProgramType.College
    CountryMusic = PySide2.QtMultimedia.QRadioData.ProgramType.CountryMusic
    Culture = PySide2.QtMultimedia.QRadioData.ProgramType.Culture
    CurrentAffairs = PySide2.QtMultimedia.QRadioData.ProgramType.CurrentAffairs
    Documentary = PySide2.QtMultimedia.QRadioData.ProgramType.Documentary
    Drama = PySide2.QtMultimedia.QRadioData.ProgramType.Drama
    EasyListening = PySide2.QtMultimedia.QRadioData.ProgramType.EasyListening
    Education = PySide2.QtMultimedia.QRadioData.ProgramType.Education
    Error = None # (!) real value is "<class 'PySide2.QtMultimedia.QRadioData.Error'>"
    Finance = PySide2.QtMultimedia.QRadioData.ProgramType.Finance
    FolkMusic = PySide2.QtMultimedia.QRadioData.ProgramType.FolkMusic
    Information = PySide2.QtMultimedia.QRadioData.ProgramType.Information
    JazzMusic = PySide2.QtMultimedia.QRadioData.ProgramType.JazzMusic
    Language = PySide2.QtMultimedia.QRadioData.ProgramType.Language
    Leisure = PySide2.QtMultimedia.QRadioData.ProgramType.Leisure
    LightClassical = PySide2.QtMultimedia.QRadioData.ProgramType.LightClassical
    NationalMusic = PySide2.QtMultimedia.QRadioData.ProgramType.NationalMusic
    News = PySide2.QtMultimedia.QRadioData.ProgramType.News
    NoError = PySide2.QtMultimedia.QRadioData.Error.NoError
    Nostalgia = PySide2.QtMultimedia.QRadioData.ProgramType.Nostalgia
    OldiesMusic = PySide2.QtMultimedia.QRadioData.ProgramType.OldiesMusic
    OpenError = PySide2.QtMultimedia.QRadioData.Error.OpenError
    OtherMusic = PySide2.QtMultimedia.QRadioData.ProgramType.OtherMusic
    OutOfRangeError = PySide2.QtMultimedia.QRadioData.Error.OutOfRangeError
    Personality = PySide2.QtMultimedia.QRadioData.ProgramType.Personality
    PhoneIn = PySide2.QtMultimedia.QRadioData.ProgramType.PhoneIn
    PopMusic = PySide2.QtMultimedia.QRadioData.ProgramType.PopMusic
    ProgramType = None # (!) real value is "<class 'PySide2.QtMultimedia.QRadioData.ProgramType'>"
    Public = PySide2.QtMultimedia.QRadioData.ProgramType.Public
    Religion = PySide2.QtMultimedia.QRadioData.ProgramType.Religion
    ReligiousMusic = PySide2.QtMultimedia.QRadioData.ProgramType.ReligiousMusic
    ReligiousTalk = PySide2.QtMultimedia.QRadioData.ProgramType.ReligiousTalk
    ResourceError = PySide2.QtMultimedia.QRadioData.Error.ResourceError
    RhythmAndBlues = PySide2.QtMultimedia.QRadioData.ProgramType.RhythmAndBlues
    RockMusic = PySide2.QtMultimedia.QRadioData.ProgramType.RockMusic
    Science = PySide2.QtMultimedia.QRadioData.ProgramType.Science
    SeriousClassical = PySide2.QtMultimedia.QRadioData.ProgramType.SeriousClassical
    SocialAffairs = PySide2.QtMultimedia.QRadioData.ProgramType.SocialAffairs
    Soft = PySide2.QtMultimedia.QRadioData.ProgramType.Soft
    SoftRhythmAndBlues = PySide2.QtMultimedia.QRadioData.ProgramType.SoftRhythmAndBlues
    SoftRock = PySide2.QtMultimedia.QRadioData.ProgramType.SoftRock
    Sport = PySide2.QtMultimedia.QRadioData.ProgramType.Sport
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887464FB80>'
    Talk = PySide2.QtMultimedia.QRadioData.ProgramType.Talk
    Top40 = PySide2.QtMultimedia.QRadioData.ProgramType.Top40
    Travel = PySide2.QtMultimedia.QRadioData.ProgramType.Travel
    Undefined = PySide2.QtMultimedia.QRadioData.ProgramType.Undefined
    Varied = PySide2.QtMultimedia.QRadioData.ProgramType.Varied
    Weather = PySide2.QtMultimedia.QRadioData.ProgramType.Weather


