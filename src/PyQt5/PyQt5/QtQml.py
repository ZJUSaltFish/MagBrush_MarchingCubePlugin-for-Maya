# encoding: utf-8
# module PyQt5.QtQml
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtQml.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


# functions

def qjsEngine(a0): # real signature unknown; restored from __doc__
    """ qjsEngine(a0: QObject) -> QJSEngine """
    return QJSEngine

def qmlAttachedPropertiesObject(a0, p_object, create=True): # real signature unknown; restored from __doc__
    """ qmlAttachedPropertiesObject(a0: type, object: QObject, create: bool = True) -> QObject """
    pass

def qmlClearTypeRegistrations(): # real signature unknown; restored from __doc__
    """ qmlClearTypeRegistrations() """
    pass

def qmlRegisterRevision(a0, revision, uri, major, minor, attachedProperties=0): # real signature unknown; restored from __doc__
    """ qmlRegisterRevision(a0: type, revision: int, uri: str, major: int, minor: int, attachedProperties: type = 0) -> int """
    return 0

def qmlRegisterSingletonType(url, uri, major, minor, qmlName): # real signature unknown; restored from __doc__
    """
    qmlRegisterSingletonType(url: QUrl, uri: str, major: int, minor: int, qmlName: str) -> int
    qmlRegisterSingletonType(a0: type, uri: str, major: int, minor: int, typeName: str, factory: Callable[[QQmlEngine, QJSEngine], Any]) -> int
    """
    return 0

def qmlRegisterType(url, uri, major, minor, qmlName): # real signature unknown; restored from __doc__
    """
    qmlRegisterType(url: QUrl, uri: str, major: int, minor: int, qmlName: str) -> int
    qmlRegisterType(a0: type, attachedProperties: type = 0) -> int
    qmlRegisterType(a0: type, uri: str, major: int, minor: int, qmlName: str, attachedProperties: type = 0) -> int
    qmlRegisterType(a0: type, revision: int, uri: str, major: int, minor: int, qmlName: str, attachedProperties: type = 0) -> int
    """
    return 0

def qmlRegisterUncreatableType(a0, uri, major, minor, qmlName, reason): # real signature unknown; restored from __doc__
    """
    qmlRegisterUncreatableType(a0: type, uri: str, major: int, minor: int, qmlName: str, reason: str) -> int
    qmlRegisterUncreatableType(a0: type, revision: int, uri: str, major: int, minor: int, qmlName: str, reason: str) -> int
    """
    return 0

def qmlTypeId(uri, versionMajor, versionMinor, qmlName): # real signature unknown; restored from __doc__
    """ qmlTypeId(uri: str, versionMajor: int, versionMinor: int, qmlName: str) -> int """
    return 0

def QQmlListProperty(type, p_object, p_list): # real signature unknown; restored from __doc__
    """
    QQmlListProperty(type, object, list)
    QQmlListProperty(type, object, append=None, count=None, at=None, clear=None)
    """
    pass

# classes

class QJSEngine(__PyQt5_QtCore.QObject):
    """
    QJSEngine()
    QJSEngine(parent: QObject)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def collectGarbage(self): # real signature unknown; restored from __doc__
        """ collectGarbage(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def evaluate(self, program, fileName='', lineNumber=1): # real signature unknown; restored from __doc__
        """ evaluate(self, program: str, fileName: str = '', lineNumber: int = 1) -> QJSValue """
        return QJSValue

    def globalObject(self): # real signature unknown; restored from __doc__
        """ globalObject(self) -> QJSValue """
        return QJSValue

    def importModule(self, fileName): # real signature unknown; restored from __doc__
        """ importModule(self, fileName: str) -> QJSValue """
        return QJSValue

    def installExtensions(self, extensions, QJSEngine_Extensions=None, QJSEngine_Extension=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ installExtensions(self, extensions: Union[QJSEngine.Extensions, QJSEngine.Extension], object: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str] = QJSValue()) """
        pass

    def installTranslatorFunctions(self, p_object, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ installTranslatorFunctions(self, object: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str] = QJSValue()) """
        pass

    def isInterrupted(self): # real signature unknown; restored from __doc__
        """ isInterrupted(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def newArray(self, length=0): # real signature unknown; restored from __doc__
        """ newArray(self, length: int = 0) -> QJSValue """
        return QJSValue

    def newErrorObject(self, errorType, message=''): # real signature unknown; restored from __doc__
        """ newErrorObject(self, errorType: QJSValue.ErrorType, message: str = '') -> QJSValue """
        return QJSValue

    def newObject(self): # real signature unknown; restored from __doc__
        """ newObject(self) -> QJSValue """
        return QJSValue

    def newQMetaObject(self, metaObject): # real signature unknown; restored from __doc__
        """ newQMetaObject(self, metaObject: QMetaObject) -> QJSValue """
        return QJSValue

    def newQObject(self, p_object): # real signature unknown; restored from __doc__
        """ newQObject(self, object: QObject) -> QJSValue """
        return QJSValue

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInterrupted(self, interrupted): # real signature unknown; restored from __doc__
        """ setInterrupted(self, interrupted: bool) """
        pass

    def setUiLanguage(self, language): # real signature unknown; restored from __doc__
        """ setUiLanguage(self, language: str) """
        pass

    def throwError(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        throwError(self, message: str)
        throwError(self, errorType: QJSValue.ErrorType, message: str = '')
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uiLanguage(self): # real signature unknown; restored from __doc__
        """ uiLanguage(self) -> str """
        return ""

    def uiLanguageChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, parent=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    AllExtensions = -1
    ConsoleExtension = 2
    GarbageCollectionExtension = 4
    TranslationExtension = 1


class QJSValue(__sip.simplewrapper):
    """
    QJSValue(value: QJSValue.SpecialValue = QJSValue.UndefinedValue)
    QJSValue(other: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str])
    """
    def call(self, args, Union=None, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None, *args_1, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ call(self, args: Iterable[Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]] = []) -> QJSValue """
        pass

    def callAsConstructor(self, args, Union=None, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None, *args_1, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ callAsConstructor(self, args: Iterable[Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]] = []) -> QJSValue """
        pass

    def callWithInstance(self, instance, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ callWithInstance(self, instance: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str], args: Iterable[Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]] = []) -> QJSValue """
        pass

    def deleteProperty(self, name): # real signature unknown; restored from __doc__
        """ deleteProperty(self, name: str) -> bool """
        return False

    def equals(self, other, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None): # real signature unknown; restored from __doc__
        """ equals(self, other: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) -> bool """
        return False

    def errorType(self): # real signature unknown; restored from __doc__
        """ errorType(self) -> QJSValue.ErrorType """
        pass

    def hasOwnProperty(self, name): # real signature unknown; restored from __doc__
        """ hasOwnProperty(self, name: str) -> bool """
        return False

    def hasProperty(self, name): # real signature unknown; restored from __doc__
        """ hasProperty(self, name: str) -> bool """
        return False

    def isArray(self): # real signature unknown; restored from __doc__
        """ isArray(self) -> bool """
        return False

    def isBool(self): # real signature unknown; restored from __doc__
        """ isBool(self) -> bool """
        return False

    def isCallable(self): # real signature unknown; restored from __doc__
        """ isCallable(self) -> bool """
        return False

    def isDate(self): # real signature unknown; restored from __doc__
        """ isDate(self) -> bool """
        return False

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isNumber(self): # real signature unknown; restored from __doc__
        """ isNumber(self) -> bool """
        return False

    def isObject(self): # real signature unknown; restored from __doc__
        """ isObject(self) -> bool """
        return False

    def isQObject(self): # real signature unknown; restored from __doc__
        """ isQObject(self) -> bool """
        return False

    def isRegExp(self): # real signature unknown; restored from __doc__
        """ isRegExp(self) -> bool """
        return False

    def isString(self): # real signature unknown; restored from __doc__
        """ isString(self) -> bool """
        return False

    def isUndefined(self): # real signature unknown; restored from __doc__
        """ isUndefined(self) -> bool """
        return False

    def isVariant(self): # real signature unknown; restored from __doc__
        """ isVariant(self) -> bool """
        return False

    def property(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        property(self, name: str) -> QJSValue
        property(self, arrayIndex: int) -> QJSValue
        """
        return QJSValue

    def prototype(self): # real signature unknown; restored from __doc__
        """ prototype(self) -> QJSValue """
        return QJSValue

    def setProperty(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setProperty(self, name: str, value: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str])
        setProperty(self, arrayIndex: int, value: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str])
        """
        pass

    def setPrototype(self, prototype, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None): # real signature unknown; restored from __doc__
        """ setPrototype(self, prototype: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) """
        pass

    def strictlyEquals(self, other, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None): # real signature unknown; restored from __doc__
        """ strictlyEquals(self, other: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) -> bool """
        return False

    def toBool(self): # real signature unknown; restored from __doc__
        """ toBool(self) -> bool """
        return False

    def toDateTime(self): # real signature unknown; restored from __doc__
        """ toDateTime(self) -> QDateTime """
        pass

    def toInt(self): # real signature unknown; restored from __doc__
        """ toInt(self) -> int """
        return 0

    def toNumber(self): # real signature unknown; restored from __doc__
        """ toNumber(self) -> float """
        return 0.0

    def toQObject(self): # real signature unknown; restored from __doc__
        """ toQObject(self) -> QObject """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def toUInt(self): # real signature unknown; restored from __doc__
        """ toUInt(self) -> int """
        return 0

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> Any """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    EvalError = 2
    GenericError = 1
    NullValue = 0
    RangeError = 3
    ReferenceError = 4
    SyntaxError = 5
    TypeError = 6
    UndefinedValue = 1
    URIError = 7


class QJSValueIterator(__sip.simplewrapper):
    """ QJSValueIterator(value: Union[QJSValue, QJSValue.SpecialValue, bool, int, float, str]) """
    def hasNext(self): # real signature unknown; restored from __doc__
        """ hasNext(self) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> QJSValue """
        return QJSValue

    def __init__(self, value, QJSValue=None, QJSValue_SpecialValue=None, bool=None, p_int=None, p_float=None, p_str=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlAbstractUrlInterceptor(__sip.simplewrapper):
    """
    QQmlAbstractUrlInterceptor()
    QQmlAbstractUrlInterceptor(a0: QQmlAbstractUrlInterceptor)
    """
    def intercept(self, path, type): # real signature unknown; restored from __doc__
        """ intercept(self, path: QUrl, type: QQmlAbstractUrlInterceptor.DataType) -> QUrl """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    JavaScriptFile = 1
    QmldirFile = 2
    QmlFile = 0
    UrlString = 4096


class QQmlEngine(QJSEngine):
    """ QQmlEngine(parent: typing.Optional[QObject] = None) """
    def addImageProvider(self, id, a1): # real signature unknown; restored from __doc__
        """ addImageProvider(self, id: str, a1: QQmlImageProviderBase) """
        pass

    def addImportPath(self, dir): # real signature unknown; restored from __doc__
        """ addImportPath(self, dir: str) """
        pass

    def addNamedBundle(self, name, fileName): # real signature unknown; restored from __doc__
        """ addNamedBundle(self, name: str, fileName: str) -> bool """
        return False

    def addPluginPath(self, dir): # real signature unknown; restored from __doc__
        """ addPluginPath(self, dir: str) """
        pass

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearComponentCache(self): # real signature unknown; restored from __doc__
        """ clearComponentCache(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextForObject(self, a0): # real signature unknown; restored from __doc__
        """ contextForObject(a0: QObject) -> QQmlContext """
        return QQmlContext

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, a0): # real signature unknown; restored from __doc__
        """ event(self, a0: QEvent) -> bool """
        return False

    def exit(self, *args, **kwargs): # real signature unknown
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

    def imageProvider(self, id): # real signature unknown; restored from __doc__
        """ imageProvider(self, id: str) -> QQmlImageProviderBase """
        return QQmlImageProviderBase

    def importPathList(self): # real signature unknown; restored from __doc__
        """ importPathList(self) -> List[str] """
        return []

    def importPlugin(self, filePath, uri, errors, QQmlError=None): # real signature unknown; restored from __doc__
        """ importPlugin(self, filePath: str, uri: str, errors: Iterable[QQmlError]) -> bool """
        return False

    def incubationController(self): # real signature unknown; restored from __doc__
        """ incubationController(self) -> QQmlIncubationController """
        return QQmlIncubationController

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> QNetworkAccessManager """
        pass

    def networkAccessManagerFactory(self): # real signature unknown; restored from __doc__
        """ networkAccessManagerFactory(self) -> QQmlNetworkAccessManagerFactory """
        return QQmlNetworkAccessManagerFactory

    def objectOwnership(self, a0): # real signature unknown; restored from __doc__
        """ objectOwnership(a0: QObject) -> QQmlEngine.ObjectOwnership """
        pass

    def offlineStorageDatabaseFilePath(self, databaseName): # real signature unknown; restored from __doc__
        """ offlineStorageDatabaseFilePath(self, databaseName: str) -> str """
        return ""

    def offlineStoragePath(self): # real signature unknown; restored from __doc__
        """ offlineStoragePath(self) -> str """
        return ""

    def outputWarningsToStandardError(self): # real signature unknown; restored from __doc__
        """ outputWarningsToStandardError(self) -> bool """
        return False

    def pluginPathList(self): # real signature unknown; restored from __doc__
        """ pluginPathList(self) -> List[str] """
        return []

    def quit(self, *args, **kwargs): # real signature unknown
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

    def removeImageProvider(self, id): # real signature unknown; restored from __doc__
        """ removeImageProvider(self, id: str) """
        pass

    def retranslate(self): # real signature unknown; restored from __doc__
        """ retranslate(self) """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ rootContext(self) -> QQmlContext """
        return QQmlContext

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, a0): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, a0: QUrl) """
        pass

    def setContextForObject(self, a0, a1): # real signature unknown; restored from __doc__
        """ setContextForObject(a0: QObject, a1: QQmlContext) """
        pass

    def setImportPathList(self, paths, p_str=None): # real signature unknown; restored from __doc__
        """ setImportPathList(self, paths: Iterable[str]) """
        pass

    def setIncubationController(self, a0): # real signature unknown; restored from __doc__
        """ setIncubationController(self, a0: QQmlIncubationController) """
        pass

    def setNetworkAccessManagerFactory(self, a0): # real signature unknown; restored from __doc__
        """ setNetworkAccessManagerFactory(self, a0: QQmlNetworkAccessManagerFactory) """
        pass

    def setObjectOwnership(self, a0, a1): # real signature unknown; restored from __doc__
        """ setObjectOwnership(a0: QObject, a1: QQmlEngine.ObjectOwnership) """
        pass

    def setOfflineStoragePath(self, dir): # real signature unknown; restored from __doc__
        """ setOfflineStoragePath(self, dir: str) """
        pass

    def setOutputWarningsToStandardError(self, a0): # real signature unknown; restored from __doc__
        """ setOutputWarningsToStandardError(self, a0: bool) """
        pass

    def setPluginPathList(self, paths, p_str=None): # real signature unknown; restored from __doc__
        """ setPluginPathList(self, paths: Iterable[str]) """
        pass

    def singletonInstance(self, qmlTypeId): # real signature unknown; restored from __doc__
        """ singletonInstance(self, qmlTypeId: int) -> QObject """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def trimComponentCache(self): # real signature unknown; restored from __doc__
        """ trimComponentCache(self) """
        pass

    def warnings(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    CppOwnership = 0
    JavaScriptOwnership = 1


class QQmlApplicationEngine(QQmlEngine):
    """
    QQmlApplicationEngine(parent: typing.Optional[QObject] = None)
    QQmlApplicationEngine(url: QUrl, parent: typing.Optional[QObject] = None)
    QQmlApplicationEngine(filePath: str, parent: typing.Optional[QObject] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        load(self, url: QUrl)
        load(self, filePath: str)
        """
        pass

    def loadData(self, data, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ loadData(self, data: Union[QByteArray, bytes, bytearray], url: QUrl = QUrl()) """
        pass

    def objectCreated(self, *args, **kwargs): # real signature unknown
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

    def rootObjects(self): # real signature unknown; restored from __doc__
        """ rootObjects(self) -> List[QObject] """
        return []

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialProperties(self, initialProperties, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setInitialProperties(self, initialProperties: Dict[str, Any]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QQmlComponent(__PyQt5_QtCore.QObject):
    """
    QQmlComponent(a0: QQmlEngine, parent: typing.Optional[QObject] = None)
    QQmlComponent(a0: QQmlEngine, fileName: str, parent: typing.Optional[QObject] = None)
    QQmlComponent(a0: QQmlEngine, fileName: str, mode: QQmlComponent.CompilationMode, parent: typing.Optional[QObject] = None)
    QQmlComponent(a0: QQmlEngine, url: QUrl, parent: typing.Optional[QObject] = None)
    QQmlComponent(a0: QQmlEngine, url: QUrl, mode: QQmlComponent.CompilationMode, parent: typing.Optional[QObject] = None)
    QQmlComponent(parent: typing.Optional[QObject] = None)
    """
    def beginCreate(self, a0): # real signature unknown; restored from __doc__
        """ beginCreate(self, a0: QQmlContext) -> QObject """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def completeCreate(self): # real signature unknown; restored from __doc__
        """ completeCreate(self) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        create(self, context: typing.Optional[QQmlContext] = None) -> QObject
        create(self, a0: QQmlIncubator, context: typing.Optional[QQmlContext] = None, forContext: typing.Optional[QQmlContext] = None)
        """
        pass

    def createWithInitialProperties(self, initialProperties, p_str=None, Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createWithInitialProperties(self, initialProperties: Dict[str, Any], context: typing.Optional[QQmlContext] = None) -> QObject """
        pass

    def creationContext(self): # real signature unknown; restored from __doc__
        """ creationContext(self) -> QQmlContext """
        return QQmlContext

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        return QQmlEngine

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> List[QQmlError] """
        return []

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isLoading(self): # real signature unknown; restored from __doc__
        """ isLoading(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isReady(self): # real signature unknown; restored from __doc__
        """ isReady(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def loadUrl(self, url, mode=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        loadUrl(self, url: QUrl)
        loadUrl(self, url: QUrl, mode: QQmlComponent.CompilationMode)
        """
        pass

    def progress(self): # real signature unknown; restored from __doc__
        """ progress(self) -> float """
        return 0.0

    def progressChanged(self, *args, **kwargs): # real signature unknown
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

    def setData(self, a0, QByteArray=None, bytes=None, bytearray=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setData(self, a0: Union[QByteArray, bytes, bytearray], baseUrl: QUrl) """
        pass

    def setInitialProperties(self, component, properties, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setInitialProperties(self, component: QObject, properties: Dict[str, Any]) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QQmlComponent.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    Asynchronous = 1
    Error = 3
    Loading = 2
    Null = 0
    PreferSynchronous = 0
    Ready = 1


class QQmlContext(__PyQt5_QtCore.QObject):
    """
    QQmlContext(engine: QQmlEngine, parent: typing.Optional[QObject] = None)
    QQmlContext(parentContext: QQmlContext, parent: typing.Optional[QObject] = None)
    """
    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contextObject(self): # real signature unknown; restored from __doc__
        """ contextObject(self) -> QObject """
        pass

    def contextProperty(self, a0): # real signature unknown; restored from __doc__
        """ contextProperty(self, a0: str) -> Any """
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        return QQmlEngine

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nameForObject(self, a0): # real signature unknown; restored from __doc__
        """ nameForObject(self, a0: QObject) -> str """
        return ""

    def parentContext(self): # real signature unknown; restored from __doc__
        """ parentContext(self) -> QQmlContext """
        return QQmlContext

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resolvedUrl(self, a0): # real signature unknown; restored from __doc__
        """ resolvedUrl(self, a0: QUrl) -> QUrl """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setBaseUrl(self, a0): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, a0: QUrl) """
        pass

    def setContextObject(self, a0): # real signature unknown; restored from __doc__
        """ setContextObject(self, a0: QObject) """
        pass

    def setContextProperties(self, properties, QQmlContext_PropertyPair=None): # real signature unknown; restored from __doc__
        """ setContextProperties(self, properties: Iterable[QQmlContext.PropertyPair]) """
        pass

    def setContextProperty(self, a0, a1): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContextProperty(self, a0: str, a1: QObject)
        setContextProperty(self, a0: str, a1: Any)
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass



class QQmlEngineExtensionPlugin(__PyQt5_QtCore.QObject):
    """ QQmlEngineExtensionPlugin(parent: typing.Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def initializeEngine(self, engine, uri): # real signature unknown; restored from __doc__
        """ initializeEngine(self, engine: QQmlEngine, uri: str) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QQmlError(__sip.simplewrapper):
    """
    QQmlError()
    QQmlError(a0: QQmlError)
    """
    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ line(self) -> int """
        return 0

    def messageType(self): # real signature unknown; restored from __doc__
        """ messageType(self) -> QtMsgType """
        pass

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def setColumn(self, a0): # real signature unknown; restored from __doc__
        """ setColumn(self, a0: int) """
        pass

    def setDescription(self, a0): # real signature unknown; restored from __doc__
        """ setDescription(self, a0: str) """
        pass

    def setLine(self, a0): # real signature unknown; restored from __doc__
        """ setLine(self, a0: int) """
        pass

    def setMessageType(self, messageType): # real signature unknown; restored from __doc__
        """ setMessageType(self, messageType: QtMsgType) """
        pass

    def setObject(self, a0): # real signature unknown; restored from __doc__
        """ setObject(self, a0: QObject) """
        pass

    def setUrl(self, a0): # real signature unknown; restored from __doc__
        """ setUrl(self, a0: QUrl) """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> QUrl """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlExpression(__PyQt5_QtCore.QObject):
    """
    QQmlExpression()
    QQmlExpression(a0: QQmlContext, a1: QObject, a2: str, parent: typing.Optional[QObject] = None)
    QQmlExpression(a0: QQmlScriptString, context: typing.Optional[QQmlContext] = None, scope: typing.Optional[QObject] = None, parent: typing.Optional[QObject] = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> QQmlContext """
        return QQmlContext

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        return QQmlEngine

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> QQmlError """
        return QQmlError

    def evaluate(self): # real signature unknown; restored from __doc__
        """ evaluate(self) -> Tuple[Any, bool] """
        pass

    def expression(self): # real signature unknown; restored from __doc__
        """ expression(self) -> str """
        return ""

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def notifyOnValueChanged(self): # real signature unknown; restored from __doc__
        """ notifyOnValueChanged(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def scopeObject(self): # real signature unknown; restored from __doc__
        """ scopeObject(self) -> QObject """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExpression(self, a0): # real signature unknown; restored from __doc__
        """ setExpression(self, a0: str) """
        pass

    def setNotifyOnValueChanged(self, a0): # real signature unknown; restored from __doc__
        """ setNotifyOnValueChanged(self, a0: bool) """
        pass

    def setSourceLocation(self, fileName, line, column=0): # real signature unknown; restored from __doc__
        """ setSourceLocation(self, fileName: str, line: int, column: int = 0) """
        pass

    def sourceFile(self): # real signature unknown; restored from __doc__
        """ sourceFile(self) -> str """
        return ""

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, a0=None, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


class QQmlExtensionPlugin(__PyQt5_QtCore.QObject):
    """ QQmlExtensionPlugin(parent: typing.Optional[QObject] = None) """
    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> QUrl """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def initializeEngine(self, engine, uri): # real signature unknown; restored from __doc__
        """ initializeEngine(self, engine: QQmlEngine, uri: str) """
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registerTypes(self, uri): # real signature unknown; restored from __doc__
        """ registerTypes(self, uri: str) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QQmlFileSelector(__PyQt5_QtCore.QObject):
    """ QQmlFileSelector(engine: QQmlEngine, parent: typing.Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, a0): # real signature unknown; restored from __doc__
        """ get(a0: QQmlEngine) -> QQmlFileSelector """
        return QQmlFileSelector

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def selector(self): # real signature unknown; restored from __doc__
        """ selector(self) -> QFileSelector """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setExtraSelectors(self, strings, p_str=None): # real signature unknown; restored from __doc__
        """ setExtraSelectors(self, strings: Iterable[str]) """
        pass

    def setSelector(self, selector): # real signature unknown; restored from __doc__
        """ setSelector(self, selector: QFileSelector) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, engine, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QQmlImageProviderBase(__sip.wrapper):
    # no doc
    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QQmlImageProviderBase.Flags """
        pass

    def imageType(self): # real signature unknown; restored from __doc__
        """ imageType(self) -> QQmlImageProviderBase.ImageType """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ForceAsynchronousImageLoading = 1
    Image = 0
    ImageResponse = 4
    Pixmap = 1
    Texture = 2


class QQmlIncubationController(__sip.simplewrapper):
    """ QQmlIncubationController() """
    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> QQmlEngine """
        return QQmlEngine

    def incubateFor(self, msecs): # real signature unknown; restored from __doc__
        """ incubateFor(self, msecs: int) """
        pass

    def incubatingObjectCount(self): # real signature unknown; restored from __doc__
        """ incubatingObjectCount(self) -> int """
        return 0

    def incubatingObjectCountChanged(self, a0): # real signature unknown; restored from __doc__
        """ incubatingObjectCountChanged(self, a0: int) """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlIncubator(__sip.simplewrapper):
    """ QQmlIncubator(mode: QQmlIncubator.IncubationMode = QQmlIncubator.Asynchronous) """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> List[QQmlError] """
        return []

    def forceCompletion(self): # real signature unknown; restored from __doc__
        """ forceCompletion(self) """
        pass

    def incubationMode(self): # real signature unknown; restored from __doc__
        """ incubationMode(self) -> QQmlIncubator.IncubationMode """
        pass

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isLoading(self): # real signature unknown; restored from __doc__
        """ isLoading(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isReady(self): # real signature unknown; restored from __doc__
        """ isReady(self) -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def setInitialProperties(self, initialProperties, p_str=None, Any=None): # real signature unknown; restored from __doc__
        """ setInitialProperties(self, initialProperties: Dict[str, Any]) """
        pass

    def setInitialState(self, a0): # real signature unknown; restored from __doc__
        """ setInitialState(self, a0: QObject) """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> QQmlIncubator.Status """
        pass

    def statusChanged(self, a0): # real signature unknown; restored from __doc__
        """ statusChanged(self, a0: QQmlIncubator.Status) """
        pass

    def __init__(self, mode=None): # real signature unknown; restored from __doc__
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Asynchronous = 0
    AsynchronousIfNested = 1
    Error = 3
    Loading = 2
    Null = 0
    Ready = 1
    Synchronous = 2


class QQmlListReference(__sip.simplewrapper):
    """
    QQmlListReference()
    QQmlListReference(a0: QObject, property: str, engine: typing.Optional[QQmlEngine] = None)
    QQmlListReference(a0: QQmlListReference)
    """
    def append(self, a0): # real signature unknown; restored from __doc__
        """ append(self, a0: QObject) -> bool """
        return False

    def at(self, a0): # real signature unknown; restored from __doc__
        """ at(self, a0: int) -> QObject """
        pass

    def canAppend(self): # real signature unknown; restored from __doc__
        """ canAppend(self) -> bool """
        return False

    def canAt(self): # real signature unknown; restored from __doc__
        """ canAt(self) -> bool """
        return False

    def canClear(self): # real signature unknown; restored from __doc__
        """ canClear(self) -> bool """
        return False

    def canCount(self): # real signature unknown; restored from __doc__
        """ canCount(self) -> bool """
        return False

    def canRemoveLast(self): # real signature unknown; restored from __doc__
        """ canRemoveLast(self) -> bool """
        return False

    def canReplace(self): # real signature unknown; restored from __doc__
        """ canReplace(self) -> bool """
        return False

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def isManipulable(self): # real signature unknown; restored from __doc__
        """ isManipulable(self) -> bool """
        return False

    def isReadable(self): # real signature unknown; restored from __doc__
        """ isReadable(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def listElementType(self): # real signature unknown; restored from __doc__
        """ listElementType(self) -> QMetaObject """
        pass

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def removeLast(self): # real signature unknown; restored from __doc__
        """ removeLast(self) -> bool """
        return False

    def replace(self, a0, a1): # real signature unknown; restored from __doc__
        """ replace(self, a0: int, a1: QObject) -> bool """
        return False

    def __init__(self, a0=None, property=None, engine=None, QQmlEngine=None, *args=None, **kwargs=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlNetworkAccessManagerFactory(__sip.simplewrapper):
    """
    QQmlNetworkAccessManagerFactory()
    QQmlNetworkAccessManagerFactory(a0: QQmlNetworkAccessManagerFactory)
    """
    def create(self, parent): # real signature unknown; restored from __doc__
        """ create(self, parent: QObject) -> QNetworkAccessManager """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlParserStatus(__sip.simplewrapper):
    """
    QQmlParserStatus()
    QQmlParserStatus(a0: QQmlParserStatus)
    """
    def classBegin(self): # real signature unknown; restored from __doc__
        """ classBegin(self) """
        pass

    def componentComplete(self): # real signature unknown; restored from __doc__
        """ componentComplete(self) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlProperty(__sip.simplewrapper):
    """
    QQmlProperty()
    QQmlProperty(a0: QObject)
    QQmlProperty(a0: QObject, a1: QQmlContext)
    QQmlProperty(a0: QObject, a1: QQmlEngine)
    QQmlProperty(a0: QObject, a1: str)
    QQmlProperty(a0: QObject, a1: str, a2: QQmlContext)
    QQmlProperty(a0: QObject, a1: str, a2: QQmlEngine)
    QQmlProperty(a0: QQmlProperty)
    """
    def connectNotifySignal(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        connectNotifySignal(self, slot: PYQT_SLOT) -> bool
        connectNotifySignal(self, dest: QObject, method: int) -> bool
        """
        return False

    def hasNotifySignal(self): # real signature unknown; restored from __doc__
        """ hasNotifySignal(self) -> bool """
        return False

    def index(self): # real signature unknown; restored from __doc__
        """ index(self) -> int """
        return 0

    def isDesignable(self): # real signature unknown; restored from __doc__
        """ isDesignable(self) -> bool """
        return False

    def isProperty(self): # real signature unknown; restored from __doc__
        """ isProperty(self) -> bool """
        return False

    def isResettable(self): # real signature unknown; restored from __doc__
        """ isResettable(self) -> bool """
        return False

    def isSignalProperty(self): # real signature unknown; restored from __doc__
        """ isSignalProperty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def isWritable(self): # real signature unknown; restored from __doc__
        """ isWritable(self) -> bool """
        return False

    def method(self): # real signature unknown; restored from __doc__
        """ method(self) -> QMetaMethod """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def needsNotifySignal(self): # real signature unknown; restored from __doc__
        """ needsNotifySignal(self) -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> QObject """
        pass

    def property(self): # real signature unknown; restored from __doc__
        """ property(self) -> QMetaProperty """
        pass

    def propertyType(self): # real signature unknown; restored from __doc__
        """ propertyType(self) -> int """
        return 0

    def propertyTypeCategory(self): # real signature unknown; restored from __doc__
        """ propertyTypeCategory(self) -> QQmlProperty.PropertyTypeCategory """
        pass

    def propertyTypeName(self): # real signature unknown; restored from __doc__
        """ propertyTypeName(self) -> str """
        return ""

    def read(self, a0=None, a1=None, a2=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        read(self) -> Any
        read(a0: QObject, a1: str) -> Any
        read(a0: QObject, a1: str, a2: QQmlContext) -> Any
        read(a0: QObject, a1: str, a2: QQmlEngine) -> Any
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> QQmlProperty.Type """
        pass

    def write(self, a0, a1=None, a2=None, a3=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        write(self, a0: Any) -> bool
        write(a0: QObject, a1: str, a2: Any) -> bool
        write(a0: QObject, a1: str, a2: Any, a3: QQmlContext) -> bool
        write(a0: QObject, a1: str, a2: Any, a3: QQmlEngine) -> bool
        """
        return False

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, a0=None, a1=None, a2=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Invalid = 0
    InvalidCategory = 0
    List = 1
    Normal = 3
    Object = 2
    Property = 1
    SignalProperty = 2


class QQmlPropertyMap(__PyQt5_QtCore.QObject):
    """ QQmlPropertyMap(parent: typing.Optional[QObject] = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, key): # real signature unknown; restored from __doc__
        """ clear(self, key: str) """
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, key): # real signature unknown; restored from __doc__
        """ contains(self, key: str) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, key, value): # real signature unknown; restored from __doc__
        """ insert(self, key: str, value: Any) """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """ keys(self) -> List[str] """
        return []

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateValue(self, key, input): # real signature unknown; restored from __doc__
        """ updateValue(self, key: str, input: Any) -> Any """
        pass

    def value(self, key): # real signature unknown; restored from __doc__
        """ value(self, key: str) -> Any """
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
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

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, parent, QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass


class QQmlPropertyValueSource(__sip.simplewrapper):
    """
    QQmlPropertyValueSource()
    QQmlPropertyValueSource(a0: QQmlPropertyValueSource)
    """
    def setTarget(self, a0): # real signature unknown; restored from __doc__
        """ setTarget(self, a0: QQmlProperty) """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QQmlScriptString(__sip.simplewrapper):
    """
    QQmlScriptString()
    QQmlScriptString(a0: QQmlScriptString)
    """
    def booleanLiteral(self): # real signature unknown; restored from __doc__
        """ booleanLiteral(self) -> Tuple[bool, bool] """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isNullLiteral(self): # real signature unknown; restored from __doc__
        """ isNullLiteral(self) -> bool """
        return False

    def isUndefinedLiteral(self): # real signature unknown; restored from __doc__
        """ isUndefinedLiteral(self) -> bool """
        return False

    def numberLiteral(self): # real signature unknown; restored from __doc__
        """ numberLiteral(self) -> Tuple[float, bool] """
        pass

    def stringLiteral(self): # real signature unknown; restored from __doc__
        """ stringLiteral(self) -> str """
        return ""

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __hash__ = None


# variables with complex values



