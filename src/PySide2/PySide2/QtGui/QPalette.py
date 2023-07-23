# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QPalette(__Shiboken.Object):
    """
    QPalette(self) -> None
    QPalette(self, button: PySide2.QtCore.Qt.GlobalColor) -> None
    QPalette(self, button: PySide2.QtGui.QColor) -> None
    QPalette(self, button: PySide2.QtGui.QColor, window: PySide2.QtGui.QColor) -> None
    QPalette(self, palette: PySide2.QtGui.QPalette) -> None
    QPalette(self, windowText: PySide2.QtGui.QBrush, button: PySide2.QtGui.QBrush, light: PySide2.QtGui.QBrush, dark: PySide2.QtGui.QBrush, mid: PySide2.QtGui.QBrush, text: PySide2.QtGui.QBrush, bright_text: PySide2.QtGui.QBrush, base: PySide2.QtGui.QBrush, window: PySide2.QtGui.QBrush) -> None
    QPalette(self, windowText: PySide2.QtGui.QColor, window: PySide2.QtGui.QColor, light: PySide2.QtGui.QColor, dark: PySide2.QtGui.QColor, mid: PySide2.QtGui.QColor, text: PySide2.QtGui.QColor, base: PySide2.QtGui.QColor) -> None
    """
    def alternateBase(self): # real signature unknown; restored from __doc__
        """ alternateBase(self) -> PySide2.QtGui.QBrush """
        pass

    def background(self): # real signature unknown; restored from __doc__
        """ background(self) -> PySide2.QtGui.QBrush """
        pass

    def base(self): # real signature unknown; restored from __doc__
        """ base(self) -> PySide2.QtGui.QBrush """
        pass

    def brightText(self): # real signature unknown; restored from __doc__
        """ brightText(self) -> PySide2.QtGui.QBrush """
        pass

    def brush(self, cg, cr): # real signature unknown; restored from __doc__
        """
        brush(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole) -> PySide2.QtGui.QBrush
        brush(self, cr: PySide2.QtGui.QPalette.ColorRole) -> PySide2.QtGui.QBrush
        """
        pass

    def button(self): # real signature unknown; restored from __doc__
        """ button(self) -> PySide2.QtGui.QBrush """
        pass

    def buttonText(self): # real signature unknown; restored from __doc__
        """ buttonText(self) -> PySide2.QtGui.QBrush """
        pass

    def cacheKey(self): # real signature unknown; restored from __doc__
        """ cacheKey(self) -> int """
        return 0

    def color(self, cg, cr): # real signature unknown; restored from __doc__
        """
        color(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole) -> PySide2.QtGui.QColor
        color(self, cr: PySide2.QtGui.QPalette.ColorRole) -> PySide2.QtGui.QColor
        """
        pass

    def currentColorGroup(self): # real signature unknown; restored from __doc__
        """ currentColorGroup(self) -> PySide2.QtGui.QPalette.ColorGroup """
        pass

    def dark(self): # real signature unknown; restored from __doc__
        """ dark(self) -> PySide2.QtGui.QBrush """
        pass

    def foreground(self): # real signature unknown; restored from __doc__
        """ foreground(self) -> PySide2.QtGui.QBrush """
        pass

    def highlight(self): # real signature unknown; restored from __doc__
        """ highlight(self) -> PySide2.QtGui.QBrush """
        pass

    def highlightedText(self): # real signature unknown; restored from __doc__
        """ highlightedText(self) -> PySide2.QtGui.QBrush """
        pass

    def isBrushSet(self, cg, cr): # real signature unknown; restored from __doc__
        """ isBrushSet(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole) -> bool """
        return False

    def isCopyOf(self, p): # real signature unknown; restored from __doc__
        """ isCopyOf(self, p: PySide2.QtGui.QPalette) -> bool """
        return False

    def isEqual(self, cr1, cr2): # real signature unknown; restored from __doc__
        """ isEqual(self, cr1: PySide2.QtGui.QPalette.ColorGroup, cr2: PySide2.QtGui.QPalette.ColorGroup) -> bool """
        return False

    def light(self): # real signature unknown; restored from __doc__
        """ light(self) -> PySide2.QtGui.QBrush """
        pass

    def link(self): # real signature unknown; restored from __doc__
        """ link(self) -> PySide2.QtGui.QBrush """
        pass

    def linkVisited(self): # real signature unknown; restored from __doc__
        """ linkVisited(self) -> PySide2.QtGui.QBrush """
        pass

    def mid(self): # real signature unknown; restored from __doc__
        """ mid(self) -> PySide2.QtGui.QBrush """
        pass

    def midlight(self): # real signature unknown; restored from __doc__
        """ midlight(self) -> PySide2.QtGui.QBrush """
        pass

    def placeholderText(self): # real signature unknown; restored from __doc__
        """ placeholderText(self) -> PySide2.QtGui.QBrush """
        pass

    def resolve(self): # real signature unknown; restored from __doc__
        """
        resolve(self) -> int
        resolve(self, arg__1: PySide2.QtGui.QPalette) -> PySide2.QtGui.QPalette
        resolve(self, mask: int) -> None
        """
        return 0

    def setBrush(self, cg, cr, brush): # real signature unknown; restored from __doc__
        """
        setBrush(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole, brush: PySide2.QtGui.QBrush) -> None
        setBrush(self, cr: PySide2.QtGui.QPalette.ColorRole, brush: PySide2.QtGui.QBrush) -> None
        """
        pass

    def setColor(self, cg, cr, color): # real signature unknown; restored from __doc__
        """
        setColor(self, cg: PySide2.QtGui.QPalette.ColorGroup, cr: PySide2.QtGui.QPalette.ColorRole, color: PySide2.QtGui.QColor) -> None
        setColor(self, cr: PySide2.QtGui.QPalette.ColorRole, color: PySide2.QtGui.QColor) -> None
        """
        pass

    def setColorGroup(self, cr, windowText, button, light, dark, mid, text, bright_text, base, window): # real signature unknown; restored from __doc__
        """ setColorGroup(self, cr: PySide2.QtGui.QPalette.ColorGroup, windowText: PySide2.QtGui.QBrush, button: PySide2.QtGui.QBrush, light: PySide2.QtGui.QBrush, dark: PySide2.QtGui.QBrush, mid: PySide2.QtGui.QBrush, text: PySide2.QtGui.QBrush, bright_text: PySide2.QtGui.QBrush, base: PySide2.QtGui.QBrush, window: PySide2.QtGui.QBrush) -> None """
        pass

    def setCurrentColorGroup(self, cg): # real signature unknown; restored from __doc__
        """ setCurrentColorGroup(self, cg: PySide2.QtGui.QPalette.ColorGroup) -> None """
        pass

    def shadow(self): # real signature unknown; restored from __doc__
        """ shadow(self) -> PySide2.QtGui.QBrush """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtGui.QPalette) -> None """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> PySide2.QtGui.QBrush """
        pass

    def toolTipBase(self): # real signature unknown; restored from __doc__
        """ toolTipBase(self) -> PySide2.QtGui.QBrush """
        pass

    def toolTipText(self): # real signature unknown; restored from __doc__
        """ toolTipText(self) -> PySide2.QtGui.QBrush """
        pass

    def window(self): # real signature unknown; restored from __doc__
        """ window(self) -> PySide2.QtGui.QBrush """
        pass

    def windowText(self): # real signature unknown; restored from __doc__
        """ windowText(self) -> PySide2.QtGui.QBrush """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, ds): # real signature unknown; restored from __doc__
        """
        __lshift__(self, ds: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, ds): # real signature unknown; restored from __doc__
        """
        __rshift__(self, ds: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    Active = PySide2.QtGui.QPalette.ColorGroup.Active
    All = PySide2.QtGui.QPalette.ColorGroup.All
    AlternateBase = PySide2.QtGui.QPalette.ColorRole.AlternateBase
    Background = PySide2.QtGui.QPalette.ColorRole.Background
    Base = PySide2.QtGui.QPalette.ColorRole.Base
    BrightText = PySide2.QtGui.QPalette.ColorRole.BrightText
    Button = PySide2.QtGui.QPalette.ColorRole.Button
    ButtonText = PySide2.QtGui.QPalette.ColorRole.ButtonText
    ColorGroup = None # (!) real value is "<class 'PySide2.QtGui.QPalette.ColorGroup'>"
    ColorRole = None # (!) real value is "<class 'PySide2.QtGui.QPalette.ColorRole'>"
    Current = PySide2.QtGui.QPalette.ColorGroup.Current
    Dark = PySide2.QtGui.QPalette.ColorRole.Dark
    Disabled = PySide2.QtGui.QPalette.ColorGroup.Disabled
    Foreground = PySide2.QtGui.QPalette.ColorRole.Foreground
    Highlight = PySide2.QtGui.QPalette.ColorRole.Highlight
    HighlightedText = PySide2.QtGui.QPalette.ColorRole.HighlightedText
    Inactive = PySide2.QtGui.QPalette.ColorGroup.Inactive
    Light = PySide2.QtGui.QPalette.ColorRole.Light
    Link = PySide2.QtGui.QPalette.ColorRole.Link
    LinkVisited = PySide2.QtGui.QPalette.ColorRole.LinkVisited
    Mid = PySide2.QtGui.QPalette.ColorRole.Mid
    Midlight = PySide2.QtGui.QPalette.ColorRole.Midlight
    NColorGroups = PySide2.QtGui.QPalette.ColorGroup.NColorGroups
    NColorRoles = PySide2.QtGui.QPalette.ColorRole.NColorRoles
    Normal = PySide2.QtGui.QPalette.ColorGroup.Normal
    NoRole = PySide2.QtGui.QPalette.ColorRole.NoRole
    PlaceholderText = PySide2.QtGui.QPalette.ColorRole.PlaceholderText
    Shadow = PySide2.QtGui.QPalette.ColorRole.Shadow
    Text = PySide2.QtGui.QPalette.ColorRole.Text
    ToolTipBase = PySide2.QtGui.QPalette.ColorRole.ToolTipBase
    ToolTipText = PySide2.QtGui.QPalette.ColorRole.ToolTipText
    Window = PySide2.QtGui.QPalette.ColorRole.Window
    WindowText = PySide2.QtGui.QPalette.ColorRole.WindowText
    __hash__ = None


