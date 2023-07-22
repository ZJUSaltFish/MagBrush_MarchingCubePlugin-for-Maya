# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaControl import QMediaControl

class QCameraExposureControl(QMediaControl):
    """ QCameraExposureControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def actualValue(self, parameter): # real signature unknown; restored from __doc__
        """ actualValue(self, parameter: PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter) -> typing.Any """
        pass

    def actualValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isParameterSupported(self, parameter): # real signature unknown; restored from __doc__
        """ isParameterSupported(self, parameter: PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter) -> bool """
        return False

    def parameterRangeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def requestedValue(self, parameter): # real signature unknown; restored from __doc__
        """ requestedValue(self, parameter: PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter) -> typing.Any """
        pass

    def requestedValueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, parameter, value): # real signature unknown; restored from __doc__
        """ setValue(self, parameter: PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter, value: typing.Any) -> bool """
        return False

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

    Aperture = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.Aperture
    ExposureCompensation = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.ExposureCompensation
    ExposureMode = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.ExposureMode
    ExposureParameter = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter'>"
    ExtendedExposureParameter = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.ExtendedExposureParameter
    FlashCompensation = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.FlashCompensation
    FlashPower = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.FlashPower
    ISO = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.ISO
    MeteringMode = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.MeteringMode
    ShutterSpeed = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.ShutterSpeed
    SpotMeteringPoint = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.SpotMeteringPoint
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000188746A4B80>'
    TorchPower = PySide2.QtMultimedia.QCameraExposureControl.ExposureParameter.TorchPower


