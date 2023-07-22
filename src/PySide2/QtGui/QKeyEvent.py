# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QInputEvent import QInputEvent

class QKeyEvent(QInputEvent):
    """
    QKeyEvent(self, type: PySide2.QtCore.QEvent.Type, key: int, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, nativeScanCode: int, nativeVirtualKey: int, nativeModifiers: int, text: str = '', autorep: bool = False, count: int = 1) -> None
    QKeyEvent(self, type: PySide2.QtCore.QEvent.Type, key: int, modifiers: PySide2.QtCore.Qt.KeyboardModifiers, text: str = '', autorep: bool = False, count: int = 1) -> None
    """
    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def isAutoRepeat(self): # real signature unknown; restored from __doc__
        """ isAutoRepeat(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> int """
        return 0

    def matches(self, key): # real signature unknown; restored from __doc__
        """ matches(self, key: PySide2.QtGui.QKeySequence.StandardKey) -> bool """
        return False

    def modifiers(self): # real signature unknown; restored from __doc__
        """ modifiers(self) -> PySide2.QtCore.Qt.KeyboardModifiers """
        pass

    def nativeModifiers(self): # real signature unknown; restored from __doc__
        """ nativeModifiers(self) -> int """
        return 0

    def nativeScanCode(self): # real signature unknown; restored from __doc__
        """ nativeScanCode(self) -> int """
        return 0

    def nativeVirtualKey(self): # real signature unknown; restored from __doc__
        """ nativeVirtualKey(self) -> int """
        return 0

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, type, key, modifiers, nativeScanCode, nativeVirtualKey, nativeModifiers, text='', autorep=False, count=1): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    autor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nModifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nScanCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nVirtualKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


