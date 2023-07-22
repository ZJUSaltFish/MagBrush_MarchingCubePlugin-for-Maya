# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QSizePolicy(__Shiboken.Object):
    """
    QSizePolicy(self) -> None
    QSizePolicy(self, horizontal: PySide2.QtWidgets.QSizePolicy.Policy, vertical: PySide2.QtWidgets.QSizePolicy.Policy, type: PySide2.QtWidgets.QSizePolicy.ControlType = PySide2.QtWidgets.QSizePolicy.ControlType.DefaultType) -> None
    """
    def controlType(self): # real signature unknown; restored from __doc__
        """ controlType(self) -> PySide2.QtWidgets.QSizePolicy.ControlType """
        pass

    def expandingDirections(self): # real signature unknown; restored from __doc__
        """ expandingDirections(self) -> PySide2.QtCore.Qt.Orientations """
        pass

    def hasHeightForWidth(self): # real signature unknown; restored from __doc__
        """ hasHeightForWidth(self) -> bool """
        return False

    def hasWidthForHeight(self): # real signature unknown; restored from __doc__
        """ hasWidthForHeight(self) -> bool """
        return False

    def horizontalPolicy(self): # real signature unknown; restored from __doc__
        """ horizontalPolicy(self) -> PySide2.QtWidgets.QSizePolicy.Policy """
        pass

    def horizontalStretch(self): # real signature unknown; restored from __doc__
        """ horizontalStretch(self) -> int """
        return 0

    def retainSizeWhenHidden(self): # real signature unknown; restored from __doc__
        """ retainSizeWhenHidden(self) -> bool """
        return False

    def setControlType(self, type): # real signature unknown; restored from __doc__
        """ setControlType(self, type: PySide2.QtWidgets.QSizePolicy.ControlType) -> None """
        pass

    def setHeightForWidth(self, b): # real signature unknown; restored from __doc__
        """ setHeightForWidth(self, b: bool) -> None """
        pass

    def setHorizontalPolicy(self, d): # real signature unknown; restored from __doc__
        """ setHorizontalPolicy(self, d: PySide2.QtWidgets.QSizePolicy.Policy) -> None """
        pass

    def setHorizontalStretch(self, stretchFactor): # real signature unknown; restored from __doc__
        """ setHorizontalStretch(self, stretchFactor: int) -> None """
        pass

    def setRetainSizeWhenHidden(self, retainSize): # real signature unknown; restored from __doc__
        """ setRetainSizeWhenHidden(self, retainSize: bool) -> None """
        pass

    def setVerticalPolicy(self, d): # real signature unknown; restored from __doc__
        """ setVerticalPolicy(self, d: PySide2.QtWidgets.QSizePolicy.Policy) -> None """
        pass

    def setVerticalStretch(self, stretchFactor): # real signature unknown; restored from __doc__
        """ setVerticalStretch(self, stretchFactor: int) -> None """
        pass

    def setWidthForHeight(self, b): # real signature unknown; restored from __doc__
        """ setWidthForHeight(self, b: bool) -> None """
        pass

    def transpose(self): # real signature unknown; restored from __doc__
        """ transpose(self) -> None """
        pass

    def transposed(self): # real signature unknown; restored from __doc__
        """ transposed(self) -> PySide2.QtWidgets.QSizePolicy """
        pass

    def verticalPolicy(self): # real signature unknown; restored from __doc__
        """ verticalPolicy(self) -> PySide2.QtWidgets.QSizePolicy.Policy """
        pass

    def verticalStretch(self): # real signature unknown; restored from __doc__
        """ verticalStretch(self) -> int """
        return 0

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

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
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

    def __rshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __rshift__(self, arg__1: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    ButtonBox = PySide2.QtWidgets.QSizePolicy.ControlType.ButtonBox
    CheckBox = PySide2.QtWidgets.QSizePolicy.ControlType.CheckBox
    ComboBox = PySide2.QtWidgets.QSizePolicy.ControlType.ComboBox
    ControlType = None # (!) real value is "<class 'PySide2.QtWidgets.QSizePolicy.ControlType'>"
    ControlTypes = None # (!) real value is "<class 'PySide2.QtWidgets.QSizePolicy.ControlTypes'>"
    DefaultType = PySide2.QtWidgets.QSizePolicy.ControlType.DefaultType
    ExpandFlag = PySide2.QtWidgets.QSizePolicy.PolicyFlag.ExpandFlag
    Expanding = PySide2.QtWidgets.QSizePolicy.Policy.Expanding
    Fixed = PySide2.QtWidgets.QSizePolicy.Policy.Fixed
    Frame = PySide2.QtWidgets.QSizePolicy.ControlType.Frame
    GroupBox = PySide2.QtWidgets.QSizePolicy.ControlType.GroupBox
    GrowFlag = PySide2.QtWidgets.QSizePolicy.PolicyFlag.GrowFlag
    Ignored = PySide2.QtWidgets.QSizePolicy.Policy.Ignored
    IgnoreFlag = PySide2.QtWidgets.QSizePolicy.PolicyFlag.IgnoreFlag
    Label = PySide2.QtWidgets.QSizePolicy.ControlType.Label
    Line = PySide2.QtWidgets.QSizePolicy.ControlType.Line
    LineEdit = PySide2.QtWidgets.QSizePolicy.ControlType.LineEdit
    Maximum = PySide2.QtWidgets.QSizePolicy.Policy.Maximum
    Minimum = PySide2.QtWidgets.QSizePolicy.Policy.Minimum
    MinimumExpanding = PySide2.QtWidgets.QSizePolicy.Policy.MinimumExpanding
    Policy = None # (!) real value is "<class 'PySide2.QtWidgets.QSizePolicy.Policy'>"
    PolicyFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QSizePolicy.PolicyFlag'>"
    Preferred = PySide2.QtWidgets.QSizePolicy.Policy.Preferred
    PushButton = PySide2.QtWidgets.QSizePolicy.ControlType.PushButton
    RadioButton = PySide2.QtWidgets.QSizePolicy.ControlType.RadioButton
    ShrinkFlag = PySide2.QtWidgets.QSizePolicy.PolicyFlag.ShrinkFlag
    Slider = PySide2.QtWidgets.QSizePolicy.ControlType.Slider
    SpinBox = PySide2.QtWidgets.QSizePolicy.ControlType.SpinBox
    TabWidget = PySide2.QtWidgets.QSizePolicy.ControlType.TabWidget
    ToolButton = PySide2.QtWidgets.QSizePolicy.ControlType.ToolButton
    __hash__ = None


