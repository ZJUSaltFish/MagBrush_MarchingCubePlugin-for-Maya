# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QSystemTrayIcon(__PyQt5_QtCore.QObject):
    """
    QSystemTrayIcon(parent: typing.Optional[QObject] = None)
    QSystemTrayIcon(icon: QIcon, parent: typing.Optional[QObject] = None)
    """
    def activated(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextMenu(self): # real signature unknown; restored from __doc__
        """ contextMenu(self) -> QMenu """
        return QMenu

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event: QEvent) -> bool """
        return False

    def geometry(self): # real signature unknown; restored from __doc__
        """ geometry(self) -> QRect """
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> QIcon """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSystemTrayAvailable(self): # real signature unknown; restored from __doc__
        """ isSystemTrayAvailable() -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def messageClicked(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setContextMenu(self, menu): # real signature unknown; restored from __doc__
        """ setContextMenu(self, menu: QMenu) """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: QIcon) """
        pass

    def setToolTip(self, tip): # real signature unknown; restored from __doc__
        """ setToolTip(self, tip: str) """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def showMessage(self, title, msg, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        showMessage(self, title: str, msg: str, icon: QSystemTrayIcon.MessageIcon = QSystemTrayIcon.Information, msecs: int = 10000)
        showMessage(self, title: str, msg: str, icon: QIcon, msecs: int = 10000)
        """
        pass

    def supportsMessages(self): # real signature unknown; restored from __doc__
        """ supportsMessages() -> bool """
        return False

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Context = 1
    Critical = 3
    DoubleClick = 2
    Information = 1
    MiddleClick = 4
    NoIcon = 0
    Trigger = 3
    Unknown = 0
    Warning = 2


