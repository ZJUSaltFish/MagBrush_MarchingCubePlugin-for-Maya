# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QMediaControl import QMediaControl

class QCameraFeedbackControl(QMediaControl):
    """ QCameraFeedbackControl(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def isEventFeedbackEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ isEventFeedbackEnabled(self, arg__1: PySide2.QtMultimedia.QCameraFeedbackControl.EventType) -> bool """
        return False

    def isEventFeedbackLocked(self, arg__1): # real signature unknown; restored from __doc__
        """ isEventFeedbackLocked(self, arg__1: PySide2.QtMultimedia.QCameraFeedbackControl.EventType) -> bool """
        return False

    def resetEventFeedback(self, arg__1): # real signature unknown; restored from __doc__
        """ resetEventFeedback(self, arg__1: PySide2.QtMultimedia.QCameraFeedbackControl.EventType) -> None """
        pass

    def setEventFeedbackEnabled(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ setEventFeedbackEnabled(self, arg__1: PySide2.QtMultimedia.QCameraFeedbackControl.EventType, arg__2: bool) -> bool """
        return False

    def setEventFeedbackSound(self, arg__1, filePath): # real signature unknown; restored from __doc__
        """ setEventFeedbackSound(self, arg__1: PySide2.QtMultimedia.QCameraFeedbackControl.EventType, filePath: str) -> bool """
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

    AutoFocusFailed = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.AutoFocusFailed
    AutoFocusInProgress = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.AutoFocusInProgress
    AutoFocusLocked = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.AutoFocusLocked
    EventType = None # (!) real value is "<class 'PySide2.QtMultimedia.QCameraFeedbackControl.EventType'>"
    ImageCaptured = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.ImageCaptured
    ImageError = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.ImageError
    ImageSaved = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.ImageSaved
    RecordingInProgress = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.RecordingInProgress
    RecordingStarted = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.RecordingStarted
    RecordingStopped = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.RecordingStopped
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000188746A4680>'
    ViewfinderStarted = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.ViewfinderStarted
    ViewfinderStopped = PySide2.QtMultimedia.QCameraFeedbackControl.EventType.ViewfinderStopped


