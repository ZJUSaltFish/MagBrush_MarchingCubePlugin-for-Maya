# encoding: utf-8
# module PyQt5.QtWebChannel
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtWebChannel.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore


# no functions
# classes

class QWebChannel(__PyQt5_QtCore.QObject):
    """ QWebChannel(parent: typing.Optional[QObject] = None) """
    def blockUpdates(self): # real signature unknown; restored from __doc__
        """ blockUpdates(self) -> bool """
        return False

    def blockUpdatesChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def connectTo(self, transport): # real signature unknown; restored from __doc__
        """ connectTo(self, transport: QWebChannelAbstractTransport) """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def deregisterObject(self, p_object): # real signature unknown; restored from __doc__
        """ deregisterObject(self, object: QObject) """
        pass

    def disconnectFrom(self, transport): # real signature unknown; restored from __doc__
        """ disconnectFrom(self, transport: QWebChannelAbstractTransport) """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registeredObjects(self): # real signature unknown; restored from __doc__
        """ registeredObjects(self) -> Dict[str, QObject] """
        return {}

    def registerObject(self, id, p_object): # real signature unknown; restored from __doc__
        """ registerObject(self, id: str, object: QObject) """
        pass

    def registerObjects(self, objects, p_str=None, QObject=None): # real signature unknown; restored from __doc__
        """ registerObjects(self, objects: Dict[str, QObject]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBlockUpdates(self, block): # real signature unknown; restored from __doc__
        """ setBlockUpdates(self, block: bool) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QWebChannelAbstractTransport(__PyQt5_QtCore.QObject):
    """ QWebChannelAbstractTransport(parent: typing.Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def messageReceived(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def sendMessage(self, message, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ sendMessage(self, message: Dict[str, Union[QJsonValue, QJsonValue.Type, Iterable[QJsonValue], bool, int, float, None, str]]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


# variables with complex values



