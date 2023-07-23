# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QGuiApplication(__PySide2_QtCore.QCoreApplication):
    """
    QGuiApplication(self) -> None
    QGuiApplication(self, arg__1: typing.Sequence[str]) -> None
    """
    def allWindows(self): # real signature unknown; restored from __doc__
        """ allWindows() -> typing.List[PySide2.QtGui.QWindow] """
        pass

    def applicationDisplayName(self): # real signature unknown; restored from __doc__
        """ applicationDisplayName() -> str """
        return ""

    def applicationDisplayNameChanged(self, *args, **kwargs): # real signature unknown
        pass

    def applicationState(self): # real signature unknown; restored from __doc__
        """ applicationState() -> PySide2.QtCore.Qt.ApplicationState """
        pass

    def applicationStateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def changeOverrideCursor(self, arg__1): # real signature unknown; restored from __doc__
        """ changeOverrideCursor(arg__1: PySide2.QtGui.QCursor) -> None """
        pass

    def clipboard(self): # real signature unknown; restored from __doc__
        """ clipboard() -> PySide2.QtGui.QClipboard """
        pass

    def commitDataRequest(self, *args, **kwargs): # real signature unknown
        pass

    def desktopFileName(self): # real signature unknown; restored from __doc__
        """ desktopFileName() -> str """
        return ""

    def desktopSettingsAware(self): # real signature unknown; restored from __doc__
        """ desktopSettingsAware() -> bool """
        return False

    def devicePixelRatio(self): # real signature unknown; restored from __doc__
        """ devicePixelRatio(self) -> float """
        return 0.0

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_() -> int """
        return 0

    def focusObject(self): # real signature unknown; restored from __doc__
        """ focusObject() -> PySide2.QtCore.QObject """
        pass

    def focusObjectChanged(self, *args, **kwargs): # real signature unknown
        pass

    def focusWindow(self): # real signature unknown; restored from __doc__
        """ focusWindow() -> PySide2.QtGui.QWindow """
        pass

    def focusWindowChanged(self, *args, **kwargs): # real signature unknown
        pass

    def font(self): # real signature unknown; restored from __doc__
        """ font() -> PySide2.QtGui.QFont """
        pass

    def fontChanged(self, *args, **kwargs): # real signature unknown
        pass

    def fontDatabaseChanged(self, *args, **kwargs): # real signature unknown
        pass

    def highDpiScaleFactorRoundingPolicy(self): # real signature unknown; restored from __doc__
        """ highDpiScaleFactorRoundingPolicy() -> PySide2.QtCore.Qt.HighDpiScaleFactorRoundingPolicy """
        pass

    def inputMethod(self): # real signature unknown; restored from __doc__
        """ inputMethod() -> PySide2.QtGui.QInputMethod """
        pass

    def isFallbackSessionManagementEnabled(self): # real signature unknown; restored from __doc__
        """ isFallbackSessionManagementEnabled() -> bool """
        return False

    def isLeftToRight(self): # real signature unknown; restored from __doc__
        """ isLeftToRight() -> bool """
        return False

    def isRightToLeft(self): # real signature unknown; restored from __doc__
        """ isRightToLeft() -> bool """
        return False

    def isSavingSession(self): # real signature unknown; restored from __doc__
        """ isSavingSession(self) -> bool """
        return False

    def isSessionRestored(self): # real signature unknown; restored from __doc__
        """ isSessionRestored(self) -> bool """
        return False

    def keyboardModifiers(self): # real signature unknown; restored from __doc__
        """ keyboardModifiers() -> PySide2.QtCore.Qt.KeyboardModifiers """
        pass

    def lastWindowClosed(self, *args, **kwargs): # real signature unknown
        pass

    def layoutDirection(self): # real signature unknown; restored from __doc__
        """ layoutDirection() -> PySide2.QtCore.Qt.LayoutDirection """
        pass

    def layoutDirectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def modalWindow(self): # real signature unknown; restored from __doc__
        """ modalWindow() -> PySide2.QtGui.QWindow """
        pass

    def mouseButtons(self): # real signature unknown; restored from __doc__
        """ mouseButtons() -> PySide2.QtCore.Qt.MouseButtons """
        pass

    def notify(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ notify(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def overrideCursor(self): # real signature unknown; restored from __doc__
        """ overrideCursor() -> PySide2.QtGui.QCursor """
        pass

    def palette(self): # real signature unknown; restored from __doc__
        """ palette() -> PySide2.QtGui.QPalette """
        pass

    def paletteChanged(self, *args, **kwargs): # real signature unknown
        pass

    def platformName(self): # real signature unknown; restored from __doc__
        """ platformName() -> str """
        return ""

    def primaryScreen(self): # real signature unknown; restored from __doc__
        """ primaryScreen() -> PySide2.QtGui.QScreen """
        pass

    def primaryScreenChanged(self, *args, **kwargs): # real signature unknown
        pass

    def queryKeyboardModifiers(self): # real signature unknown; restored from __doc__
        """ queryKeyboardModifiers() -> PySide2.QtCore.Qt.KeyboardModifiers """
        pass

    def quitOnLastWindowClosed(self): # real signature unknown; restored from __doc__
        """ quitOnLastWindowClosed() -> bool """
        return False

    def restoreOverrideCursor(self): # real signature unknown; restored from __doc__
        """ restoreOverrideCursor() -> None """
        pass

    def saveStateRequest(self, *args, **kwargs): # real signature unknown
        pass

    def screenAdded(self, *args, **kwargs): # real signature unknown
        pass

    def screenAt(self, point): # real signature unknown; restored from __doc__
        """ screenAt(point: PySide2.QtCore.QPoint) -> PySide2.QtGui.QScreen """
        pass

    def screenRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def screens(self): # real signature unknown; restored from __doc__
        """ screens() -> typing.List[PySide2.QtGui.QScreen] """
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ sessionId(self) -> str """
        return ""

    def sessionKey(self): # real signature unknown; restored from __doc__
        """ sessionKey(self) -> str """
        return ""

    def setApplicationDisplayName(self, name): # real signature unknown; restored from __doc__
        """ setApplicationDisplayName(name: str) -> None """
        pass

    def setDesktopFileName(self, name): # real signature unknown; restored from __doc__
        """ setDesktopFileName(name: str) -> None """
        pass

    def setDesktopSettingsAware(self, on): # real signature unknown; restored from __doc__
        """ setDesktopSettingsAware(on: bool) -> None """
        pass

    def setFallbackSessionManagementEnabled(self, arg__1): # real signature unknown; restored from __doc__
        """ setFallbackSessionManagementEnabled(arg__1: bool) -> None """
        pass

    def setFont(self, arg__1): # real signature unknown; restored from __doc__
        """ setFont(arg__1: PySide2.QtGui.QFont) -> None """
        pass

    def setHighDpiScaleFactorRoundingPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setHighDpiScaleFactorRoundingPolicy(policy: PySide2.QtCore.Qt.HighDpiScaleFactorRoundingPolicy) -> None """
        pass

    def setLayoutDirection(self, direction): # real signature unknown; restored from __doc__
        """ setLayoutDirection(direction: PySide2.QtCore.Qt.LayoutDirection) -> None """
        pass

    def setOverrideCursor(self, arg__1): # real signature unknown; restored from __doc__
        """ setOverrideCursor(arg__1: PySide2.QtGui.QCursor) -> None """
        pass

    def setPalette(self, pal): # real signature unknown; restored from __doc__
        """ setPalette(pal: PySide2.QtGui.QPalette) -> None """
        pass

    def setQuitOnLastWindowClosed(self, quit): # real signature unknown; restored from __doc__
        """ setQuitOnLastWindowClosed(quit: bool) -> None """
        pass

    def setWindowIcon(self, icon): # real signature unknown; restored from __doc__
        """ setWindowIcon(icon: PySide2.QtGui.QIcon) -> None """
        pass

    def styleHints(self): # real signature unknown; restored from __doc__
        """ styleHints() -> PySide2.QtGui.QStyleHints """
        pass

    def sync(self): # real signature unknown; restored from __doc__
        """ sync() -> None """
        pass

    def topLevelAt(self, pos): # real signature unknown; restored from __doc__
        """ topLevelAt(pos: PySide2.QtCore.QPoint) -> PySide2.QtGui.QWindow """
        pass

    def topLevelWindows(self): # real signature unknown; restored from __doc__
        """ topLevelWindows() -> typing.List[PySide2.QtGui.QWindow] """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00870300>'


