# encoding: utf-8
# module PySide2.QtSensors
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSensors.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSensorManager(__Shiboken.Object):
    """ QSensorManager(self) -> None """
    def createBackend(self, sensor): # real signature unknown; restored from __doc__
        """ createBackend(sensor: PySide2.QtSensors.QSensor) -> PySide2.QtSensors.QSensorBackend """
        pass

    def isBackendRegistered(self, type, identifier): # real signature unknown; restored from __doc__
        """ isBackendRegistered(type: PySide2.QtCore.QByteArray, identifier: PySide2.QtCore.QByteArray) -> bool """
        return False

    def registerBackend(self, type, identifier, factory): # real signature unknown; restored from __doc__
        """ registerBackend(type: PySide2.QtCore.QByteArray, identifier: PySide2.QtCore.QByteArray, factory: PySide2.QtSensors.QSensorBackendFactory) -> None """
        pass

    def setDefaultBackend(self, type, identifier): # real signature unknown; restored from __doc__
        """ setDefaultBackend(type: PySide2.QtCore.QByteArray, identifier: PySide2.QtCore.QByteArray) -> None """
        pass

    def unregisterBackend(self, type, identifier): # real signature unknown; restored from __doc__
        """ unregisterBackend(type: PySide2.QtCore.QByteArray, identifier: PySide2.QtCore.QByteArray) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


