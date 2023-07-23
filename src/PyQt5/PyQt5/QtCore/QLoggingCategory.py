# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QLoggingCategory(__sip.simplewrapper):
    """
    QLoggingCategory(category: str)
    QLoggingCategory(category: str, severityLevel: QtMsgType)
    """
    def categoryName(self): # real signature unknown; restored from __doc__
        """ categoryName(self) -> str """
        return ""

    def defaultCategory(self): # real signature unknown; restored from __doc__
        """ defaultCategory() -> QLoggingCategory """
        return QLoggingCategory

    def isCriticalEnabled(self): # real signature unknown; restored from __doc__
        """ isCriticalEnabled(self) -> bool """
        return False

    def isDebugEnabled(self): # real signature unknown; restored from __doc__
        """ isDebugEnabled(self) -> bool """
        return False

    def isEnabled(self, type): # real signature unknown; restored from __doc__
        """ isEnabled(self, type: QtMsgType) -> bool """
        return False

    def isInfoEnabled(self): # real signature unknown; restored from __doc__
        """ isInfoEnabled(self) -> bool """
        return False

    def isWarningEnabled(self): # real signature unknown; restored from __doc__
        """ isWarningEnabled(self) -> bool """
        return False

    def setEnabled(self, type, enable): # real signature unknown; restored from __doc__
        """ setEnabled(self, type: QtMsgType, enable: bool) """
        pass

    def setFilterRules(self, rules): # real signature unknown; restored from __doc__
        """ setFilterRules(rules: str) """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, category, severityLevel=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



