# encoding: utf-8
# module PySide2.QtWinExtras
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWinExtras.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QtWin(__Shiboken.Object):
    # no doc
    def colorizationColor(self): # real signature unknown; restored from __doc__
        """ colorizationColor() -> typing.Tuple[PySide2.QtGui.QColor, bool] """
        pass

    def disableBlurBehindWindow(self, window): # real signature unknown; restored from __doc__
        """
        disableBlurBehindWindow(window: PySide2.QtGui.QWindow) -> None
        disableBlurBehindWindow(window: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def enableBlurBehindWindow(self, window): # real signature unknown; restored from __doc__
        """
        enableBlurBehindWindow(window: PySide2.QtGui.QWindow) -> None
        enableBlurBehindWindow(window: PySide2.QtGui.QWindow, region: PySide2.QtGui.QRegion) -> None
        enableBlurBehindWindow(window: PySide2.QtWidgets.QWidget) -> None
        enableBlurBehindWindow(window: PySide2.QtWidgets.QWidget, region: PySide2.QtGui.QRegion) -> None
        """
        pass

    def errorStringFromHresult(self, hresult): # real signature unknown; restored from __doc__
        """ errorStringFromHresult(hresult: int) -> str """
        return ""

    def extendFrameIntoClientArea(self, window, left, top, right, bottom): # real signature unknown; restored from __doc__
        """
        extendFrameIntoClientArea(window: PySide2.QtGui.QWindow, left: int, top: int, right: int, bottom: int) -> None
        extendFrameIntoClientArea(window: PySide2.QtGui.QWindow, margins: PySide2.QtCore.QMargins) -> None
        extendFrameIntoClientArea(window: PySide2.QtWidgets.QWidget, left: int, top: int, right: int, bottom: int) -> None
        extendFrameIntoClientArea(window: PySide2.QtWidgets.QWidget, margins: PySide2.QtCore.QMargins) -> None
        """
        pass

    def isCompositionEnabled(self): # real signature unknown; restored from __doc__
        """ isCompositionEnabled() -> bool """
        return False

    def isCompositionOpaque(self): # real signature unknown; restored from __doc__
        """ isCompositionOpaque() -> bool """
        return False

    def isWindowExcludedFromPeek(self, window): # real signature unknown; restored from __doc__
        """
        isWindowExcludedFromPeek(window: PySide2.QtGui.QWindow) -> bool
        isWindowExcludedFromPeek(window: PySide2.QtWidgets.QWidget) -> bool
        """
        return False

    def isWindowPeekDisallowed(self, window): # real signature unknown; restored from __doc__
        """
        isWindowPeekDisallowed(window: PySide2.QtGui.QWindow) -> bool
        isWindowPeekDisallowed(window: PySide2.QtWidgets.QWidget) -> bool
        """
        return False

    def markFullscreenWindow(self, arg__1, fullscreen=True): # real signature unknown; restored from __doc__
        """
        markFullscreenWindow(arg__1: PySide2.QtGui.QWindow, fullscreen: bool = True) -> None
        markFullscreenWindow(window: PySide2.QtWidgets.QWidget, fullscreen: bool = True) -> None
        """
        pass

    def realColorizationColor(self): # real signature unknown; restored from __doc__
        """ realColorizationColor() -> PySide2.QtGui.QColor """
        pass

    def resetExtendedFrame(self, window): # real signature unknown; restored from __doc__
        """
        resetExtendedFrame(window: PySide2.QtGui.QWindow) -> None
        resetExtendedFrame(window: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def setCompositionEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setCompositionEnabled(enabled: bool) -> None """
        pass

    def setCurrentProcessExplicitAppUserModelID(self, id): # real signature unknown; restored from __doc__
        """ setCurrentProcessExplicitAppUserModelID(id: str) -> None """
        pass

    def setWindowDisallowPeek(self, window, disallow): # real signature unknown; restored from __doc__
        """
        setWindowDisallowPeek(window: PySide2.QtGui.QWindow, disallow: bool) -> None
        setWindowDisallowPeek(window: PySide2.QtWidgets.QWidget, disallow: bool) -> None
        """
        pass

    def setWindowExcludedFromPeek(self, window, exclude): # real signature unknown; restored from __doc__
        """
        setWindowExcludedFromPeek(window: PySide2.QtGui.QWindow, exclude: bool) -> None
        setWindowExcludedFromPeek(window: PySide2.QtWidgets.QWidget, exclude: bool) -> None
        """
        pass

    def setWindowFlip3DPolicy(self, window, policy): # real signature unknown; restored from __doc__
        """
        setWindowFlip3DPolicy(window: PySide2.QtGui.QWindow, policy: PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy) -> None
        setWindowFlip3DPolicy(window: PySide2.QtWidgets.QWidget, policy: PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy) -> None
        """
        pass

    def stringFromHresult(self, hresult): # real signature unknown; restored from __doc__
        """ stringFromHresult(hresult: int) -> str """
        return ""

    def taskbarActivateTab(self, arg__1): # real signature unknown; restored from __doc__
        """
        taskbarActivateTab(arg__1: PySide2.QtGui.QWindow) -> None
        taskbarActivateTab(window: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def taskbarActivateTabAlt(self, arg__1): # real signature unknown; restored from __doc__
        """
        taskbarActivateTabAlt(arg__1: PySide2.QtGui.QWindow) -> None
        taskbarActivateTabAlt(window: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def taskbarAddTab(self, arg__1): # real signature unknown; restored from __doc__
        """
        taskbarAddTab(arg__1: PySide2.QtGui.QWindow) -> None
        taskbarAddTab(window: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def taskbarDeleteTab(self, arg__1): # real signature unknown; restored from __doc__
        """
        taskbarDeleteTab(arg__1: PySide2.QtGui.QWindow) -> None
        taskbarDeleteTab(window: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def windowFlip3DPolicy(self, arg__1): # real signature unknown; restored from __doc__
        """
        windowFlip3DPolicy(arg__1: PySide2.QtGui.QWindow) -> PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy
        windowFlip3DPolicy(window: PySide2.QtWidgets.QWidget) -> PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    FlipDefault = PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy.FlipDefault
    FlipExcludeAbove = PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy.FlipExcludeAbove
    FlipExcludeBelow = PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy.FlipExcludeBelow
    HBitmapAlpha = PySide2.QtWinExtras.QtWin.HBitmapFormat.HBitmapAlpha
    HBitmapFormat = None # (!) real value is "<class 'PySide2.QtWinExtras.QtWin.HBitmapFormat'>"
    HBitmapNoAlpha = PySide2.QtWinExtras.QtWin.HBitmapFormat.HBitmapNoAlpha
    HBitmapPremultipliedAlpha = PySide2.QtWinExtras.QtWin.HBitmapFormat.HBitmapPremultipliedAlpha
    WindowFlip3DPolicy = None # (!) real value is "<class 'PySide2.QtWinExtras.QtWin.WindowFlip3DPolicy'>"


class QWinEvent(__PySide2_QtCore.QEvent):
    """ QWinEvent(self, type: int) -> None """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    ColorizationChange = 65533
    CompositionChange = 65532
    TaskbarButtonCreated = 65531
    ThemeChange = 65530


class QWinColorizationChangeEvent(QWinEvent):
    """ QWinColorizationChangeEvent(self, color: int, opaque: bool) -> None """
    def color(self): # real signature unknown; restored from __doc__
        """ color(self) -> int """
        return 0

    def opaqueBlend(self): # real signature unknown; restored from __doc__
        """ opaqueBlend(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, color, opaque): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QWinCompositionChangeEvent(QWinEvent):
    """ QWinCompositionChangeEvent(self, enabled: bool) -> None """
    def isCompositionEnabled(self): # real signature unknown; restored from __doc__
        """ isCompositionEnabled(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, enabled): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QWinJumpList(__PySide2_QtCore.QObject):
    """ QWinJumpList(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addCategory(self, category): # real signature unknown; restored from __doc__
        """
        addCategory(self, category: PySide2.QtWinExtras.QWinJumpListCategory) -> None
        addCategory(self, title: str, items: typing.Sequence[PySide2.QtWinExtras.QWinJumpListItem] = []) -> PySide2.QtWinExtras.QWinJumpListCategory
        """
        pass

    def categories(self): # real signature unknown; restored from __doc__
        """ categories(self) -> typing.List[PySide2.QtWinExtras.QWinJumpListCategory] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def frequent(self): # real signature unknown; restored from __doc__
        """ frequent(self) -> PySide2.QtWinExtras.QWinJumpListCategory """
        pass

    def identifier(self): # real signature unknown; restored from __doc__
        """ identifier(self) -> str """
        return ""

    def recent(self): # real signature unknown; restored from __doc__
        """ recent(self) -> PySide2.QtWinExtras.QWinJumpListCategory """
        pass

    def setIdentifier(self, identifier): # real signature unknown; restored from __doc__
        """ setIdentifier(self, identifier: str) -> None """
        pass

    def tasks(self): # real signature unknown; restored from __doc__
        """ tasks(self) -> PySide2.QtWinExtras.QWinJumpListCategory """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000026C0D2DA9C0>'


class QWinJumpListCategory(__Shiboken.Object):
    """ QWinJumpListCategory(self, title: str = '') -> None """
    def addDestination(self, filePath): # real signature unknown; restored from __doc__
        """ addDestination(self, filePath: str) -> PySide2.QtWinExtras.QWinJumpListItem """
        pass

    def addItem(self, item): # real signature unknown; restored from __doc__
        """ addItem(self, item: PySide2.QtWinExtras.QWinJumpListItem) -> None """
        pass

    def addLink(self, icon, title, executablePath, arguments, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addLink(self, icon: PySide2.QtGui.QIcon, title: str, executablePath: str, arguments: typing.Sequence[str] = []) -> PySide2.QtWinExtras.QWinJumpListItem
        addLink(self, title: str, executablePath: str, arguments: typing.Sequence[str] = []) -> PySide2.QtWinExtras.QWinJumpListItem
        """
        pass

    def addSeparator(self): # real signature unknown; restored from __doc__
        """ addSeparator(self) -> PySide2.QtWinExtras.QWinJumpListItem """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def items(self): # real signature unknown; restored from __doc__
        """ items(self) -> typing.List[PySide2.QtWinExtras.QWinJumpListItem] """
        pass

    def setTitle(self, title): # real signature unknown; restored from __doc__
        """ setTitle(self, title: str) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtWinExtras.QWinJumpListCategory.Type """
        pass

    def __init__(self, title=''): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Custom = PySide2.QtWinExtras.QWinJumpListCategory.Type.Custom
    Frequent = PySide2.QtWinExtras.QWinJumpListCategory.Type.Frequent
    Recent = PySide2.QtWinExtras.QWinJumpListCategory.Type.Recent
    Tasks = PySide2.QtWinExtras.QWinJumpListCategory.Type.Tasks
    Type = None # (!) real value is "<class 'PySide2.QtWinExtras.QWinJumpListCategory.Type'>"


class QWinJumpListItem(__Shiboken.Object):
    """ QWinJumpListItem(self, type: PySide2.QtWinExtras.QWinJumpListItem.Type) -> None """
    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments(self) -> typing.List[str] """
        pass

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def filePath(self): # real signature unknown; restored from __doc__
        """ filePath(self) -> str """
        return ""

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def setArguments(self, arguments, p_str=None): # real signature unknown; restored from __doc__
        """ setArguments(self, arguments: typing.Sequence[str]) -> None """
        pass

    def setDescription(self, description): # real signature unknown; restored from __doc__
        """ setDescription(self, description: str) -> None """
        pass

    def setFilePath(self, filePath): # real signature unknown; restored from __doc__
        """ setFilePath(self, filePath: str) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setTitle(self, title): # real signature unknown; restored from __doc__
        """ setTitle(self, title: str) -> None """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: PySide2.QtWinExtras.QWinJumpListItem.Type) -> None """
        pass

    def setWorkingDirectory(self, workingDirectory): # real signature unknown; restored from __doc__
        """ setWorkingDirectory(self, workingDirectory: str) -> None """
        pass

    def title(self): # real signature unknown; restored from __doc__
        """ title(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtWinExtras.QWinJumpListItem.Type """
        pass

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ workingDirectory(self) -> str """
        return ""

    def __init__(self, type): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Destination = PySide2.QtWinExtras.QWinJumpListItem.Type.Destination
    Link = PySide2.QtWinExtras.QWinJumpListItem.Type.Link
    Separator = PySide2.QtWinExtras.QWinJumpListItem.Type.Separator
    Type = None # (!) real value is "<class 'PySide2.QtWinExtras.QWinJumpListItem.Type'>"


class QWinTaskbarButton(__PySide2_QtCore.QObject):
    """ QWinTaskbarButton(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def clearOverlayIcon(self): # real signature unknown; restored from __doc__
        """ clearOverlayIcon(self) -> None """
        pass

    def eventFilter(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ eventFilter(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtCore.QEvent) -> bool """
        return False

    def overlayAccessibleDescription(self): # real signature unknown; restored from __doc__
        """ overlayAccessibleDescription(self) -> str """
        return ""

    def overlayIcon(self): # real signature unknown; restored from __doc__
        """ overlayIcon(self) -> PySide2.QtGui.QIcon """
        pass

    def progress(self): # real signature unknown; restored from __doc__
        """ progress(self) -> PySide2.QtWinExtras.QWinTaskbarProgress """
        pass

    def setOverlayAccessibleDescription(self, description): # real signature unknown; restored from __doc__
        """ setOverlayAccessibleDescription(self, description: str) -> None """
        pass

    def setOverlayIcon(self, icon): # real signature unknown; restored from __doc__
        """ setOverlayIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setWindow(self, window): # real signature unknown; restored from __doc__
        """ setWindow(self, window: PySide2.QtGui.QWindow) -> None """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtGui.QWindow """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000026C0D2DA680>'


class QWinTaskbarProgress(__PySide2_QtCore.QObject):
    """ QWinTaskbarProgress(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) -> None """
        pass

    def isPaused(self): # real signature unknown; restored from __doc__
        """ isPaused(self) -> bool """
        return False

    def isStopped(self): # real signature unknown; restored from __doc__
        """ isStopped(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def maximum(self): # real signature unknown; restored from __doc__
        """ maximum(self) -> int """
        return 0

    def maximumChanged(self, *args, **kwargs): # real signature unknown
        pass

    def minimum(self): # real signature unknown; restored from __doc__
        """ minimum(self) -> int """
        return 0

    def minimumChanged(self, *args, **kwargs): # real signature unknown
        pass

    def pause(self): # real signature unknown; restored from __doc__
        """ pause(self) -> None """
        pass

    def pausedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def resume(self): # real signature unknown; restored from __doc__
        """ resume(self) -> None """
        pass

    def setMaximum(self, maximum): # real signature unknown; restored from __doc__
        """ setMaximum(self, maximum: int) -> None """
        pass

    def setMinimum(self, minimum): # real signature unknown; restored from __doc__
        """ setMinimum(self, minimum: int) -> None """
        pass

    def setPaused(self, paused): # real signature unknown; restored from __doc__
        """ setPaused(self, paused: bool) -> None """
        pass

    def setRange(self, minimum, maximum): # real signature unknown; restored from __doc__
        """ setRange(self, minimum: int, maximum: int) -> None """
        pass

    def setValue(self, value): # real signature unknown; restored from __doc__
        """ setValue(self, value: int) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) -> None """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def stoppedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> int """
        return 0

    def valueChanged(self, *args, **kwargs): # real signature unknown
        pass

    def visibilityChanged(self, *args, **kwargs): # real signature unknown
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000026C0D2DA540>'


class QWinThumbnailToolBar(__PySide2_QtCore.QObject):
    """ QWinThumbnailToolBar(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addButton(self, button): # real signature unknown; restored from __doc__
        """ addButton(self, button: PySide2.QtWinExtras.QWinThumbnailToolButton) -> None """
        pass

    def buttons(self): # real signature unknown; restored from __doc__
        """ buttons(self) -> typing.List[PySide2.QtWinExtras.QWinThumbnailToolButton] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def iconicLivePreviewPixmap(self): # real signature unknown; restored from __doc__
        """ iconicLivePreviewPixmap(self) -> PySide2.QtGui.QPixmap """
        pass

    def iconicLivePreviewPixmapRequested(self, *args, **kwargs): # real signature unknown
        pass

    def iconicPixmapNotificationsEnabled(self): # real signature unknown; restored from __doc__
        """ iconicPixmapNotificationsEnabled(self) -> bool """
        return False

    def iconicThumbnailPixmap(self): # real signature unknown; restored from __doc__
        """ iconicThumbnailPixmap(self) -> PySide2.QtGui.QPixmap """
        pass

    def iconicThumbnailPixmapRequested(self, *args, **kwargs): # real signature unknown
        pass

    def removeButton(self, button): # real signature unknown; restored from __doc__
        """ removeButton(self, button: PySide2.QtWinExtras.QWinThumbnailToolButton) -> None """
        pass

    def setButtons(self, buttons, PySide2_QtWinExtras_QWinThumbnailToolButton=None): # real signature unknown; restored from __doc__
        """ setButtons(self, buttons: typing.Sequence[PySide2.QtWinExtras.QWinThumbnailToolButton]) -> None """
        pass

    def setIconicLivePreviewPixmap(self, arg__1): # real signature unknown; restored from __doc__
        """ setIconicLivePreviewPixmap(self, arg__1: PySide2.QtGui.QPixmap) -> None """
        pass

    def setIconicPixmapNotificationsEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setIconicPixmapNotificationsEnabled(self, enabled: bool) -> None """
        pass

    def setIconicThumbnailPixmap(self, arg__1): # real signature unknown; restored from __doc__
        """ setIconicThumbnailPixmap(self, arg__1: PySide2.QtGui.QPixmap) -> None """
        pass

    def setWindow(self, window): # real signature unknown; restored from __doc__
        """ setWindow(self, window: PySide2.QtGui.QWindow) -> None """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtGui.QWindow """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000026C0D2DA340>'


class QWinThumbnailToolButton(__PySide2_QtCore.QObject):
    """ QWinThumbnailToolButton(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def click(self): # real signature unknown; restored from __doc__
        """ click(self) -> None """
        pass

    def clicked(self, *args, **kwargs): # real signature unknown
        pass

    def dismissOnClick(self): # real signature unknown; restored from __doc__
        """ dismissOnClick(self) -> bool """
        return False

    def icon(self): # real signature unknown; restored from __doc__
        """ icon(self) -> PySide2.QtGui.QIcon """
        pass

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def isFlat(self): # real signature unknown; restored from __doc__
        """ isFlat(self) -> bool """
        return False

    def isInteractive(self): # real signature unknown; restored from __doc__
        """ isInteractive(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def setDismissOnClick(self, dismiss): # real signature unknown; restored from __doc__
        """ setDismissOnClick(self, dismiss: bool) -> None """
        pass

    def setEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setEnabled(self, enabled: bool) -> None """
        pass

    def setFlat(self, flat): # real signature unknown; restored from __doc__
        """ setFlat(self, flat: bool) -> None """
        pass

    def setIcon(self, icon): # real signature unknown; restored from __doc__
        """ setIcon(self, icon: PySide2.QtGui.QIcon) -> None """
        pass

    def setInteractive(self, interactive): # real signature unknown; restored from __doc__
        """ setInteractive(self, interactive: bool) -> None """
        pass

    def setToolTip(self, toolTip): # real signature unknown; restored from __doc__
        """ setToolTip(self, toolTip: str) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def toolTip(self): # real signature unknown; restored from __doc__
        """ toolTip(self) -> str """
        return ""

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000026C0D2DA280>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026C0C3617B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtWinExtras', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026C0C3617B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtWinExtras.cp310-win_amd64.pyd')"

