# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaControl import QMediaControl

class QMediaStreamsControl(QMediaControl):
    """ QMediaStreamsControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def activeStreamsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, streamNumber): # real signature unknown; restored from __doc__
        """ isActive(self, streamNumber: int) -> bool """
        return False

    def metaData(self, streamNumber, key): # real signature unknown; restored from __doc__
        """ metaData(self, streamNumber: int, key: str) -> typing.Any """
        pass

    def setActive(self, streamNumber, state): # real signature unknown; restored from __doc__
        """ setActive(self, streamNumber: int, state: bool) -> None """
        pass

    def streamCount(self): # real signature unknown; restored from __doc__
        """ streamCount(self) -> int """
        return 0

    def streamsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def streamType(self, streamNumber): # real signature unknown; restored from __doc__
        """ streamType(self, streamNumber: int) -> PySide2.QtMultimedia.QMediaStreamsControl.StreamType """
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

    AudioStream = PySide2.QtMultimedia.QMediaStreamsControl.StreamType.AudioStream
    DataStream = PySide2.QtMultimedia.QMediaStreamsControl.StreamType.DataStream
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887467A740>'
    StreamType = None # (!) real value is "<class 'PySide2.QtMultimedia.QMediaStreamsControl.StreamType'>"
    SubPictureStream = PySide2.QtMultimedia.QMediaStreamsControl.StreamType.SubPictureStream
    UnknownStream = PySide2.QtMultimedia.QMediaStreamsControl.StreamType.UnknownStream
    VideoStream = PySide2.QtMultimedia.QMediaStreamsControl.StreamType.VideoStream


