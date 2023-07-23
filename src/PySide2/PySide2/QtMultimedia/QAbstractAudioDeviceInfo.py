# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAbstractAudioDeviceInfo(__PySide2_QtCore.QObject):
    """ QAbstractAudioDeviceInfo(self) -> None """
    def deviceName(self): # real signature unknown; restored from __doc__
        """ deviceName(self) -> str """
        return ""

    def isFormatSupported(self, format): # real signature unknown; restored from __doc__
        """ isFormatSupported(self, format: PySide2.QtMultimedia.QAudioFormat) -> bool """
        return False

    def preferredFormat(self): # real signature unknown; restored from __doc__
        """ preferredFormat(self) -> PySide2.QtMultimedia.QAudioFormat """
        pass

    def supportedByteOrders(self): # real signature unknown; restored from __doc__
        """ supportedByteOrders(self) -> typing.List[PySide2.QtMultimedia.QAudioFormat.Endian] """
        pass

    def supportedChannelCounts(self): # real signature unknown; restored from __doc__
        """ supportedChannelCounts(self) -> typing.List[int] """
        pass

    def supportedCodecs(self): # real signature unknown; restored from __doc__
        """ supportedCodecs(self) -> typing.List[str] """
        pass

    def supportedSampleRates(self): # real signature unknown; restored from __doc__
        """ supportedSampleRates(self) -> typing.List[int] """
        pass

    def supportedSampleSizes(self): # real signature unknown; restored from __doc__
        """ supportedSampleSizes(self) -> typing.List[int] """
        pass

    def supportedSampleTypes(self): # real signature unknown; restored from __doc__
        """ supportedSampleTypes(self) -> typing.List[PySide2.QtMultimedia.QAudioFormat.SampleType] """
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887464DC80>'


