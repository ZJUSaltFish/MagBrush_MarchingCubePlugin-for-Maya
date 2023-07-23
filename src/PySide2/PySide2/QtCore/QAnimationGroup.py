# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractAnimation import QAbstractAnimation

class QAnimationGroup(QAbstractAnimation):
    """ QAnimationGroup(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addAnimation(self, animation): # real signature unknown; restored from __doc__
        """ addAnimation(self, animation: PySide2.QtCore.QAbstractAnimation) -> None """
        pass

    def animationAt(self, index): # real signature unknown; restored from __doc__
        """ animationAt(self, index: int) -> PySide2.QtCore.QAbstractAnimation """
        pass

    def animationCount(self): # real signature unknown; restored from __doc__
        """ animationCount(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: PySide2.QtCore.QEvent) -> bool """
        return False

    def indexOfAnimation(self, animation): # real signature unknown; restored from __doc__
        """ indexOfAnimation(self, animation: PySide2.QtCore.QAbstractAnimation) -> int """
        return 0

    def insertAnimation(self, index, animation): # real signature unknown; restored from __doc__
        """ insertAnimation(self, index: int, animation: PySide2.QtCore.QAbstractAnimation) -> None """
        pass

    def removeAnimation(self, animation): # real signature unknown; restored from __doc__
        """ removeAnimation(self, animation: PySide2.QtCore.QAbstractAnimation) -> None """
        pass

    def takeAnimation(self, index): # real signature unknown; restored from __doc__
        """ takeAnimation(self, index: int) -> PySide2.QtCore.QAbstractAnimation """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E64FC0>'


