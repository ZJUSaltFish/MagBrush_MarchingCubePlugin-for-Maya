# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QCameraImageProcessing(__PySide2_QtCore.QObject):
    # no doc
    def brightness(self): # real signature unknown; restored from __doc__
        """ brightness(self) -> float """
        return 0.0

    def colorFilter(self): # real signature unknown; restored from __doc__
        """ colorFilter(self) -> PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter """
        pass

    def contrast(self): # real signature unknown; restored from __doc__
        """ contrast(self) -> float """
        return 0.0

    def denoisingLevel(self): # real signature unknown; restored from __doc__
        """ denoisingLevel(self) -> float """
        return 0.0

    def isAvailable(self): # real signature unknown; restored from __doc__
        """ isAvailable(self) -> bool """
        return False

    def isColorFilterSupported(self, filter): # real signature unknown; restored from __doc__
        """ isColorFilterSupported(self, filter: PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter) -> bool """
        return False

    def isWhiteBalanceModeSupported(self, mode): # real signature unknown; restored from __doc__
        """ isWhiteBalanceModeSupported(self, mode: PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode) -> bool """
        return False

    def manualWhiteBalance(self): # real signature unknown; restored from __doc__
        """ manualWhiteBalance(self) -> float """
        return 0.0

    def saturation(self): # real signature unknown; restored from __doc__
        """ saturation(self) -> float """
        return 0.0

    def setBrightness(self, value): # real signature unknown; restored from __doc__
        """ setBrightness(self, value: float) -> None """
        pass

    def setColorFilter(self, filter): # real signature unknown; restored from __doc__
        """ setColorFilter(self, filter: PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter) -> None """
        pass

    def setContrast(self, value): # real signature unknown; restored from __doc__
        """ setContrast(self, value: float) -> None """
        pass

    def setDenoisingLevel(self, value): # real signature unknown; restored from __doc__
        """ setDenoisingLevel(self, value: float) -> None """
        pass

    def setManualWhiteBalance(self, colorTemperature): # real signature unknown; restored from __doc__
        """ setManualWhiteBalance(self, colorTemperature: float) -> None """
        pass

    def setSaturation(self, value): # real signature unknown; restored from __doc__
        """ setSaturation(self, value: float) -> None """
        pass

    def setSharpeningLevel(self, value): # real signature unknown; restored from __doc__
        """ setSharpeningLevel(self, value: float) -> None """
        pass

    def setWhiteBalanceMode(self, mode): # real signature unknown; restored from __doc__
        """ setWhiteBalanceMode(self, mode: PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode) -> None """
        pass

    def sharpeningLevel(self): # real signature unknown; restored from __doc__
        """ sharpeningLevel(self) -> float """
        return 0.0

    def whiteBalanceMode(self): # real signature unknown; restored from __doc__
        """ whiteBalanceMode(self) -> PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ColorFilter = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter'>"
    ColorFilterAqua = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterAqua
    ColorFilterBlackboard = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterBlackboard
    ColorFilterGrayscale = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterGrayscale
    ColorFilterNegative = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterNegative
    ColorFilterNone = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterNone
    ColorFilterPosterize = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterPosterize
    ColorFilterSepia = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterSepia
    ColorFilterSolarize = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterSolarize
    ColorFilterVendor = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterVendor
    ColorFilterWhiteboard = PySide2.QtMultimedia.QCameraImageProcessing.ColorFilter.ColorFilterWhiteboard
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000188746A6080>'
    WhiteBalanceAuto = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceAuto
    WhiteBalanceCloudy = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceCloudy
    WhiteBalanceFlash = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceFlash
    WhiteBalanceFluorescent = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceFluorescent
    WhiteBalanceManual = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceManual
    WhiteBalanceMode = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode'>"
    WhiteBalanceShade = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceShade
    WhiteBalanceSunlight = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceSunlight
    WhiteBalanceSunset = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceSunset
    WhiteBalanceTungsten = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceTungsten
    WhiteBalanceVendor = PySide2.QtMultimedia.QCameraImageProcessing.WhiteBalanceMode.WhiteBalanceVendor


