# encoding: utf-8
# module PySide2.QtWebChannel
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtWebChannel.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore


# no functions
# classes

class QWebChannel(__PySide2_QtCore.QObject):
    """ QWebChannel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def blockUpdates(self): # real signature unknown; restored from __doc__
        """ blockUpdates(self) -> bool """
        return False

    def blockUpdatesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def connectTo(self, transport): # real signature unknown; restored from __doc__
        """ connectTo(self, transport: PySide2.QtWebChannel.QWebChannelAbstractTransport) -> None """
        pass

    def deregisterObject(self, p_object): # real signature unknown; restored from __doc__
        """ deregisterObject(self, object: PySide2.QtCore.QObject) -> None """
        pass

    def disconnectFrom(self, transport): # real signature unknown; restored from __doc__
        """ disconnectFrom(self, transport: PySide2.QtWebChannel.QWebChannelAbstractTransport) -> None """
        pass

    def registeredObjects(self): # real signature unknown; restored from __doc__
        """ registeredObjects(self) -> typing.Dict[str, PySide2.QtCore.QObject] """
        pass

    def registerObject(self, id, p_object): # real signature unknown; restored from __doc__
        """ registerObject(self, id: str, object: PySide2.QtCore.QObject) -> None """
        pass

    def registerObjects(self, objects, p_str=None, PySide2_QtCore_QObject=None): # real signature unknown; restored from __doc__
        """ registerObjects(self, objects: typing.Dict[str, PySide2.QtCore.QObject]) -> None """
        pass

    def setBlockUpdates(self, block): # real signature unknown; restored from __doc__
        """ setBlockUpdates(self, block: bool) -> None """
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000284D0A50100>'


class QWebChannelAbstractTransport(__PySide2_QtCore.QObject):
    """ QWebChannelAbstractTransport(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def messageReceived(self, *args, **kwargs): # real signature unknown
        pass

    def sendMessage(self, message, p_str=None, PySide2_QtCore_QJsonValue=None): # real signature unknown; restored from __doc__
        """ sendMessage(self, message: typing.Dict[str, PySide2.QtCore.QJsonValue]) -> None """
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000284D00E6E40>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000284CFE717B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtWebChannel', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000284CFE717B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtWebChannel.cp310-win_amd64.pyd')"

