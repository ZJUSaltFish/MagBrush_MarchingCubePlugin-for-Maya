# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaControl import QMediaControl

class QCameraImageProcessingControl(QMediaControl):
    """ QCameraImageProcessingControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def isParameterSupported(self, arg__1): # real signature unknown; restored from __doc__
        """ isParameterSupported(self, arg__1: PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter) -> bool """
        return False

    def isParameterValueSupported(self, parameter, value): # real signature unknown; restored from __doc__
        """ isParameterValueSupported(self, parameter: PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter, value: typing.Any) -> bool """
        return False

    def parameter(self, parameter): # real signature unknown; restored from __doc__
        """ parameter(self, parameter: PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter) -> typing.Any """
        pass

    def setParameter(self, parameter, value): # real signature unknown; restored from __doc__
        """ setParameter(self, parameter: PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter, value: typing.Any) -> None """
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

    Brightness = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.Brightness
    BrightnessAdjustment = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.BrightnessAdjustment
    ColorFilter = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.ColorFilter
    ColorTemperature = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.ColorTemperature
    Contrast = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.Contrast
    ContrastAdjustment = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.ContrastAdjustment
    Denoising = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.Denoising
    DenoisingAdjustment = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.DenoisingAdjustment
    ExtendedParameter = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.ExtendedParameter
    ProcessingParameter = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter'>"
    Saturation = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.Saturation
    SaturationAdjustment = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.SaturationAdjustment
    Sharpening = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.Sharpening
    SharpeningAdjustment = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.SharpeningAdjustment
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887467BB40>'
    WhiteBalancePreset = PySide2.QtMultimedia.QCameraImageProcessingControl.ProcessingParameter.WhiteBalancePreset


