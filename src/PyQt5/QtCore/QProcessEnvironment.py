# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QProcessEnvironment(__sip.simplewrapper):
    """
    QProcessEnvironment()
    QProcessEnvironment(other: QProcessEnvironment)
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def contains(self, name): # real signature unknown; restored from __doc__
        """ contains(self, name: str) -> bool """
        return False

    def insert(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        insert(self, name: str, value: str)
        insert(self, e: QProcessEnvironment)
        """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def keys(self): # real signature unknown; restored from __doc__
        """ keys(self) -> List[str] """
        return []

    def remove(self, name): # real signature unknown; restored from __doc__
        """ remove(self, name: str) """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: QProcessEnvironment) """
        pass

    def systemEnvironment(self): # real signature unknown; restored from __doc__
        """ systemEnvironment() -> QProcessEnvironment """
        return QProcessEnvironment

    def toStringList(self): # real signature unknown; restored from __doc__
        """ toStringList(self) -> List[str] """
        return []

    def value(self, name, defaultValue=''): # real signature unknown; restored from __doc__
        """ value(self, name: str, defaultValue: str = '') -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, other=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


