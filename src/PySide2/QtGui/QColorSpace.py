# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QColorSpace(__Shiboken.Object):
    """
    QColorSpace(self) -> None
    QColorSpace(self, colorSpace: PySide2.QtGui.QColorSpace) -> None
    QColorSpace(self, namedColorSpace: PySide2.QtGui.QColorSpace.NamedColorSpace) -> None
    QColorSpace(self, primaries: PySide2.QtGui.QColorSpace.Primaries, fun: PySide2.QtGui.QColorSpace.TransferFunction, gamma: float = 0.0) -> None
    QColorSpace(self, primaries: PySide2.QtGui.QColorSpace.Primaries, gamma: float) -> None
    QColorSpace(self, whitePoint: PySide2.QtCore.QPointF, redPoint: PySide2.QtCore.QPointF, greenPoint: PySide2.QtCore.QPointF, bluePoint: PySide2.QtCore.QPointF, fun: PySide2.QtGui.QColorSpace.TransferFunction, gamma: float = 0.0) -> None
    """
    def fromIccProfile(self, iccProfile): # real signature unknown; restored from __doc__
        """ fromIccProfile(iccProfile: PySide2.QtCore.QByteArray) -> PySide2.QtGui.QColorSpace """
        pass

    def gamma(self): # real signature unknown; restored from __doc__
        """ gamma(self) -> float """
        return 0.0

    def iccProfile(self): # real signature unknown; restored from __doc__
        """ iccProfile(self) -> PySide2.QtCore.QByteArray """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def primaries(self): # real signature unknown; restored from __doc__
        """ primaries(self) -> PySide2.QtGui.QColorSpace.Primaries """
        pass

    def setPrimaries(self, primariesId): # real signature unknown; restored from __doc__
        """
        setPrimaries(self, primariesId: PySide2.QtGui.QColorSpace.Primaries) -> None
        setPrimaries(self, whitePoint: PySide2.QtCore.QPointF, redPoint: PySide2.QtCore.QPointF, greenPoint: PySide2.QtCore.QPointF, bluePoint: PySide2.QtCore.QPointF) -> None
        """
        pass

    def setTransferFunction(self, transferFunction, gamma=0.0): # real signature unknown; restored from __doc__
        """ setTransferFunction(self, transferFunction: PySide2.QtGui.QColorSpace.TransferFunction, gamma: float = 0.0) -> None """
        pass

    def swap(self, colorSpace): # real signature unknown; restored from __doc__
        """ swap(self, colorSpace: PySide2.QtGui.QColorSpace) -> None """
        pass

    def transferFunction(self): # real signature unknown; restored from __doc__
        """ transferFunction(self) -> PySide2.QtGui.QColorSpace.TransferFunction """
        pass

    def withTransferFunction(self, transferFunction, gamma=0.0): # real signature unknown; restored from __doc__
        """ withTransferFunction(self, transferFunction: PySide2.QtGui.QColorSpace.TransferFunction, gamma: float = 0.0) -> PySide2.QtGui.QColorSpace """
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

    AdobeRgb = PySide2.QtGui.QColorSpace.NamedColorSpace.AdobeRgb
    DisplayP3 = PySide2.QtGui.QColorSpace.NamedColorSpace.DisplayP3
    NamedColorSpace = None # (!) real value is "<class 'PySide2.QtGui.QColorSpace.NamedColorSpace'>"
    Primaries = None # (!) real value is "<class 'PySide2.QtGui.QColorSpace.Primaries'>"
    ProPhotoRgb = PySide2.QtGui.QColorSpace.NamedColorSpace.ProPhotoRgb
    SRgb = PySide2.QtGui.QColorSpace.NamedColorSpace.SRgb
    SRgbLinear = PySide2.QtGui.QColorSpace.NamedColorSpace.SRgbLinear
    TransferFunction = None # (!) real value is "<class 'PySide2.QtGui.QColorSpace.TransferFunction'>"
    __hash__ = None


