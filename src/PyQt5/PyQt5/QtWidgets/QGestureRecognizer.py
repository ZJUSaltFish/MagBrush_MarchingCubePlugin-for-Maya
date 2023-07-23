# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QGestureRecognizer(__sip.wrapper):
    """
    QGestureRecognizer()
    QGestureRecognizer(a0: QGestureRecognizer)
    """
    def create(self, target): # real signature unknown; restored from __doc__
        """ create(self, target: QObject) -> QGesture """
        return QGesture

    def recognize(self, state, watched, event): # real signature unknown; restored from __doc__
        """ recognize(self, state: QGesture, watched: QObject, event: QEvent) -> QGestureRecognizer.Result """
        pass

    def registerRecognizer(self, recognizer): # real signature unknown; restored from __doc__
        """ registerRecognizer(recognizer: QGestureRecognizer) -> Qt.GestureType """
        pass

    def reset(self, state): # real signature unknown; restored from __doc__
        """ reset(self, state: QGesture) """
        pass

    def unregisterRecognizer(self, type): # real signature unknown; restored from __doc__
        """ unregisterRecognizer(type: Qt.GestureType) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    CancelGesture = 16
    ConsumeEventHint = 256
    FinishGesture = 8
    Ignore = 1
    MayBeGesture = 2
    TriggerGesture = 4


