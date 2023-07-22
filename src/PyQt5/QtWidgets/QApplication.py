# encoding: utf-8
# module PyQt5.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWidgets.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import sip as __sip


class QApplication(__PyQt5_QtGui.QGuiApplication):
    """ QApplication(argv: List[str]) """
    def aboutQt(self): # real signature unknown; restored from __doc__
        """ aboutQt() """
        pass

    def activeModalWidget(self): # real signature unknown; restored from __doc__
        """ activeModalWidget() -> QWidget """
        return QWidget

    def activePopupWidget(self): # real signature unknown; restored from __doc__
        """ activePopupWidget() -> QWidget """
        return QWidget

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ activeWindow() -> QWidget """
        return QWidget

    def alert(self, widget, msecs=0): # real signature unknown; restored from __doc__
        """ alert(widget: QWidget, msecs: int = 0) """
        pass

    def allWidgets(self): # real signature unknown; restored from __doc__
        """ allWidgets() -> List[QWidget] """
        return []

    def autoSipEnabled(self): # real signature unknown; restored from __doc__
        """ autoSipEnabled(self) -> bool """
        return False

    def beep(self): # real signature unknown; restored from __doc__
        """ beep() """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closeAllWindows(self): # real signature unknown; restored from __doc__
        """ closeAllWindows() """
        pass

    def colorSpec(self): # real signature unknown; restored from __doc__
        """ colorSpec() -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def cursorFlashTime(self): # real signature unknown; restored from __doc__
        """ cursorFlashTime() -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def desktop(self): # real signature unknown; restored from __doc__
        """ desktop() -> QDesktopWidget """
        return QDesktopWidget

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def doubleClickInterval(self): # real signature unknown; restored from __doc__
        """ doubleClickInterval() -> int """
        return 0

    def event(self, a0): # real signature unknown; restored from __doc__
        """ event(self, a0: QEvent) -> bool """
        return False

    def exec(self): # real signature unknown; restored from __doc__
        """ exec() -> int """
        return 0

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def focusChanged(self, *args, **kwargs): # real signature unknown
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

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget() -> QWidget """
        return QWidget

    def font(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        font() -> QFont
        font(a0: QWidget) -> QFont
        font(className: str) -> QFont
        """
        pass

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics() -> QFontMetrics """
        pass

    def globalStrut(self): # real signature unknown; restored from __doc__
        """ globalStrut() -> QSize """
        pass

    def isEffectEnabled(self, a0): # real signature unknown; restored from __doc__
        """ isEffectEnabled(a0: Qt.UIEffect) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keyboardInputInterval(self): # real signature unknown; restored from __doc__
        """ keyboardInputInterval() -> int """
        return 0

    def notify(self, a0, a1): # real signature unknown; restored from __doc__
        """ notify(self, a0: QObject, a1: QEvent) -> bool """
        return False

    def palette(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        palette() -> QPalette
        palette(a0: QWidget) -> QPalette
        palette(className: str) -> QPalette
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setActiveWindow(self, act): # real signature unknown; restored from __doc__
        """ setActiveWindow(act: QWidget) """
        pass

    def setAutoSipEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoSipEnabled(self, enabled: bool) """
        pass

    def setColorSpec(self, a0): # real signature unknown; restored from __doc__
        """ setColorSpec(a0: int) """
        pass

    def setCursorFlashTime(self, a0): # real signature unknown; restored from __doc__
        """ setCursorFlashTime(a0: int) """
        pass

    def setDoubleClickInterval(self, a0): # real signature unknown; restored from __doc__
        """ setDoubleClickInterval(a0: int) """
        pass

    def setEffectEnabled(self, a0, enabled=True): # real signature unknown; restored from __doc__
        """ setEffectEnabled(a0: Qt.UIEffect, enabled: bool = True) """
        pass

    def setFont(self, a0, className, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFont(a0: QFont, className: typing.Optional[str] = None) """
        pass

    def setGlobalStrut(self, a0): # real signature unknown; restored from __doc__
        """ setGlobalStrut(a0: QSize) """
        pass

    def setKeyboardInputInterval(self, a0): # real signature unknown; restored from __doc__
        """ setKeyboardInputInterval(a0: int) """
        pass

    def setPalette(self, a0, className, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setPalette(a0: QPalette, className: typing.Optional[str] = None) """
        pass

    def setStartDragDistance(self, l): # real signature unknown; restored from __doc__
        """ setStartDragDistance(l: int) """
        pass

    def setStartDragTime(self, ms): # real signature unknown; restored from __doc__
        """ setStartDragTime(ms: int) """
        pass

    def setStyle(self, a0): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setStyle(a0: QStyle)
        setStyle(a0: str) -> QStyle
        """
        return QStyle

    def setStyleSheet(self, sheet): # real signature unknown; restored from __doc__
        """ setStyleSheet(self, sheet: str) """
        pass

    def setWheelScrollLines(self, a0): # real signature unknown; restored from __doc__
        """ setWheelScrollLines(a0: int) """
        pass

    def setWindowIcon(self, icon): # real signature unknown; restored from __doc__
        """ setWindowIcon(icon: QIcon) """
        pass

    def startDragDistance(self): # real signature unknown; restored from __doc__
        """ startDragDistance() -> int """
        return 0

    def startDragTime(self): # real signature unknown; restored from __doc__
        """ startDragTime() -> int """
        return 0

    def style(self): # real signature unknown; restored from __doc__
        """ style() -> QStyle """
        return QStyle

    def styleSheet(self): # real signature unknown; restored from __doc__
        """ styleSheet(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def topLevelAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        topLevelAt(p: QPoint) -> QWidget
        topLevelAt(x: int, y: int) -> QWidget
        """
        return QWidget

    def topLevelWidgets(self): # real signature unknown; restored from __doc__
        """ topLevelWidgets() -> List[QWidget] """
        return []

    def wheelScrollLines(self): # real signature unknown; restored from __doc__
        """ wheelScrollLines() -> int """
        return 0

    def widgetAt(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        widgetAt(p: QPoint) -> QWidget
        widgetAt(x: int, y: int) -> QWidget
        """
        return QWidget

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ windowIcon() -> QIcon """
        pass

    def __init__(self, argv, p_str=None): # real signature unknown; restored from __doc__
        pass

    CustomColor = 1
    ManyColor = 2
    NormalColor = 0


