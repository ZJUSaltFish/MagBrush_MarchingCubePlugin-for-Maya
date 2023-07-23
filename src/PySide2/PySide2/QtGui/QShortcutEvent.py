# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QShortcutEvent(__PySide2_QtCore.QEvent):
    """ QShortcutEvent(self, key: PySide2.QtGui.QKeySequence, id: int, ambiguous: bool = False) -> None """
    def isAmbiguous(self): # real signature unknown; restored from __doc__
        """ isAmbiguous(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> PySide2.QtGui.QKeySequence """
        pass

    def shortcutId(self): # real signature unknown; restored from __doc__
        """ shortcutId(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, key, id, ambiguous=False): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


