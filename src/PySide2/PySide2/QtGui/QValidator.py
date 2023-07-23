# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QValidator(__PySide2_QtCore.QObject):
    """ QValidator(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def fixup(self, arg__1): # real signature unknown; restored from __doc__
        """ fixup(self, arg__1: str) -> None """
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> PySide2.QtCore.QLocale """
        pass

    def setLocale(self, locale): # real signature unknown; restored from __doc__
        """ setLocale(self, locale: PySide2.QtCore.QLocale) -> None """
        pass

    def validate(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ validate(self, arg__1: str, arg__2: int) -> PySide2.QtGui.QValidator.State """
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

    Acceptable = PySide2.QtGui.QValidator.State.Acceptable
    Intermediate = PySide2.QtGui.QValidator.State.Intermediate
    Invalid = PySide2.QtGui.QValidator.State.Invalid
    State = None # (!) real value is "<class 'PySide2.QtGui.QValidator.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00845580>'


