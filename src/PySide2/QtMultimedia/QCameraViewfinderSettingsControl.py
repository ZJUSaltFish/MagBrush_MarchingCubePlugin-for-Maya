# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaControl import QMediaControl

class QCameraViewfinderSettingsControl(QMediaControl):
    """ QCameraViewfinderSettingsControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def isViewfinderParameterSupported(self, parameter): # real signature unknown; restored from __doc__
        """ isViewfinderParameterSupported(self, parameter: PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter) -> bool """
        return False

    def setViewfinderParameter(self, parameter, value): # real signature unknown; restored from __doc__
        """ setViewfinderParameter(self, parameter: PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter, value: typing.Any) -> None """
        pass

    def viewfinderParameter(self, parameter): # real signature unknown; restored from __doc__
        """ viewfinderParameter(self, parameter: PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter) -> typing.Any """
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

    MaximumFrameRate = PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter.MaximumFrameRate
    MinimumFrameRate = PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter.MinimumFrameRate
    PixelAspectRatio = PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter.PixelAspectRatio
    PixelFormat = PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter.PixelFormat
    Resolution = PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter.Resolution
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887467B400>'
    UserParameter = PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter.UserParameter
    ViewfinderParameter = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraViewfinderSettingsControl.ViewfinderParameter'>"


