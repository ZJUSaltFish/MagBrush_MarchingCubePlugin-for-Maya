# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QEvent(__Shiboken.Object):
    """
    QEvent(self, other: PySide2.QtCore.QEvent) -> None
    QEvent(self, type: PySide2.QtCore.QEvent.Type) -> None
    """
    def accept(self): # real signature unknown; restored from __doc__
        """ accept(self) -> None """
        pass

    def ignore(self): # real signature unknown; restored from __doc__
        """ ignore(self) -> None """
        pass

    def isAccepted(self): # real signature unknown; restored from __doc__
        """ isAccepted(self) -> bool """
        return False

    def registerEventType(self, hint=-1): # real signature unknown; restored from __doc__
        """ registerEventType(hint: int = -1) -> int """
        return 0

    def setAccepted(self, accepted): # real signature unknown; restored from __doc__
        """ setAccepted(self, accepted: bool) -> None """
        pass

    def spontaneous(self): # real signature unknown; restored from __doc__
        """ spontaneous(self) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtCore.QEvent.Type """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, other): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AcceptDropsChange = PySide2.QtCore.QEvent.Type.AcceptDropsChange
    ActionAdded = PySide2.QtCore.QEvent.Type.ActionAdded
    ActionChanged = PySide2.QtCore.QEvent.Type.ActionChanged
    ActionRemoved = PySide2.QtCore.QEvent.Type.ActionRemoved
    ActivateControl = PySide2.QtCore.QEvent.Type.ActivateControl
    ActivationChange = PySide2.QtCore.QEvent.Type.ActivationChange
    ApplicationActivate = PySide2.QtCore.QEvent.Type.ApplicationActivate
    ApplicationActivated = PySide2.QtCore.QEvent.Type.ApplicationActivated
    ApplicationDeactivate = PySide2.QtCore.QEvent.Type.ApplicationDeactivate
    ApplicationDeactivated = PySide2.QtCore.QEvent.Type.ApplicationDeactivated
    ApplicationFontChange = PySide2.QtCore.QEvent.Type.ApplicationFontChange
    ApplicationLayoutDirectionChange = PySide2.QtCore.QEvent.Type.ApplicationLayoutDirectionChange
    ApplicationPaletteChange = PySide2.QtCore.QEvent.Type.ApplicationPaletteChange
    ApplicationStateChange = PySide2.QtCore.QEvent.Type.ApplicationStateChange
    ApplicationWindowIconChange = PySide2.QtCore.QEvent.Type.ApplicationWindowIconChange
    ChildAdded = PySide2.QtCore.QEvent.Type.ChildAdded
    ChildPolished = PySide2.QtCore.QEvent.Type.ChildPolished
    ChildRemoved = PySide2.QtCore.QEvent.Type.ChildRemoved
    Clipboard = PySide2.QtCore.QEvent.Type.Clipboard
    Close = PySide2.QtCore.QEvent.Type.Close
    CloseSoftwareInputPanel = PySide2.QtCore.QEvent.Type.CloseSoftwareInputPanel
    ContentsRectChange = PySide2.QtCore.QEvent.Type.ContentsRectChange
    ContextMenu = PySide2.QtCore.QEvent.Type.ContextMenu
    Create = PySide2.QtCore.QEvent.Type.Create
    CursorChange = PySide2.QtCore.QEvent.Type.CursorChange
    DeactivateControl = PySide2.QtCore.QEvent.Type.DeactivateControl
    DeferredDelete = PySide2.QtCore.QEvent.Type.DeferredDelete
    Destroy = PySide2.QtCore.QEvent.Type.Destroy
    DragEnter = PySide2.QtCore.QEvent.Type.DragEnter
    DragLeave = PySide2.QtCore.QEvent.Type.DragLeave
    DragMove = PySide2.QtCore.QEvent.Type.DragMove
    DragResponse = PySide2.QtCore.QEvent.Type.DragResponse
    Drop = PySide2.QtCore.QEvent.Type.Drop
    DynamicPropertyChange = PySide2.QtCore.QEvent.Type.DynamicPropertyChange
    EmbeddingControl = PySide2.QtCore.QEvent.Type.EmbeddingControl
    EnabledChange = PySide2.QtCore.QEvent.Type.EnabledChange
    Enter = PySide2.QtCore.QEvent.Type.Enter
    EnterWhatsThisMode = PySide2.QtCore.QEvent.Type.EnterWhatsThisMode
    Expose = PySide2.QtCore.QEvent.Type.Expose
    FileOpen = PySide2.QtCore.QEvent.Type.FileOpen
    FocusAboutToChange = PySide2.QtCore.QEvent.Type.FocusAboutToChange
    FocusIn = PySide2.QtCore.QEvent.Type.FocusIn
    FocusOut = PySide2.QtCore.QEvent.Type.FocusOut
    FontChange = PySide2.QtCore.QEvent.Type.FontChange
    FutureCallOut = PySide2.QtCore.QEvent.Type.FutureCallOut
    Gesture = PySide2.QtCore.QEvent.Type.Gesture
    GestureOverride = PySide2.QtCore.QEvent.Type.GestureOverride
    GrabKeyboard = PySide2.QtCore.QEvent.Type.GrabKeyboard
    GrabMouse = PySide2.QtCore.QEvent.Type.GrabMouse
    GraphicsSceneContextMenu = PySide2.QtCore.QEvent.Type.GraphicsSceneContextMenu
    GraphicsSceneDragEnter = PySide2.QtCore.QEvent.Type.GraphicsSceneDragEnter
    GraphicsSceneDragLeave = PySide2.QtCore.QEvent.Type.GraphicsSceneDragLeave
    GraphicsSceneDragMove = PySide2.QtCore.QEvent.Type.GraphicsSceneDragMove
    GraphicsSceneDrop = PySide2.QtCore.QEvent.Type.GraphicsSceneDrop
    GraphicsSceneHelp = PySide2.QtCore.QEvent.Type.GraphicsSceneHelp
    GraphicsSceneHoverEnter = PySide2.QtCore.QEvent.Type.GraphicsSceneHoverEnter
    GraphicsSceneHoverLeave = PySide2.QtCore.QEvent.Type.GraphicsSceneHoverLeave
    GraphicsSceneHoverMove = PySide2.QtCore.QEvent.Type.GraphicsSceneHoverMove
    GraphicsSceneMouseDoubleClick = PySide2.QtCore.QEvent.Type.GraphicsSceneMouseDoubleClick
    GraphicsSceneMouseMove = PySide2.QtCore.QEvent.Type.GraphicsSceneMouseMove
    GraphicsSceneMousePress = PySide2.QtCore.QEvent.Type.GraphicsSceneMousePress
    GraphicsSceneMouseRelease = PySide2.QtCore.QEvent.Type.GraphicsSceneMouseRelease
    GraphicsSceneMove = PySide2.QtCore.QEvent.Type.GraphicsSceneMove
    GraphicsSceneResize = PySide2.QtCore.QEvent.Type.GraphicsSceneResize
    GraphicsSceneWheel = PySide2.QtCore.QEvent.Type.GraphicsSceneWheel
    HelpRequest = PySide2.QtCore.QEvent.Type.HelpRequest
    Hide = PySide2.QtCore.QEvent.Type.Hide
    HideToParent = PySide2.QtCore.QEvent.Type.HideToParent
    HoverEnter = PySide2.QtCore.QEvent.Type.HoverEnter
    HoverLeave = PySide2.QtCore.QEvent.Type.HoverLeave
    HoverMove = PySide2.QtCore.QEvent.Type.HoverMove
    IconDrag = PySide2.QtCore.QEvent.Type.IconDrag
    IconTextChange = PySide2.QtCore.QEvent.Type.IconTextChange
    InputMethod = PySide2.QtCore.QEvent.Type.InputMethod
    InputMethodQuery = PySide2.QtCore.QEvent.Type.InputMethodQuery
    KeyboardLayoutChange = PySide2.QtCore.QEvent.Type.KeyboardLayoutChange
    KeyPress = PySide2.QtCore.QEvent.Type.KeyPress
    KeyRelease = PySide2.QtCore.QEvent.Type.KeyRelease
    LanguageChange = PySide2.QtCore.QEvent.Type.LanguageChange
    LayoutDirectionChange = PySide2.QtCore.QEvent.Type.LayoutDirectionChange
    LayoutRequest = PySide2.QtCore.QEvent.Type.LayoutRequest
    Leave = PySide2.QtCore.QEvent.Type.Leave
    LeaveWhatsThisMode = PySide2.QtCore.QEvent.Type.LeaveWhatsThisMode
    LocaleChange = PySide2.QtCore.QEvent.Type.LocaleChange
    MacGLClearDrawable = PySide2.QtCore.QEvent.Type.MacGLClearDrawable
    MacGLWindowChange = PySide2.QtCore.QEvent.Type.MacGLWindowChange
    MacSizeChange = PySide2.QtCore.QEvent.Type.MacSizeChange
    MaxUser = PySide2.QtCore.QEvent.Type.MaxUser
    MetaCall = PySide2.QtCore.QEvent.Type.MetaCall
    ModifiedChange = PySide2.QtCore.QEvent.Type.ModifiedChange
    MouseButtonDblClick = PySide2.QtCore.QEvent.Type.MouseButtonDblClick
    MouseButtonPress = PySide2.QtCore.QEvent.Type.MouseButtonPress
    MouseButtonRelease = PySide2.QtCore.QEvent.Type.MouseButtonRelease
    MouseMove = PySide2.QtCore.QEvent.Type.MouseMove
    MouseTrackingChange = PySide2.QtCore.QEvent.Type.MouseTrackingChange
    Move = PySide2.QtCore.QEvent.Type.Move
    NativeGesture = PySide2.QtCore.QEvent.Type.NativeGesture
    NetworkReplyUpdated = PySide2.QtCore.QEvent.Type.NetworkReplyUpdated
    NonClientAreaMouseButtonDblClick = PySide2.QtCore.QEvent.Type.NonClientAreaMouseButtonDblClick
    NonClientAreaMouseButtonPress = PySide2.QtCore.QEvent.Type.NonClientAreaMouseButtonPress
    NonClientAreaMouseButtonRelease = PySide2.QtCore.QEvent.Type.NonClientAreaMouseButtonRelease
    NonClientAreaMouseMove = PySide2.QtCore.QEvent.Type.NonClientAreaMouseMove
    None_ = PySide2.QtCore.QEvent.Type.None_
    OkRequest = PySide2.QtCore.QEvent.Type.OkRequest
    OrientationChange = PySide2.QtCore.QEvent.Type.OrientationChange
    Paint = PySide2.QtCore.QEvent.Type.Paint
    PaletteChange = PySide2.QtCore.QEvent.Type.PaletteChange
    ParentAboutToChange = PySide2.QtCore.QEvent.Type.ParentAboutToChange
    ParentChange = PySide2.QtCore.QEvent.Type.ParentChange
    PlatformPanel = PySide2.QtCore.QEvent.Type.PlatformPanel
    PlatformSurface = PySide2.QtCore.QEvent.Type.PlatformSurface
    Pointer = PySide2.QtCore.QEvent.Type.Pointer
    Polish = PySide2.QtCore.QEvent.Type.Polish
    PolishRequest = PySide2.QtCore.QEvent.Type.PolishRequest
    QueryWhatsThis = PySide2.QtCore.QEvent.Type.QueryWhatsThis
    Quit = PySide2.QtCore.QEvent.Type.Quit
    ReadOnlyChange = PySide2.QtCore.QEvent.Type.ReadOnlyChange
    RequestSoftwareInputPanel = PySide2.QtCore.QEvent.Type.RequestSoftwareInputPanel
    Resize = PySide2.QtCore.QEvent.Type.Resize
    ScreenChangeInternal = PySide2.QtCore.QEvent.Type.ScreenChangeInternal
    Scroll = PySide2.QtCore.QEvent.Type.Scroll
    ScrollPrepare = PySide2.QtCore.QEvent.Type.ScrollPrepare
    Shortcut = PySide2.QtCore.QEvent.Type.Shortcut
    ShortcutOverride = PySide2.QtCore.QEvent.Type.ShortcutOverride
    Show = PySide2.QtCore.QEvent.Type.Show
    ShowToParent = PySide2.QtCore.QEvent.Type.ShowToParent
    ShowWindowRequest = PySide2.QtCore.QEvent.Type.ShowWindowRequest
    SockAct = PySide2.QtCore.QEvent.Type.SockAct
    SockClose = PySide2.QtCore.QEvent.Type.SockClose
    Speech = PySide2.QtCore.QEvent.Type.Speech
    StateMachineSignal = PySide2.QtCore.QEvent.Type.StateMachineSignal
    StateMachineWrapped = PySide2.QtCore.QEvent.Type.StateMachineWrapped
    StatusTip = PySide2.QtCore.QEvent.Type.StatusTip
    Style = PySide2.QtCore.QEvent.Type.Style
    StyleAnimationUpdate = PySide2.QtCore.QEvent.Type.StyleAnimationUpdate
    StyleChange = PySide2.QtCore.QEvent.Type.StyleChange
    TabletEnterProximity = PySide2.QtCore.QEvent.Type.TabletEnterProximity
    TabletLeaveProximity = PySide2.QtCore.QEvent.Type.TabletLeaveProximity
    TabletMove = PySide2.QtCore.QEvent.Type.TabletMove
    TabletPress = PySide2.QtCore.QEvent.Type.TabletPress
    TabletRelease = PySide2.QtCore.QEvent.Type.TabletRelease
    TabletTrackingChange = PySide2.QtCore.QEvent.Type.TabletTrackingChange
    ThemeChange = PySide2.QtCore.QEvent.Type.ThemeChange
    ThreadChange = PySide2.QtCore.QEvent.Type.ThreadChange
    Timer = PySide2.QtCore.QEvent.Type.Timer
    ToolBarChange = PySide2.QtCore.QEvent.Type.ToolBarChange
    ToolTip = PySide2.QtCore.QEvent.Type.ToolTip
    ToolTipChange = PySide2.QtCore.QEvent.Type.ToolTipChange
    TouchBegin = PySide2.QtCore.QEvent.Type.TouchBegin
    TouchCancel = PySide2.QtCore.QEvent.Type.TouchCancel
    TouchEnd = PySide2.QtCore.QEvent.Type.TouchEnd
    TouchUpdate = PySide2.QtCore.QEvent.Type.TouchUpdate
    Type = None # (!) real value is "<class 'PySide2.QtCore.QEvent.Type'>"
    UngrabKeyboard = PySide2.QtCore.QEvent.Type.UngrabKeyboard
    UngrabMouse = PySide2.QtCore.QEvent.Type.UngrabMouse
    UpdateLater = PySide2.QtCore.QEvent.Type.UpdateLater
    UpdateRequest = PySide2.QtCore.QEvent.Type.UpdateRequest
    User = PySide2.QtCore.QEvent.Type.User
    WhatsThis = PySide2.QtCore.QEvent.Type.WhatsThis
    WhatsThisClicked = PySide2.QtCore.QEvent.Type.WhatsThisClicked
    Wheel = PySide2.QtCore.QEvent.Type.Wheel
    WindowActivate = PySide2.QtCore.QEvent.Type.WindowActivate
    WindowBlocked = PySide2.QtCore.QEvent.Type.WindowBlocked
    WindowChangeInternal = PySide2.QtCore.QEvent.Type.WindowChangeInternal
    WindowDeactivate = PySide2.QtCore.QEvent.Type.WindowDeactivate
    WindowIconChange = PySide2.QtCore.QEvent.Type.WindowIconChange
    WindowStateChange = PySide2.QtCore.QEvent.Type.WindowStateChange
    WindowTitleChange = PySide2.QtCore.QEvent.Type.WindowTitleChange
    WindowUnblocked = PySide2.QtCore.QEvent.Type.WindowUnblocked
    WinEventAct = PySide2.QtCore.QEvent.Type.WinEventAct
    WinIdChange = PySide2.QtCore.QEvent.Type.WinIdChange
    ZeroTimerEvent = PySide2.QtCore.QEvent.Type.ZeroTimerEvent
    ZOrderChange = PySide2.QtCore.QEvent.Type.ZOrderChange


