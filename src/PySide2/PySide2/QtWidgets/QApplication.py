# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QApplication(__PySide2_QtGui.QGuiApplication):
    """
    QApplication(self) -> None
    QApplication(self, arg__1: typing.Sequence[str]) -> None
    """
    def aboutQt(self): # real signature unknown; restored from __doc__
        """ aboutQt() -> None """
        pass

    def activeModalWidget(self): # real signature unknown; restored from __doc__
        """ activeModalWidget() -> PySide2.QtWidgets.QWidget """
        pass

    def activePopupWidget(self): # real signature unknown; restored from __doc__
        """ activePopupWidget() -> PySide2.QtWidgets.QWidget """
        pass

    def activeWindow(self): # real signature unknown; restored from __doc__
        """ activeWindow() -> PySide2.QtWidgets.QWidget """
        pass

    def alert(self, widget, duration=0): # real signature unknown; restored from __doc__
        """ alert(widget: PySide2.QtWidgets.QWidget, duration: int = 0) -> None """
        pass

    def allWidgets(self): # real signature unknown; restored from __doc__
        """ allWidgets() -> typing.List[PySide2.QtWidgets.QWidget] """
        pass

    def autoSipEnabled(self): # real signature unknown; restored from __doc__
        """ autoSipEnabled(self) -> bool """
        return False

    def beep(self): # real signature unknown; restored from __doc__
        """ beep() -> None """
        pass

    def closeAllWindows(self): # real signature unknown; restored from __doc__
        """ closeAllWindows() -> None """
        pass

    def colorSpec(self): # real signature unknown; restored from __doc__
        """ colorSpec() -> int """
        return 0

    def cursorFlashTime(self): # real signature unknown; restored from __doc__
        """ cursorFlashTime() -> int """
        return 0

    def desktop(self): # real signature unknown; restored from __doc__
        """ desktop() -> PySide2.QtWidgets.QDesktopWidget """
        pass

    def doubleClickInterval(self): # real signature unknown; restored from __doc__
        """ doubleClickInterval() -> int """
        return 0

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def focusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def focusWidget(self): # real signature unknown; restored from __doc__
        """ focusWidget() -> PySide2.QtWidgets.QWidget """
        pass

    def font(self): # real signature unknown; restored from __doc__
        """
        font() -> PySide2.QtGui.QFont
        font(arg__1: PySide2.QtWidgets.QWidget) -> PySide2.QtGui.QFont
        font(className: bytes) -> PySide2.QtGui.QFont
        """
        pass

    def fontMetrics(self): # real signature unknown; restored from __doc__
        """ fontMetrics() -> PySide2.QtGui.QFontMetrics """
        pass

    def globalStrut(self): # real signature unknown; restored from __doc__
        """ globalStrut() -> PySide2.QtCore.QSize """
        pass

    def isEffectEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ isEffectEnabled(arg__1: PySide2.QtCore.Qt.UIEffect) -> bool """
        return False

    def keyboardInputInterval(self): # real signature unknown; restored from __doc__
        """ keyboardInputInterval() -> int """
        return 0

    def notify(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ notify(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def palette(self): # real signature unknown; restored from __doc__
        """
        palette() -> PySide2.QtGui.QPalette
        palette(arg__1: PySide2.QtWidgets.QWidget) -> PySide2.QtGui.QPalette
        palette(className: bytes) -> PySide2.QtGui.QPalette
        """
        pass

    def setActiveWindow(self, act): # real signature unknown; restored from __doc__
        """ setActiveWindow(act: PySide2.QtWidgets.QWidget) -> None """
        pass

    def setAutoSipEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoSipEnabled(self, enabled: bool) -> None """
        pass

    def setColorSpec(self, arg__1): # real signature unknown; restored from __doc__
        """ setColorSpec(arg__1: int) -> None """
        pass

    def setCursorFlashTime(self, arg__1): # real signature unknown; restored from __doc__
        """ setCursorFlashTime(arg__1: int) -> None """
        pass

    def setDoubleClickInterval(self, arg__1): # real signature unknown; restored from __doc__
        """ setDoubleClickInterval(arg__1: int) -> None """
        pass

    def setEffectEnabled(self, arg__1, enable=True): # real signature unknown; restored from __doc__
        """ setEffectEnabled(arg__1: PySide2.QtCore.Qt.UIEffect, enable: bool = True) -> None """
        pass

    def setFont(self, arg__1): # real signature unknown; restored from __doc__
        """
        setFont(arg__1: PySide2.QtGui.QFont) -> None
        setFont(arg__1: PySide2.QtGui.QFont, className: typing.Optional[bytes] = None) -> None
        """
        pass

    def setGlobalStrut(self, arg__1): # real signature unknown; restored from __doc__
        """ setGlobalStrut(arg__1: PySide2.QtCore.QSize) -> None """
        pass

    def setKeyboardInputInterval(self, arg__1): # real signature unknown; restored from __doc__
        """ setKeyboardInputInterval(arg__1: int) -> None """
        pass

    def setPalette(self, arg__1, className, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        setPalette(arg__1: PySide2.QtGui.QPalette, className: typing.Optional[bytes] = None) -> None
        setPalette(pal: PySide2.QtGui.QPalette) -> None
        """
        pass

    def setStartDragDistance(self, l): # real signature unknown; restored from __doc__
        """ setStartDragDistance(l: int) -> None """
        pass

    def setStartDragTime(self, ms): # real signature unknown; restored from __doc__
        """ setStartDragTime(ms: int) -> None """
        pass

    def setStyle(self, arg__1): # real signature unknown; restored from __doc__
        """
        setStyle(arg__1: PySide2.QtWidgets.QStyle) -> None
        setStyle(arg__1: str) -> PySide2.QtWidgets.QStyle
        """
        pass

    def setStyleSheet(self, sheet): # real signature unknown; restored from __doc__
        """ setStyleSheet(self, sheet: str) -> None """
        pass

    def setWheelScrollLines(self, arg__1): # real signature unknown; restored from __doc__
        """ setWheelScrollLines(arg__1: int) -> None """
        pass

    def setWindowIcon(self, icon): # real signature unknown; restored from __doc__
        """ setWindowIcon(icon: PySide2.QtGui.QIcon) -> None """
        pass

    def startDragDistance(self): # real signature unknown; restored from __doc__
        """ startDragDistance() -> int """
        return 0

    def startDragTime(self): # real signature unknown; restored from __doc__
        """ startDragTime() -> int """
        return 0

    def style(self): # real signature unknown; restored from __doc__
        """ style() -> PySide2.QtWidgets.QStyle """
        pass

    def styleSheet(self): # real signature unknown; restored from __doc__
        """ styleSheet(self) -> str """
        return ""

    def topLevelAt(self, p): # real signature unknown; restored from __doc__
        """
        topLevelAt(p: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QWidget
        topLevelAt(x: int, y: int) -> PySide2.QtWidgets.QWidget
        """
        pass

    def topLevelWidgets(self): # real signature unknown; restored from __doc__
        """ topLevelWidgets() -> typing.List[PySide2.QtWidgets.QWidget] """
        pass

    def wheelScrollLines(self): # real signature unknown; restored from __doc__
        """ wheelScrollLines() -> int """
        return 0

    def widgetAt(self, p): # real signature unknown; restored from __doc__
        """
        widgetAt(p: PySide2.QtCore.QPoint) -> PySide2.QtWidgets.QWidget
        widgetAt(x: int, y: int) -> PySide2.QtWidgets.QWidget
        """
        pass

    def windowIcon(self): # real signature unknown; restored from __doc__
        """ windowIcon() -> PySide2.QtGui.QIcon """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ColorSpec = None # (!) real value is "<class 'PySide2.QtWidgets.QApplication.ColorSpec'>"
    CustomColor = PySide2.QtWidgets.QApplication.ColorSpec.CustomColor
    ManyColor = PySide2.QtWidgets.QApplication.ColorSpec.ManyColor
    NormalColor = PySide2.QtWidgets.QApplication.ColorSpec.NormalColor
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50873200>'


