# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QAbstractSpinBox import QAbstractSpinBox

class QSpinBox(QAbstractSpinBox):
    """ QSpinBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
    def cleanText(self): # real signature unknown; restored from __doc__
        """ cleanText(self) -> str """
        return ""

    def displayIntegerBase(self): # real signature unknown; restored from __doc__
        """ displayIntegerBase(self) -> int """
        return 0

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def fixup(self, p_str): # real signature unknown; restored from __doc__
        """ fixup(self, str: str) -> None """
        pass

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def setDisplayIntegerBase(self, base): # real signature unknown; restored from __doc__
        """ setDisplayIntegerBase(self, base: int) -> None """
        pass

    def setMaximum(self, max): # real signature unknown; restored from __doc__
        """ setMaximum(self, max: int) -> None """
        pass

    def setMinimum(self, min): # real signature unknown; restored from __doc__
        """ setMinimum(self, min: int) -> None """
        pass

    def setPrefix(self, prefix): # real signature unknown; restored from __doc__
        """ setPrefix(self, prefix: str) -> None """
        pass

    def setRange(self, min, max): # real signature unknown; restored from __doc__
        """ setRange(self, min: int, max: int) -> None """
        pass

    def setSingleStep(self, val): # real signature unknown; restored from __doc__
        """ setSingleStep(self, val: int) -> None """
        pass

    def setStepType(self, stepType): # real signature unknown; restored from __doc__
        """ setStepType(self, stepType: PySide2.QtWidgets.QAbstractSpinBox.StepType) -> None """
        pass

    def setSuffix(self, suffix): # real signature unknown; restored from __doc__
        """ setSuffix(self, suffix: str) -> None """
        pass

    def setValue(self, val): # real signature unknown; restored from __doc__
        """ setValue(self, val: int) -> None """
        pass

    def singleStep(self): # real signature unknown; restored from __doc__
        """ singleStep(self) -> int """
        return 0

    def stepType(self): # real signature unknown; restored from __doc__
        """ stepType(self) -> PySide2.QtWidgets.QAbstractSpinBox.StepType """
        pass

    def suffix(self): # real signature unknown; restored from __doc__
        """ suffix(self) -> str """
        return ""

    def textChanged(self, *args, **kwargs): # real signature unknown
        pass

    def textFromValue(self, val): # real signature unknown; restored from __doc__
        """ textFromValue(self, val: int) -> str """
        return ""

    def validate(self, input, pos): # real signature unknown; restored from __doc__
        """ validate(self, input: str, pos: int) -> PySide2.QtGui.QValidator.State """
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def valueFromText(self, text): # real signature unknown; restored from __doc__
        """ valueFromText(self, text: str) -> int """
        return 0

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F507D6440>'


