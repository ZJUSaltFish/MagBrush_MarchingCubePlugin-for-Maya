# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAnimationGroup import QAnimationGroup

class QSequentialAnimationGroup(QAnimationGroup):
    """ QSequentialAnimationGroup(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addPause(self, msecs): # real signature unknown; restored from __doc__
        """ addPause(self, msecs: int) -> PySide2.QtCore.QPauseAnimation """
        pass

    def currentAnimation(self): # real signature unknown; restored from __doc__
        """ currentAnimation(self) -> PySide2.QtCore.QAbstractAnimation """
        pass

    def currentAnimationChanged(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def insertPause(self, index, msecs): # real signature unknown; restored from __doc__
        """ insertPause(self, index: int, msecs: int) -> PySide2.QtCore.QPauseAnimation """
        pass

    def updateCurrentTime(self, arg__1): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, arg__1: int) -> None """
        pass

    def updateDirection(self, direction): # real signature unknown; restored from __doc__
        """ updateDirection(self, direction: PySide2.QtCore.QAbstractAnimation.Direction) -> None """
        pass

    def updateState(self, newState, oldState): # real signature unknown; restored from __doc__
        """ updateState(self, newState: PySide2.QtCore.QAbstractAnimation.State, oldState: PySide2.QtCore.QAbstractAnimation.State) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E65280>'


