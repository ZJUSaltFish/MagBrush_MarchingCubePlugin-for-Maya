# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QEvent import QEvent

class QChildEvent(QEvent):
    """ QChildEvent(self, type: PySide2.QtCore.QEvent.Type, child: PySide2.QtCore.QObject) -> None """
    def added(self): # real signature unknown; restored from __doc__
        """ added(self) -> bool """
        return False

    def child(self): # real signature unknown; restored from __doc__
        """ child(self) -> PySide2.QtCore.QObject """
        pass

    def polished(self): # real signature unknown; restored from __doc__
        """ polished(self) -> bool """
        return False

    def removed(self): # real signature unknown; restored from __doc__
        """ removed(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type, child): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


