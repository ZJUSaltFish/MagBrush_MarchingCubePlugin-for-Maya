# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QEvent import QEvent

class QChildEvent(QEvent):
    """
    QChildEvent(type: QEvent.Type, child: QObject)
    QChildEvent(a0: QChildEvent)
    """
    def added(self): # real signature unknown; restored from __doc__
        """ added(self) -> bool """
        return False

    def child(self): # real signature unknown; restored from __doc__
        """ child(self) -> QObject """
        return QObject

    def polished(self): # real signature unknown; restored from __doc__
        """ polished(self) -> bool """
        return False

    def removed(self): # real signature unknown; restored from __doc__
        """ removed(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


