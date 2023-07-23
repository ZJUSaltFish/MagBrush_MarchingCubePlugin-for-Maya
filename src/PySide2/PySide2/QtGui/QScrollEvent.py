# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QScrollEvent(__PySide2_QtCore.QEvent):
    """ QScrollEvent(self, contentPos: PySide2.QtCore.QPointF, overshoot: PySide2.QtCore.QPointF, scrollState: PySide2.QtGui.QScrollEvent.ScrollState) -> None """
    def contentPos(self): # real signature unknown; restored from __doc__
        """ contentPos(self) -> PySide2.QtCore.QPointF """
        pass

    def overshootDistance(self): # real signature unknown; restored from __doc__
        """ overshootDistance(self) -> PySide2.QtCore.QPointF """
        pass

    def scrollState(self): # real signature unknown; restored from __doc__
        """ scrollState(self) -> PySide2.QtGui.QScrollEvent.ScrollState """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, contentPos, overshoot, scrollState): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ScrollFinished = PySide2.QtGui.QScrollEvent.ScrollState.ScrollFinished
    ScrollStarted = PySide2.QtGui.QScrollEvent.ScrollState.ScrollStarted
    ScrollState = None # (!) real value is "<class 'PySide2.QtGui.QScrollEvent.ScrollState'>"
    ScrollUpdated = PySide2.QtGui.QScrollEvent.ScrollState.ScrollUpdated


