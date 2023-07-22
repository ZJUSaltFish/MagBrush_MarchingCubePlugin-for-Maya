# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QTouchDevice(__Shiboken.Object):
    """ QTouchDevice(self) -> None """
    def capabilities(self): # real signature unknown; restored from __doc__
        """ capabilities(self) -> PySide2.QtGui.QTouchDevice.Capabilities """
        pass

    def devices(self): # real signature unknown; restored from __doc__
        """ devices() -> typing.List[PySide2.QtGui.QTouchDevice] """
        pass

    def maximumTouchPoints(self): # real signature unknown; restored from __doc__
        """ maximumTouchPoints(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def setCapabilities(self, caps): # real signature unknown; restored from __doc__
        """ setCapabilities(self, caps: PySide2.QtGui.QTouchDevice.Capabilities) -> None """
        pass

    def setMaximumTouchPoints(self, max): # real signature unknown; restored from __doc__
        """ setMaximumTouchPoints(self, max: int) -> None """
        pass

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def setType(self, devType): # real signature unknown; restored from __doc__
        """ setType(self, devType: PySide2.QtGui.QTouchDevice.DeviceType) -> None """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtGui.QTouchDevice.DeviceType """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Area = PySide2.QtGui.QTouchDevice.CapabilityFlag.Area
    Capabilities = None # (!) real value is "<class 'PySide2.QtGui.QTouchDevice.Capabilities'>"
    CapabilityFlag = None # (!) real value is "<class 'PySide2.QtGui.QTouchDevice.CapabilityFlag'>"
    DeviceType = None # (!) real value is "<class 'PySide2.QtGui.QTouchDevice.DeviceType'>"
    MouseEmulation = PySide2.QtGui.QTouchDevice.CapabilityFlag.MouseEmulation
    NormalizedPosition = PySide2.QtGui.QTouchDevice.CapabilityFlag.NormalizedPosition
    Position = PySide2.QtGui.QTouchDevice.CapabilityFlag.Position
    Pressure = PySide2.QtGui.QTouchDevice.CapabilityFlag.Pressure
    RawPositions = PySide2.QtGui.QTouchDevice.CapabilityFlag.RawPositions
    TouchPad = PySide2.QtGui.QTouchDevice.DeviceType.TouchPad
    TouchScreen = PySide2.QtGui.QTouchDevice.DeviceType.TouchScreen
    Velocity = PySide2.QtGui.QTouchDevice.CapabilityFlag.Velocity


