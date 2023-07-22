# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSound(__PySide2_QtCore.QObject):
    """ QSound(self, filename: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def loops(self): # real signature unknown; restored from __doc__
        """ loops(self) -> int """
        return 0

    def loopsRemaining(self): # real signature unknown; restored from __doc__
        """ loopsRemaining(self) -> int """
        return 0

    def play(self, filename): # real signature unknown; restored from __doc__
        """
        play(filename: str) -> None
        play(self) -> None
        """
        pass

    def setLoops(self, arg__1): # real signature unknown; restored from __doc__
        """ setLoops(self, arg__1: int) -> None """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, filename, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Infinite = PySide2.QtMultimedia.QSound.Loop.Infinite
    Loop = None # (!) real value is "<class 'PySide2.QtMultimedia.QSound.Loop'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001887464E9C0>'


