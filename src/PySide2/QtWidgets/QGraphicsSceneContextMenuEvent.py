# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGraphicsSceneEvent import QGraphicsSceneEvent

class QGraphicsSceneContextMenuEvent(QGraphicsSceneEvent):
    """ QGraphicsSceneContextMenuEvent(self, type: typing.Optional[PySide2.QtCore.QEvent.Type] = None) -> None """
    def modifiers(self): # real signature unknown; restored from __doc__
        """ modifiers(self) -> PySide2.QtCore.Qt.KeyboardModifiers """
        pass

    def pos(self): # real signature unknown; restored from __doc__
        """ pos(self) -> PySide2.QtCore.QPointF """
        pass

    def reason(self): # real signature unknown; restored from __doc__
        """ reason(self) -> PySide2.QtWidgets.QGraphicsSceneContextMenuEvent.Reason """
        pass

    def scenePos(self): # real signature unknown; restored from __doc__
        """ scenePos(self) -> PySide2.QtCore.QPointF """
        pass

    def screenPos(self): # real signature unknown; restored from __doc__
        """ screenPos(self) -> PySide2.QtCore.QPoint """
        pass

    def setModifiers(self, modifiers): # real signature unknown; restored from __doc__
        """ setModifiers(self, modifiers: PySide2.QtCore.Qt.KeyboardModifiers) -> None """
        pass

    def setPos(self, pos): # real signature unknown; restored from __doc__
        """ setPos(self, pos: PySide2.QtCore.QPointF) -> None """
        pass

    def setReason(self, reason): # real signature unknown; restored from __doc__
        """ setReason(self, reason: PySide2.QtWidgets.QGraphicsSceneContextMenuEvent.Reason) -> None """
        pass

    def setScenePos(self, pos): # real signature unknown; restored from __doc__
        """ setScenePos(self, pos: PySide2.QtCore.QPointF) -> None """
        pass

    def setScreenPos(self, pos): # real signature unknown; restored from __doc__
        """ setScreenPos(self, pos: PySide2.QtCore.QPoint) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type, PySide2_QtCore_QEvent_Type=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Keyboard = PySide2.QtWidgets.QGraphicsSceneContextMenuEvent.Reason.Keyboard
    Mouse = PySide2.QtWidgets.QGraphicsSceneContextMenuEvent.Reason.Mouse
    Other = PySide2.QtWidgets.QGraphicsSceneContextMenuEvent.Reason.Other
    Reason = None # (!) real value is "<class 'PySide2.QtWidgets.QGraphicsSceneContextMenuEvent.Reason'>"


