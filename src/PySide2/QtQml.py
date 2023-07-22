# encoding: utf-8
# module PySide2.QtQml
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtQml.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# functions

def qmlRegisterType(arg__1, arg__2, arg__3, arg__4, arg__5): # real signature unknown; restored from __doc__
    """ qmlRegisterType(arg__1: type, arg__2: bytes, arg__3: int, arg__4: int, arg__5: bytes) -> int """
    return 0

# classes

class ListProperty(__PySide2_QtCore.Property):
    """ ListProperty(type: type, append: typing.Callable, at: typing.Optional[typing.Callable] = None, clear: typing.Optional[typing.Callable] = None, count: typing.Optional[typing.Callable] = None) -> None """
    def __init__(self, type, append, at, typing_Callable=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass


class QJSEngine(__PySide2_QtCore.QObject):
    """
    QJSEngine(self) -> None
    QJSEngine(self, parent: PySide2.QtCore.QObject) -> None
    """
    def collectGarbage(self): # real signature unknown; restored from __doc__
        """ collectGarbage(self) -> None """
        pass

    def evaluate(self, program, fileName='', lineNumber=1): # real signature unknown; restored from __doc__
        """ evaluate(self, program: str, fileName: str = '', lineNumber: int = 1) -> PySide2.QtQml.QJSValue """
        pass

    def globalObject(self): # real signature unknown; restored from __doc__
        """ globalObject(self) -> PySide2.QtQml.QJSValue """
        pass

    def importModule(self, fileName): # real signature unknown; restored from __doc__
        """ importModule(self, fileName: str) -> PySide2.QtQml.QJSValue """
        pass

    def installExtensions(self, extensions, p_object=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ installExtensions(self, extensions: PySide2.QtQml.QJSEngine.Extensions, object: PySide2.QtQml.QJSValue = Default(QJSValue)) -> None """
        pass

    def installTranslatorFunctions(self, p_object=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ installTranslatorFunctions(self, object: PySide2.QtQml.QJSValue = Default(QJSValue)) -> None """
        pass

    def isInterrupted(self): # real signature unknown; restored from __doc__
        """ isInterrupted(self) -> bool """
        return False

    def newArray(self, length=0): # real signature unknown; restored from __doc__
        """ newArray(self, length: int = 0) -> PySide2.QtQml.QJSValue """
        pass

    def newErrorObject(self, errorType, message=''): # real signature unknown; restored from __doc__
        """ newErrorObject(self, errorType: PySide2.QtQml.QJSValue.ErrorType, message: str = '') -> PySide2.QtQml.QJSValue """
        pass

    def newObject(self): # real signature unknown; restored from __doc__
        """ newObject(self) -> PySide2.QtQml.QJSValue """
        pass

    def newQMetaObject(self, metaObject): # real signature unknown; restored from __doc__
        """ newQMetaObject(self, metaObject: PySide2.QtCore.QMetaObject) -> PySide2.QtQml.QJSValue """
        pass

    def newQObject(self, p_object): # real signature unknown; restored from __doc__
        """ newQObject(self, object: PySide2.QtCore.QObject) -> PySide2.QtQml.QJSValue """
        pass

    def setInterrupted(self, interrupted): # real signature unknown; restored from __doc__
        """ setInterrupted(self, interrupted: bool) -> None """
        pass

    def setUiLanguage(self, language): # real signature unknown; restored from __doc__
        """ setUiLanguage(self, language: str) -> None """
        pass

    def throwError(self, errorType, message=''): # real signature unknown; restored from __doc__
        """
        throwError(self, errorType: PySide2.QtQml.QJSValue.ErrorType, message: str = '') -> None
        throwError(self, message: str) -> None
        """
        pass

    def toScriptValue(self, arg__1): # real signature unknown; restored from __doc__
        """ toScriptValue(self, arg__1: typing.Any) -> PySide2.QtQml.QJSValue """
        pass

    def uiLanguage(self): # real signature unknown; restored from __doc__
        """ uiLanguage(self) -> str """
        return ""

    def uiLanguageChanged(self, *args, **kwargs): # real signature unknown
        pass

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

    AllExtensions = PySide2.QtQml.QJSEngine.Extension.AllExtensions
    ConsoleExtension = PySide2.QtQml.QJSEngine.Extension.ConsoleExtension
    Extension = None # (!) real value is "<class 'PySide2.QtQml.QJSEngine.Extension'>"
    Extensions = None # (!) real value is "<class 'PySide2.QtQml.QJSEngine.Extensions'>"
    GarbageCollectionExtension = PySide2.QtQml.QJSEngine.Extension.GarbageCollectionExtension
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D98940>'
    TranslationExtension = PySide2.QtQml.QJSEngine.Extension.TranslationExtension


class QJSValue(__Shiboken.Object):
    """
    QJSValue(self, other: PySide2.QtQml.QJSValue) -> None
    QJSValue(self, str: bytes) -> None
    QJSValue(self, value: PySide2.QtQml.QJSValue.SpecialValue = PySide2.QtQml.QJSValue.SpecialValue.UndefinedValue) -> None
    QJSValue(self, value: str) -> None
    QJSValue(self, value: bool) -> None
    QJSValue(self, value: float) -> None
    QJSValue(self, value: int) -> None
    QJSValue(self, value: int) -> None
    """
    def call(self, args, PySide2_QtQml_QJSValue=None, *args_1, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ call(self, args: typing.Sequence[PySide2.QtQml.QJSValue] = []) -> PySide2.QtQml.QJSValue """
        pass

    def callAsConstructor(self, args, PySide2_QtQml_QJSValue=None, *args_1, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ callAsConstructor(self, args: typing.Sequence[PySide2.QtQml.QJSValue] = []) -> PySide2.QtQml.QJSValue """
        pass

    def callWithInstance(self, instance, args, PySide2_QtQml_QJSValue=None, *args_1, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ callWithInstance(self, instance: PySide2.QtQml.QJSValue, args: typing.Sequence[PySide2.QtQml.QJSValue] = []) -> PySide2.QtQml.QJSValue """
        pass

    def deleteProperty(self, name): # real signature unknown; restored from __doc__
        """ deleteProperty(self, name: str) -> bool """
        return False

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> PySide2.QtQml.QJSEngine """
        pass

    def equals(self, other): # real signature unknown; restored from __doc__
        """ equals(self, other: PySide2.QtQml.QJSValue) -> bool """
        return False

    def errorType(self): # real signature unknown; restored from __doc__
        """ errorType(self) -> PySide2.QtQml.QJSValue.ErrorType """
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

    def isQMetaObject(self): # real signature unknown; restored from __doc__
        """ isQMetaObject(self) -> bool """
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

    def property(self, arrayIndex): # real signature unknown; restored from __doc__
        """
        property(self, arrayIndex: int) -> PySide2.QtQml.QJSValue
        property(self, name: str) -> PySide2.QtQml.QJSValue
        """
        pass

    def prototype(self): # real signature unknown; restored from __doc__
        """ prototype(self) -> PySide2.QtQml.QJSValue """
        pass

    def setProperty(self, arrayIndex, value): # real signature unknown; restored from __doc__
        """
        setProperty(self, arrayIndex: int, value: PySide2.QtQml.QJSValue) -> None
        setProperty(self, name: str, value: PySide2.QtQml.QJSValue) -> None
        """
        pass

    def setPrototype(self, prototype): # real signature unknown; restored from __doc__
        """ setPrototype(self, prototype: PySide2.QtQml.QJSValue) -> None """
        pass

    def strictlyEquals(self, other): # real signature unknown; restored from __doc__
        """ strictlyEquals(self, other: PySide2.QtQml.QJSValue) -> bool """
        return False

    def toBool(self): # real signature unknown; restored from __doc__
        """ toBool(self) -> bool """
        return False

    def toDateTime(self): # real signature unknown; restored from __doc__
        """ toDateTime(self) -> PySide2.QtCore.QDateTime """
        pass

    def toInt(self): # real signature unknown; restored from __doc__
        """ toInt(self) -> int """
        return 0

    def toNumber(self): # real signature unknown; restored from __doc__
        """ toNumber(self) -> float """
        return 0.0

    def toQMetaObject(self): # real signature unknown; restored from __doc__
        """ toQMetaObject(self) -> PySide2.QtCore.QMetaObject """
        pass

    def toQObject(self): # real signature unknown; restored from __doc__
        """ toQObject(self) -> PySide2.QtCore.QObject """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def toUInt(self): # real signature unknown; restored from __doc__
        """ toUInt(self) -> int """
        return 0

    def toVariant(self): # real signature unknown; restored from __doc__
        """ toVariant(self) -> typing.Any """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self, other): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    ErrorType = None # (!) real value is "<class 'PySide2.QtQml.QJSValue.ErrorType'>"
    EvalError = PySide2.QtQml.QJSValue.ErrorType.EvalError
    GenericError = PySide2.QtQml.QJSValue.ErrorType.GenericError
    NoError = PySide2.QtQml.QJSValue.ErrorType.NoError
    NullValue = PySide2.QtQml.QJSValue.SpecialValue.NullValue
    RangeError = PySide2.QtQml.QJSValue.ErrorType.RangeError
    ReferenceError = PySide2.QtQml.QJSValue.ErrorType.ReferenceError
    SpecialValue = None # (!) real value is "<class 'PySide2.QtQml.QJSValue.SpecialValue'>"
    SyntaxError = PySide2.QtQml.QJSValue.ErrorType.SyntaxError
    TypeError = PySide2.QtQml.QJSValue.ErrorType.TypeError
    UndefinedValue = PySide2.QtQml.QJSValue.SpecialValue.UndefinedValue
    URIError = PySide2.QtQml.QJSValue.ErrorType.URIError


class QJSValueIterator(__Shiboken.Object):
    """ QJSValueIterator(self, value: PySide2.QtQml.QJSValue) -> None """
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
        """ value(self) -> PySide2.QtQml.QJSValue """
        pass

    def __init__(self, value): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QQmlAbstractUrlInterceptor(__Shiboken.Object):
    """ QQmlAbstractUrlInterceptor(self) -> None """
    def intercept(self, path, type): # real signature unknown; restored from __doc__
        """ intercept(self, path: PySide2.QtCore.QUrl, type: PySide2.QtQml.QQmlAbstractUrlInterceptor.DataType) -> PySide2.QtCore.QUrl """
        pass

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

    DataType = None # (!) real value is "<class 'PySide2.QtQml.QQmlAbstractUrlInterceptor.DataType'>"
    JavaScriptFile = PySide2.QtQml.QQmlAbstractUrlInterceptor.DataType.JavaScriptFile
    QmldirFile = PySide2.QtQml.QQmlAbstractUrlInterceptor.DataType.QmldirFile
    QmlFile = PySide2.QtQml.QQmlAbstractUrlInterceptor.DataType.QmlFile
    UrlString = PySide2.QtQml.QQmlAbstractUrlInterceptor.DataType.UrlString


class QQmlEngine(QJSEngine):
    """ QQmlEngine(self, p: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addImageProvider(self, id, arg__2): # real signature unknown; restored from __doc__
        """ addImageProvider(self, id: str, arg__2: PySide2.QtQml.QQmlImageProviderBase) -> None """
        pass

    def addImportPath(self, dir): # real signature unknown; restored from __doc__
        """ addImportPath(self, dir: str) -> None """
        pass

    def addNamedBundle(self, name, fileName): # real signature unknown; restored from __doc__
        """ addNamedBundle(self, name: str, fileName: str) -> bool """
        return False

    def addPluginPath(self, dir): # real signature unknown; restored from __doc__
        """ addPluginPath(self, dir: str) -> None """
        pass

    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def clearComponentCache(self): # real signature unknown; restored from __doc__
        """ clearComponentCache(self) -> None """
        pass

    def contextForObject(self, arg__1): # real signature unknown; restored from __doc__
        """ contextForObject(arg__1: PySide2.QtCore.QObject) -> PySide2.QtQml.QQmlContext """
        pass

    def event(self, arg__1): # real signature unknown; restored from __doc__
        """ event(self, arg__1: PySide2.QtCore.QEvent) -> bool """
        return False

    def exit(self, *args, **kwargs): # real signature unknown
        pass

    def imageProvider(self, id): # real signature unknown; restored from __doc__
        """ imageProvider(self, id: str) -> PySide2.QtQml.QQmlImageProviderBase """
        pass

    def importPathList(self): # real signature unknown; restored from __doc__
        """ importPathList(self) -> typing.List[str] """
        pass

    def importPlugin(self, filePath, uri, errors, PySide2_QtQml_QQmlError=None): # real signature unknown; restored from __doc__
        """ importPlugin(self, filePath: str, uri: str, errors: typing.Sequence[PySide2.QtQml.QQmlError]) -> bool """
        return False

    def incubationController(self): # real signature unknown; restored from __doc__
        """ incubationController(self) -> PySide2.QtQml.QQmlIncubationController """
        pass

    def networkAccessManager(self): # real signature unknown; restored from __doc__
        """ networkAccessManager(self) -> PySide2.QtNetwork.QNetworkAccessManager """
        pass

    def networkAccessManagerFactory(self): # real signature unknown; restored from __doc__
        """ networkAccessManagerFactory(self) -> PySide2.QtQml.QQmlNetworkAccessManagerFactory """
        pass

    def objectOwnership(self, arg__1): # real signature unknown; restored from __doc__
        """ objectOwnership(arg__1: PySide2.QtCore.QObject) -> PySide2.QtQml.QQmlEngine.ObjectOwnership """
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
        """ pluginPathList(self) -> typing.List[str] """
        pass

    def quit(self, *args, **kwargs): # real signature unknown
        pass

    def removeImageProvider(self, id): # real signature unknown; restored from __doc__
        """ removeImageProvider(self, id: str) -> None """
        pass

    def retranslate(self): # real signature unknown; restored from __doc__
        """ retranslate(self) -> None """
        pass

    def rootContext(self): # real signature unknown; restored from __doc__
        """ rootContext(self) -> PySide2.QtQml.QQmlContext """
        pass

    def setBaseUrl(self, arg__1): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, arg__1: PySide2.QtCore.QUrl) -> None """
        pass

    def setContextForObject(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ setContextForObject(arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtQml.QQmlContext) -> None """
        pass

    def setImportPathList(self, paths, p_str=None): # real signature unknown; restored from __doc__
        """ setImportPathList(self, paths: typing.Sequence[str]) -> None """
        pass

    def setIncubationController(self, arg__1): # real signature unknown; restored from __doc__
        """ setIncubationController(self, arg__1: PySide2.QtQml.QQmlIncubationController) -> None """
        pass

    def setNetworkAccessManagerFactory(self, arg__1): # real signature unknown; restored from __doc__
        """ setNetworkAccessManagerFactory(self, arg__1: PySide2.QtQml.QQmlNetworkAccessManagerFactory) -> None """
        pass

    def setObjectOwnership(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ setObjectOwnership(arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtQml.QQmlEngine.ObjectOwnership) -> None """
        pass

    def setOfflineStoragePath(self, dir): # real signature unknown; restored from __doc__
        """ setOfflineStoragePath(self, dir: str) -> None """
        pass

    def setOutputWarningsToStandardError(self, arg__1): # real signature unknown; restored from __doc__
        """ setOutputWarningsToStandardError(self, arg__1: bool) -> None """
        pass

    def setPluginPathList(self, paths, p_str=None): # real signature unknown; restored from __doc__
        """ setPluginPathList(self, paths: typing.Sequence[str]) -> None """
        pass

    def setUrlInterceptor(self, urlInterceptor): # real signature unknown; restored from __doc__
        """ setUrlInterceptor(self, urlInterceptor: PySide2.QtQml.QQmlAbstractUrlInterceptor) -> None """
        pass

    def trimComponentCache(self): # real signature unknown; restored from __doc__
        """ trimComponentCache(self) -> None """
        pass

    def urlInterceptor(self): # real signature unknown; restored from __doc__
        """ urlInterceptor(self) -> PySide2.QtQml.QQmlAbstractUrlInterceptor """
        pass

    def warnings(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, p, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    CppOwnership = PySide2.QtQml.QQmlEngine.ObjectOwnership.CppOwnership
    JavaScriptOwnership = PySide2.QtQml.QQmlEngine.ObjectOwnership.JavaScriptOwnership
    ObjectOwnership = None # (!) real value is "<class 'PySide2.QtQml.QQmlEngine.ObjectOwnership'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D99040>'


class QQmlApplicationEngine(QQmlEngine):
    """
    QQmlApplicationEngine(self, filePath: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlApplicationEngine(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlApplicationEngine(self, url: PySide2.QtCore.QUrl, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def load(self, filePath): # real signature unknown; restored from __doc__
        """
        load(self, filePath: str) -> None
        load(self, url: PySide2.QtCore.QUrl) -> None
        """
        pass

    def loadData(self, data, url=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ loadData(self, data: PySide2.QtCore.QByteArray, url: PySide2.QtCore.QUrl = Default(QUrl)) -> None """
        pass

    def objectCreated(self, *args, **kwargs): # real signature unknown
        pass

    def rootObjects(self): # real signature unknown; restored from __doc__
        """ rootObjects(self) -> typing.List[PySide2.QtCore.QObject] """
        pass

    def setInitialProperties(self, initialProperties, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setInitialProperties(self, initialProperties: typing.Dict[str, typing.Any]) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, filePath, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D99240>'


class QQmlComponent(__PySide2_QtCore.QObject):
    """
    QQmlComponent(self, arg__1: PySide2.QtQml.QQmlEngine, fileName: str, mode: PySide2.QtQml.QQmlComponent.CompilationMode, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlComponent(self, arg__1: PySide2.QtQml.QQmlEngine, fileName: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlComponent(self, arg__1: PySide2.QtQml.QQmlEngine, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlComponent(self, arg__1: PySide2.QtQml.QQmlEngine, url: PySide2.QtCore.QUrl, mode: PySide2.QtQml.QQmlComponent.CompilationMode, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlComponent(self, arg__1: PySide2.QtQml.QQmlEngine, url: PySide2.QtCore.QUrl, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlComponent(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def beginCreate(self, arg__1): # real signature unknown; restored from __doc__
        """ beginCreate(self, arg__1: PySide2.QtQml.QQmlContext) -> PySide2.QtCore.QObject """
        pass

    def completeCreate(self): # real signature unknown; restored from __doc__
        """ completeCreate(self) -> None """
        pass

    def create(self, arg__1, context, PySide2_QtQml_QQmlContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        create(self, arg__1: PySide2.QtQml.QQmlIncubator, context: typing.Optional[PySide2.QtQml.QQmlContext] = None, forContext: typing.Optional[PySide2.QtQml.QQmlContext] = None) -> None
        create(self, context: typing.Optional[PySide2.QtQml.QQmlContext] = None) -> PySide2.QtCore.QObject
        """
        pass

    def createWithInitialProperties(self, initialProperties, p_str=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ createWithInitialProperties(self, initialProperties: typing.Dict[str, typing.Any], context: typing.Optional[PySide2.QtQml.QQmlContext] = None) -> PySide2.QtCore.QObject """
        pass

    def creationContext(self): # real signature unknown; restored from __doc__
        """ creationContext(self) -> PySide2.QtQml.QQmlContext """
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> PySide2.QtQml.QQmlEngine """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> typing.List[PySide2.QtQml.QQmlError] """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

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

    def loadUrl(self, url): # real signature unknown; restored from __doc__
        """
        loadUrl(self, url: PySide2.QtCore.QUrl) -> None
        loadUrl(self, url: PySide2.QtCore.QUrl, mode: PySide2.QtQml.QQmlComponent.CompilationMode) -> None
        """
        pass

    def progress(self): # real signature unknown; restored from __doc__
        """ progress(self) -> float """
        return 0.0

    def progressChanged(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, arg__1, baseUrl): # real signature unknown; restored from __doc__
        """ setData(self, arg__1: PySide2.QtCore.QByteArray, baseUrl: PySide2.QtCore.QUrl) -> None """
        pass

    def setInitialProperties(self, component, properties, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setInitialProperties(self, component: PySide2.QtCore.QObject, properties: typing.Dict[str, typing.Any]) -> None """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtQml.QQmlComponent.Status """
        pass

    def statusChanged(self, *args, **kwargs): # real signature unknown
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1, fileName, mode, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Asynchronous = PySide2.QtQml.QQmlComponent.CompilationMode.Asynchronous
    CompilationMode = None # (!) real value is "<class 'PySide2.QtQml.QQmlComponent.CompilationMode'>"
    Error = PySide2.QtQml.QQmlComponent.Status.Error
    Loading = PySide2.QtQml.QQmlComponent.Status.Loading
    Null = PySide2.QtQml.QQmlComponent.Status.Null
    PreferSynchronous = PySide2.QtQml.QQmlComponent.CompilationMode.PreferSynchronous
    Ready = PySide2.QtQml.QQmlComponent.Status.Ready
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D87FC0>'
    Status = None # (!) real value is "<class 'PySide2.QtQml.QQmlComponent.Status'>"


class QQmlContext(__PySide2_QtCore.QObject):
    """
    QQmlContext(self, parent: PySide2.QtQml.QQmlContext, objParent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlContext(self, parent: PySide2.QtQml.QQmlEngine, objParent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def contextObject(self): # real signature unknown; restored from __doc__
        """ contextObject(self) -> PySide2.QtCore.QObject """
        pass

    def contextProperty(self, arg__1): # real signature unknown; restored from __doc__
        """ contextProperty(self, arg__1: str) -> typing.Any """
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> PySide2.QtQml.QQmlEngine """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nameForObject(self, arg__1): # real signature unknown; restored from __doc__
        """ nameForObject(self, arg__1: PySide2.QtCore.QObject) -> str """
        return ""

    def parentContext(self): # real signature unknown; restored from __doc__
        """ parentContext(self) -> PySide2.QtQml.QQmlContext """
        pass

    def resolvedUrl(self, arg__1): # real signature unknown; restored from __doc__
        """ resolvedUrl(self, arg__1: PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl """
        pass

    def setBaseUrl(self, arg__1): # real signature unknown; restored from __doc__
        """ setBaseUrl(self, arg__1: PySide2.QtCore.QUrl) -> None """
        pass

    def setContextObject(self, arg__1): # real signature unknown; restored from __doc__
        """ setContextObject(self, arg__1: PySide2.QtCore.QObject) -> None """
        pass

    def setContextProperty(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        setContextProperty(self, arg__1: str, arg__2: PySide2.QtCore.QObject) -> None
        setContextProperty(self, arg__1: str, arg__2: typing.Any) -> None
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, objParent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D87940>'


class QQmlDebuggingEnabler(__Shiboken.Object):
    """ QQmlDebuggingEnabler(self, printWarning: bool = True) -> None """
    def connectToLocalDebugger(self, socketFileName, mode=None): # real signature unknown; restored from __doc__
        """ connectToLocalDebugger(socketFileName: str, mode: PySide2.QtQml.QQmlDebuggingEnabler.StartMode = PySide2.QtQml.QQmlDebuggingEnabler.StartMode.DoNotWaitForClient) -> bool """
        return False

    def debuggerServices(self): # real signature unknown; restored from __doc__
        """ debuggerServices() -> typing.List[str] """
        pass

    def inspectorServices(self): # real signature unknown; restored from __doc__
        """ inspectorServices() -> typing.List[str] """
        pass

    def nativeDebuggerServices(self): # real signature unknown; restored from __doc__
        """ nativeDebuggerServices() -> typing.List[str] """
        pass

    def profilerServices(self): # real signature unknown; restored from __doc__
        """ profilerServices() -> typing.List[str] """
        pass

    def setServices(self, services, p_str=None): # real signature unknown; restored from __doc__
        """ setServices(services: typing.Sequence[str]) -> None """
        pass

    def startDebugConnector(self, pluginName, configuration, p_str=None, typing_Any=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ startDebugConnector(pluginName: str, configuration: typing.Dict[str, typing.Any] = typing.Dict[str, typing.Any]) -> bool """
        pass

    def startTcpDebugServer(self, port, mode=None, hostName=''): # real signature unknown; restored from __doc__
        """ startTcpDebugServer(port: int, mode: PySide2.QtQml.QQmlDebuggingEnabler.StartMode = PySide2.QtQml.QQmlDebuggingEnabler.StartMode.DoNotWaitForClient, hostName: str = '') -> bool """
        return False

    def __init__(self, printWarning=True): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DoNotWaitForClient = PySide2.QtQml.QQmlDebuggingEnabler.StartMode.DoNotWaitForClient
    StartMode = None # (!) real value is "<class 'PySide2.QtQml.QQmlDebuggingEnabler.StartMode'>"
    WaitForClient = PySide2.QtQml.QQmlDebuggingEnabler.StartMode.WaitForClient


class QQmlError(__Shiboken.Object):
    """
    QQmlError(self) -> None
    QQmlError(self, arg__1: PySide2.QtQml.QQmlError) -> None
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
        """ messageType(self) -> PySide2.QtCore.QtMsgType """
        pass

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> PySide2.QtCore.QObject """
        pass

    def setColumn(self, arg__1): # real signature unknown; restored from __doc__
        """ setColumn(self, arg__1: int) -> None """
        pass

    def setDescription(self, arg__1): # real signature unknown; restored from __doc__
        """ setDescription(self, arg__1: str) -> None """
        pass

    def setLine(self, arg__1): # real signature unknown; restored from __doc__
        """ setLine(self, arg__1: int) -> None """
        pass

    def setMessageType(self, messageType): # real signature unknown; restored from __doc__
        """ setMessageType(self, messageType: PySide2.QtCore.QtMsgType) -> None """
        pass

    def setObject(self, arg__1): # real signature unknown; restored from __doc__
        """ setObject(self, arg__1: PySide2.QtCore.QObject) -> None """
        pass

    def setUrl(self, arg__1): # real signature unknown; restored from __doc__
        """ setUrl(self, arg__1: PySide2.QtCore.QUrl) -> None """
        pass

    def toString(self): # real signature unknown; restored from __doc__
        """ toString(self) -> str """
        return ""

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
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


class QQmlExpression(__PySide2_QtCore.QObject):
    """
    QQmlExpression(self) -> None
    QQmlExpression(self, arg__1: PySide2.QtQml.QQmlContext, arg__2: PySide2.QtCore.QObject, arg__3: str, arg__4: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QQmlExpression(self, arg__1: PySide2.QtQml.QQmlScriptString, arg__2: typing.Optional[PySide2.QtQml.QQmlContext] = None, arg__3: typing.Optional[PySide2.QtCore.QObject] = None, arg__4: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) -> None """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def context(self): # real signature unknown; restored from __doc__
        """ context(self) -> PySide2.QtQml.QQmlContext """
        pass

    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> PySide2.QtQml.QQmlEngine """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtQml.QQmlError """
        pass

    def evaluate(self): # real signature unknown; restored from __doc__
        """ evaluate(self) -> typing.Tuple[typing.Any, bool] """
        pass

    def expression(self): # real signature unknown; restored from __doc__
        """ expression(self) -> str """
        return ""

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def notifyOnValueChanged(self): # real signature unknown; restored from __doc__
        """ notifyOnValueChanged(self) -> bool """
        return False

    def scopeObject(self): # real signature unknown; restored from __doc__
        """ scopeObject(self) -> PySide2.QtCore.QObject """
        pass

    def setExpression(self, arg__1): # real signature unknown; restored from __doc__
        """ setExpression(self, arg__1: str) -> None """
        pass

    def setNotifyOnValueChanged(self, arg__1): # real signature unknown; restored from __doc__
        """ setNotifyOnValueChanged(self, arg__1: bool) -> None """
        pass

    def setSourceLocation(self, fileName, line, column=0): # real signature unknown; restored from __doc__
        """ setSourceLocation(self, fileName: str, line: int, column: int = 0) -> None """
        pass

    def sourceFile(self): # real signature unknown; restored from __doc__
        """ sourceFile(self) -> str """
        return ""

    def valueChanged(self, *args, **kwargs): # real signature unknown
        pass

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D87640>'


class QQmlTypesExtensionInterface(__Shiboken.Object):
    """ QQmlTypesExtensionInterface(self) -> None """
    def registerTypes(self, uri): # real signature unknown; restored from __doc__
        """ registerTypes(self, uri: bytes) -> None """
        pass

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


class QQmlExtensionInterface(QQmlTypesExtensionInterface):
    """ QQmlExtensionInterface(self) -> None """
    def initializeEngine(self, engine, uri): # real signature unknown; restored from __doc__
        """ initializeEngine(self, engine: PySide2.QtQml.QQmlEngine, uri: bytes) -> None """
        pass

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


class QQmlExtensionPlugin(__PySide2_QtCore.QObject, QQmlExtensionInterface):
    """ QQmlExtensionPlugin(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def baseUrl(self): # real signature unknown; restored from __doc__
        """ baseUrl(self) -> PySide2.QtCore.QUrl """
        pass

    def initializeEngine(self, engine, uri): # real signature unknown; restored from __doc__
        """ initializeEngine(self, engine: PySide2.QtQml.QQmlEngine, uri: bytes) -> None """
        pass

    def registerTypes(self, uri): # real signature unknown; restored from __doc__
        """ registerTypes(self, uri: bytes) -> None """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D87340>'


class QQmlFile(__Shiboken.Object):
    """
    QQmlFile(self) -> None
    QQmlFile(self, arg__1: PySide2.QtQml.QQmlEngine, arg__2: PySide2.QtCore.QUrl) -> None
    QQmlFile(self, arg__1: PySide2.QtQml.QQmlEngine, arg__2: str) -> None
    """
    def clear(self): # real signature unknown; restored from __doc__
        """
        clear(self) -> None
        clear(self, arg__1: PySide2.QtCore.QObject) -> None
        """
        pass

    def connectDownloadProgress(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        connectDownloadProgress(self, arg__1: PySide2.QtCore.QObject, arg__2: bytes) -> bool
        connectDownloadProgress(self, arg__1: PySide2.QtCore.QObject, arg__2: int) -> bool
        """
        return False

    def connectFinished(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        connectFinished(self, arg__1: PySide2.QtCore.QObject, arg__2: bytes) -> bool
        connectFinished(self, arg__1: PySide2.QtCore.QObject, arg__2: int) -> bool
        """
        return False

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> bytes """
        return b""

    def dataByteArray(self): # real signature unknown; restored from __doc__
        """ dataByteArray(self) -> PySide2.QtCore.QByteArray """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> str """
        return ""

    def isError(self): # real signature unknown; restored from __doc__
        """ isError(self) -> bool """
        return False

    def isLoading(self): # real signature unknown; restored from __doc__
        """ isLoading(self) -> bool """
        return False

    def isLocalFile(self, url): # real signature unknown; restored from __doc__
        """
        isLocalFile(url: PySide2.QtCore.QUrl) -> bool
        isLocalFile(url: str) -> bool
        """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isReady(self): # real signature unknown; restored from __doc__
        """ isReady(self) -> bool """
        return False

    def isSynchronous(self, url): # real signature unknown; restored from __doc__
        """
        isSynchronous(url: PySide2.QtCore.QUrl) -> bool
        isSynchronous(url: str) -> bool
        """
        return False

    def load(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        load(self, arg__1: PySide2.QtQml.QQmlEngine, arg__2: PySide2.QtCore.QUrl) -> None
        load(self, arg__1: PySide2.QtQml.QQmlEngine, arg__2: str) -> None
        """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtQml.QQmlFile.Status """
        pass

    def url(self): # real signature unknown; restored from __doc__
        """ url(self) -> PySide2.QtCore.QUrl """
        pass

    def urlToLocalFileOrQrc(self, arg__1): # real signature unknown; restored from __doc__
        """
        urlToLocalFileOrQrc(arg__1: PySide2.QtCore.QUrl) -> str
        urlToLocalFileOrQrc(arg__1: str) -> str
        """
        return ""

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Error = PySide2.QtQml.QQmlFile.Status.Error
    Loading = PySide2.QtQml.QQmlFile.Status.Loading
    Null = PySide2.QtQml.QQmlFile.Status.Null
    Ready = PySide2.QtQml.QQmlFile.Status.Ready
    Status = None # (!) real value is "<class 'PySide2.QtQml.QQmlFile.Status'>"


class QQmlFileSelector(__PySide2_QtCore.QObject):
    """ QQmlFileSelector(self, engine: PySide2.QtQml.QQmlEngine, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def get(self, arg__1): # real signature unknown; restored from __doc__
        """ get(arg__1: PySide2.QtQml.QQmlEngine) -> PySide2.QtQml.QQmlFileSelector """
        pass

    def selector(self): # real signature unknown; restored from __doc__
        """ selector(self) -> PySide2.QtCore.QFileSelector """
        pass

    def setExtraSelectors(self, strings, p_str=None): # real signature unknown; restored from __doc__
        """ setExtraSelectors(self, strings: typing.Sequence[str]) -> None """
        pass

    def setSelector(self, selector): # real signature unknown; restored from __doc__
        """ setSelector(self, selector: PySide2.QtCore.QFileSelector) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, engine, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D871C0>'


class QQmlImageProviderBase(__Shiboken.Object):
    # no doc
    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> PySide2.QtQml.QQmlImageProviderBase.Flags """
        pass

    def imageType(self): # real signature unknown; restored from __doc__
        """ imageType(self) -> PySide2.QtQml.QQmlImageProviderBase.ImageType """
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

    Flag = None # (!) real value is "<class 'PySide2.QtQml.QQmlImageProviderBase.Flag'>"
    Flags = None # (!) real value is "<class 'PySide2.QtQml.QQmlImageProviderBase.Flags'>"
    ForceAsynchronousImageLoading = PySide2.QtQml.QQmlImageProviderBase.Flag.ForceAsynchronousImageLoading
    Image = PySide2.QtQml.QQmlImageProviderBase.ImageType.Image
    ImageResponse = PySide2.QtQml.QQmlImageProviderBase.ImageType.ImageResponse
    ImageType = None # (!) real value is "<class 'PySide2.QtQml.QQmlImageProviderBase.ImageType'>"
    Invalid = PySide2.QtQml.QQmlImageProviderBase.ImageType.Invalid
    Pixmap = PySide2.QtQml.QQmlImageProviderBase.ImageType.Pixmap
    Texture = PySide2.QtQml.QQmlImageProviderBase.ImageType.Texture


class QQmlIncubationController(__Shiboken.Object):
    """ QQmlIncubationController(self) -> None """
    def engine(self): # real signature unknown; restored from __doc__
        """ engine(self) -> PySide2.QtQml.QQmlEngine """
        pass

    def incubateFor(self, msecs): # real signature unknown; restored from __doc__
        """ incubateFor(self, msecs: int) -> None """
        pass

    def incubateWhile(self, msecs=0): # real signature unknown; restored from __doc__
        """ incubateWhile(self, msecs: int = 0) -> bool """
        return False

    def incubatingObjectCount(self): # real signature unknown; restored from __doc__
        """ incubatingObjectCount(self) -> int """
        return 0

    def incubatingObjectCountChanged(self, arg__1): # real signature unknown; restored from __doc__
        """ incubatingObjectCountChanged(self, arg__1: int) -> None """
        pass

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


class QQmlIncubator(__Shiboken.Object):
    """ QQmlIncubator(self, arg__1: PySide2.QtQml.QQmlIncubator.IncubationMode = PySide2.QtQml.QQmlIncubator.IncubationMode.Asynchronous) -> None """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def errors(self): # real signature unknown; restored from __doc__
        """ errors(self) -> typing.List[PySide2.QtQml.QQmlError] """
        pass

    def forceCompletion(self): # real signature unknown; restored from __doc__
        """ forceCompletion(self) -> None """
        pass

    def incubationMode(self): # real signature unknown; restored from __doc__
        """ incubationMode(self) -> PySide2.QtQml.QQmlIncubator.IncubationMode """
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
        """ object(self) -> PySide2.QtCore.QObject """
        pass

    def setInitialProperties(self, initialProperties, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setInitialProperties(self, initialProperties: typing.Dict[str, typing.Any]) -> None """
        pass

    def setInitialState(self, arg__1): # real signature unknown; restored from __doc__
        """ setInitialState(self, arg__1: PySide2.QtCore.QObject) -> None """
        pass

    def status(self): # real signature unknown; restored from __doc__
        """ status(self) -> PySide2.QtQml.QQmlIncubator.Status """
        pass

    def statusChanged(self, arg__1): # real signature unknown; restored from __doc__
        """ statusChanged(self, arg__1: PySide2.QtQml.QQmlIncubator.Status) -> None """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, arg__1=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Asynchronous = PySide2.QtQml.QQmlIncubator.IncubationMode.Asynchronous
    AsynchronousIfNested = PySide2.QtQml.QQmlIncubator.IncubationMode.AsynchronousIfNested
    Error = PySide2.QtQml.QQmlIncubator.Status.Error
    IncubationMode = None # (!) real value is "<class 'PySide2.QtQml.QQmlIncubator.IncubationMode'>"
    Loading = PySide2.QtQml.QQmlIncubator.Status.Loading
    Null = PySide2.QtQml.QQmlIncubator.Status.Null
    Ready = PySide2.QtQml.QQmlIncubator.Status.Ready
    Status = None # (!) real value is "<class 'PySide2.QtQml.QQmlIncubator.Status'>"
    Synchronous = PySide2.QtQml.QQmlIncubator.IncubationMode.Synchronous


class QQmlListReference(__Shiboken.Object):
    """
    QQmlListReference(self) -> None
    QQmlListReference(self, arg__1: PySide2.QtCore.QObject, property: bytes, arg__3: typing.Optional[PySide2.QtQml.QQmlEngine] = None) -> None
    QQmlListReference(self, arg__1: PySide2.QtQml.QQmlListReference) -> None
    """
    def append(self, arg__1): # real signature unknown; restored from __doc__
        """ append(self, arg__1: PySide2.QtCore.QObject) -> bool """
        return False

    def at(self, arg__1): # real signature unknown; restored from __doc__
        """ at(self, arg__1: int) -> PySide2.QtCore.QObject """
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
        """ listElementType(self) -> PySide2.QtCore.QMetaObject """
        pass

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> PySide2.QtCore.QObject """
        pass

    def removeLast(self): # real signature unknown; restored from __doc__
        """ removeLast(self) -> bool """
        return False

    def replace(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ replace(self, arg__1: int, arg__2: PySide2.QtCore.QObject) -> bool """
        return False

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QQmlNetworkAccessManagerFactory(__Shiboken.Object):
    """ QQmlNetworkAccessManagerFactory(self) -> None """
    def create(self, parent): # real signature unknown; restored from __doc__
        """ create(self, parent: PySide2.QtCore.QObject) -> PySide2.QtNetwork.QNetworkAccessManager """
        pass

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


class QQmlParserStatus(__Shiboken.Object):
    """ QQmlParserStatus(self) -> None """
    def classBegin(self): # real signature unknown; restored from __doc__
        """ classBegin(self) -> None """
        pass

    def componentComplete(self): # real signature unknown; restored from __doc__
        """ componentComplete(self) -> None """
        pass

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


class QQmlProperty(__Shiboken.Object):
    """
    QQmlProperty(self) -> None
    QQmlProperty(self, arg__1: PySide2.QtCore.QObject) -> None
    QQmlProperty(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtQml.QQmlContext) -> None
    QQmlProperty(self, arg__1: PySide2.QtCore.QObject, arg__2: PySide2.QtQml.QQmlEngine) -> None
    QQmlProperty(self, arg__1: PySide2.QtCore.QObject, arg__2: str) -> None
    QQmlProperty(self, arg__1: PySide2.QtCore.QObject, arg__2: str, arg__3: PySide2.QtQml.QQmlContext) -> None
    QQmlProperty(self, arg__1: PySide2.QtCore.QObject, arg__2: str, arg__3: PySide2.QtQml.QQmlEngine) -> None
    QQmlProperty(self, arg__1: PySide2.QtQml.QQmlProperty) -> None
    """
    def connectNotifySignal(self, dest, method): # real signature unknown; restored from __doc__
        """
        connectNotifySignal(self, dest: PySide2.QtCore.QObject, method: int) -> bool
        connectNotifySignal(self, dest: PySide2.QtCore.QObject, slot: bytes) -> bool
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
        """ method(self) -> PySide2.QtCore.QMetaMethod """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def needsNotifySignal(self): # real signature unknown; restored from __doc__
        """ needsNotifySignal(self) -> bool """
        return False

    def object(self): # real signature unknown; restored from __doc__
        """ object(self) -> PySide2.QtCore.QObject """
        pass

    def property(self): # real signature unknown; restored from __doc__
        """ property(self) -> PySide2.QtCore.QMetaProperty """
        pass

    def propertyType(self): # real signature unknown; restored from __doc__
        """ propertyType(self) -> int """
        return 0

    def propertyTypeCategory(self): # real signature unknown; restored from __doc__
        """ propertyTypeCategory(self) -> PySide2.QtQml.QQmlProperty.PropertyTypeCategory """
        pass

    def propertyTypeName(self): # real signature unknown; restored from __doc__
        """ propertyTypeName(self) -> bytes """
        return b""

    def read(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        read(arg__1: PySide2.QtCore.QObject, arg__2: str) -> typing.Any
        read(arg__1: PySide2.QtCore.QObject, arg__2: str, arg__3: PySide2.QtQml.QQmlContext) -> typing.Any
        read(arg__1: PySide2.QtCore.QObject, arg__2: str, arg__3: PySide2.QtQml.QQmlEngine) -> typing.Any
        read(self) -> typing.Any
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """ reset(self) -> bool """
        return False

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtQml.QQmlProperty.Type """
        pass

    def write(self, arg__1, arg__2, arg__3): # real signature unknown; restored from __doc__
        """
        write(arg__1: PySide2.QtCore.QObject, arg__2: str, arg__3: typing.Any) -> bool
        write(arg__1: PySide2.QtCore.QObject, arg__2: str, arg__3: typing.Any, arg__4: PySide2.QtQml.QQmlContext) -> bool
        write(arg__1: PySide2.QtCore.QObject, arg__2: str, arg__3: typing.Any, arg__4: PySide2.QtQml.QQmlEngine) -> bool
        write(self, arg__1: typing.Any) -> bool
        """
        return False

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    Invalid = PySide2.QtQml.QQmlProperty.Type.Invalid
    InvalidCategory = PySide2.QtQml.QQmlProperty.PropertyTypeCategory.InvalidCategory
    List = PySide2.QtQml.QQmlProperty.PropertyTypeCategory.List
    Normal = PySide2.QtQml.QQmlProperty.PropertyTypeCategory.Normal
    Object = PySide2.QtQml.QQmlProperty.PropertyTypeCategory.Object
    Property = PySide2.QtQml.QQmlProperty.Type.Property
    PropertyTypeCategory = None # (!) real value is "<class 'PySide2.QtQml.QQmlProperty.PropertyTypeCategory'>"
    SignalProperty = PySide2.QtQml.QQmlProperty.Type.SignalProperty
    Type = None # (!) real value is "<class 'PySide2.QtQml.QQmlProperty.Type'>"
    __hash__ = None


class QQmlPropertyMap(__PySide2_QtCore.QObject):
    """ QQmlPropertyMap(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def clear(self, key): # real signature unknown; restored from __doc__
        """ clear(self, key: str) -> None """
        pass

    def contains(self, key): # real signature unknown; restored from __doc__
        """ contains(self, key: str) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def insert(self, key, value): # real signature unknown; restored from __doc__
        """ insert(self, key: str, value: typing.Any) -> None """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def keys(self): # real signature unknown; restored from __doc__
        """ keys(self) -> typing.List[str] """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def updateValue(self, key, input): # real signature unknown; restored from __doc__
        """ updateValue(self, key: str, input: typing.Any) -> typing.Any """
        pass

    def value(self, key): # real signature unknown; restored from __doc__
        """ value(self, key: str) -> typing.Any """
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000023C51D87040>'


class QQmlPropertyValueSource(__Shiboken.Object):
    """ QQmlPropertyValueSource(self) -> None """
    def setTarget(self, arg__1): # real signature unknown; restored from __doc__
        """ setTarget(self, arg__1: PySide2.QtQml.QQmlProperty) -> None """
        pass

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


class QQmlScriptString(__Shiboken.Object):
    """
    QQmlScriptString(self) -> None
    QQmlScriptString(self, arg__1: PySide2.QtQml.QQmlScriptString) -> None
    """
    def booleanLiteral(self): # real signature unknown; restored from __doc__
        """ booleanLiteral(self) -> typing.Tuple[bool, bool] """
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
        """ numberLiteral(self) -> typing.Tuple[float, bool] """
        pass

    def stringLiteral(self): # real signature unknown; restored from __doc__
        """ stringLiteral(self) -> str """
        return ""

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

    __hash__ = None


class QtQml(__Shiboken.Object):
    # no doc
    def qmlAttachedPropertiesObject(self, arg__2, arg__3, create): # real signature unknown; restored from __doc__
        """ qmlAttachedPropertiesObject(arg__2: PySide2.QtCore.QObject, arg__3: PySide2.QtCore.QMetaObject, create: bool) -> typing.Tuple[PySide2.QtCore.QObject, int] """
        pass

    def qmlAttachedPropertiesObjectById(self, arg__1, arg__2, create=True): # real signature unknown; restored from __doc__
        """ qmlAttachedPropertiesObjectById(arg__1: int, arg__2: PySide2.QtCore.QObject, create: bool = True) -> PySide2.QtCore.QObject """
        pass

    def qmlContext(self, arg__1): # real signature unknown; restored from __doc__
        """ qmlContext(arg__1: PySide2.QtCore.QObject) -> PySide2.QtQml.QQmlContext """
        pass

    def qmlEngine(self, arg__1): # real signature unknown; restored from __doc__
        """ qmlEngine(arg__1: PySide2.QtCore.QObject) -> PySide2.QtQml.QQmlEngine """
        pass

    def qmlExecuteDeferred(self, arg__1): # real signature unknown; restored from __doc__
        """ qmlExecuteDeferred(arg__1: PySide2.QtCore.QObject) -> None """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class VolatileBool(object):
    # no doc
    def get(self): # real signature unknown; restored from __doc__
        """
        get() -> bool
        
        B.get() -> Bool. Returns the value of the volatile boolean
        """
        return False

    def set(self, a): # real signature unknown; restored from __doc__
        """
        set(a: object) -> None
        
        B.set(a) -> None. Sets the value of the volatile boolean
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023C50FE17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtQml', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000023C50FE17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtQml.cp310-win_amd64.pyd')"

