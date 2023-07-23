# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QWidget import QWidget

class QAbstractSlider(QWidget):
    """ QAbstractSlider(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def actionTriggered(self, *args, **kwargs): # real signature unknown
        pass

    def changeEvent(self, e): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: PySide2.QtCore.QEvent) -> None """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def hasTracking(self): # real signature unknown; restored from __doc__
        """ hasTracking(self) -> bool """
        return False

    def invertedAppearance(self): # real signature unknown; restored from __doc__
        """ invertedAppearance(self) -> bool """
        return False

    def invertedControls(self): # real signature unknown; restored from __doc__
        """ invertedControls(self) -> bool """
        return False

    def isSliderDown(self): # real signature unknown; restored from __doc__
        """ isSliderDown(self) -> bool """
        return False

    def keyPressEvent(self, ev): # real signature unknown; restored from __doc__
        """ keyPressEvent(self, ev: PySide2.QtGui.QKeyEvent) -> None """
        pass

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def orientation(self): # real signature unknown; restored from __doc__
        """ orientation(self) -> PySide2.QtCore.Qt.Orientation """
        pass

    def pageStep(self): # real signature unknown; restored from __doc__
        """ pageStep(self) -> int """
        return 0

    def rangeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def repeatAction(self): # real signature unknown; restored from __doc__
        """ repeatAction(self) -> PySide2.QtWidgets.QAbstractSlider.SliderAction """
        pass

    def setInvertedAppearance(self, arg__1): # real signature unknown; restored from __doc__
        """ setInvertedAppearance(self, arg__1: bool) -> None """
        pass

    def setInvertedControls(self, arg__1): # real signature unknown; restored from __doc__
        """ setInvertedControls(self, arg__1: bool) -> None """
        pass

    def setMaximum(self, arg__1): # real signature unknown; restored from __doc__
        """ setMaximum(self, arg__1: int) -> None """
        pass

    def setMinimum(self, arg__1): # real signature unknown; restored from __doc__
        """ setMinimum(self, arg__1: int) -> None """
        pass

    def setOrientation(self, arg__1): # real signature unknown; restored from __doc__
        """ setOrientation(self, arg__1: PySide2.QtCore.Qt.Orientation) -> None """
        pass

    def setPageStep(self, arg__1): # real signature unknown; restored from __doc__
        """ setPageStep(self, arg__1: int) -> None """
        pass

    def setRange(self, min, max): # real signature unknown; restored from __doc__
        """ setRange(self, min: int, max: int) -> None """
        pass

    def setRepeatAction(self, action, thresholdTime=500, repeatTime=50): # real signature unknown; restored from __doc__
        """ setRepeatAction(self, action: PySide2.QtWidgets.QAbstractSlider.SliderAction, thresholdTime: int = 500, repeatTime: int = 50) -> None """
        pass

    def setSingleStep(self, arg__1): # real signature unknown; restored from __doc__
        """ setSingleStep(self, arg__1: int) -> None """
        pass

    def setSliderDown(self, arg__1): # real signature unknown; restored from __doc__
        """ setSliderDown(self, arg__1: bool) -> None """
        pass

    def setSliderPosition(self, arg__1): # real signature unknown; restored from __doc__
        """ setSliderPosition(self, arg__1: int) -> None """
        pass

    def setTracking(self, enable): # real signature unknown; restored from __doc__
        """ setTracking(self, enable: bool) -> None """
        pass

    def setValue(self, arg__1): # real signature unknown; restored from __doc__
        """ setValue(self, arg__1: int) -> None """
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ singleStep(self) -> int """
        return 0

    def sliderChange(self, change): # real signature unknown; restored from __doc__
        """ sliderChange(self, change: PySide2.QtWidgets.QAbstractSlider.SliderChange) -> None """
        pass

    def sliderMoved(self, *args, **kwargs): # real signature unknown
        pass

    def sliderPosition(self): # real signature unknown; restored from __doc__
        """ sliderPosition(self) -> int """
        return 0

    def sliderPressed(self, *args, **kwargs): # real signature unknown
        pass

    def sliderReleased(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def triggerAction(self, action): # real signature unknown; restored from __doc__
        """ triggerAction(self, action: PySide2.QtWidgets.QAbstractSlider.SliderAction) -> None """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def wheelEvent(self, e): # real signature unknown; restored from __doc__
        """ wheelEvent(self, e: PySide2.QtGui.QWheelEvent) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    SliderAction = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractSlider.SliderAction'>"
    SliderChange = None # (!) real value is "<class 'PySide2.QtWidgets.QAbstractSlider.SliderChange'>"
    SliderMove = PySide2.QtWidgets.QAbstractSlider.SliderAction.SliderMove
    SliderNoAction = PySide2.QtWidgets.QAbstractSlider.SliderAction.SliderNoAction
    SliderOrientationChange = PySide2.QtWidgets.QAbstractSlider.SliderChange.SliderOrientationChange
    SliderPageStepAdd = PySide2.QtWidgets.QAbstractSlider.SliderAction.SliderPageStepAdd
    SliderPageStepSub = PySide2.QtWidgets.QAbstractSlider.SliderAction.SliderPageStepSub
    SliderRangeChange = PySide2.QtWidgets.QAbstractSlider.SliderChange.SliderRangeChange
    SliderSingleStepAdd = PySide2.QtWidgets.QAbstractSlider.SliderAction.SliderSingleStepAdd
    SliderSingleStepSub = PySide2.QtWidgets.QAbstractSlider.SliderAction.SliderSingleStepSub
    SliderStepsChange = PySide2.QtWidgets.QAbstractSlider.SliderChange.SliderStepsChange
    SliderToMaximum = PySide2.QtWidgets.QAbstractSlider.SliderAction.SliderToMaximum
    SliderToMinimum = PySide2.QtWidgets.QAbstractSlider.SliderAction.SliderToMinimum
    SliderValueChange = PySide2.QtWidgets.QAbstractSlider.SliderChange.SliderValueChange
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507D6F40>'


