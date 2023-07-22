# encoding: utf-8
# module PySide2.QtMultimedia
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtMultimedia.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QMediaTimeRange(__Shiboken.Object):
    """
    QMediaTimeRange(self) -> None
    QMediaTimeRange(self, arg__1: PySide2.QtMultimedia.QMediaTimeInterval) -> None
    QMediaTimeRange(self, range: PySide2.QtMultimedia.QMediaTimeRange) -> None
    QMediaTimeRange(self, start: int, end: int) -> None
    """
    def addInterval(self, interval): # real signature unknown; restored from __doc__
        """
        addInterval(self, interval: PySide2.QtMultimedia.QMediaTimeInterval) -> None
        addInterval(self, start: int, end: int) -> None
        """
        pass

    def addTimeRange(self, arg__1): # real signature unknown; restored from __doc__
        """ addTimeRange(self, arg__1: PySide2.QtMultimedia.QMediaTimeRange) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def contains(self, time): # real signature unknown; restored from __doc__
        """ contains(self, time: int) -> bool """
        return False

    def earliestTime(self): # real signature unknown; restored from __doc__
        """ earliestTime(self) -> int """
        return 0

    def intervals(self): # real signature unknown; restored from __doc__
        """ intervals(self) -> typing.List[PySide2.QtMultimedia.QMediaTimeInterval] """
        pass

    def isContinuous(self): # real signature unknown; restored from __doc__
        """ isContinuous(self) -> bool """
        return False

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def latestTime(self): # real signature unknown; restored from __doc__
        """ latestTime(self) -> int """
        return 0

    def removeInterval(self, interval): # real signature unknown; restored from __doc__
        """
        removeInterval(self, interval: PySide2.QtMultimedia.QMediaTimeInterval) -> None
        removeInterval(self, start: int, end: int) -> None
        """
        pass

    def removeTimeRange(self, arg__1): # real signature unknown; restored from __doc__
        """ removeTimeRange(self, arg__1: PySide2.QtMultimedia.QMediaTimeRange) -> None """
        pass

    def __add__(self, arg__2): # real signature unknown; restored from __doc__
        """
        __add__(self, arg__2: PySide2.QtMultimedia.QMediaTimeRange) -> PySide2.QtMultimedia.QMediaTimeRange
        
        Return self+value.
        """
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

    def __iadd__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __iadd__(self, arg__1: PySide2.QtMultimedia.QMediaTimeInterval) -> PySide2.QtMultimedia.QMediaTimeRange
        __iadd__(self, arg__1: PySide2.QtMultimedia.QMediaTimeRange) -> PySide2.QtMultimedia.QMediaTimeRange
        
        Return self+=value.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __isub__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __isub__(self, arg__1: PySide2.QtMultimedia.QMediaTimeInterval) -> PySide2.QtMultimedia.QMediaTimeRange
        __isub__(self, arg__1: PySide2.QtMultimedia.QMediaTimeRange) -> PySide2.QtMultimedia.QMediaTimeRange
        
        Return self-=value.
        """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __sub__(self, arg__2): # real signature unknown; restored from __doc__
        """
        __sub__(self, arg__2: PySide2.QtMultimedia.QMediaTimeRange) -> PySide2.QtMultimedia.QMediaTimeRange
        
        Return self-value.
        """
        pass

    __hash__ = None


