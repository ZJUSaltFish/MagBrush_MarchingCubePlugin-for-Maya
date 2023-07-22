# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaControl import QMediaControl

class QCameraImageCaptureControl(QMediaControl):
    """ QCameraImageCaptureControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def cancelCapture(self): # real signature unknown; restored from __doc__
        """ cancelCapture(self) -> None """
        pass

    def capture(self, fileName): # real signature unknown; restored from __doc__
        """ capture(self, fileName: str) -> int """
        return 0

    def driveMode(self): # real signature unknown; restored from __doc__
        """ driveMode(self) -> PySide2.QtMultimedia.QCameraImageCapture.DriveMode """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def imageAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def imageCaptured(self, *args, **kwargs): # real signature unknown
        pass

    def imageExposed(self, *args, **kwargs): # real signature unknown
        pass

    def imageMetadataAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def imageSaved(self, *args, **kwargs): # real signature unknown
        pass

    def isReadyForCapture(self): # real signature unknown; restored from __doc__
        """ isReadyForCapture(self) -> bool """
        return False

    def readyForCaptureChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setDriveMode(self, mode): # real signature unknown; restored from __doc__
        """ setDriveMode(self, mode: PySide2.QtMultimedia.QCameraImageCapture.DriveMode) -> None """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887467BDC0>'


