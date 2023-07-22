# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


from .QAction import QAction

class QWidgetAction(QAction):
    """ QWidgetAction(parent: QObject) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createdWidgets(self): # real signature unknown; restored from __doc__
        """ createdWidgets(self) -> List[QWidget] """
        return []

    def createWidget(self, parent): # real signature unknown; restored from __doc__
        """ createWidget(self, parent: QWidget) -> QWidget """
        return QWidget

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultWidget(self): # real signature unknown; restored from __doc__
        """ defaultWidget(self) -> QWidget """
        return QWidget

    def deleteWidget(self, widget): # real signature unknown; restored from __doc__
        """ deleteWidget(self, widget: QWidget) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0): # real signature unknown; restored from __doc__
        """ event(self, a0: QEvent) -> bool """
        return False

    def eventFilter(self, a0, a1): # real signature unknown; restored from __doc__
        """ eventFilter(self, a0: QObject, a1: QEvent) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def releaseWidget(self, widget): # real signature unknown; restored from __doc__
        """ releaseWidget(self, widget: QWidget) """
        pass

    def requestWidget(self, parent): # real signature unknown; restored from __doc__
        """ requestWidget(self, parent: QWidget) -> QWidget """
        return QWidget

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultWidget(self, w): # real signature unknown; restored from __doc__
        """ setDefaultWidget(self, w: QWidget) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent): # real signature unknown; restored from __doc__
        pass


