# encoding: utf-8
# module PySide2.QtWidgets
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWidgets.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtGui as __PySide2_QtGui
import Shiboken as __Shiboken


from .QGesture import QGesture

class QPinchGesture(QGesture):
    """ QPinchGesture(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def centerPoint(self): # real signature unknown; restored from __doc__
        """ centerPoint(self) -> PySide2.QtCore.QPointF """
        pass

    def changeFlags(self): # real signature unknown; restored from __doc__
        """ changeFlags(self) -> PySide2.QtWidgets.QPinchGesture.ChangeFlags """
        pass

    def lastCenterPoint(self): # real signature unknown; restored from __doc__
        """ lastCenterPoint(self) -> PySide2.QtCore.QPointF """
        pass

    def lastRotationAngle(self): # real signature unknown; restored from __doc__
        """ lastRotationAngle(self) -> float """
        return 0.0

    def lastScaleFactor(self): # real signature unknown; restored from __doc__
        """ lastScaleFactor(self) -> float """
        return 0.0

    def rotationAngle(self): # real signature unknown; restored from __doc__
        """ rotationAngle(self) -> float """
        return 0.0

    def scaleFactor(self): # real signature unknown; restored from __doc__
        """ scaleFactor(self) -> float """
        return 0.0

    def setCenterPoint(self, value): # real signature unknown; restored from __doc__
        """ setCenterPoint(self, value: PySide2.QtCore.QPointF) -> None """
        pass

    def setChangeFlags(self, value): # real signature unknown; restored from __doc__
        """ setChangeFlags(self, value: PySide2.QtWidgets.QPinchGesture.ChangeFlags) -> None """
        pass

    def setLastCenterPoint(self, value): # real signature unknown; restored from __doc__
        """ setLastCenterPoint(self, value: PySide2.QtCore.QPointF) -> None """
        pass

    def setLastRotationAngle(self, value): # real signature unknown; restored from __doc__
        """ setLastRotationAngle(self, value: float) -> None """
        pass

    def setLastScaleFactor(self, value): # real signature unknown; restored from __doc__
        """ setLastScaleFactor(self, value: float) -> None """
        pass

    def setRotationAngle(self, value): # real signature unknown; restored from __doc__
        """ setRotationAngle(self, value: float) -> None """
        pass

    def setScaleFactor(self, value): # real signature unknown; restored from __doc__
        """ setScaleFactor(self, value: float) -> None """
        pass

    def setStartCenterPoint(self, value): # real signature unknown; restored from __doc__
        """ setStartCenterPoint(self, value: PySide2.QtCore.QPointF) -> None """
        pass

    def setTotalChangeFlags(self, value): # real signature unknown; restored from __doc__
        """ setTotalChangeFlags(self, value: PySide2.QtWidgets.QPinchGesture.ChangeFlags) -> None """
        pass

    def setTotalRotationAngle(self, value): # real signature unknown; restored from __doc__
        """ setTotalRotationAngle(self, value: float) -> None """
        pass

    def setTotalScaleFactor(self, value): # real signature unknown; restored from __doc__
        """ setTotalScaleFactor(self, value: float) -> None """
        pass

    def startCenterPoint(self): # real signature unknown; restored from __doc__
        """ startCenterPoint(self) -> PySide2.QtCore.QPointF """
        pass

    def totalChangeFlags(self): # real signature unknown; restored from __doc__
        """ totalChangeFlags(self) -> PySide2.QtWidgets.QPinchGesture.ChangeFlags """
        pass

    def totalRotationAngle(self): # real signature unknown; restored from __doc__
        """ totalRotationAngle(self) -> float """
        return 0.0

    def totalScaleFactor(self): # real signature unknown; restored from __doc__
        """ totalScaleFactor(self) -> float """
        return 0.0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    CenterPointChanged = PySide2.QtWidgets.QPinchGesture.ChangeFlag.CenterPointChanged
    ChangeFlag = None # (!) real value is "<class 'PySide2.QtWidgets.QPinchGesture.ChangeFlag'>"
    ChangeFlags = None # (!) real value is "<class 'PySide2.QtWidgets.QPinchGesture.ChangeFlags'>"
    RotationAngleChanged = PySide2.QtWidgets.QPinchGesture.ChangeFlag.RotationAngleChanged
    ScaleFactorChanged = PySide2.QtWidgets.QPinchGesture.ChangeFlag.ScaleFactorChanged
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000014F5085BA40>'


