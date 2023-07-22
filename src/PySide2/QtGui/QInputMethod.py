# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QInputMethod(__PySide2_QtCore.QObject):
    # no doc
    def anchorRectangle(self): # real signature unknown; restored from __doc__
        """ anchorRectangle(self) -> PySide2.QtCore.QRectF """
        pass

    def anchorRectangleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def animatingChanged(self, *args, **kwargs): # real signature unknown
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit(self) -> None """
        pass

    def cursorRectangle(self): # real signature unknown; restored from __doc__
        """ cursorRectangle(self) -> PySide2.QtCore.QRectF """
        pass

    def cursorRectangleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) -> None """
        pass

    def inputDirection(self): # real signature unknown; restored from __doc__
        """ inputDirection(self) -> PySide2.QtCore.Qt.LayoutDirection """
        pass

    def inputDirectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def inputItemClipRectangle(self): # real signature unknown; restored from __doc__
        """ inputItemClipRectangle(self) -> PySide2.QtCore.QRectF """
        pass

    def inputItemClipRectangleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def inputItemRectangle(self): # real signature unknown; restored from __doc__
        """ inputItemRectangle(self) -> PySide2.QtCore.QRectF """
        pass

    def inputItemTransform(self): # real signature unknown; restored from __doc__
        """ inputItemTransform(self) -> PySide2.QtGui.QTransform """
        pass

    def invokeAction(self, a, cursorPosition): # real signature unknown; restored from __doc__
        """ invokeAction(self, a: PySide2.QtGui.QInputMethod.Action, cursorPosition: int) -> None """
        pass

    def isAnimating(self): # real signature unknown; restored from __doc__
        """ isAnimating(self) -> bool """
        return False

    def isVisible(self): # real signature unknown; restored from __doc__
        """ isVisible(self) -> bool """
        return False

    def keyboardRectangle(self): # real signature unknown; restored from __doc__
        """ keyboardRectangle(self) -> PySide2.QtCore.QRectF """
        pass

    def keyboardRectangleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def locale(self): # real signature unknown; restored from __doc__
        """ locale(self) -> PySide2.QtCore.QLocale """
        pass

    def localeChanged(self, *args, **kwargs): # real signature unknown
        pass

    def queryFocusObject(self, query, argument): # real signature unknown; restored from __doc__
        """ queryFocusObject(query: PySide2.QtCore.Qt.InputMethodQuery, argument: typing.Any) -> typing.Any """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> None """
        pass

    def setInputItemRectangle(self, rect): # real signature unknown; restored from __doc__
        """ setInputItemRectangle(self, rect: PySide2.QtCore.QRectF) -> None """
        pass

    def setInputItemTransform(self, transform): # real signature unknown; restored from __doc__
        """ setInputItemTransform(self, transform: PySide2.QtGui.QTransform) -> None """
        pass

    def setVisible(self, visible): # real signature unknown; restored from __doc__
        """ setVisible(self, visible: bool) -> None """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) -> None """
        pass

    def update(self, queries): # real signature unknown; restored from __doc__
        """ update(self, queries: PySide2.QtCore.Qt.InputMethodQueries) -> None """
        pass

    def visibleChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Action = None # (!) real value is "<class 'PySide2.QtGui.QInputMethod.Action'>"
    Click = PySide2.QtGui.QInputMethod.Action.Click
    ContextMenu = PySide2.QtGui.QInputMethod.Action.ContextMenu
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00832700>'


