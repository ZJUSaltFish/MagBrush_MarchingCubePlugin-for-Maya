# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QStyle(__PySide2_QtCore.QObject):
    """ QStyle(self) -> None """
    def alignedRect(self, direction, alignment, size, rectangle): # real signature unknown; restored from __doc__
        """ alignedRect(direction: PySide2.QtCore.Qt.LayoutDirection, alignment: PySide2.QtCore.Qt.Alignment, size: PySide2.QtCore.QSize, rectangle: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect """
        pass

    def combinedLayoutSpacing(self, controls1, controls2, orientation, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ combinedLayoutSpacing(self, controls1: PySide2.QtWidgets.QSizePolicy.ControlTypes, controls2: PySide2.QtWidgets.QSizePolicy.ControlTypes, orientation: PySide2.QtCore.Qt.Orientation, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> int """
        pass

    def drawComplexControl(self, cc, opt, p, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawComplexControl(self, cc: PySide2.QtWidgets.QStyle.ComplexControl, opt: PySide2.QtWidgets.QStyleOptionComplex, p: PySide2.QtGui.QPainter, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def drawControl(self, element, opt, p, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawControl(self, element: PySide2.QtWidgets.QStyle.ControlElement, opt: PySide2.QtWidgets.QStyleOption, p: PySide2.QtGui.QPainter, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def drawItemPixmap(self, painter, rect, alignment, pixmap): # real signature unknown; restored from __doc__
        """ drawItemPixmap(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, alignment: int, pixmap: PySide2.QtGui.QPixmap) -> None """
        pass

    def drawItemText(self, painter, rect, flags, pal, enabled, text, textRole=None): # real signature unknown; restored from __doc__
        """ drawItemText(self, painter: PySide2.QtGui.QPainter, rect: PySide2.QtCore.QRect, flags: int, pal: PySide2.QtGui.QPalette, enabled: bool, text: str, textRole: PySide2.QtGui.QPalette.ColorRole = PySide2.QtGui.QPalette.ColorRole.NoRole) -> None """
        pass

    def drawPrimitive(self, pe, opt, p, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ drawPrimitive(self, pe: PySide2.QtWidgets.QStyle.PrimitiveElement, opt: PySide2.QtWidgets.QStyleOption, p: PySide2.QtGui.QPainter, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None """
        pass

    def generatedIconPixmap(self, iconMode, pixmap, opt): # real signature unknown; restored from __doc__
        """ generatedIconPixmap(self, iconMode: PySide2.QtGui.QIcon.Mode, pixmap: PySide2.QtGui.QPixmap, opt: PySide2.QtWidgets.QStyleOption) -> PySide2.QtGui.QPixmap """
        pass

    def hitTestComplexControl(self, cc, opt, pt, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hitTestComplexControl(self, cc: PySide2.QtWidgets.QStyle.ComplexControl, opt: PySide2.QtWidgets.QStyleOptionComplex, pt: PySide2.QtCore.QPoint, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtWidgets.QStyle.SubControl """
        pass

    def itemPixmapRect(self, r, flags, pixmap): # real signature unknown; restored from __doc__
        """ itemPixmapRect(self, r: PySide2.QtCore.QRect, flags: int, pixmap: PySide2.QtGui.QPixmap) -> PySide2.QtCore.QRect """
        pass

    def itemTextRect(self, fm, r, flags, enabled, text): # real signature unknown; restored from __doc__
        """ itemTextRect(self, fm: PySide2.QtGui.QFontMetrics, r: PySide2.QtCore.QRect, flags: int, enabled: bool, text: str) -> PySide2.QtCore.QRect """
        pass

    def layoutSpacing(self, control1, control2, orientation, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ layoutSpacing(self, control1: PySide2.QtWidgets.QSizePolicy.ControlType, control2: PySide2.QtWidgets.QSizePolicy.ControlType, orientation: PySide2.QtCore.Qt.Orientation, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> int """
        pass

    def pixelMetric(self, metric, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ pixelMetric(self, metric: PySide2.QtWidgets.QStyle.PixelMetric, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> int """
        pass

    def polish(self, application): # real signature unknown; restored from __doc__
        """
        polish(self, application: PySide2.QtWidgets.QApplication) -> None
        polish(self, palette: PySide2.QtGui.QPalette) -> None
        polish(self, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def proxy(self): # real signature unknown; restored from __doc__
        """ proxy(self) -> PySide2.QtWidgets.QStyle """
        pass

    def sizeFromContents(self, ct, opt, contentsSize, w, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sizeFromContents(self, ct: PySide2.QtWidgets.QStyle.ContentsType, opt: PySide2.QtWidgets.QStyleOption, contentsSize: PySide2.QtCore.QSize, w: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtCore.QSize """
        pass

    def sliderPositionFromValue(self, min, max, val, space, upsideDown=False): # real signature unknown; restored from __doc__
        """ sliderPositionFromValue(min: int, max: int, val: int, space: int, upsideDown: bool = False) -> int """
        return 0

    def sliderValueFromPosition(self, min, max, pos, space, upsideDown=False): # real signature unknown; restored from __doc__
        """ sliderValueFromPosition(min: int, max: int, pos: int, space: int, upsideDown: bool = False) -> int """
        return 0

    def standardIcon(self, standardIcon, option, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardIcon(self, standardIcon: PySide2.QtWidgets.QStyle.StandardPixmap, option: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtGui.QIcon """
        pass

    def standardPalette(self): # real signature unknown; restored from __doc__
        """ standardPalette(self) -> PySide2.QtGui.QPalette """
        pass

    def standardPixmap(self, standardPixmap, opt, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ standardPixmap(self, standardPixmap: PySide2.QtWidgets.QStyle.StandardPixmap, opt: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtGui.QPixmap """
        pass

    def styleHint(self, stylehint, opt, PySide2_QtWidgets_QStyleOption=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ styleHint(self, stylehint: PySide2.QtWidgets.QStyle.StyleHint, opt: typing.Optional[PySide2.QtWidgets.QStyleOption] = None, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None, returnData: typing.Optional[PySide2.QtWidgets.QStyleHintReturn] = None) -> int """
        pass

    def subControlRect(self, cc, opt, sc, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ subControlRect(self, cc: PySide2.QtWidgets.QStyle.ComplexControl, opt: PySide2.QtWidgets.QStyleOptionComplex, sc: PySide2.QtWidgets.QStyle.SubControl, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtCore.QRect """
        pass

    def subElementRect(self, subElement, option, widget, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ subElementRect(self, subElement: PySide2.QtWidgets.QStyle.SubElement, option: PySide2.QtWidgets.QStyleOption, widget: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> PySide2.QtCore.QRect """
        pass

    def unpolish(self, application): # real signature unknown; restored from __doc__
        """
        unpolish(self, application: PySide2.QtWidgets.QApplication) -> None
        unpolish(self, widget: PySide2.QtWidgets.QWidget) -> None
        """
        pass

    def visualAlignment(self, direction, alignment): # real signature unknown; restored from __doc__
        """ visualAlignment(direction: PySide2.QtCore.Qt.LayoutDirection, alignment: PySide2.QtCore.Qt.Alignment) -> PySide2.QtCore.Qt.Alignment """
        pass

    def visualPos(self, direction, boundingRect, logicalPos): # real signature unknown; restored from __doc__
        """ visualPos(direction: PySide2.QtCore.Qt.LayoutDirection, boundingRect: PySide2.QtCore.QRect, logicalPos: PySide2.QtCore.QPoint) -> PySide2.QtCore.QPoint """
        pass

    def visualRect(self, direction, boundingRect, logicalRect): # real signature unknown; restored from __doc__
        """ visualRect(direction: PySide2.QtCore.Qt.LayoutDirection, boundingRect: PySide2.QtCore.QRect, logicalRect: PySide2.QtCore.QRect) -> PySide2.QtCore.QRect """
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

    CC_ComboBox = PySide2.QtWidgets.QStyle.ComplexControl.CC_ComboBox
    CC_CustomBase = PySide2.QtWidgets.QStyle.ComplexControl.CC_CustomBase
    CC_Dial = PySide2.QtWidgets.QStyle.ComplexControl.CC_Dial
    CC_GroupBox = PySide2.QtWidgets.QStyle.ComplexControl.CC_GroupBox
    CC_MdiControls = PySide2.QtWidgets.QStyle.ComplexControl.CC_MdiControls
    CC_ScrollBar = PySide2.QtWidgets.QStyle.ComplexControl.CC_ScrollBar
    CC_Slider = PySide2.QtWidgets.QStyle.ComplexControl.CC_Slider
    CC_SpinBox = PySide2.QtWidgets.QStyle.ComplexControl.CC_SpinBox
    CC_TitleBar = PySide2.QtWidgets.QStyle.ComplexControl.CC_TitleBar
    CC_ToolButton = PySide2.QtWidgets.QStyle.ComplexControl.CC_ToolButton
    CE_CheckBox = PySide2.QtWidgets.QStyle.ControlElement.CE_CheckBox
    CE_CheckBoxLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_CheckBoxLabel
    CE_ColumnViewGrip = PySide2.QtWidgets.QStyle.ControlElement.CE_ColumnViewGrip
    CE_ComboBoxLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_ComboBoxLabel
    CE_CustomBase = PySide2.QtWidgets.QStyle.ControlElement.CE_CustomBase
    CE_DockWidgetTitle = PySide2.QtWidgets.QStyle.ControlElement.CE_DockWidgetTitle
    CE_FocusFrame = PySide2.QtWidgets.QStyle.ControlElement.CE_FocusFrame
    CE_Header = PySide2.QtWidgets.QStyle.ControlElement.CE_Header
    CE_HeaderEmptyArea = PySide2.QtWidgets.QStyle.ControlElement.CE_HeaderEmptyArea
    CE_HeaderLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_HeaderLabel
    CE_HeaderSection = PySide2.QtWidgets.QStyle.ControlElement.CE_HeaderSection
    CE_ItemViewItem = PySide2.QtWidgets.QStyle.ControlElement.CE_ItemViewItem
    CE_MenuBarEmptyArea = PySide2.QtWidgets.QStyle.ControlElement.CE_MenuBarEmptyArea
    CE_MenuBarItem = PySide2.QtWidgets.QStyle.ControlElement.CE_MenuBarItem
    CE_MenuEmptyArea = PySide2.QtWidgets.QStyle.ControlElement.CE_MenuEmptyArea
    CE_MenuHMargin = PySide2.QtWidgets.QStyle.ControlElement.CE_MenuHMargin
    CE_MenuItem = PySide2.QtWidgets.QStyle.ControlElement.CE_MenuItem
    CE_MenuScroller = PySide2.QtWidgets.QStyle.ControlElement.CE_MenuScroller
    CE_MenuTearoff = PySide2.QtWidgets.QStyle.ControlElement.CE_MenuTearoff
    CE_MenuVMargin = PySide2.QtWidgets.QStyle.ControlElement.CE_MenuVMargin
    CE_ProgressBar = PySide2.QtWidgets.QStyle.ControlElement.CE_ProgressBar
    CE_ProgressBarContents = PySide2.QtWidgets.QStyle.ControlElement.CE_ProgressBarContents
    CE_ProgressBarGroove = PySide2.QtWidgets.QStyle.ControlElement.CE_ProgressBarGroove
    CE_ProgressBarLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_ProgressBarLabel
    CE_PushButton = PySide2.QtWidgets.QStyle.ControlElement.CE_PushButton
    CE_PushButtonBevel = PySide2.QtWidgets.QStyle.ControlElement.CE_PushButtonBevel
    CE_PushButtonLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_PushButtonLabel
    CE_RadioButton = PySide2.QtWidgets.QStyle.ControlElement.CE_RadioButton
    CE_RadioButtonLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_RadioButtonLabel
    CE_RubberBand = PySide2.QtWidgets.QStyle.ControlElement.CE_RubberBand
    CE_ScrollBarAddLine = PySide2.QtWidgets.QStyle.ControlElement.CE_ScrollBarAddLine
    CE_ScrollBarAddPage = PySide2.QtWidgets.QStyle.ControlElement.CE_ScrollBarAddPage
    CE_ScrollBarFirst = PySide2.QtWidgets.QStyle.ControlElement.CE_ScrollBarFirst
    CE_ScrollBarLast = PySide2.QtWidgets.QStyle.ControlElement.CE_ScrollBarLast
    CE_ScrollBarSlider = PySide2.QtWidgets.QStyle.ControlElement.CE_ScrollBarSlider
    CE_ScrollBarSubLine = PySide2.QtWidgets.QStyle.ControlElement.CE_ScrollBarSubLine
    CE_ScrollBarSubPage = PySide2.QtWidgets.QStyle.ControlElement.CE_ScrollBarSubPage
    CE_ShapedFrame = PySide2.QtWidgets.QStyle.ControlElement.CE_ShapedFrame
    CE_SizeGrip = PySide2.QtWidgets.QStyle.ControlElement.CE_SizeGrip
    CE_Splitter = PySide2.QtWidgets.QStyle.ControlElement.CE_Splitter
    CE_TabBarTab = PySide2.QtWidgets.QStyle.ControlElement.CE_TabBarTab
    CE_TabBarTabLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_TabBarTabLabel
    CE_TabBarTabShape = PySide2.QtWidgets.QStyle.ControlElement.CE_TabBarTabShape
    CE_ToolBar = PySide2.QtWidgets.QStyle.ControlElement.CE_ToolBar
    CE_ToolBoxTab = PySide2.QtWidgets.QStyle.ControlElement.CE_ToolBoxTab
    CE_ToolBoxTabLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_ToolBoxTabLabel
    CE_ToolBoxTabShape = PySide2.QtWidgets.QStyle.ControlElement.CE_ToolBoxTabShape
    CE_ToolButtonLabel = PySide2.QtWidgets.QStyle.ControlElement.CE_ToolButtonLabel
    ComplexControl = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.ComplexControl'>"
    ContentsType = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.ContentsType'>"
    ControlElement = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.ControlElement'>"
    CT_CheckBox = PySide2.QtWidgets.QStyle.ContentsType.CT_CheckBox
    CT_ComboBox = PySide2.QtWidgets.QStyle.ContentsType.CT_ComboBox
    CT_CustomBase = PySide2.QtWidgets.QStyle.ContentsType.CT_CustomBase
    CT_DialogButtons = PySide2.QtWidgets.QStyle.ContentsType.CT_DialogButtons
    CT_GroupBox = PySide2.QtWidgets.QStyle.ContentsType.CT_GroupBox
    CT_HeaderSection = PySide2.QtWidgets.QStyle.ContentsType.CT_HeaderSection
    CT_ItemViewItem = PySide2.QtWidgets.QStyle.ContentsType.CT_ItemViewItem
    CT_LineEdit = PySide2.QtWidgets.QStyle.ContentsType.CT_LineEdit
    CT_MdiControls = PySide2.QtWidgets.QStyle.ContentsType.CT_MdiControls
    CT_Menu = PySide2.QtWidgets.QStyle.ContentsType.CT_Menu
    CT_MenuBar = PySide2.QtWidgets.QStyle.ContentsType.CT_MenuBar
    CT_MenuBarItem = PySide2.QtWidgets.QStyle.ContentsType.CT_MenuBarItem
    CT_MenuItem = PySide2.QtWidgets.QStyle.ContentsType.CT_MenuItem
    CT_ProgressBar = PySide2.QtWidgets.QStyle.ContentsType.CT_ProgressBar
    CT_PushButton = PySide2.QtWidgets.QStyle.ContentsType.CT_PushButton
    CT_RadioButton = PySide2.QtWidgets.QStyle.ContentsType.CT_RadioButton
    CT_ScrollBar = PySide2.QtWidgets.QStyle.ContentsType.CT_ScrollBar
    CT_SizeGrip = PySide2.QtWidgets.QStyle.ContentsType.CT_SizeGrip
    CT_Slider = PySide2.QtWidgets.QStyle.ContentsType.CT_Slider
    CT_SpinBox = PySide2.QtWidgets.QStyle.ContentsType.CT_SpinBox
    CT_Splitter = PySide2.QtWidgets.QStyle.ContentsType.CT_Splitter
    CT_TabBarTab = PySide2.QtWidgets.QStyle.ContentsType.CT_TabBarTab
    CT_TabWidget = PySide2.QtWidgets.QStyle.ContentsType.CT_TabWidget
    CT_ToolButton = PySide2.QtWidgets.QStyle.ContentsType.CT_ToolButton
    PE_CustomBase = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_CustomBase
    PE_Frame = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_Frame
    PE_FrameButtonBevel = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameButtonBevel
    PE_FrameButtonTool = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameButtonTool
    PE_FrameDefaultButton = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameDefaultButton
    PE_FrameDockWidget = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameDockWidget
    PE_FrameFocusRect = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameFocusRect
    PE_FrameGroupBox = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameGroupBox
    PE_FrameLineEdit = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameLineEdit
    PE_FrameMenu = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameMenu
    PE_FrameStatusBar = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameStatusBar
    PE_FrameStatusBarItem = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameStatusBarItem
    PE_FrameTabBarBase = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameTabBarBase
    PE_FrameTabWidget = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameTabWidget
    PE_FrameWindow = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_FrameWindow
    PE_IndicatorArrowDown = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorArrowDown
    PE_IndicatorArrowLeft = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorArrowLeft
    PE_IndicatorArrowRight = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorArrowRight
    PE_IndicatorArrowUp = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorArrowUp
    PE_IndicatorBranch = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorBranch
    PE_IndicatorButtonDropDown = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorButtonDropDown
    PE_IndicatorCheckBox = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorCheckBox
    PE_IndicatorColumnViewArrow = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorColumnViewArrow
    PE_IndicatorDockWidgetResizeHandle = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorDockWidgetResizeHandle
    PE_IndicatorHeaderArrow = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorHeaderArrow
    PE_IndicatorItemViewItemCheck = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorItemViewItemCheck
    PE_IndicatorItemViewItemDrop = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorItemViewItemDrop
    PE_IndicatorMenuCheckMark = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorMenuCheckMark
    PE_IndicatorProgressChunk = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorProgressChunk
    PE_IndicatorRadioButton = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorRadioButton
    PE_IndicatorSpinDown = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorSpinDown
    PE_IndicatorSpinMinus = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorSpinMinus
    PE_IndicatorSpinPlus = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorSpinPlus
    PE_IndicatorSpinUp = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorSpinUp
    PE_IndicatorTabClose = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorTabClose
    PE_IndicatorTabTear = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorTabTear
    PE_IndicatorTabTearLeft = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorTabTearLeft
    PE_IndicatorTabTearRight = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorTabTearRight
    PE_IndicatorToolBarHandle = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorToolBarHandle
    PE_IndicatorToolBarSeparator = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorToolBarSeparator
    PE_IndicatorViewItemCheck = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_IndicatorViewItemCheck
    PE_PanelButtonBevel = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelButtonBevel
    PE_PanelButtonCommand = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelButtonCommand
    PE_PanelButtonTool = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelButtonTool
    PE_PanelItemViewItem = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelItemViewItem
    PE_PanelItemViewRow = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelItemViewRow
    PE_PanelLineEdit = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelLineEdit
    PE_PanelMenu = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelMenu
    PE_PanelMenuBar = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelMenuBar
    PE_PanelScrollAreaCorner = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelScrollAreaCorner
    PE_PanelStatusBar = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelStatusBar
    PE_PanelTipLabel = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelTipLabel
    PE_PanelToolBar = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_PanelToolBar
    PE_Widget = PySide2.QtWidgets.QStyle.PrimitiveElement.PE_Widget
    PixelMetric = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.PixelMetric'>"
    PM_ButtonDefaultIndicator = PySide2.QtWidgets.QStyle.PixelMetric.PM_ButtonDefaultIndicator
    PM_ButtonIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_ButtonIconSize
    PM_ButtonMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_ButtonMargin
    PM_ButtonShiftHorizontal = PySide2.QtWidgets.QStyle.PixelMetric.PM_ButtonShiftHorizontal
    PM_ButtonShiftVertical = PySide2.QtWidgets.QStyle.PixelMetric.PM_ButtonShiftVertical
    PM_CheckBoxLabelSpacing = PySide2.QtWidgets.QStyle.PixelMetric.PM_CheckBoxLabelSpacing
    PM_ComboBoxFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_ComboBoxFrameWidth
    PM_CustomBase = PySide2.QtWidgets.QStyle.PixelMetric.PM_CustomBase
    PM_DefaultChildMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_DefaultChildMargin
    PM_DefaultFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_DefaultFrameWidth
    PM_DefaultLayoutSpacing = PySide2.QtWidgets.QStyle.PixelMetric.PM_DefaultLayoutSpacing
    PM_DefaultTopLevelMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_DefaultTopLevelMargin
    PM_DialogButtonsButtonHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_DialogButtonsButtonHeight
    PM_DialogButtonsButtonWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_DialogButtonsButtonWidth
    PM_DialogButtonsSeparator = PySide2.QtWidgets.QStyle.PixelMetric.PM_DialogButtonsSeparator
    PM_DockWidgetFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_DockWidgetFrameWidth
    PM_DockWidgetHandleExtent = PySide2.QtWidgets.QStyle.PixelMetric.PM_DockWidgetHandleExtent
    PM_DockWidgetSeparatorExtent = PySide2.QtWidgets.QStyle.PixelMetric.PM_DockWidgetSeparatorExtent
    PM_DockWidgetTitleBarButtonMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_DockWidgetTitleBarButtonMargin
    PM_DockWidgetTitleMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_DockWidgetTitleMargin
    PM_ExclusiveIndicatorHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_ExclusiveIndicatorHeight
    PM_ExclusiveIndicatorWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_ExclusiveIndicatorWidth
    PM_FocusFrameHMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_FocusFrameHMargin
    PM_FocusFrameVMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_FocusFrameVMargin
    PM_HeaderDefaultSectionSizeHorizontal = PySide2.QtWidgets.QStyle.PixelMetric.PM_HeaderDefaultSectionSizeHorizontal
    PM_HeaderDefaultSectionSizeVertical = PySide2.QtWidgets.QStyle.PixelMetric.PM_HeaderDefaultSectionSizeVertical
    PM_HeaderGripMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_HeaderGripMargin
    PM_HeaderMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_HeaderMargin
    PM_HeaderMarkSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_HeaderMarkSize
    PM_IconViewIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_IconViewIconSize
    PM_IndicatorHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_IndicatorHeight
    PM_IndicatorWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_IndicatorWidth
    PM_LargeIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_LargeIconSize
    PM_LayoutBottomMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_LayoutBottomMargin
    PM_LayoutHorizontalSpacing = PySide2.QtWidgets.QStyle.PixelMetric.PM_LayoutHorizontalSpacing
    PM_LayoutLeftMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_LayoutLeftMargin
    PM_LayoutRightMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_LayoutRightMargin
    PM_LayoutTopMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_LayoutTopMargin
    PM_LayoutVerticalSpacing = PySide2.QtWidgets.QStyle.PixelMetric.PM_LayoutVerticalSpacing
    PM_ListViewIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_ListViewIconSize
    PM_MaximumDragDistance = PySide2.QtWidgets.QStyle.PixelMetric.PM_MaximumDragDistance
    PM_MDIFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_MDIFrameWidth
    PM_MDIMinimizedWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_MDIMinimizedWidth
    PM_MdiSubWindowFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_MdiSubWindowFrameWidth
    PM_MdiSubWindowMinimizedWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_MdiSubWindowMinimizedWidth
    PM_MenuBarHMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuBarHMargin
    PM_MenuBarItemSpacing = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuBarItemSpacing
    PM_MenuBarPanelWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuBarPanelWidth
    PM_MenuBarVMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuBarVMargin
    PM_MenuButtonIndicator = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuButtonIndicator
    PM_MenuDesktopFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuDesktopFrameWidth
    PM_MenuHMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuHMargin
    PM_MenuPanelWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuPanelWidth
    PM_MenuScrollerHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuScrollerHeight
    PM_MenuTearoffHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuTearoffHeight
    PM_MenuVMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_MenuVMargin
    PM_MessageBoxIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_MessageBoxIconSize
    PM_ProgressBarChunkWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_ProgressBarChunkWidth
    PM_RadioButtonLabelSpacing = PySide2.QtWidgets.QStyle.PixelMetric.PM_RadioButtonLabelSpacing
    PM_ScrollBarExtent = PySide2.QtWidgets.QStyle.PixelMetric.PM_ScrollBarExtent
    PM_ScrollBarSliderMin = PySide2.QtWidgets.QStyle.PixelMetric.PM_ScrollBarSliderMin
    PM_ScrollView_ScrollBarOverlap = PySide2.QtWidgets.QStyle.PixelMetric.PM_ScrollView_ScrollBarOverlap
    PM_ScrollView_ScrollBarSpacing = PySide2.QtWidgets.QStyle.PixelMetric.PM_ScrollView_ScrollBarSpacing
    PM_SizeGripSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_SizeGripSize
    PM_SliderControlThickness = PySide2.QtWidgets.QStyle.PixelMetric.PM_SliderControlThickness
    PM_SliderLength = PySide2.QtWidgets.QStyle.PixelMetric.PM_SliderLength
    PM_SliderSpaceAvailable = PySide2.QtWidgets.QStyle.PixelMetric.PM_SliderSpaceAvailable
    PM_SliderThickness = PySide2.QtWidgets.QStyle.PixelMetric.PM_SliderThickness
    PM_SliderTickmarkOffset = PySide2.QtWidgets.QStyle.PixelMetric.PM_SliderTickmarkOffset
    PM_SmallIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_SmallIconSize
    PM_SpinBoxFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_SpinBoxFrameWidth
    PM_SpinBoxSliderHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_SpinBoxSliderHeight
    PM_SplitterWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_SplitterWidth
    PM_SubMenuOverlap = PySide2.QtWidgets.QStyle.PixelMetric.PM_SubMenuOverlap
    PM_TabBarBaseHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarBaseHeight
    PM_TabBarBaseOverlap = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarBaseOverlap
    PM_TabBarIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarIconSize
    PM_TabBarScrollButtonWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarScrollButtonWidth
    PM_TabBarTabHSpace = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarTabHSpace
    PM_TabBarTabOverlap = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarTabOverlap
    PM_TabBarTabShiftHorizontal = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarTabShiftHorizontal
    PM_TabBarTabShiftVertical = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarTabShiftVertical
    PM_TabBarTabVSpace = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBarTabVSpace
    PM_TabBar_ScrollButtonOverlap = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabBar_ScrollButtonOverlap
    PM_TabCloseIndicatorHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabCloseIndicatorHeight
    PM_TabCloseIndicatorWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_TabCloseIndicatorWidth
    PM_TextCursorWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_TextCursorWidth
    PM_TitleBarButtonIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_TitleBarButtonIconSize
    PM_TitleBarButtonSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_TitleBarButtonSize
    PM_TitleBarHeight = PySide2.QtWidgets.QStyle.PixelMetric.PM_TitleBarHeight
    PM_ToolBarExtensionExtent = PySide2.QtWidgets.QStyle.PixelMetric.PM_ToolBarExtensionExtent
    PM_ToolBarFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_ToolBarFrameWidth
    PM_ToolBarHandleExtent = PySide2.QtWidgets.QStyle.PixelMetric.PM_ToolBarHandleExtent
    PM_ToolBarIconSize = PySide2.QtWidgets.QStyle.PixelMetric.PM_ToolBarIconSize
    PM_ToolBarItemMargin = PySide2.QtWidgets.QStyle.PixelMetric.PM_ToolBarItemMargin
    PM_ToolBarItemSpacing = PySide2.QtWidgets.QStyle.PixelMetric.PM_ToolBarItemSpacing
    PM_ToolBarSeparatorExtent = PySide2.QtWidgets.QStyle.PixelMetric.PM_ToolBarSeparatorExtent
    PM_ToolTipLabelFrameWidth = PySide2.QtWidgets.QStyle.PixelMetric.PM_ToolTipLabelFrameWidth
    PM_TreeViewIndentation = PySide2.QtWidgets.QStyle.PixelMetric.PM_TreeViewIndentation
    PrimitiveElement = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.PrimitiveElement'>"
    RequestSoftwareInputPanel = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.RequestSoftwareInputPanel'>"
    RSIP_OnMouseClick = PySide2.QtWidgets.QStyle.RequestSoftwareInputPanel.RSIP_OnMouseClick
    RSIP_OnMouseClickAndAlreadyFocused = PySide2.QtWidgets.QStyle.RequestSoftwareInputPanel.RSIP_OnMouseClickAndAlreadyFocused
    SC_All = PySide2.QtWidgets.QStyle.SubControl.SC_All
    SC_ComboBoxArrow = PySide2.QtWidgets.QStyle.SubControl.SC_ComboBoxArrow
    SC_ComboBoxEditField = PySide2.QtWidgets.QStyle.SubControl.SC_ComboBoxEditField
    SC_ComboBoxFrame = PySide2.QtWidgets.QStyle.SubControl.SC_ComboBoxFrame
    SC_ComboBoxListBoxPopup = PySide2.QtWidgets.QStyle.SubControl.SC_ComboBoxListBoxPopup
    SC_CustomBase = PySide2.QtWidgets.QStyle.SubControl.SC_CustomBase
    SC_DialGroove = PySide2.QtWidgets.QStyle.SubControl.SC_DialGroove
    SC_DialHandle = PySide2.QtWidgets.QStyle.SubControl.SC_DialHandle
    SC_DialTickmarks = PySide2.QtWidgets.QStyle.SubControl.SC_DialTickmarks
    SC_GroupBoxCheckBox = PySide2.QtWidgets.QStyle.SubControl.SC_GroupBoxCheckBox
    SC_GroupBoxContents = PySide2.QtWidgets.QStyle.SubControl.SC_GroupBoxContents
    SC_GroupBoxFrame = PySide2.QtWidgets.QStyle.SubControl.SC_GroupBoxFrame
    SC_GroupBoxLabel = PySide2.QtWidgets.QStyle.SubControl.SC_GroupBoxLabel
    SC_MdiCloseButton = PySide2.QtWidgets.QStyle.SubControl.SC_MdiCloseButton
    SC_MdiMinButton = PySide2.QtWidgets.QStyle.SubControl.SC_MdiMinButton
    SC_MdiNormalButton = PySide2.QtWidgets.QStyle.SubControl.SC_MdiNormalButton
    SC_None = PySide2.QtWidgets.QStyle.SubControl.SC_None
    SC_ScrollBarAddLine = PySide2.QtWidgets.QStyle.SubControl.SC_ScrollBarAddLine
    SC_ScrollBarAddPage = PySide2.QtWidgets.QStyle.SubControl.SC_ScrollBarAddPage
    SC_ScrollBarFirst = PySide2.QtWidgets.QStyle.SubControl.SC_ScrollBarFirst
    SC_ScrollBarGroove = PySide2.QtWidgets.QStyle.SubControl.SC_ScrollBarGroove
    SC_ScrollBarLast = PySide2.QtWidgets.QStyle.SubControl.SC_ScrollBarLast
    SC_ScrollBarSlider = PySide2.QtWidgets.QStyle.SubControl.SC_ScrollBarSlider
    SC_ScrollBarSubLine = PySide2.QtWidgets.QStyle.SubControl.SC_ScrollBarSubLine
    SC_ScrollBarSubPage = PySide2.QtWidgets.QStyle.SubControl.SC_ScrollBarSubPage
    SC_SliderGroove = PySide2.QtWidgets.QStyle.SubControl.SC_SliderGroove
    SC_SliderHandle = PySide2.QtWidgets.QStyle.SubControl.SC_SliderHandle
    SC_SliderTickmarks = PySide2.QtWidgets.QStyle.SubControl.SC_SliderTickmarks
    SC_SpinBoxDown = PySide2.QtWidgets.QStyle.SubControl.SC_SpinBoxDown
    SC_SpinBoxEditField = PySide2.QtWidgets.QStyle.SubControl.SC_SpinBoxEditField
    SC_SpinBoxFrame = PySide2.QtWidgets.QStyle.SubControl.SC_SpinBoxFrame
    SC_SpinBoxUp = PySide2.QtWidgets.QStyle.SubControl.SC_SpinBoxUp
    SC_TitleBarCloseButton = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarCloseButton
    SC_TitleBarContextHelpButton = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarContextHelpButton
    SC_TitleBarLabel = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarLabel
    SC_TitleBarMaxButton = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarMaxButton
    SC_TitleBarMinButton = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarMinButton
    SC_TitleBarNormalButton = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarNormalButton
    SC_TitleBarShadeButton = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarShadeButton
    SC_TitleBarSysMenu = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarSysMenu
    SC_TitleBarUnshadeButton = PySide2.QtWidgets.QStyle.SubControl.SC_TitleBarUnshadeButton
    SC_ToolButton = PySide2.QtWidgets.QStyle.SubControl.SC_ToolButton
    SC_ToolButtonMenu = PySide2.QtWidgets.QStyle.SubControl.SC_ToolButtonMenu
    SE_CheckBoxClickRect = PySide2.QtWidgets.QStyle.SubElement.SE_CheckBoxClickRect
    SE_CheckBoxContents = PySide2.QtWidgets.QStyle.SubElement.SE_CheckBoxContents
    SE_CheckBoxFocusRect = PySide2.QtWidgets.QStyle.SubElement.SE_CheckBoxFocusRect
    SE_CheckBoxIndicator = PySide2.QtWidgets.QStyle.SubElement.SE_CheckBoxIndicator
    SE_CheckBoxLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_CheckBoxLayoutItem
    SE_ComboBoxFocusRect = PySide2.QtWidgets.QStyle.SubElement.SE_ComboBoxFocusRect
    SE_ComboBoxLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_ComboBoxLayoutItem
    SE_CustomBase = PySide2.QtWidgets.QStyle.SubElement.SE_CustomBase
    SE_DateTimeEditLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_DateTimeEditLayoutItem
    SE_DialogButtonBoxLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_DialogButtonBoxLayoutItem
    SE_DockWidgetCloseButton = PySide2.QtWidgets.QStyle.SubElement.SE_DockWidgetCloseButton
    SE_DockWidgetFloatButton = PySide2.QtWidgets.QStyle.SubElement.SE_DockWidgetFloatButton
    SE_DockWidgetIcon = PySide2.QtWidgets.QStyle.SubElement.SE_DockWidgetIcon
    SE_DockWidgetTitleBarText = PySide2.QtWidgets.QStyle.SubElement.SE_DockWidgetTitleBarText
    SE_FrameContents = PySide2.QtWidgets.QStyle.SubElement.SE_FrameContents
    SE_FrameLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_FrameLayoutItem
    SE_GroupBoxLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_GroupBoxLayoutItem
    SE_HeaderArrow = PySide2.QtWidgets.QStyle.SubElement.SE_HeaderArrow
    SE_HeaderLabel = PySide2.QtWidgets.QStyle.SubElement.SE_HeaderLabel
    SE_ItemViewItemCheckIndicator = PySide2.QtWidgets.QStyle.SubElement.SE_ItemViewItemCheckIndicator
    SE_ItemViewItemDecoration = PySide2.QtWidgets.QStyle.SubElement.SE_ItemViewItemDecoration
    SE_ItemViewItemFocusRect = PySide2.QtWidgets.QStyle.SubElement.SE_ItemViewItemFocusRect
    SE_ItemViewItemText = PySide2.QtWidgets.QStyle.SubElement.SE_ItemViewItemText
    SE_LabelLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_LabelLayoutItem
    SE_LineEditContents = PySide2.QtWidgets.QStyle.SubElement.SE_LineEditContents
    SE_ProgressBarContents = PySide2.QtWidgets.QStyle.SubElement.SE_ProgressBarContents
    SE_ProgressBarGroove = PySide2.QtWidgets.QStyle.SubElement.SE_ProgressBarGroove
    SE_ProgressBarLabel = PySide2.QtWidgets.QStyle.SubElement.SE_ProgressBarLabel
    SE_ProgressBarLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_ProgressBarLayoutItem
    SE_PushButtonBevel = PySide2.QtWidgets.QStyle.SubElement.SE_PushButtonBevel
    SE_PushButtonContents = PySide2.QtWidgets.QStyle.SubElement.SE_PushButtonContents
    SE_PushButtonFocusRect = PySide2.QtWidgets.QStyle.SubElement.SE_PushButtonFocusRect
    SE_PushButtonLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_PushButtonLayoutItem
    SE_RadioButtonClickRect = PySide2.QtWidgets.QStyle.SubElement.SE_RadioButtonClickRect
    SE_RadioButtonContents = PySide2.QtWidgets.QStyle.SubElement.SE_RadioButtonContents
    SE_RadioButtonFocusRect = PySide2.QtWidgets.QStyle.SubElement.SE_RadioButtonFocusRect
    SE_RadioButtonIndicator = PySide2.QtWidgets.QStyle.SubElement.SE_RadioButtonIndicator
    SE_RadioButtonLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_RadioButtonLayoutItem
    SE_ShapedFrameContents = PySide2.QtWidgets.QStyle.SubElement.SE_ShapedFrameContents
    SE_SliderFocusRect = PySide2.QtWidgets.QStyle.SubElement.SE_SliderFocusRect
    SE_SliderLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_SliderLayoutItem
    SE_SpinBoxLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_SpinBoxLayoutItem
    SE_TabBarScrollLeftButton = PySide2.QtWidgets.QStyle.SubElement.SE_TabBarScrollLeftButton
    SE_TabBarScrollRightButton = PySide2.QtWidgets.QStyle.SubElement.SE_TabBarScrollRightButton
    SE_TabBarTabLeftButton = PySide2.QtWidgets.QStyle.SubElement.SE_TabBarTabLeftButton
    SE_TabBarTabRightButton = PySide2.QtWidgets.QStyle.SubElement.SE_TabBarTabRightButton
    SE_TabBarTabText = PySide2.QtWidgets.QStyle.SubElement.SE_TabBarTabText
    SE_TabBarTearIndicator = PySide2.QtWidgets.QStyle.SubElement.SE_TabBarTearIndicator
    SE_TabBarTearIndicatorLeft = PySide2.QtWidgets.QStyle.SubElement.SE_TabBarTearIndicatorLeft
    SE_TabBarTearIndicatorRight = PySide2.QtWidgets.QStyle.SubElement.SE_TabBarTearIndicatorRight
    SE_TabWidgetLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_TabWidgetLayoutItem
    SE_TabWidgetLeftCorner = PySide2.QtWidgets.QStyle.SubElement.SE_TabWidgetLeftCorner
    SE_TabWidgetRightCorner = PySide2.QtWidgets.QStyle.SubElement.SE_TabWidgetRightCorner
    SE_TabWidgetTabBar = PySide2.QtWidgets.QStyle.SubElement.SE_TabWidgetTabBar
    SE_TabWidgetTabContents = PySide2.QtWidgets.QStyle.SubElement.SE_TabWidgetTabContents
    SE_TabWidgetTabPane = PySide2.QtWidgets.QStyle.SubElement.SE_TabWidgetTabPane
    SE_ToolBarHandle = PySide2.QtWidgets.QStyle.SubElement.SE_ToolBarHandle
    SE_ToolBoxTabContents = PySide2.QtWidgets.QStyle.SubElement.SE_ToolBoxTabContents
    SE_ToolButtonLayoutItem = PySide2.QtWidgets.QStyle.SubElement.SE_ToolButtonLayoutItem
    SE_TreeViewDisclosureItem = PySide2.QtWidgets.QStyle.SubElement.SE_TreeViewDisclosureItem
    SE_ViewItemCheckIndicator = PySide2.QtWidgets.QStyle.SubElement.SE_ViewItemCheckIndicator
    SH_BlinkCursorWhenTextSelected = PySide2.QtWidgets.QStyle.StyleHint.SH_BlinkCursorWhenTextSelected
    SH_Button_FocusPolicy = PySide2.QtWidgets.QStyle.StyleHint.SH_Button_FocusPolicy
    SH_ComboBox_AllowWheelScrolling = PySide2.QtWidgets.QStyle.StyleHint.SH_ComboBox_AllowWheelScrolling
    SH_ComboBox_LayoutDirection = PySide2.QtWidgets.QStyle.StyleHint.SH_ComboBox_LayoutDirection
    SH_ComboBox_ListMouseTracking = PySide2.QtWidgets.QStyle.StyleHint.SH_ComboBox_ListMouseTracking
    SH_ComboBox_Popup = PySide2.QtWidgets.QStyle.StyleHint.SH_ComboBox_Popup
    SH_ComboBox_PopupFrameStyle = PySide2.QtWidgets.QStyle.StyleHint.SH_ComboBox_PopupFrameStyle
    SH_ComboBox_UseNativePopup = PySide2.QtWidgets.QStyle.StyleHint.SH_ComboBox_UseNativePopup
    SH_CustomBase = PySide2.QtWidgets.QStyle.StyleHint.SH_CustomBase
    SH_DialogButtonBox_ButtonsHaveIcons = PySide2.QtWidgets.QStyle.StyleHint.SH_DialogButtonBox_ButtonsHaveIcons
    SH_DialogButtonLayout = PySide2.QtWidgets.QStyle.StyleHint.SH_DialogButtonLayout
    SH_DialogButtons_DefaultButton = PySide2.QtWidgets.QStyle.StyleHint.SH_DialogButtons_DefaultButton
    SH_Dial_BackgroundRole = PySide2.QtWidgets.QStyle.StyleHint.SH_Dial_BackgroundRole
    SH_DitherDisabledText = PySide2.QtWidgets.QStyle.StyleHint.SH_DitherDisabledText
    SH_DockWidget_ButtonsHaveFrame = PySide2.QtWidgets.QStyle.StyleHint.SH_DockWidget_ButtonsHaveFrame
    SH_DrawMenuBarSeparator = PySide2.QtWidgets.QStyle.StyleHint.SH_DrawMenuBarSeparator
    SH_EtchDisabledText = PySide2.QtWidgets.QStyle.StyleHint.SH_EtchDisabledText
    SH_FocusFrame_AboveWidget = PySide2.QtWidgets.QStyle.StyleHint.SH_FocusFrame_AboveWidget
    SH_FocusFrame_Mask = PySide2.QtWidgets.QStyle.StyleHint.SH_FocusFrame_Mask
    SH_FontDialog_SelectAssociatedText = PySide2.QtWidgets.QStyle.StyleHint.SH_FontDialog_SelectAssociatedText
    SH_FormLayoutFieldGrowthPolicy = PySide2.QtWidgets.QStyle.StyleHint.SH_FormLayoutFieldGrowthPolicy
    SH_FormLayoutFormAlignment = PySide2.QtWidgets.QStyle.StyleHint.SH_FormLayoutFormAlignment
    SH_FormLayoutLabelAlignment = PySide2.QtWidgets.QStyle.StyleHint.SH_FormLayoutLabelAlignment
    SH_FormLayoutWrapPolicy = PySide2.QtWidgets.QStyle.StyleHint.SH_FormLayoutWrapPolicy
    SH_GroupBox_TextLabelColor = PySide2.QtWidgets.QStyle.StyleHint.SH_GroupBox_TextLabelColor
    SH_GroupBox_TextLabelVerticalAlignment = PySide2.QtWidgets.QStyle.StyleHint.SH_GroupBox_TextLabelVerticalAlignment
    SH_Header_ArrowAlignment = PySide2.QtWidgets.QStyle.StyleHint.SH_Header_ArrowAlignment
    SH_ItemView_ActivateItemOnSingleClick = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_ActivateItemOnSingleClick
    SH_ItemView_ArrowKeysNavigateIntoChildren = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_ArrowKeysNavigateIntoChildren
    SH_ItemView_ChangeHighlightOnFocus = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_ChangeHighlightOnFocus
    SH_ItemView_DrawDelegateFrame = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_DrawDelegateFrame
    SH_ItemView_EllipsisLocation = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_EllipsisLocation
    SH_ItemView_MovementWithoutUpdatingSelection = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_MovementWithoutUpdatingSelection
    SH_ItemView_PaintAlternatingRowColorsForEmptyArea = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_PaintAlternatingRowColorsForEmptyArea
    SH_ItemView_ScrollMode = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_ScrollMode
    SH_ItemView_ShowDecorationSelected = PySide2.QtWidgets.QStyle.StyleHint.SH_ItemView_ShowDecorationSelected
    SH_LineEdit_PasswordCharacter = PySide2.QtWidgets.QStyle.StyleHint.SH_LineEdit_PasswordCharacter
    SH_LineEdit_PasswordMaskDelay = PySide2.QtWidgets.QStyle.StyleHint.SH_LineEdit_PasswordMaskDelay
    SH_ListViewExpand_SelectMouseType = PySide2.QtWidgets.QStyle.StyleHint.SH_ListViewExpand_SelectMouseType
    SH_MainWindow_SpaceBelowMenuBar = PySide2.QtWidgets.QStyle.StyleHint.SH_MainWindow_SpaceBelowMenuBar
    SH_MenuBar_AltKeyNavigation = PySide2.QtWidgets.QStyle.StyleHint.SH_MenuBar_AltKeyNavigation
    SH_MenuBar_MouseTracking = PySide2.QtWidgets.QStyle.StyleHint.SH_MenuBar_MouseTracking
    SH_Menu_AllowActiveAndDisabled = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_AllowActiveAndDisabled
    SH_Menu_FadeOutOnHide = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_FadeOutOnHide
    SH_Menu_FillScreenWithScroll = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_FillScreenWithScroll
    SH_Menu_FlashTriggeredItem = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_FlashTriggeredItem
    SH_Menu_KeyboardSearch = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_KeyboardSearch
    SH_Menu_Mask = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_Mask
    SH_Menu_MouseTracking = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_MouseTracking
    SH_Menu_Scrollable = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_Scrollable
    SH_Menu_SelectionWrap = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SelectionWrap
    SH_Menu_SloppySubMenus = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SloppySubMenus
    SH_Menu_SpaceActivatesItem = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SpaceActivatesItem
    SH_Menu_SubMenuDontStartSloppyOnLeave = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SubMenuDontStartSloppyOnLeave
    SH_Menu_SubMenuPopupDelay = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SubMenuPopupDelay
    SH_Menu_SubMenuResetWhenReenteringParent = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SubMenuResetWhenReenteringParent
    SH_Menu_SubMenuSloppyCloseTimeout = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SubMenuSloppyCloseTimeout
    SH_Menu_SubMenuSloppySelectOtherActions = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SubMenuSloppySelectOtherActions
    SH_Menu_SubMenuUniDirection = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SubMenuUniDirection
    SH_Menu_SubMenuUniDirectionFailCount = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SubMenuUniDirectionFailCount
    SH_Menu_SupportsSections = PySide2.QtWidgets.QStyle.StyleHint.SH_Menu_SupportsSections
    SH_MessageBox_CenterButtons = PySide2.QtWidgets.QStyle.StyleHint.SH_MessageBox_CenterButtons
    SH_MessageBox_TextInteractionFlags = PySide2.QtWidgets.QStyle.StyleHint.SH_MessageBox_TextInteractionFlags
    SH_MessageBox_UseBorderForButtonSpacing = PySide2.QtWidgets.QStyle.StyleHint.SH_MessageBox_UseBorderForButtonSpacing
    SH_PrintDialog_RightAlignButtons = PySide2.QtWidgets.QStyle.StyleHint.SH_PrintDialog_RightAlignButtons
    SH_ProgressDialog_CenterCancelButton = PySide2.QtWidgets.QStyle.StyleHint.SH_ProgressDialog_CenterCancelButton
    SH_ProgressDialog_TextLabelAlignment = PySide2.QtWidgets.QStyle.StyleHint.SH_ProgressDialog_TextLabelAlignment
    SH_RequestSoftwareInputPanel = PySide2.QtWidgets.QStyle.StyleHint.SH_RequestSoftwareInputPanel
    SH_RichText_FullWidthSelection = PySide2.QtWidgets.QStyle.StyleHint.SH_RichText_FullWidthSelection
    SH_RubberBand_Mask = PySide2.QtWidgets.QStyle.StyleHint.SH_RubberBand_Mask
    SH_ScrollBar_ContextMenu = PySide2.QtWidgets.QStyle.StyleHint.SH_ScrollBar_ContextMenu
    SH_ScrollBar_LeftClickAbsolutePosition = PySide2.QtWidgets.QStyle.StyleHint.SH_ScrollBar_LeftClickAbsolutePosition
    SH_ScrollBar_MiddleClickAbsolutePosition = PySide2.QtWidgets.QStyle.StyleHint.SH_ScrollBar_MiddleClickAbsolutePosition
    SH_ScrollBar_RollBetweenButtons = PySide2.QtWidgets.QStyle.StyleHint.SH_ScrollBar_RollBetweenButtons
    SH_ScrollBar_ScrollWhenPointerLeavesControl = PySide2.QtWidgets.QStyle.StyleHint.SH_ScrollBar_ScrollWhenPointerLeavesControl
    SH_ScrollBar_StopMouseOverSlider = PySide2.QtWidgets.QStyle.StyleHint.SH_ScrollBar_StopMouseOverSlider
    SH_ScrollBar_Transient = PySide2.QtWidgets.QStyle.StyleHint.SH_ScrollBar_Transient
    SH_ScrollView_FrameOnlyAroundContents = PySide2.QtWidgets.QStyle.StyleHint.SH_ScrollView_FrameOnlyAroundContents
    SH_Slider_AbsoluteSetButtons = PySide2.QtWidgets.QStyle.StyleHint.SH_Slider_AbsoluteSetButtons
    SH_Slider_PageSetButtons = PySide2.QtWidgets.QStyle.StyleHint.SH_Slider_PageSetButtons
    SH_Slider_SloppyKeyEvents = PySide2.QtWidgets.QStyle.StyleHint.SH_Slider_SloppyKeyEvents
    SH_Slider_SnapToValue = PySide2.QtWidgets.QStyle.StyleHint.SH_Slider_SnapToValue
    SH_Slider_StopMouseOverSlider = PySide2.QtWidgets.QStyle.StyleHint.SH_Slider_StopMouseOverSlider
    SH_SpellCheckUnderlineStyle = PySide2.QtWidgets.QStyle.StyleHint.SH_SpellCheckUnderlineStyle
    SH_SpinBox_AnimateButton = PySide2.QtWidgets.QStyle.StyleHint.SH_SpinBox_AnimateButton
    SH_SpinBox_ButtonsInsideFrame = PySide2.QtWidgets.QStyle.StyleHint.SH_SpinBox_ButtonsInsideFrame
    SH_SpinBox_ClickAutoRepeatRate = PySide2.QtWidgets.QStyle.StyleHint.SH_SpinBox_ClickAutoRepeatRate
    SH_SpinBox_ClickAutoRepeatThreshold = PySide2.QtWidgets.QStyle.StyleHint.SH_SpinBox_ClickAutoRepeatThreshold
    SH_SpinBox_KeyPressAutoRepeatRate = PySide2.QtWidgets.QStyle.StyleHint.SH_SpinBox_KeyPressAutoRepeatRate
    SH_SpinBox_StepModifier = PySide2.QtWidgets.QStyle.StyleHint.SH_SpinBox_StepModifier
    SH_SpinControls_DisableOnBounds = PySide2.QtWidgets.QStyle.StyleHint.SH_SpinControls_DisableOnBounds
    SH_Splitter_OpaqueResize = PySide2.QtWidgets.QStyle.StyleHint.SH_Splitter_OpaqueResize
    SH_TabBar_Alignment = PySide2.QtWidgets.QStyle.StyleHint.SH_TabBar_Alignment
    SH_TabBar_ChangeCurrentDelay = PySide2.QtWidgets.QStyle.StyleHint.SH_TabBar_ChangeCurrentDelay
    SH_TabBar_CloseButtonPosition = PySide2.QtWidgets.QStyle.StyleHint.SH_TabBar_CloseButtonPosition
    SH_TabBar_ElideMode = PySide2.QtWidgets.QStyle.StyleHint.SH_TabBar_ElideMode
    SH_TabBar_PreferNoArrows = PySide2.QtWidgets.QStyle.StyleHint.SH_TabBar_PreferNoArrows
    SH_TabBar_SelectMouseType = PySide2.QtWidgets.QStyle.StyleHint.SH_TabBar_SelectMouseType
    SH_Table_GridLineColor = PySide2.QtWidgets.QStyle.StyleHint.SH_Table_GridLineColor
    SH_TabWidget_DefaultTabPosition = PySide2.QtWidgets.QStyle.StyleHint.SH_TabWidget_DefaultTabPosition
    SH_TextControl_FocusIndicatorTextCharFormat = PySide2.QtWidgets.QStyle.StyleHint.SH_TextControl_FocusIndicatorTextCharFormat
    SH_TitleBar_AutoRaise = PySide2.QtWidgets.QStyle.StyleHint.SH_TitleBar_AutoRaise
    SH_TitleBar_ModifyNotification = PySide2.QtWidgets.QStyle.StyleHint.SH_TitleBar_ModifyNotification
    SH_TitleBar_NoBorder = PySide2.QtWidgets.QStyle.StyleHint.SH_TitleBar_NoBorder
    SH_TitleBar_ShowToolTipsOnButtons = PySide2.QtWidgets.QStyle.StyleHint.SH_TitleBar_ShowToolTipsOnButtons
    SH_ToolBar_Movable = PySide2.QtWidgets.QStyle.StyleHint.SH_ToolBar_Movable
    SH_ToolBox_SelectedPageTitleBold = PySide2.QtWidgets.QStyle.StyleHint.SH_ToolBox_SelectedPageTitleBold
    SH_ToolButtonStyle = PySide2.QtWidgets.QStyle.StyleHint.SH_ToolButtonStyle
    SH_ToolButton_PopupDelay = PySide2.QtWidgets.QStyle.StyleHint.SH_ToolButton_PopupDelay
    SH_ToolTipLabel_Opacity = PySide2.QtWidgets.QStyle.StyleHint.SH_ToolTipLabel_Opacity
    SH_ToolTip_FallAsleepDelay = PySide2.QtWidgets.QStyle.StyleHint.SH_ToolTip_FallAsleepDelay
    SH_ToolTip_Mask = PySide2.QtWidgets.QStyle.StyleHint.SH_ToolTip_Mask
    SH_ToolTip_WakeUpDelay = PySide2.QtWidgets.QStyle.StyleHint.SH_ToolTip_WakeUpDelay
    SH_UnderlineShortcut = PySide2.QtWidgets.QStyle.StyleHint.SH_UnderlineShortcut
    SH_Widget_Animate = PySide2.QtWidgets.QStyle.StyleHint.SH_Widget_Animate
    SH_Widget_Animation_Duration = PySide2.QtWidgets.QStyle.StyleHint.SH_Widget_Animation_Duration
    SH_Widget_ShareActivation = PySide2.QtWidgets.QStyle.StyleHint.SH_Widget_ShareActivation
    SH_WindowFrame_Mask = PySide2.QtWidgets.QStyle.StyleHint.SH_WindowFrame_Mask
    SH_WizardStyle = PySide2.QtWidgets.QStyle.StyleHint.SH_WizardStyle
    SH_Workspace_FillSpaceOnMaximize = PySide2.QtWidgets.QStyle.StyleHint.SH_Workspace_FillSpaceOnMaximize
    SP_ArrowBack = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ArrowBack
    SP_ArrowDown = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ArrowDown
    SP_ArrowForward = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ArrowForward
    SP_ArrowLeft = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ArrowLeft
    SP_ArrowRight = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ArrowRight
    SP_ArrowUp = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ArrowUp
    SP_BrowserReload = PySide2.QtWidgets.QStyle.StandardPixmap.SP_BrowserReload
    SP_BrowserStop = PySide2.QtWidgets.QStyle.StandardPixmap.SP_BrowserStop
    SP_CommandLink = PySide2.QtWidgets.QStyle.StandardPixmap.SP_CommandLink
    SP_ComputerIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ComputerIcon
    SP_CustomBase = PySide2.QtWidgets.QStyle.StandardPixmap.SP_CustomBase
    SP_DesktopIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DesktopIcon
    SP_DialogAbortButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogAbortButton
    SP_DialogApplyButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogApplyButton
    SP_DialogCancelButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogCancelButton
    SP_DialogCloseButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton
    SP_DialogDiscardButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogDiscardButton
    SP_DialogHelpButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogHelpButton
    SP_DialogIgnoreButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogIgnoreButton
    SP_DialogNoButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogNoButton
    SP_DialogNoToAllButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogNoToAllButton
    SP_DialogOkButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogOkButton
    SP_DialogOpenButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogOpenButton
    SP_DialogResetButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogResetButton
    SP_DialogRetryButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogRetryButton
    SP_DialogSaveAllButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogSaveAllButton
    SP_DialogSaveButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogSaveButton
    SP_DialogYesButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogYesButton
    SP_DialogYesToAllButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DialogYesToAllButton
    SP_DirClosedIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DirClosedIcon
    SP_DirHomeIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DirHomeIcon
    SP_DirIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DirIcon
    SP_DirLinkIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DirLinkIcon
    SP_DirLinkOpenIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DirLinkOpenIcon
    SP_DirOpenIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DirOpenIcon
    SP_DockWidgetCloseButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DockWidgetCloseButton
    SP_DriveCDIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DriveCDIcon
    SP_DriveDVDIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DriveDVDIcon
    SP_DriveFDIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DriveFDIcon
    SP_DriveHDIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DriveHDIcon
    SP_DriveNetIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_DriveNetIcon
    SP_FileDialogBack = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogBack
    SP_FileDialogContentsView = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogContentsView
    SP_FileDialogDetailedView = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogDetailedView
    SP_FileDialogEnd = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogEnd
    SP_FileDialogInfoView = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogInfoView
    SP_FileDialogListView = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogListView
    SP_FileDialogNewFolder = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogNewFolder
    SP_FileDialogStart = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogStart
    SP_FileDialogToParent = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileDialogToParent
    SP_FileIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileIcon
    SP_FileLinkIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_FileLinkIcon
    SP_LineEditClearButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_LineEditClearButton
    SP_MediaPause = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaPause
    SP_MediaPlay = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaPlay
    SP_MediaSeekBackward = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaSeekBackward
    SP_MediaSeekForward = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaSeekForward
    SP_MediaSkipBackward = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaSkipBackward
    SP_MediaSkipForward = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaSkipForward
    SP_MediaStop = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaStop
    SP_MediaVolume = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaVolume
    SP_MediaVolumeMuted = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MediaVolumeMuted
    SP_MessageBoxCritical = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MessageBoxCritical
    SP_MessageBoxInformation = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MessageBoxInformation
    SP_MessageBoxQuestion = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MessageBoxQuestion
    SP_MessageBoxWarning = PySide2.QtWidgets.QStyle.StandardPixmap.SP_MessageBoxWarning
    SP_RestoreDefaultsButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_RestoreDefaultsButton
    SP_TitleBarCloseButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TitleBarCloseButton
    SP_TitleBarContextHelpButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TitleBarContextHelpButton
    SP_TitleBarMaxButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TitleBarMaxButton
    SP_TitleBarMenuButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TitleBarMenuButton
    SP_TitleBarMinButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TitleBarMinButton
    SP_TitleBarNormalButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TitleBarNormalButton
    SP_TitleBarShadeButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TitleBarShadeButton
    SP_TitleBarUnshadeButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TitleBarUnshadeButton
    SP_ToolBarHorizontalExtensionButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ToolBarHorizontalExtensionButton
    SP_ToolBarVerticalExtensionButton = PySide2.QtWidgets.QStyle.StandardPixmap.SP_ToolBarVerticalExtensionButton
    SP_TrashIcon = PySide2.QtWidgets.QStyle.StandardPixmap.SP_TrashIcon
    SP_VistaShield = PySide2.QtWidgets.QStyle.StandardPixmap.SP_VistaShield
    StandardPixmap = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.StandardPixmap'>"
    State = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.State'>"
    StateFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.StateFlag'>"
    State_Active = PySide2.QtWidgets.QStyle.StateFlag.State_Active
    State_AutoRaise = PySide2.QtWidgets.QStyle.StateFlag.State_AutoRaise
    State_Bottom = PySide2.QtWidgets.QStyle.StateFlag.State_Bottom
    State_Children = PySide2.QtWidgets.QStyle.StateFlag.State_Children
    State_DownArrow = PySide2.QtWidgets.QStyle.StateFlag.State_DownArrow
    State_Editing = PySide2.QtWidgets.QStyle.StateFlag.State_Editing
    State_Enabled = PySide2.QtWidgets.QStyle.StateFlag.State_Enabled
    State_FocusAtBorder = PySide2.QtWidgets.QStyle.StateFlag.State_FocusAtBorder
    State_HasFocus = PySide2.QtWidgets.QStyle.StateFlag.State_HasFocus
    State_Horizontal = PySide2.QtWidgets.QStyle.StateFlag.State_Horizontal
    State_Item = PySide2.QtWidgets.QStyle.StateFlag.State_Item
    State_KeyboardFocusChange = PySide2.QtWidgets.QStyle.StateFlag.State_KeyboardFocusChange
    State_Mini = PySide2.QtWidgets.QStyle.StateFlag.State_Mini
    State_MouseOver = PySide2.QtWidgets.QStyle.StateFlag.State_MouseOver
    State_NoChange = PySide2.QtWidgets.QStyle.StateFlag.State_NoChange
    State_None = PySide2.QtWidgets.QStyle.StateFlag.State_None
    State_Off = PySide2.QtWidgets.QStyle.StateFlag.State_Off
    State_On = PySide2.QtWidgets.QStyle.StateFlag.State_On
    State_Open = PySide2.QtWidgets.QStyle.StateFlag.State_Open
    State_Raised = PySide2.QtWidgets.QStyle.StateFlag.State_Raised
    State_ReadOnly = PySide2.QtWidgets.QStyle.StateFlag.State_ReadOnly
    State_Selected = PySide2.QtWidgets.QStyle.StateFlag.State_Selected
    State_Sibling = PySide2.QtWidgets.QStyle.StateFlag.State_Sibling
    State_Small = PySide2.QtWidgets.QStyle.StateFlag.State_Small
    State_Sunken = PySide2.QtWidgets.QStyle.StateFlag.State_Sunken
    State_Top = PySide2.QtWidgets.QStyle.StateFlag.State_Top
    State_UpArrow = PySide2.QtWidgets.QStyle.StateFlag.State_UpArrow
    State_Window = PySide2.QtWidgets.QStyle.StateFlag.State_Window
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50782800>'
    StyleHint = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.StyleHint'>"
    SubControl = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.SubControl'>"
    SubControls = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.SubControls'>"
    SubElement = None # (!) real value is "<class 'PySide2.QtWidgets.QStyle.SubElement'>"


