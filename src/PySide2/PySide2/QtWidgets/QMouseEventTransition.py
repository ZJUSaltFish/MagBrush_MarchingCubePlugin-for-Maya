# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QMouseEventTransition(__PySide2_QtCore.QEventTransition):
    """
    QMouseEventTransition(self, object: PySide2.QtCore.QObject, type: PySide2.QtCore.QEvent.Type, button: PySide2.QtCore.Qt.MouseButton, sourceState: typing.Optional[PySide2.QtCore.QState] = None) -> None
    QMouseEventTransition(self, sourceState: typing.Optional[PySide2.QtCore.QState] = None) -> None
    """
    def button(self): # real signature unknown; restored from __doc__
        """ button(self) -> PySide2.QtCore.Qt.MouseButton """
        pass

    def eventTest(self, event): # real signature unknown; restored from __doc__
        """ eventTest(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def hitTestPath(self): # real signature unknown; restored from __doc__
        """ hitTestPath(self) -> PySide2.QtGui.QPainterPath """
        pass

    def modifierMask(self): # real signature unknown; restored from __doc__
        """ modifierMask(self) -> PySide2.QtCore.Qt.KeyboardModifiers """
        pass

    def onTransition(self, event): # real signature unknown; restored from __doc__
        """ onTransition(self, event: PySide2.QtCore.QEvent) -> None """
        pass

    def setButton(self, button): # real signature unknown; restored from __doc__
        """ setButton(self, button: PySide2.QtCore.Qt.MouseButton) -> None """
        pass

    def setHitTestPath(self, path): # real signature unknown; restored from __doc__
        """ setHitTestPath(self, path: PySide2.QtGui.QPainterPath) -> None """
        pass

    def setModifierMask(self, modifiers): # real signature unknown; restored from __doc__
        """ setModifierMask(self, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, p_object, type, button, sourceState, PySide2_QtCore_QState=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50888B80>'


