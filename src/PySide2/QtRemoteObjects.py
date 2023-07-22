# encoding: utf-8
# module PySide2.QtRemoteObjects
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtRemoteObjects.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QAbstractItemModelReplica(__PySide2_QtCore.QAbstractItemModel):
    # no doc
    def availableRoles(self): # real signature unknown; restored from __doc__
        """ availableRoles(self) -> typing.List[int] """
        pass

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def data(self, index, role=None): # real signature unknown; restored from __doc__
        """ data(self, index: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def hasChildren(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasChildren(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def hasData(self, index, role): # real signature unknown; restored from __doc__
        """ hasData(self, index: PySide2.QtCore.QModelIndex, role: int) -> bool """
        return False

    def headerData(self, section, orientation, role): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int) -> typing.Any """
        pass

    def index(self, row, column, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ index(self, row: int, column: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> PySide2.QtCore.QModelIndex """
        pass

    def initialized(self, *args, **kwargs): # real signature unknown
        pass

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def parent(self): # real signature unknown; restored from __doc__
        """
        parent(self) -> PySide2.QtCore.QObject
        parent(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex
        """
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ roleNames(self) -> typing.Dict[int, PySide2.QtCore.QByteArray] """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def selectionModel(self): # real signature unknown; restored from __doc__
        """ selectionModel(self) -> PySide2.QtCore.QItemSelectionModel """
        pass

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D45980>'


class QRemoteObjectAbstractPersistedStore(__PySide2_QtCore.QObject):
    """ QRemoteObjectAbstractPersistedStore(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def restoreProperties(self, repName, repSig): # real signature unknown; restored from __doc__
        """ restoreProperties(self, repName: str, repSig: PySide2.QtCore.QByteArray) -> typing.List[typing.Any] """
        pass

    def saveProperties(self, repName, repSig, values, typing_Any=None): # real signature unknown; restored from __doc__
        """ saveProperties(self, repName: str, repSig: PySide2.QtCore.QByteArray, values: typing.Sequence[typing.Any]) -> None """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D44600>'


class QRemoteObjectReplica(__PySide2_QtCore.QObject):
    """ QRemoteObjectReplica(self) -> None """
    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) -> None """
        pass

    def initialized(self, *args, **kwargs): # real signature unknown
        pass

    def initializeNode(self, node, name=''): # real signature unknown; restored from __doc__
        """ initializeNode(self, node: PySide2.QtRemoteObjects.QRemoteObjectNode, name: str = '') -> None """
        pass

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def isReplicaValid(self): # real signature unknown; restored from __doc__
        """ isReplicaValid(self) -> bool """
        return False

    def node(self): # real signature unknown; restored from __doc__
        """ node(self) -> PySide2.QtRemoteObjects.QRemoteObjectNode """
        pass

    def notified(self, *args, **kwargs): # real signature unknown
        pass

    def persistProperties(self, repName, repSig, props, typing_Any=None): # real signature unknown; restored from __doc__
        """ persistProperties(self, repName: str, repSig: PySide2.QtCore.QByteArray, props: typing.Sequence[typing.Any]) -> None """
        pass

    def propAsVariant(self, i): # real signature unknown; restored from __doc__
        """ propAsVariant(self, i: int) -> typing.Any """
        pass

    def retrieveProperties(self, repName, repSig): # real signature unknown; restored from __doc__
        """ retrieveProperties(self, repName: str, repSig: PySide2.QtCore.QByteArray) -> typing.List[typing.Any] """
        pass

    def send(self, call, index, args, typing_Any=None): # real signature unknown; restored from __doc__
        """ send(self, call: PySide2.QtCore.QMetaObject.Call, index: int, args: typing.Sequence[typing.Any]) -> None """
        pass

    def sendWithReply(self, call, index, args, typing_Any=None): # real signature unknown; restored from __doc__
        """ sendWithReply(self, call: PySide2.QtCore.QMetaObject.Call, index: int, args: typing.Sequence[typing.Any]) -> PySide2.QtRemoteObjects.QRemoteObjectPendingCall """
        pass

    def setChild(self, i, arg__2): # real signature unknown; restored from __doc__
        """ setChild(self, i: int, arg__2: typing.Any) -> None """
        pass

    def setNode(self, node): # real signature unknown; restored from __doc__
        """ setNode(self, node: PySide2.QtRemoteObjects.QRemoteObjectNode) -> None """
        pass

    def setProperties(self, arg__1, typing_Any=None): # real signature unknown; restored from __doc__
        """ setProperties(self, arg__1: typing.Sequence[typing.Any]) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtRemoteObjects.QRemoteObjectReplica.State """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def waitForSource(self, timeout=30000): # real signature unknown; restored from __doc__
        """ waitForSource(self, timeout: int = 30000) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Default = PySide2.QtRemoteObjects.QRemoteObjectReplica.State.Default
    SignatureMismatch = PySide2.QtRemoteObjects.QRemoteObjectReplica.State.SignatureMismatch
    State = None # (!) real value is "<class 'PySide2.QtRemoteObjects.QRemoteObjectReplica.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D44D00>'
    Suspect = PySide2.QtRemoteObjects.QRemoteObjectReplica.State.Suspect
    Uninitialized = PySide2.QtRemoteObjects.QRemoteObjectReplica.State.Uninitialized
    Valid = PySide2.QtRemoteObjects.QRemoteObjectReplica.State.Valid


class QRemoteObjectDynamicReplica(QRemoteObjectReplica):
    # no doc
    def initialized(self, *args, **kwargs): # real signature unknown
        pass

    def notified(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D44FC0>'


class QRemoteObjectNode(__PySide2_QtCore.QObject):
    """
    QRemoteObjectNode(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QRemoteObjectNode(self, registryAddress: PySide2.QtCore.QUrl, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def acquireDynamic(self, name): # real signature unknown; restored from __doc__
        """ acquireDynamic(self, name: str) -> PySide2.QtRemoteObjects.QRemoteObjectDynamicReplica """
        pass

    def acquireModel(self, name): # real signature unknown; restored from __doc__
        """ acquireModel(self, name: str) -> PySide2.QtRemoteObjects.QAbstractItemModelReplica """
        pass

    def addClientSideConnection(self, ioDevice): # real signature unknown; restored from __doc__
        """ addClientSideConnection(self, ioDevice: PySide2.QtCore.QIODevice) -> None """
        pass

    def connectToNode(self, address): # real signature unknown; restored from __doc__
        """ connectToNode(self, address: PySide2.QtCore.QUrl) -> bool """
        return False

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def heartbeatInterval(self): # real signature unknown; restored from __doc__
        """ heartbeatInterval(self) -> int """
        return 0

    def heartbeatIntervalChanged(self, *args, **kwargs): # real signature unknown
        pass

    def instances(self, typeName): # real signature unknown; restored from __doc__
        """ instances(self, typeName: str) -> typing.List[str] """
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode """
        pass

    def persistedStore(self): # real signature unknown; restored from __doc__
        """ persistedStore(self) -> PySide2.QtRemoteObjects.QRemoteObjectAbstractPersistedStore """
        pass

    def registry(self): # real signature unknown; restored from __doc__
        """ registry(self) -> PySide2.QtRemoteObjects.QRemoteObjectRegistry """
        pass

    def registryUrl(self): # real signature unknown; restored from __doc__
        """ registryUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def remoteObjectAdded(self, *args, **kwargs): # real signature unknown
        pass

    def remoteObjectRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def setHeartbeatInterval(self, interval): # real signature unknown; restored from __doc__
        """ setHeartbeatInterval(self, interval: int) -> None """
        pass

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def setPersistedStore(self, persistedStore): # real signature unknown; restored from __doc__
        """ setPersistedStore(self, persistedStore: PySide2.QtRemoteObjects.QRemoteObjectAbstractPersistedStore) -> None """
        pass

    def setRegistryUrl(self, registryAddress): # real signature unknown; restored from __doc__
        """ setRegistryUrl(self, registryAddress: PySide2.QtCore.QUrl) -> bool """
        return False

    def timerEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ timerEvent(self, arg__1: PySide2.QtCore.QTimerEvent) -> None """
        pass

    def waitForRegistry(self, timeout=30000): # real signature unknown; restored from __doc__
        """ waitForRegistry(self, timeout: int = 30000) -> bool """
        return False

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

    ErrorCode = None # (!) real value is "<class 'PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode'>"
    HostUrlInvalid = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.HostUrlInvalid
    ListenFailed = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.ListenFailed
    MissingObjectName = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.MissingObjectName
    NodeIsNoServer = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.NodeIsNoServer
    NoError = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.NoError
    OperationNotValidOnClientNode = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.OperationNotValidOnClientNode
    ProtocolMismatch = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.ProtocolMismatch
    RegistryAlreadyHosted = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.RegistryAlreadyHosted
    RegistryNotAcquired = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.RegistryNotAcquired
    ServerAlreadyCreated = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.ServerAlreadyCreated
    SourceNotRegistered = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.SourceNotRegistered
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D44500>'
    UnintendedRegistryHosting = PySide2.QtRemoteObjects.QRemoteObjectNode.ErrorCode.UnintendedRegistryHosting


class QRemoteObjectHostBase(QRemoteObjectNode):
    # no doc
    def addHostSideConnection(self, ioDevice): # real signature unknown; restored from __doc__
        """ addHostSideConnection(self, ioDevice: PySide2.QtCore.QIODevice) -> None """
        pass

    def disableRemoting(self, remoteObject): # real signature unknown; restored from __doc__
        """ disableRemoting(self, remoteObject: PySide2.QtCore.QObject) -> bool """
        return False

    def enableRemoting(self, model, name, roles, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        enableRemoting(self, model: PySide2.QtCore.QAbstractItemModel, name: str, roles: typing.List[int], selectionModel: typing.Optional[PySide2.QtCore.QItemSelectionModel] = None) -> bool
        enableRemoting(self, object: PySide2.QtCore.QObject, name: str = '') -> bool
        """
        pass

    def hostUrl(self): # real signature unknown; restored from __doc__
        """ hostUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def proxy(self, registryUrl, hostUrl={}): # real signature unknown; restored from __doc__
        """ proxy(self, registryUrl: PySide2.QtCore.QUrl, hostUrl: PySide2.QtCore.QUrl = {}) -> bool """
        return False

    def reverseProxy(self): # real signature unknown; restored from __doc__
        """ reverseProxy(self) -> bool """
        return False

    def setHostUrl(self, hostAddress, allowedSchemas=None): # real signature unknown; restored from __doc__
        """ setHostUrl(self, hostAddress: PySide2.QtCore.QUrl, allowedSchemas: PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas = PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly) -> bool """
        return False

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AllowedSchemas = None # (!) real value is "<class 'PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas'>"
    AllowExternalRegistration = PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.AllowExternalRegistration
    BuiltInSchemasOnly = PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D45540>'


class QRemoteObjectHost(QRemoteObjectHostBase):
    """
    QRemoteObjectHost(self, address: PySide2.QtCore.QUrl, parent: PySide2.QtCore.QObject) -> None
    QRemoteObjectHost(self, address: PySide2.QtCore.QUrl, registryAddress: PySide2.QtCore.QUrl = Default(QUrl), allowedSchemas: PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas = PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QRemoteObjectHost(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def hostUrl(self): # real signature unknown; restored from __doc__
        """ hostUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def hostUrlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setHostUrl(self, hostAddress, allowedSchemas=None): # real signature unknown; restored from __doc__
        """ setHostUrl(self, hostAddress: PySide2.QtCore.QUrl, allowedSchemas: PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas = PySide2.QtRemoteObjects.QRemoteObjectHostBase.AllowedSchemas.BuiltInSchemasOnly) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, address, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D45680>'


class QRemoteObjectPendingCall(__Shiboken.Object):
    """
    QRemoteObjectPendingCall(self) -> None
    QRemoteObjectPendingCall(self, other: PySide2.QtRemoteObjects.QRemoteObjectPendingCall) -> None
    """
    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtRemoteObjects.QRemoteObjectPendingCall.Error """
        pass

    def fromCompletedCall(self, returnValue): # real signature unknown; restored from __doc__
        """ fromCompletedCall(returnValue: typing.Any) -> PySide2.QtRemoteObjects.QRemoteObjectPendingCall """
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def returnValue(self): # real signature unknown; restored from __doc__
        """ returnValue(self) -> typing.Any """
        pass

    def waitForFinished(self, timeout=30000): # real signature unknown; restored from __doc__
        """ waitForFinished(self, timeout: int = 30000) -> bool """
        return False

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Error = None # (!) real value is "<class 'PySide2.QtRemoteObjects.QRemoteObjectPendingCall.Error'>"
    InvalidMessage = PySide2.QtRemoteObjects.QRemoteObjectPendingCall.Error.InvalidMessage
    NoError = PySide2.QtRemoteObjects.QRemoteObjectPendingCall.Error.NoError


class QRemoteObjectPendingCallWatcher(__PySide2_QtCore.QObject, QRemoteObjectPendingCall):
    """ QRemoteObjectPendingCallWatcher(self, call: PySide2.QtRemoteObjects.QRemoteObjectPendingCall, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def isFinished(self): # real signature unknown; restored from __doc__
        """ isFinished(self) -> bool """
        return False

    def waitForFinished(self): # real signature unknown; restored from __doc__
        """ waitForFinished(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, call, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D45100>'


class QRemoteObjectRegistry(QRemoteObjectReplica):
    # no doc
    def addSource(self, entry, p_str=None, PySide2_QtRemoteObjects_QRemoteObjectSourceLocationInfo=None): # real signature unknown; restored from __doc__
        """ addSource(self, entry: typing.Tuple[str, PySide2.QtRemoteObjects.QRemoteObjectSourceLocationInfo]) -> None """
        pass

    def initialize(self): # real signature unknown; restored from __doc__
        """ initialize(self) -> None """
        pass

    def pushToRegistryIfNeeded(self): # real signature unknown; restored from __doc__
        """ pushToRegistryIfNeeded(self) -> None """
        pass

    def registerMetatypes(self): # real signature unknown; restored from __doc__
        """ registerMetatypes() -> None """
        pass

    def remoteObjectAdded(self, *args, **kwargs): # real signature unknown
        pass

    def remoteObjectRemoved(self, *args, **kwargs): # real signature unknown
        pass

    def removeSource(self, entry, p_str=None, PySide2_QtRemoteObjects_QRemoteObjectSourceLocationInfo=None): # real signature unknown; restored from __doc__
        """ removeSource(self, entry: typing.Tuple[str, PySide2.QtRemoteObjects.QRemoteObjectSourceLocationInfo]) -> None """
        pass

    def sourceLocations(self): # real signature unknown; restored from __doc__
        """ sourceLocations(self) -> typing.Dict[str, PySide2.QtRemoteObjects.QRemoteObjectSourceLocationInfo] """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D44EC0>'


class QRemoteObjectRegistryHost(QRemoteObjectHostBase):
    """ QRemoteObjectRegistryHost(self, registryAddress: PySide2.QtCore.QUrl = Default(QUrl), parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def setRegistryUrl(self, registryUrl): # real signature unknown; restored from __doc__
        """ setRegistryUrl(self, registryUrl: PySide2.QtCore.QUrl) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, registryAddress=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D45800>'


class QRemoteObjectSettingsStore(QRemoteObjectAbstractPersistedStore):
    """ QRemoteObjectSettingsStore(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def restoreProperties(self, repName, repSig): # real signature unknown; restored from __doc__
        """ restoreProperties(self, repName: str, repSig: PySide2.QtCore.QByteArray) -> typing.List[typing.Any] """
        pass

    def saveProperties(self, repName, repSig, values, typing_Any=None): # real signature unknown; restored from __doc__
        """ saveProperties(self, repName: str, repSig: PySide2.QtCore.QByteArray, values: typing.Sequence[typing.Any]) -> None """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000025DF4D44700>'


class QRemoteObjectSourceLocationInfo(__Shiboken.Object):
    """
    QRemoteObjectSourceLocationInfo(self) -> None
    QRemoteObjectSourceLocationInfo(self, QRemoteObjectSourceLocationInfo: PySide2.QtRemoteObjects.QRemoteObjectSourceLocationInfo) -> None
    QRemoteObjectSourceLocationInfo(self, typeName_: str, hostUrl_: PySide2.QtCore.QUrl) -> None
    """
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

    def __lshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __lshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
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

    def __rshift__(self, stream): # real signature unknown; restored from __doc__
        """
        __rshift__(self, stream: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    hostUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025DF41917B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtRemoteObjects', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025DF41917B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtRemoteObjects.cp310-win_amd64.pyd')"

