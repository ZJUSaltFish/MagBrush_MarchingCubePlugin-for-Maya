# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


class QShortcut(__PySide2_QtCore.QObject):
    """
    QShortcut(self, arg__1: PySide2.QtGui.QKeySequence, arg__2: PySide2.QtWidgets.QWidget, arg__3: typing.Callable, arg__4: PySide2.QtCore.Qt.ShortcutContext = PySide2.QtCore.Qt.ShortcutContext.WindowShortcut) -> None
    QShortcut(self, key: PySide2.QtGui.QKeySequence, parent: PySide2.QtWidgets.QWidget, member: typing.Optional[bytes] = None, ambiguousMember: typing.Optional[bytes] = None, shortcutContext: PySide2.QtCore.Qt.ShortcutContext = PySide2.QtCore.Qt.ShortcutContext.WindowShortcut) -> None
    QShortcut(self, parent: PySide2.QtWidgets.QWidget) -> None
    """
    def activated(self, *args, **kwargs): # real signature unknown
        pass

    def activatedAmbiguously(self, *args, **kwargs): # real signature unknown
        pass

    def autoRepeat(self): # real signature unknown; restored from __doc__
        """ autoRepeat(self) -> bool """
        return False

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> PySide2.QtCore.Qt.ShortcutContext """
        pass

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> int """
        return 0

    def isEnabled(self): # real signature unknown; restored from __doc__
        """ isEnabled(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> PySide2.QtGui.QKeySequence """
        pass

    def parentWidget(self): # real signature unknown; restored from __doc__
        """ parentWidget(self) -> PySide2.QtWidgets.QWidget """
        pass

    def setAutoRepeat(self, on): # real signature unknown; restored from __doc__
        """ setAutoRepeat(self, on: bool) -> None """
        pass

    def setContext(self, context): # real signature unknown; restored from __doc__
        """ setContext(self, context: PySide2.QtCore.Qt.ShortcutContext) -> None """
        pass

    def setEnabled(self, enable): # real signature unknown; restored from __doc__
        """ setEnabled(self, enable: bool) -> None """
        pass

    def setKey(self, key): # real signature unknown; restored from __doc__
        """ setKey(self, key: PySide2.QtGui.QKeySequence) -> None """
        pass

    def setWhatsThis(self, text): # real signature unknown; restored from __doc__
        """ setWhatsThis(self, text: str) -> None """
        pass

    def whatsThis(self): # real signature unknown; restored from __doc__
        """ whatsThis(self) -> str """
        return ""

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1, arg__2, arg__3, arg__4=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F50783900>'


