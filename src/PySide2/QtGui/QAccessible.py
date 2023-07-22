# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QAccessible(__Shiboken.Object):
    # no doc
    def accessibleInterface(self, uniqueId): # real signature unknown; restored from __doc__
        """ accessibleInterface(uniqueId: int) -> PySide2.QtGui.QAccessibleInterface """
        pass

    def cleanup(self): # real signature unknown; restored from __doc__
        """ cleanup() -> None """
        pass

    def deleteAccessibleInterface(self, uniqueId): # real signature unknown; restored from __doc__
        """ deleteAccessibleInterface(uniqueId: int) -> None """
        pass

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive() -> bool """
        return False

    def qAccessibleTextBoundaryHelper(self, cursor, boundaryType): # real signature unknown; restored from __doc__
        """ qAccessibleTextBoundaryHelper(cursor: PySide2.QtGui.QTextCursor, boundaryType: PySide2.QtGui.QAccessible.TextBoundaryType) -> typing.Tuple[int, int] """
        pass

    def queryAccessibleInterface(self, arg__1): # real signature unknown; restored from __doc__
        """ queryAccessibleInterface(arg__1: PySide2.QtCore.QObject) -> PySide2.QtGui.QAccessibleInterface """
        pass

    def registerAccessibleInterface(self, iface): # real signature unknown; restored from __doc__
        """ registerAccessibleInterface(iface: PySide2.QtGui.QAccessibleInterface) -> int """
        return 0

    def setActive(self, active): # real signature unknown; restored from __doc__
        """ setActive(active: bool) -> None """
        pass

    def setRootObject(self, p_object): # real signature unknown; restored from __doc__
        """ setRootObject(object: PySide2.QtCore.QObject) -> None """
        pass

    def uniqueId(self, iface): # real signature unknown; restored from __doc__
        """ uniqueId(iface: PySide2.QtGui.QAccessibleInterface) -> int """
        return 0

    def updateAccessibility(self, event): # real signature unknown; restored from __doc__
        """ updateAccessibility(event: PySide2.QtGui.QAccessibleEvent) -> None """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Accelerator = PySide2.QtGui.QAccessible.Text.Accelerator
    AcceleratorChanged = PySide2.QtGui.QAccessible.Event.AcceleratorChanged
    ActionChanged = PySide2.QtGui.QAccessible.Event.ActionChanged
    ActionInterface = PySide2.QtGui.QAccessible.InterfaceType.ActionInterface
    ActiveDescendantChanged = PySide2.QtGui.QAccessible.Event.ActiveDescendantChanged
    Alert = PySide2.QtGui.QAccessible.Event.Alert
    AlertMessage = PySide2.QtGui.QAccessible.Role.AlertMessage
    AllRelations = PySide2.QtGui.QAccessible.RelationFlag.AllRelations
    Animation = PySide2.QtGui.QAccessible.Role.Animation
    Application = PySide2.QtGui.QAccessible.Role.Application
    Assistant = PySide2.QtGui.QAccessible.Role.Assistant
    AttributeChanged = PySide2.QtGui.QAccessible.Event.AttributeChanged
    Border = PySide2.QtGui.QAccessible.Role.Border
    Button = PySide2.QtGui.QAccessible.Role.Button
    ButtonDropDown = PySide2.QtGui.QAccessible.Role.ButtonDropDown
    ButtonDropGrid = PySide2.QtGui.QAccessible.Role.ButtonDropGrid
    ButtonMenu = PySide2.QtGui.QAccessible.Role.ButtonMenu
    Canvas = PySide2.QtGui.QAccessible.Role.Canvas
    Caret = PySide2.QtGui.QAccessible.Role.Caret
    Cell = PySide2.QtGui.QAccessible.Role.Cell
    CharBoundary = PySide2.QtGui.QAccessible.TextBoundaryType.CharBoundary
    Chart = PySide2.QtGui.QAccessible.Role.Chart
    CheckBox = PySide2.QtGui.QAccessible.Role.CheckBox
    Client = PySide2.QtGui.QAccessible.Role.Client
    Clock = PySide2.QtGui.QAccessible.Role.Clock
    ColorChooser = PySide2.QtGui.QAccessible.Role.ColorChooser
    Column = PySide2.QtGui.QAccessible.Role.Column
    ColumnHeader = PySide2.QtGui.QAccessible.Role.ColumnHeader
    ComboBox = PySide2.QtGui.QAccessible.Role.ComboBox
    ComplementaryContent = PySide2.QtGui.QAccessible.Role.ComplementaryContent
    ContextHelpEnd = PySide2.QtGui.QAccessible.Event.ContextHelpEnd
    ContextHelpStart = PySide2.QtGui.QAccessible.Event.ContextHelpStart
    Controlled = PySide2.QtGui.QAccessible.RelationFlag.Controlled
    Controller = PySide2.QtGui.QAccessible.RelationFlag.Controller
    Cursor = PySide2.QtGui.QAccessible.Role.Cursor
    DebugDescription = PySide2.QtGui.QAccessible.Text.DebugDescription
    DefaultActionChanged = PySide2.QtGui.QAccessible.Event.DefaultActionChanged
    Description = PySide2.QtGui.QAccessible.Text.Description
    DescriptionChanged = PySide2.QtGui.QAccessible.Event.DescriptionChanged
    Desktop = PySide2.QtGui.QAccessible.Role.Desktop
    Dial = PySide2.QtGui.QAccessible.Role.Dial
    Dialog = PySide2.QtGui.QAccessible.Role.Dialog
    DialogEnd = PySide2.QtGui.QAccessible.Event.DialogEnd
    DialogStart = PySide2.QtGui.QAccessible.Event.DialogStart
    Document = PySide2.QtGui.QAccessible.Role.Document
    DocumentContentChanged = PySide2.QtGui.QAccessible.Event.DocumentContentChanged
    DocumentLoadComplete = PySide2.QtGui.QAccessible.Event.DocumentLoadComplete
    DocumentLoadStopped = PySide2.QtGui.QAccessible.Event.DocumentLoadStopped
    DocumentReload = PySide2.QtGui.QAccessible.Event.DocumentReload
    DragDropEnd = PySide2.QtGui.QAccessible.Event.DragDropEnd
    DragDropStart = PySide2.QtGui.QAccessible.Event.DragDropStart
    EditableText = PySide2.QtGui.QAccessible.Role.EditableText
    EditableTextInterface = PySide2.QtGui.QAccessible.InterfaceType.EditableTextInterface
    Equation = PySide2.QtGui.QAccessible.Role.Equation
    Event = None # (!) real value is "<class 'PySide2.QtGui.QAccessible.Event'>"
    Focus = PySide2.QtGui.QAccessible.Event.Focus
    Footer = PySide2.QtGui.QAccessible.Role.Footer
    ForegroundChanged = PySide2.QtGui.QAccessible.Event.ForegroundChanged
    Form = PySide2.QtGui.QAccessible.Role.Form
    Graphic = PySide2.QtGui.QAccessible.Role.Graphic
    Grip = PySide2.QtGui.QAccessible.Role.Grip
    Grouping = PySide2.QtGui.QAccessible.Role.Grouping
    Heading = PySide2.QtGui.QAccessible.Role.Heading
    Help = PySide2.QtGui.QAccessible.Text.Help
    HelpBalloon = PySide2.QtGui.QAccessible.Role.HelpBalloon
    HelpChanged = PySide2.QtGui.QAccessible.Event.HelpChanged
    HotkeyField = PySide2.QtGui.QAccessible.Role.HotkeyField
    HyperlinkEndIndexChanged = PySide2.QtGui.QAccessible.Event.HyperlinkEndIndexChanged
    HyperlinkNumberOfAnchorsChanged = PySide2.QtGui.QAccessible.Event.HyperlinkNumberOfAnchorsChanged
    HyperlinkSelectedLinkChanged = PySide2.QtGui.QAccessible.Event.HyperlinkSelectedLinkChanged
    HyperlinkStartIndexChanged = PySide2.QtGui.QAccessible.Event.HyperlinkStartIndexChanged
    HypertextChanged = PySide2.QtGui.QAccessible.Event.HypertextChanged
    HypertextLinkActivated = PySide2.QtGui.QAccessible.Event.HypertextLinkActivated
    HypertextLinkSelected = PySide2.QtGui.QAccessible.Event.HypertextLinkSelected
    HypertextNLinksChanged = PySide2.QtGui.QAccessible.Event.HypertextNLinksChanged
    ImageInterface = PySide2.QtGui.QAccessible.InterfaceType.ImageInterface
    Indicator = PySide2.QtGui.QAccessible.Role.Indicator
    InterfaceType = None # (!) real value is "<class 'PySide2.QtGui.QAccessible.InterfaceType'>"
    InvalidEvent = PySide2.QtGui.QAccessible.Event.InvalidEvent
    Label = PySide2.QtGui.QAccessible.RelationFlag.Label
    Labelled = PySide2.QtGui.QAccessible.RelationFlag.Labelled
    LayeredPane = PySide2.QtGui.QAccessible.Role.LayeredPane
    LineBoundary = PySide2.QtGui.QAccessible.TextBoundaryType.LineBoundary
    Link = PySide2.QtGui.QAccessible.Role.Link
    List = PySide2.QtGui.QAccessible.Role.List
    ListItem = PySide2.QtGui.QAccessible.Role.ListItem
    LocationChanged = PySide2.QtGui.QAccessible.Event.LocationChanged
    MenuBar = PySide2.QtGui.QAccessible.Role.MenuBar
    MenuCommand = PySide2.QtGui.QAccessible.Event.MenuCommand
    MenuEnd = PySide2.QtGui.QAccessible.Event.MenuEnd
    MenuItem = PySide2.QtGui.QAccessible.Role.MenuItem
    MenuStart = PySide2.QtGui.QAccessible.Event.MenuStart
    Name = PySide2.QtGui.QAccessible.Text.Name
    NameChanged = PySide2.QtGui.QAccessible.Event.NameChanged
    NoBoundary = PySide2.QtGui.QAccessible.TextBoundaryType.NoBoundary
    NoRole = PySide2.QtGui.QAccessible.Role.NoRole
    Note = PySide2.QtGui.QAccessible.Role.Note
    Notification = PySide2.QtGui.QAccessible.Role.Notification
    ObjectAttributeChanged = PySide2.QtGui.QAccessible.Event.ObjectAttributeChanged
    ObjectCreated = PySide2.QtGui.QAccessible.Event.ObjectCreated
    ObjectDestroyed = PySide2.QtGui.QAccessible.Event.ObjectDestroyed
    ObjectHide = PySide2.QtGui.QAccessible.Event.ObjectHide
    ObjectReorder = PySide2.QtGui.QAccessible.Event.ObjectReorder
    ObjectShow = PySide2.QtGui.QAccessible.Event.ObjectShow
    PageChanged = PySide2.QtGui.QAccessible.Event.PageChanged
    PageTab = PySide2.QtGui.QAccessible.Role.PageTab
    PageTabList = PySide2.QtGui.QAccessible.Role.PageTabList
    Pane = PySide2.QtGui.QAccessible.Role.Pane
    Paragraph = PySide2.QtGui.QAccessible.Role.Paragraph
    ParagraphBoundary = PySide2.QtGui.QAccessible.TextBoundaryType.ParagraphBoundary
    ParentChanged = PySide2.QtGui.QAccessible.Event.ParentChanged
    PopupMenu = PySide2.QtGui.QAccessible.Role.PopupMenu
    PopupMenuEnd = PySide2.QtGui.QAccessible.Event.PopupMenuEnd
    PopupMenuStart = PySide2.QtGui.QAccessible.Event.PopupMenuStart
    ProgressBar = PySide2.QtGui.QAccessible.Role.ProgressBar
    PropertyPage = PySide2.QtGui.QAccessible.Role.PropertyPage
    PushButton = PySide2.QtGui.QAccessible.Role.PushButton
    RadioButton = PySide2.QtGui.QAccessible.Role.RadioButton
    Relation = None # (!) real value is "<class 'PySide2.QtGui.QAccessible.Relation'>"
    RelationFlag = None # (!) real value is "<class 'PySide2.QtGui.QAccessible.RelationFlag'>"
    Role = None # (!) real value is "<class 'PySide2.QtGui.QAccessible.Role'>"
    Row = PySide2.QtGui.QAccessible.Role.Row
    RowHeader = PySide2.QtGui.QAccessible.Role.RowHeader
    ScrollBar = PySide2.QtGui.QAccessible.Role.ScrollBar
    ScrollingEnd = PySide2.QtGui.QAccessible.Event.ScrollingEnd
    ScrollingStart = PySide2.QtGui.QAccessible.Event.ScrollingStart
    Section = PySide2.QtGui.QAccessible.Role.Section
    SectionChanged = PySide2.QtGui.QAccessible.Event.SectionChanged
    Selection = PySide2.QtGui.QAccessible.Event.Selection
    SelectionAdd = PySide2.QtGui.QAccessible.Event.SelectionAdd
    SelectionRemove = PySide2.QtGui.QAccessible.Event.SelectionRemove
    SelectionWithin = PySide2.QtGui.QAccessible.Event.SelectionWithin
    SentenceBoundary = PySide2.QtGui.QAccessible.TextBoundaryType.SentenceBoundary
    Separator = PySide2.QtGui.QAccessible.Role.Separator
    Slider = PySide2.QtGui.QAccessible.Role.Slider
    Sound = PySide2.QtGui.QAccessible.Role.Sound
    SoundPlayed = PySide2.QtGui.QAccessible.Event.SoundPlayed
    SpinBox = PySide2.QtGui.QAccessible.Role.SpinBox
    Splitter = PySide2.QtGui.QAccessible.Role.Splitter
    State = None # (!) real value is "<class 'PySide2.QtGui.QAccessible.State'>"
    StateChanged = PySide2.QtGui.QAccessible.Event.StateChanged
    StaticText = PySide2.QtGui.QAccessible.Role.StaticText
    StatusBar = PySide2.QtGui.QAccessible.Role.StatusBar
    Table = PySide2.QtGui.QAccessible.Role.Table
    TableCaptionChanged = PySide2.QtGui.QAccessible.Event.TableCaptionChanged
    TableCellInterface = PySide2.QtGui.QAccessible.InterfaceType.TableCellInterface
    TableColumnDescriptionChanged = PySide2.QtGui.QAccessible.Event.TableColumnDescriptionChanged
    TableColumnHeaderChanged = PySide2.QtGui.QAccessible.Event.TableColumnHeaderChanged
    TableInterface = PySide2.QtGui.QAccessible.InterfaceType.TableInterface
    TableModelChanged = PySide2.QtGui.QAccessible.Event.TableModelChanged
    TableRowDescriptionChanged = PySide2.QtGui.QAccessible.Event.TableRowDescriptionChanged
    TableRowHeaderChanged = PySide2.QtGui.QAccessible.Event.TableRowHeaderChanged
    TableSummaryChanged = PySide2.QtGui.QAccessible.Event.TableSummaryChanged
    Terminal = PySide2.QtGui.QAccessible.Role.Terminal
    Text = None # (!) real value is "<class 'PySide2.QtGui.QAccessible.Text'>"
    TextAttributeChanged = PySide2.QtGui.QAccessible.Event.TextAttributeChanged
    TextBoundaryType = None # (!) real value is "<class 'PySide2.QtGui.QAccessible.TextBoundaryType'>"
    TextCaretMoved = PySide2.QtGui.QAccessible.Event.TextCaretMoved
    TextColumnChanged = PySide2.QtGui.QAccessible.Event.TextColumnChanged
    TextInserted = PySide2.QtGui.QAccessible.Event.TextInserted
    TextInterface = PySide2.QtGui.QAccessible.InterfaceType.TextInterface
    TextRemoved = PySide2.QtGui.QAccessible.Event.TextRemoved
    TextSelectionChanged = PySide2.QtGui.QAccessible.Event.TextSelectionChanged
    TextUpdated = PySide2.QtGui.QAccessible.Event.TextUpdated
    TitleBar = PySide2.QtGui.QAccessible.Role.TitleBar
    ToolBar = PySide2.QtGui.QAccessible.Role.ToolBar
    ToolTip = PySide2.QtGui.QAccessible.Role.ToolTip
    Tree = PySide2.QtGui.QAccessible.Role.Tree
    TreeItem = PySide2.QtGui.QAccessible.Role.TreeItem
    UserRole = PySide2.QtGui.QAccessible.Role.UserRole
    UserText = PySide2.QtGui.QAccessible.Text.UserText
    Value = PySide2.QtGui.QAccessible.Text.Value
    ValueChanged = PySide2.QtGui.QAccessible.Event.ValueChanged
    ValueInterface = PySide2.QtGui.QAccessible.InterfaceType.ValueInterface
    VisibleDataChanged = PySide2.QtGui.QAccessible.Event.VisibleDataChanged
    WebDocument = PySide2.QtGui.QAccessible.Role.WebDocument
    Whitespace = PySide2.QtGui.QAccessible.Role.Whitespace
    Window = PySide2.QtGui.QAccessible.Role.Window
    WordBoundary = PySide2.QtGui.QAccessible.TextBoundaryType.WordBoundary


