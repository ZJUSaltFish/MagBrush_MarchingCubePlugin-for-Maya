# encoding: utf-8
# module PySide2.QtScxml
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtScxml.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QScxmlCompiler(__Shiboken.Object):
    """ QScxmlCompiler(self, xmlReader: PySide2.QtCore.QXmlStreamReader) -> None """
    def compile(self): # real signature unknown; restored from __doc__
        """ compile(self) -> PySide2.QtScxml.QScxmlStateMachine """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> typing.List[PySide2.QtScxml.QScxmlError] """
        pass

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def loader(self): # real signature unknown; restored from __doc__
        """ loader(self) -> PySide2.QtScxml.QScxmlCompiler.Loader """
        pass

    def setFileName(self, fileName): # real signature unknown; restored from __doc__
        """ setFileName(self, fileName: str) -> None """
        pass

    def setLoader(self, newLoader): # real signature unknown; restored from __doc__
        """ setLoader(self, newLoader: PySide2.QtScxml.QScxmlCompiler.Loader) -> None """
        pass

    def __init__(self, xmlReader): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Loader = None # (!) real value is "<class 'PySide2.QtScxml.QScxmlCompiler.Loader'>"


class QScxmlDataModel(__PySide2_QtCore.QObject):
    """ QScxmlDataModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def evaluateAssignment(self, id): # real signature unknown; restored from __doc__
        """ evaluateAssignment(self, id: int) -> bool """
        return False

    def evaluateForeach(self, id, body): # real signature unknown; restored from __doc__
        """ evaluateForeach(self, id: int, body: PySide2.QtScxml.QScxmlDataModel.ForeachLoopBody) -> bool """
        return False

    def evaluateInitialization(self, id): # real signature unknown; restored from __doc__
        """ evaluateInitialization(self, id: int) -> bool """
        return False

    def evaluateToBool(self, id): # real signature unknown; restored from __doc__
        """ evaluateToBool(self, id: int) -> typing.Tuple[bool, bool] """
        pass

    def evaluateToString(self, id): # real signature unknown; restored from __doc__
        """ evaluateToString(self, id: int) -> typing.Tuple[str, bool] """
        pass

    def evaluateToVariant(self, id): # real signature unknown; restored from __doc__
        """ evaluateToVariant(self, id: int) -> typing.Tuple[typing.Any, bool] """
        pass

    def evaluateToVoid(self, id): # real signature unknown; restored from __doc__
        """ evaluateToVoid(self, id: int) -> bool """
        return False

    def hasScxmlProperty(self, name): # real signature unknown; restored from __doc__
        """ hasScxmlProperty(self, name: str) -> bool """
        return False

    def scxmlProperty(self, name): # real signature unknown; restored from __doc__
        """ scxmlProperty(self, name: str) -> typing.Any """
        pass

    def setScxmlEvent(self, event): # real signature unknown; restored from __doc__
        """ setScxmlEvent(self, event: PySide2.QtScxml.QScxmlEvent) -> None """
        pass

    def setScxmlProperty(self, name, value, context): # real signature unknown; restored from __doc__
        """ setScxmlProperty(self, name: str, value: typing.Any, context: str) -> bool """
        return False

    def setStateMachine(self, stateMachine): # real signature unknown; restored from __doc__
        """ setStateMachine(self, stateMachine: PySide2.QtScxml.QScxmlStateMachine) -> None """
        pass

    def setup(self, initialDataValues, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setup(self, initialDataValues: typing.Dict[str, typing.Any]) -> bool """
        return False

    def stateMachine(self): # real signature unknown; restored from __doc__
        """ stateMachine(self) -> PySide2.QtScxml.QScxmlStateMachine """
        pass

    def stateMachineChanged(self, *args, **kwargs): # real signature unknown
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

    ForeachLoopBody = None # (!) real value is "<class 'PySide2.QtScxml.QScxmlDataModel.ForeachLoopBody'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A32780>'


class QScxmlCppDataModel(QScxmlDataModel):
    """ QScxmlCppDataModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def evaluateAssignment(self, id): # real signature unknown; restored from __doc__
        """ evaluateAssignment(self, id: int) -> bool """
        return False

    def evaluateForeach(self, id, body): # real signature unknown; restored from __doc__
        """ evaluateForeach(self, id: int, body: PySide2.QtScxml.QScxmlDataModel.ForeachLoopBody) -> bool """
        return False

    def evaluateInitialization(self, id): # real signature unknown; restored from __doc__
        """ evaluateInitialization(self, id: int) -> bool """
        return False

    def hasScxmlProperty(self, name): # real signature unknown; restored from __doc__
        """ hasScxmlProperty(self, name: str) -> bool """
        return False

    def inState(self, stateName): # real signature unknown; restored from __doc__
        """ inState(self, stateName: str) -> bool """
        return False

    def scxmlEvent(self): # real signature unknown; restored from __doc__
        """ scxmlEvent(self) -> PySide2.QtScxml.QScxmlEvent """
        pass

    def scxmlProperty(self, name): # real signature unknown; restored from __doc__
        """ scxmlProperty(self, name: str) -> typing.Any """
        pass

    def setScxmlEvent(self, scxmlEvent): # real signature unknown; restored from __doc__
        """ setScxmlEvent(self, scxmlEvent: PySide2.QtScxml.QScxmlEvent) -> None """
        pass

    def setScxmlProperty(self, name, value, context): # real signature unknown; restored from __doc__
        """ setScxmlProperty(self, name: str, value: typing.Any, context: str) -> bool """
        return False

    def setup(self, initialDataValues, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setup(self, initialDataValues: typing.Dict[str, typing.Any]) -> bool """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A32940>'


class QScxmlInvokableServiceFactory(__PySide2_QtCore.QObject):
    """ QScxmlInvokableServiceFactory(self, invokeInfo: PySide2.QtScxml.QScxmlExecutableContent.InvokeInfo, names: typing.List[int], parameters: typing.List[PySide2.QtScxml.QScxmlExecutableContent.ParameterInfo], parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def invoke(self, parentStateMachine): # real signature unknown; restored from __doc__
        """ invoke(self, parentStateMachine: PySide2.QtScxml.QScxmlStateMachine) -> PySide2.QtScxml.QScxmlInvokableService """
        pass

    def invokeInfo(self): # real signature unknown; restored from __doc__
        """ invokeInfo(self) -> PySide2.QtScxml.QScxmlExecutableContent.InvokeInfo """
        pass

    def names(self): # real signature unknown; restored from __doc__
        """ names(self) -> typing.List[int] """
        pass

    def parameters(self): # real signature unknown; restored from __doc__
        """ parameters(self) -> typing.List[PySide2.QtScxml.QScxmlExecutableContent.ParameterInfo] """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, invokeInfo, names, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A32080>'


class QScxmlDynamicScxmlServiceFactory(QScxmlInvokableServiceFactory):
    """ QScxmlDynamicScxmlServiceFactory(self, invokeInfo: PySide2.QtScxml.QScxmlExecutableContent.InvokeInfo, names: typing.List[int], parameters: typing.List[PySide2.QtScxml.QScxmlExecutableContent.ParameterInfo], parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def invoke(self, parentStateMachine): # real signature unknown; restored from __doc__
        """ invoke(self, parentStateMachine: PySide2.QtScxml.QScxmlStateMachine) -> PySide2.QtScxml.QScxmlInvokableService """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, invokeInfo, names, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A322C0>'


class QScxmlEcmaScriptDataModel(QScxmlDataModel):
    """ QScxmlEcmaScriptDataModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def evaluateAssignment(self, id): # real signature unknown; restored from __doc__
        """ evaluateAssignment(self, id: int) -> bool """
        return False

    def evaluateForeach(self, id, body): # real signature unknown; restored from __doc__
        """ evaluateForeach(self, id: int, body: PySide2.QtScxml.QScxmlDataModel.ForeachLoopBody) -> bool """
        return False

    def evaluateInitialization(self, id): # real signature unknown; restored from __doc__
        """ evaluateInitialization(self, id: int) -> bool """
        return False

    def evaluateToBool(self, id): # real signature unknown; restored from __doc__
        """ evaluateToBool(self, id: int) -> typing.Tuple[bool, bool] """
        pass

    def evaluateToString(self, id): # real signature unknown; restored from __doc__
        """ evaluateToString(self, id: int) -> typing.Tuple[str, bool] """
        pass

    def evaluateToVariant(self, id): # real signature unknown; restored from __doc__
        """ evaluateToVariant(self, id: int) -> typing.Tuple[typing.Any, bool] """
        pass

    def evaluateToVoid(self, id): # real signature unknown; restored from __doc__
        """ evaluateToVoid(self, id: int) -> bool """
        return False

    def hasScxmlProperty(self, name): # real signature unknown; restored from __doc__
        """ hasScxmlProperty(self, name: str) -> bool """
        return False

    def scxmlProperty(self, name): # real signature unknown; restored from __doc__
        """ scxmlProperty(self, name: str) -> typing.Any """
        pass

    def setScxmlEvent(self, event): # real signature unknown; restored from __doc__
        """ setScxmlEvent(self, event: PySide2.QtScxml.QScxmlEvent) -> None """
        pass

    def setScxmlProperty(self, name, value, context): # real signature unknown; restored from __doc__
        """ setScxmlProperty(self, name: str, value: typing.Any, context: str) -> bool """
        return False

    def setup(self, initialDataValues, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setup(self, initialDataValues: typing.Dict[str, typing.Any]) -> bool """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A32CC0>'


class QScxmlError(__Shiboken.Object):
    """
    QScxmlError(self) -> None
    QScxmlError(self, arg__1: PySide2.QtScxml.QScxmlError) -> None
    QScxmlError(self, fileName: str, line: int, column: int, description: str) -> None
    """
    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ line(self) -> int """
        return 0

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QScxmlEvent(__Shiboken.Object):
    """
    QScxmlEvent(self) -> None
    QScxmlEvent(self, other: PySide2.QtScxml.QScxmlEvent) -> None
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> typing.Any """
        pass

    def delay(self): # real signature unknown; restored from __doc__
        """ delay(self) -> int """
        return 0

    def errorMessage(self): # real signature unknown; restored from __doc__
        """ errorMessage(self) -> str """
        return ""

    def eventType(self): # real signature unknown; restored from __doc__
        """ eventType(self) -> PySide2.QtScxml.QScxmlEvent.EventType """
        pass

    def invokeId(self): # real signature unknown; restored from __doc__
        """ invokeId(self) -> str """
        return ""

    def isErrorEvent(self): # real signature unknown; restored from __doc__
        """ isErrorEvent(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def origin(self): # real signature unknown; restored from __doc__
        """ origin(self) -> str """
        return ""

    def originType(self): # real signature unknown; restored from __doc__
        """ originType(self) -> str """
        return ""

    def scxmlType(self): # real signature unknown; restored from __doc__
        """ scxmlType(self) -> str """
        return ""

    def sendId(self): # real signature unknown; restored from __doc__
        """ sendId(self) -> str """
        return ""

    def setData(self, data): # real signature unknown; restored from __doc__
        """ setData(self, data: typing.Any) -> None """
        pass

    def setDelay(self, delayInMiliSecs): # real signature unknown; restored from __doc__
        """ setDelay(self, delayInMiliSecs: int) -> None """
        pass

    def setErrorMessage(self, message): # real signature unknown; restored from __doc__
        """ setErrorMessage(self, message: str) -> None """
        pass

    def setEventType(self, type): # real signature unknown; restored from __doc__
        """ setEventType(self, type: PySide2.QtScxml.QScxmlEvent.EventType) -> None """
        pass

    def setInvokeId(self, invokeId): # real signature unknown; restored from __doc__
        """ setInvokeId(self, invokeId: str) -> None """
        pass

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def setOrigin(self, origin): # real signature unknown; restored from __doc__
        """ setOrigin(self, origin: str) -> None """
        pass

    def setOriginType(self, originType): # real signature unknown; restored from __doc__
        """ setOriginType(self, originType: str) -> None """
        pass

    def setSendId(self, sendId): # real signature unknown; restored from __doc__
        """ setSendId(self, sendId: str) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    EventType = None # (!) real value is "<class 'PySide2.QtScxml.QScxmlEvent.EventType'>"
    ExternalEvent = PySide2.QtScxml.QScxmlEvent.EventType.ExternalEvent
    InternalEvent = PySide2.QtScxml.QScxmlEvent.EventType.InternalEvent
    PlatformEvent = PySide2.QtScxml.QScxmlEvent.EventType.PlatformEvent


class QScxmlExecutableContent(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AssignmentInfo = None # (!) real value is "<class 'PySide2.QtScxml.QScxmlExecutableContent.AssignmentInfo'>"
    EvaluatorInfo = None # (!) real value is "<class 'PySide2.QtScxml.QScxmlExecutableContent.EvaluatorInfo'>"
    ForeachInfo = None # (!) real value is "<class 'PySide2.QtScxml.QScxmlExecutableContent.ForeachInfo'>"
    InvokeInfo = None # (!) real value is "<class 'PySide2.QtScxml.QScxmlExecutableContent.InvokeInfo'>"
    ParameterInfo = None # (!) real value is "<class 'PySide2.QtScxml.QScxmlExecutableContent.ParameterInfo'>"


class QScxmlInvokableService(__PySide2_QtCore.QObject):
    """ QScxmlInvokableService(self, parentStateMachine: PySide2.QtScxml.QScxmlStateMachine, parent: PySide2.QtScxml.QScxmlInvokableServiceFactory) -> None """
    def id(self): # real signature unknown; restored from __doc__
        """ id(self) -> str """
        return ""

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def parentStateMachine(self): # real signature unknown; restored from __doc__
        """ parentStateMachine(self) -> PySide2.QtScxml.QScxmlStateMachine """
        pass

    def postEvent(self, event): # real signature unknown; restored from __doc__
        """ postEvent(self, event: PySide2.QtScxml.QScxmlEvent) -> None """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> bool """
        return False

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parentStateMachine, parent): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A323C0>'


class QScxmlNullDataModel(QScxmlDataModel):
    """ QScxmlNullDataModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def evaluateAssignment(self, id): # real signature unknown; restored from __doc__
        """ evaluateAssignment(self, id: int) -> bool """
        return False

    def evaluateForeach(self, id, body): # real signature unknown; restored from __doc__
        """ evaluateForeach(self, id: int, body: PySide2.QtScxml.QScxmlDataModel.ForeachLoopBody) -> bool """
        return False

    def evaluateInitialization(self, id): # real signature unknown; restored from __doc__
        """ evaluateInitialization(self, id: int) -> bool """
        return False

    def evaluateToBool(self, id): # real signature unknown; restored from __doc__
        """ evaluateToBool(self, id: int) -> typing.Tuple[bool, bool] """
        pass

    def evaluateToString(self, id): # real signature unknown; restored from __doc__
        """ evaluateToString(self, id: int) -> typing.Tuple[str, bool] """
        pass

    def evaluateToVariant(self, id): # real signature unknown; restored from __doc__
        """ evaluateToVariant(self, id: int) -> typing.Tuple[typing.Any, bool] """
        pass

    def evaluateToVoid(self, id): # real signature unknown; restored from __doc__
        """ evaluateToVoid(self, id: int) -> bool """
        return False

    def hasScxmlProperty(self, name): # real signature unknown; restored from __doc__
        """ hasScxmlProperty(self, name: str) -> bool """
        return False

    def scxmlProperty(self, name): # real signature unknown; restored from __doc__
        """ scxmlProperty(self, name: str) -> typing.Any """
        pass

    def setScxmlEvent(self, event): # real signature unknown; restored from __doc__
        """ setScxmlEvent(self, event: PySide2.QtScxml.QScxmlEvent) -> None """
        pass

    def setScxmlProperty(self, name, value, context): # real signature unknown; restored from __doc__
        """ setScxmlProperty(self, name: str, value: typing.Any, context: str) -> bool """
        return False

    def setup(self, initialDataValues, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setup(self, initialDataValues: typing.Dict[str, typing.Any]) -> bool """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A32BC0>'


class QScxmlStateMachine(__PySide2_QtCore.QObject):
    """ QScxmlStateMachine(self, metaObject: PySide2.QtCore.QMetaObject, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def activeStateNames(self, compress=True): # real signature unknown; restored from __doc__
        """ activeStateNames(self, compress: bool = True) -> typing.List[str] """
        pass

    def cancelDelayedEvent(self, sendId): # real signature unknown; restored from __doc__
        """ cancelDelayedEvent(self, sendId: str) -> None """
        pass

    def connectToEvent(self, scxmlEventSpec, receiver, method, type=None): # real signature unknown; restored from __doc__
        """ connectToEvent(self, scxmlEventSpec: str, receiver: PySide2.QtCore.QObject, method: bytes, type: PySide2.QtCore.Qt.ConnectionType = PySide2.QtCore.Qt.ConnectionType.AutoConnection) -> PySide2.QtCore.QMetaObject.Connection """
        pass

    def connectToState(self, scxmlStateName, receiver, method, type=None): # real signature unknown; restored from __doc__
        """ connectToState(self, scxmlStateName: str, receiver: PySide2.QtCore.QObject, method: bytes, type: PySide2.QtCore.Qt.ConnectionType = PySide2.QtCore.Qt.ConnectionType.AutoConnection) -> PySide2.QtCore.QMetaObject.Connection """
        pass

    def dataModel(self): # real signature unknown; restored from __doc__
        """ dataModel(self) -> PySide2.QtScxml.QScxmlDataModel """
        pass

    def dataModelChanged(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def fromData(self, data, fileName=''): # real signature unknown; restored from __doc__
        """ fromData(data: PySide2.QtCore.QIODevice, fileName: str = '') -> PySide2.QtScxml.QScxmlStateMachine """
        pass

    def fromFile(self, fileName): # real signature unknown; restored from __doc__
        """ fromFile(fileName: str) -> PySide2.QtScxml.QScxmlStateMachine """
        pass

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) -> bool """
        return False

    def initializedChanged(self, *args, **kwargs): # real signature unknown
        pass

    def initialValues(self): # real signature unknown; restored from __doc__
        """ initialValues(self) -> typing.Dict[str, typing.Any] """
        pass

    def initialValuesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def invokedServices(self): # real signature unknown; restored from __doc__
        """ invokedServices(self) -> typing.List[PySide2.QtScxml.QScxmlInvokableService] """
        pass

    def invokedServicesChanged(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, scxmlStateName): # real signature unknown; restored from __doc__
        """
        isActive(self, scxmlStateName: str) -> bool
        isActive(self, stateIndex: int) -> bool
        """
        return False

    def isDispatchableTarget(self, target): # real signature unknown; restored from __doc__
        """ isDispatchableTarget(self, target: str) -> bool """
        return False

    def isInitialized(self): # real signature unknown; restored from __doc__
        """ isInitialized(self) -> bool """
        return False

    def isInvoked(self): # real signature unknown; restored from __doc__
        """ isInvoked(self) -> bool """
        return False

    def isRunning(self): # real signature unknown; restored from __doc__
        """ isRunning(self) -> bool """
        return False

    def loader(self): # real signature unknown; restored from __doc__
        """ loader(self) -> PySide2.QtScxml.QScxmlCompiler.Loader """
        pass

    def loaderChanged(self, *args, **kwargs): # real signature unknown
        pass

    def log(self, *args, **kwargs): # real signature unknown
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def parseErrors(self): # real signature unknown; restored from __doc__
        """ parseErrors(self) -> typing.List[PySide2.QtScxml.QScxmlError] """
        pass

    def reachedStableState(self, *args, **kwargs): # real signature unknown
        pass

    def runningChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sessionId(self): # real signature unknown; restored from __doc__
        """ sessionId(self) -> str """
        return ""

    def setDataModel(self, model): # real signature unknown; restored from __doc__
        """ setDataModel(self, model: PySide2.QtScxml.QScxmlDataModel) -> None """
        pass

    def setInitialValues(self, initialValues, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setInitialValues(self, initialValues: typing.Dict[str, typing.Any]) -> None """
        pass

    def setLoader(self, loader): # real signature unknown; restored from __doc__
        """ setLoader(self, loader: PySide2.QtScxml.QScxmlCompiler.Loader) -> None """
        pass

    def setRunning(self, running): # real signature unknown; restored from __doc__
        """ setRunning(self, running: bool) -> None """
        pass

    def setTableData(self, tableData): # real signature unknown; restored from __doc__
        """ setTableData(self, tableData: PySide2.QtScxml.QScxmlTableData) -> None """
        pass

    def start(self): # real signature unknown; restored from __doc__
        """ start(self) -> None """
        pass

    def stateNames(self, compress=True): # real signature unknown; restored from __doc__
        """ stateNames(self, compress: bool = True) -> typing.List[str] """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) -> None """
        pass

    def submitEvent(self, event): # real signature unknown; restored from __doc__
        """
        submitEvent(self, event: PySide2.QtScxml.QScxmlEvent) -> None
        submitEvent(self, eventName: str) -> None
        submitEvent(self, eventName: str, data: typing.Any) -> None
        """
        pass

    def tableData(self): # real signature unknown; restored from __doc__
        """ tableData(self) -> PySide2.QtScxml.QScxmlTableData """
        pass

    def tableDataChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, metaObject, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A31F40>'


class QScxmlStaticScxmlServiceFactory(QScxmlInvokableServiceFactory):
    """ QScxmlStaticScxmlServiceFactory(self, metaObject: PySide2.QtCore.QMetaObject, invokeInfo: PySide2.QtScxml.QScxmlExecutableContent.InvokeInfo, nameList: typing.List[int], parameters: typing.List[PySide2.QtScxml.QScxmlExecutableContent.ParameterInfo], parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def invoke(self, parentStateMachine): # real signature unknown; restored from __doc__
        """ invoke(self, parentStateMachine: PySide2.QtScxml.QScxmlStateMachine) -> PySide2.QtScxml.QScxmlInvokableService """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, metaObject, invokeInfo, nameList, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x000001D166A321C0>'


class QScxmlTableData(__Shiboken.Object):
    """ QScxmlTableData(self) -> None """
    def assignmentInfo(self, assignmentId): # real signature unknown; restored from __doc__
        """ assignmentInfo(self, assignmentId: int) -> PySide2.QtScxml.QScxmlExecutableContent.AssignmentInfo """
        pass

    def dataNames(self): # real signature unknown; restored from __doc__
        """ dataNames(self) -> typing.Tuple[typing.List[int], int] """
        pass

    def evaluatorInfo(self, evaluatorId): # real signature unknown; restored from __doc__
        """ evaluatorInfo(self, evaluatorId: int) -> PySide2.QtScxml.QScxmlExecutableContent.EvaluatorInfo """
        pass

    def foreachInfo(self, foreachId): # real signature unknown; restored from __doc__
        """ foreachInfo(self, foreachId: int) -> PySide2.QtScxml.QScxmlExecutableContent.ForeachInfo """
        pass

    def initialSetup(self): # real signature unknown; restored from __doc__
        """ initialSetup(self) -> int """
        return 0

    def instructions(self): # real signature unknown; restored from __doc__
        """ instructions(self) -> typing.List[int] """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def serviceFactory(self, id): # real signature unknown; restored from __doc__
        """ serviceFactory(self, id: int) -> PySide2.QtScxml.QScxmlInvokableServiceFactory """
        pass

    def stateMachineTable(self): # real signature unknown; restored from __doc__
        """ stateMachineTable(self) -> typing.List[int] """
        pass

    def string(self, id): # real signature unknown; restored from __doc__
        """ string(self, id: int) -> str """
        return ""

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


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D165E517B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtScxml', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D165E517B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtScxml.cp310-win_amd64.pyd')"

