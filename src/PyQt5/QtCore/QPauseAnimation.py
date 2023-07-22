# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractAnimation import QAbstractAnimation

class QPauseAnimation(QAbstractAnimation):
    """
    QPauseAnimation(parent: typing.Optional[QObject] = None)
    QPauseAnimation(msecs: int, parent: typing.Optional[QObject] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: QEvent) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDuration(self, msecs): # real signature unknown; restored from __doc__
        """ setDuration(self, msecs: int) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, a0): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, a0: int) """
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


