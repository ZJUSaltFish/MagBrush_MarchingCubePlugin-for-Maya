# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QObject import QObject

class QSocketNotifier(QObject):
    """
    QSocketNotifier(self, arg__1: object, arg__2: PySide2.QtCore.QSocketNotifier.Type, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSocketNotifier(self, socket: int, arg__2: PySide2.QtCore.QSocketNotifier.Type, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def activated(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def setEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setEnabled(self, arg__1: bool) -> None """
        pass

    def socket(self): # real signature unknown; restored from __doc__
        """ socket(self) -> int """
        return 0

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.QSocketNotifier.Type """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1, arg__2, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Exception = PySide2.QtCore.QSocketNotifier.Type.Exception
    Read = PySide2.QtCore.QSocketNotifier.Type.Read
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DDCD00>'
    Type = None # (!) real value is "<class 'PySide2.QtCore.QSocketNotifier.Type'>"
    Write = PySide2.QtCore.QSocketNotifier.Type.Write


