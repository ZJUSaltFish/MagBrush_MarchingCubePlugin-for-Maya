# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QStyleOption import QStyleOption

class QStyleOptionHeader(QStyleOption):
    """
    QStyleOptionHeader(self) -> None
    QStyleOptionHeader(self, other: PySide2.QtWidgets.QStyleOptionHeader) -> None
    QStyleOptionHeader(self, version: int) -> None
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iconAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    section = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selectedPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sortIndicator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    textAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    Beginning = PySide2.QtWidgets.QStyleOptionHeader.SectionPosition.Beginning
    End = PySide2.QtWidgets.QStyleOptionHeader.SectionPosition.End
    Middle = PySide2.QtWidgets.QStyleOptionHeader.SectionPosition.Middle
    NextAndPreviousAreSelected = PySide2.QtWidgets.QStyleOptionHeader.SelectedPosition.NextAndPreviousAreSelected
    NextIsSelected = PySide2.QtWidgets.QStyleOptionHeader.SelectedPosition.NextIsSelected
    None_ = PySide2.QtWidgets.QStyleOptionHeader.SortIndicator.None_
    NotAdjacent = PySide2.QtWidgets.QStyleOptionHeader.SelectedPosition.NotAdjacent
    OnlyOneSection = PySide2.QtWidgets.QStyleOptionHeader.SectionPosition.OnlyOneSection
    PreviousIsSelected = PySide2.QtWidgets.QStyleOptionHeader.SelectedPosition.PreviousIsSelected
    SectionPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionHeader.SectionPosition'>"
    SelectedPosition = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionHeader.SelectedPosition'>"
    SortDown = PySide2.QtWidgets.QStyleOptionHeader.SortIndicator.SortDown
    SortIndicator = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionHeader.SortIndicator'>"
    SortUp = PySide2.QtWidgets.QStyleOptionHeader.SortIndicator.SortUp
    StyleOptionType = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionHeader.StyleOptionType'>"
    StyleOptionVersion = None # (!) real value is "<class 'PySide2.QtWidgets.QStyleOptionHeader.StyleOptionVersion'>"
    Type = PySide2.QtWidgets.QStyleOptionHeader.StyleOptionType.Type
    Version = PySide2.QtWidgets.QStyleOptionHeader.StyleOptionVersion.Version


