# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractTransition import QAbstractTransition

class QEventTransition(QAbstractTransition):
    """
    QEventTransition(sourceState: typing.Optional[QState] = None)
    QEventTransition(object: QObject, type: QEvent.Type, sourceState: typing.Optional[QState] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: QEvent) -> bool """
        return False

    def eventSource(self): # real signature unknown; restored from __doc__
        """ eventSource(self) -> QObject """
        return QObject

    def eventTest(self, event): # real signature unknown; restored from __doc__
        """ eventTest(self, event: QEvent) -> bool """
        return False

    def eventType(self): # real signature unknown; restored from __doc__
        """ eventType(self) -> QEvent.Type """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def onTransition(self, event): # real signature unknown; restored from __doc__
        """ onTransition(self, event: QEvent) """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setEventSource(self, p_object): # real signature unknown; restored from __doc__
        """ setEventSource(self, object: QObject) """
        pass

    def setEventType(self, type): # real signature unknown; restored from __doc__
        """ setEventType(self, type: QEvent.Type) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


