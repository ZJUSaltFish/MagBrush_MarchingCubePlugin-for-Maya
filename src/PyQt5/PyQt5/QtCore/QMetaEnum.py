# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMetaEnum(__sip.simplewrapper):
    """
    QMetaEnum()
    QMetaEnum(a0: QMetaEnum)
    """
    def enumName(self): # real signature unknown; restored from __doc__
        """ enumName(self) -> str """
        return ""

    def isFlag(self): # real signature unknown; restored from __doc__
        """ isFlag(self) -> bool """
        return False

    def isScoped(self): # real signature unknown; restored from __doc__
        """ isScoped(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def key(self, index): # real signature unknown; restored from __doc__
        """ key(self, index: int) -> str """
        return ""

    def keyCount(self): # real signature unknown; restored from __doc__
        """ keyCount(self) -> int """
        return 0

    def keysToValue(self, keys): # real signature unknown; restored from __doc__
        """ keysToValue(self, keys: str) -> Tuple[int, bool] """
        pass

    def keyToValue(self, key): # real signature unknown; restored from __doc__
        """ keyToValue(self, key: str) -> Tuple[int, bool] """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def scope(self): # real signature unknown; restored from __doc__
        """ scope(self) -> str """
        return ""

    def value(self, index): # real signature unknown; restored from __doc__
        """ value(self, index: int) -> int """
        return 0

    def valueToKey(self, value): # real signature unknown; restored from __doc__
        """ valueToKey(self, value: int) -> str """
        return ""

    def valueToKeys(self, value): # real signature unknown; restored from __doc__
        """ valueToKeys(self, value: int) -> QByteArray """
        return QByteArray

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


