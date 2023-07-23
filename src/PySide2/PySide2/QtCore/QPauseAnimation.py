# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QAbstractAnimation import QAbstractAnimation

class QPauseAnimation(QAbstractAnimation):
    """
    QPauseAnimation(self, msecs: int, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QPauseAnimation(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def duration(self): # real signature unknown; restored from __doc__
        """ duration(self) -> int """
        return 0

    def event(self, e): # real signature unknown; restored from __doc__
        """ event(self, e: PySide2.QtCore.QEvent) -> bool """
        return False

    def setDuration(self, msecs): # real signature unknown; restored from __doc__
        """ setDuration(self, msecs: int) -> None """
        pass

    def updateCurrentTime(self, arg__1): # real signature unknown; restored from __doc__
        """ updateCurrentTime(self, arg__1: int) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, msecs, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221E64D00>'


