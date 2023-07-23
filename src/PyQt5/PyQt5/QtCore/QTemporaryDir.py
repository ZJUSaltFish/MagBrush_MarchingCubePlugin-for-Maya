# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QTemporaryDir(__sip.simplewrapper):
    """
    QTemporaryDir()
    QTemporaryDir(templateName: str)
    """
    def autoRemove(self): # real signature unknown; restored from __doc__
        """ autoRemove(self) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def filePath(self, fileName): # real signature unknown; restored from __doc__
        """ filePath(self, fileName: str) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> str """
        return ""

    def remove(self): # real signature unknown; restored from __doc__
        """ remove(self) -> bool """
        return False

    def setAutoRemove(self, b): # real signature unknown; restored from __doc__
        """ setAutoRemove(self, b: bool) """
        pass

    def __init__(self, templateName=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



