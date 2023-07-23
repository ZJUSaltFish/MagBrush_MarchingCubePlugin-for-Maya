# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaControl import QMediaControl

class QCameraControl(QMediaControl):
    """ QCameraControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def canChangeProperty(self, changeType, status): # real signature unknown; restored from __doc__
        """ canChangeProperty(self, changeType: PySide2.QtMultimedia.QCameraControl.PropertyChangeType, status: PySide2.QtMultimedia.QCamera.Status) -> bool """
        return False

    def captureMode(self): # real signature unknown; restored from __doc__
        """ captureMode(self) -> PySide2.QtMultimedia.QCamera.CaptureModes """
        pass

    def captureModeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def isCaptureModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isCaptureModeSupported(self, mode: PySide2.QtMultimedia.QCamera.CaptureModes) -> bool """
        return False

    def setCaptureMode(self, arg__1): # real signature unknown; restored from __doc__
        """ setCaptureMode(self, arg__1: PySide2.QtMultimedia.QCamera.CaptureModes) -> None """
        pass

    def setState(self, state): # real signature unknown; restored from __doc__
        """ setState(self, state: PySide2.QtMultimedia.QCamera.State) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtMultimedia.QCamera.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtMultimedia.QCamera.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
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

    CaptureMode = PySide2.QtMultimedia.QCameraControl.PropertyChangeType.CaptureMode
    ImageEncodingSettings = PySide2.QtMultimedia.QCameraControl.PropertyChangeType.ImageEncodingSettings
    PropertyChangeType = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraControl.PropertyChangeType'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000188746A4F00>'
    VideoEncodingSettings = PySide2.QtMultimedia.QCameraControl.PropertyChangeType.VideoEncodingSettings
    Viewfinder = PySide2.QtMultimedia.QCameraControl.PropertyChangeType.Viewfinder
    ViewfinderSettings = PySide2.QtMultimedia.QCameraControl.PropertyChangeType.ViewfinderSettings


