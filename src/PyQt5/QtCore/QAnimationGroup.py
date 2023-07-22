# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QAbstractAnimation import QAbstractAnimation

class QAnimationGroup(QAbstractAnimation):
    """ QAnimationGroup(parent: typing.Optional[QObject] = None) """
    def addAnimation(self, animation): # real signature unknown; restored from __doc__
        """ addAnimation(self, animation: QAbstractAnimation) """
        pass

    def animationAt(self, index): # real signature unknown; restored from __doc__
        """ animationAt(self, index: int) -> QAbstractAnimation """
        return QAbstractAnimation

    def animationCount(self): # real signature unknown; restored from __doc__
        """ animationCount(self) -> int """
        return 0

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
        return False

    def indexOfAnimation(self, animation): # real signature unknown; restored from __doc__
        """ indexOfAnimation(self, animation: QAbstractAnimation) -> int """
        return 0

    def insertAnimation(self, index, animation): # real signature unknown; restored from __doc__
        """ insertAnimation(self, index: int, animation: QAbstractAnimation) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeAnimation(self, animation): # real signature unknown; restored from __doc__
        """ removeAnimation(self, animation: QAbstractAnimation) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def takeAnimation(self, index): # real signature unknown; restored from __doc__
        """ takeAnimation(self, index: int) -> QAbstractAnimation """
        return QAbstractAnimation

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateCurrentTime(self, *args, **kwargs): # real signature unknown
        pass

    def updateDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateState(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


