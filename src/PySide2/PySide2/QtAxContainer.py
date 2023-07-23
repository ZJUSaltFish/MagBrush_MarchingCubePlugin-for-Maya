# encoding: utf-8
# module PySide2.QtAxContainer
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtAxContainer.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtWidgets as __PySide2_QtWidgets
import Shiboken as __Shiboken


# no functions
# classes

class QAxBase(__Shiboken.Object):
    """ QAxBase(self) -> None """
    def argumentsToList(self, var1, var2, var3, var4, var5, var6, var7, var8): # real signature unknown; restored from __doc__
        """ argumentsToList(var1: typing.Any, var2: typing.Any, var3: typing.Any, var4: typing.Any, var5: typing.Any, var6: typing.Any, var7: typing.Any, var8: typing.Any) -> typing.List[typing.Any] """
        pass

    def asVariant(self): # real signature unknown; restored from __doc__
        """ asVariant(self) -> typing.Any """
        pass

    def classContext(self): # real signature unknown; restored from __doc__
        """ classContext(self) -> int """
        return 0

    def className(self): # real signature unknown; restored from __doc__
        """ className(self) -> bytes """
        return b""

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def control(self): # real signature unknown; restored from __doc__
        """ control(self) -> str """
        return ""

    def disableClassInfo(self): # real signature unknown; restored from __doc__
        """ disableClassInfo(self) -> None """
        pass

    def disableEventSink(self): # real signature unknown; restored from __doc__
        """ disableEventSink(self) -> None """
        pass

    def disableMetaObject(self): # real signature unknown; restored from __doc__
        """ disableMetaObject(self) -> None """
        pass

    def dynamicCall(self, name, v1=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        dynamicCall(self, name: bytes, v1: typing.Any = Invalid(typing.Any), v2: typing.Any = Invalid(typing.Any), v3: typing.Any = Invalid(typing.Any), v4: typing.Any = Invalid(typing.Any), v5: typing.Any = Invalid(typing.Any), v6: typing.Any = Invalid(typing.Any), v7: typing.Any = Invalid(typing.Any), v8: typing.Any = Invalid(typing.Any)) -> typing.Any
        dynamicCall(self, name: bytes, vars: typing.Sequence[typing.Any]) -> typing.Any
        """
        pass

    def fallbackMetaObject(self): # real signature unknown; restored from __doc__
        """ fallbackMetaObject(self) -> PySide2.QtCore.QMetaObject """
        pass

    def generateDocumentation(self): # real signature unknown; restored from __doc__
        """ generateDocumentation(self) -> str """
        return ""

    def indexOfVerb(self, verb): # real signature unknown; restored from __doc__
        """ indexOfVerb(self, verb: str) -> int """
        return 0

    def initializeFrom(self, that): # real signature unknown; restored from __doc__
        """ initializeFrom(self, that: PySide2.QtAxContainer.QAxBase) -> None """
        pass

    def internalRelease(self): # real signature unknown; restored from __doc__
        """ internalRelease(self) -> None """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def propertyBag(self): # real signature unknown; restored from __doc__
        """ propertyBag(self) -> typing.Dict[str, typing.Any] """
        pass

    def propertyWritable(self, arg__1): # real signature unknown; restored from __doc__
        """ propertyWritable(self, arg__1: bytes) -> bool """
        return False

    def qObject(self): # real signature unknown; restored from __doc__
        """ qObject(self) -> PySide2.QtCore.QObject """
        pass

    def querySubObject(self, name, v1=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        querySubObject(self, name: bytes, v1: typing.Any = Invalid(typing.Any), v2: typing.Any = Invalid(typing.Any), v3: typing.Any = Invalid(typing.Any), v4: typing.Any = Invalid(typing.Any), v5: typing.Any = Invalid(typing.Any), v6: typing.Any = Invalid(typing.Any), v7: typing.Any = Invalid(typing.Any), v8: typing.Any = Invalid(typing.Any)) -> PySide2.QtAxContainer.QAxObject
        querySubObject(self, name: bytes, vars: typing.Sequence[typing.Any]) -> PySide2.QtAxContainer.QAxObject
        """
        pass

    def setClassContext(self, classContext): # real signature unknown; restored from __doc__
        """ setClassContext(self, classContext: int) -> None """
        pass

    def setControl(self, arg__1): # real signature unknown; restored from __doc__
        """ setControl(self, arg__1: str) -> bool """
        return False

    def setPropertyBag(self, arg__1, p_str=None, typing_Any=None): # real signature unknown; restored from __doc__
        """ setPropertyBag(self, arg__1: typing.Dict[str, typing.Any]) -> None """
        pass

    def setPropertyWritable(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """ setPropertyWritable(self, arg__1: bytes, arg__2: bool) -> None """
        pass

    def verbs(self): # real signature unknown; restored from __doc__
        """ verbs(self) -> typing.List[str] """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __lshift__(self, s): # real signature unknown; restored from __doc__
        """
        __lshift__(self, s: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self<<value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, s): # real signature unknown; restored from __doc__
        """
        __rshift__(self, s: PySide2.QtCore.QDataStream) -> PySide2.QtCore.QDataStream
        
        Return self>>value.
        """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QAxObject(__PySide2_QtCore.QObject, QAxBase):
    """
    QAxObject(self, c: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QAxObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def className(self): # real signature unknown; restored from __doc__
        """ className(self) -> bytes """
        return b""

    def doVerb(self, verb): # real signature unknown; restored from __doc__
        """ doVerb(self, verb: str) -> bool """
        return False

    def exception(self, *args, **kwargs): # real signature unknown
        pass

    def fallbackMetaObject(self): # real signature unknown; restored from __doc__
        """ fallbackMetaObject(self) -> PySide2.QtCore.QMetaObject """
        pass

    def propertyChanged(self, *args, **kwargs): # real signature unknown
        pass

    def qObject(self): # real signature unknown; restored from __doc__
        """ qObject(self) -> PySide2.QtCore.QObject """
        pass

    def signal(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, c, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000210AA3FA540>'


class QAxScript(__PySide2_QtCore.QObject):
    """ QAxScript(self, name: str, manager: PySide2.QtAxContainer.QAxScriptManager) -> None """
    def call(self, function, arguments, typing_Any=None): # real signature unknown; restored from __doc__
        """
        call(self, function: str, arguments: typing.Sequence[typing.Any]) -> typing.Any
        call(self, function: str, v1: typing.Any = Invalid(typing.Any), v2: typing.Any = Invalid(typing.Any), v3: typing.Any = Invalid(typing.Any), v4: typing.Any = Invalid(typing.Any), v5: typing.Any = Invalid(typing.Any), v6: typing.Any = Invalid(typing.Any), v7: typing.Any = Invalid(typing.Any), v8: typing.Any = Invalid(typing.Any)) -> typing.Any
        """
        pass

    def entered(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def functions(self, arg__1=None): # real signature unknown; restored from __doc__
        """ functions(self, arg__1: PySide2.QtAxContainer.QAxScript.FunctionFlags = PySide2.QtAxContainer.QAxScript.FunctionFlags.FunctionNames) -> typing.List[str] """
        pass

    def load(self, code, language=''): # real signature unknown; restored from __doc__
        """ load(self, code: str, language: str = '') -> bool """
        return False

    def scriptCode(self): # real signature unknown; restored from __doc__
        """ scriptCode(self) -> str """
        return ""

    def scriptEngine(self): # real signature unknown; restored from __doc__
        """ scriptEngine(self) -> PySide2.QtAxContainer.QAxScriptEngine """
        pass

    def scriptName(self): # real signature unknown; restored from __doc__
        """ scriptName(self) -> str """
        return ""

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, name, manager): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    FunctionFlags = None # (!) real value is "<class 'PySide2.QtAxContainer.QAxScript.FunctionFlags'>"
    FunctionNames = PySide2.QtAxContainer.QAxScript.FunctionFlags.FunctionNames
    FunctionSignatures = PySide2.QtAxContainer.QAxScript.FunctionFlags.FunctionSignatures
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000210AAEE9F40>'


class QAxScriptEngine(QAxObject):
    """ QAxScriptEngine(self, language: str, script: PySide2.QtAxContainer.QAxScript) -> None """
    def addItem(self, name): # real signature unknown; restored from __doc__
        """ addItem(self, name: str) -> None """
        pass

    def hasIntrospection(self): # real signature unknown; restored from __doc__
        """ hasIntrospection(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def scriptLanguage(self): # real signature unknown; restored from __doc__
        """ scriptLanguage(self) -> str """
        return ""

    def setState(self, st): # real signature unknown; restored from __doc__
        """ setState(self, st: PySide2.QtAxContainer.QAxScriptEngine.State) -> None """
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtAxContainer.QAxScriptEngine.State """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, language, script): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Closed = PySide2.QtAxContainer.QAxScriptEngine.State.Closed
    Connected = PySide2.QtAxContainer.QAxScriptEngine.State.Connected
    Disconnected = PySide2.QtAxContainer.QAxScriptEngine.State.Disconnected
    Initialized = PySide2.QtAxContainer.QAxScriptEngine.State.Initialized
    Started = PySide2.QtAxContainer.QAxScriptEngine.State.Started
    State = None # (!) real value is "<class 'PySide2.QtAxContainer.QAxScriptEngine.State'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000210A9F3A3C0>'
    Uninitialized = PySide2.QtAxContainer.QAxScriptEngine.State.Uninitialized


class QAxScriptManager(__PySide2_QtCore.QObject):
    """ QAxScriptManager(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addObject(self, p_object): # real signature unknown; restored from __doc__
        """ addObject(self, object: PySide2.QtAxContainer.QAxBase) -> None """
        pass

    def call(self, function, arguments, typing_Any=None): # real signature unknown; restored from __doc__
        """
        call(self, function: str, arguments: typing.Sequence[typing.Any]) -> typing.Any
        call(self, function: str, v1: typing.Any = Invalid(typing.Any), v2: typing.Any = Invalid(typing.Any), v3: typing.Any = Invalid(typing.Any), v4: typing.Any = Invalid(typing.Any), v5: typing.Any = Invalid(typing.Any), v6: typing.Any = Invalid(typing.Any), v7: typing.Any = Invalid(typing.Any), v8: typing.Any = Invalid(typing.Any)) -> typing.Any
        """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def functions(self, arg__1=None): # real signature unknown; restored from __doc__
        """ functions(self, arg__1: PySide2.QtAxContainer.QAxScript.FunctionFlags = PySide2.QtAxContainer.QAxScript.FunctionFlags.FunctionNames) -> typing.List[str] """
        pass

    def load(self, code, name, language): # real signature unknown; restored from __doc__
        """
        load(self, code: str, name: str, language: str) -> PySide2.QtAxContainer.QAxScript
        load(self, file: str, name: str) -> PySide2.QtAxContainer.QAxScript
        """
        pass

    def registerEngine(self, name, extension, code=''): # real signature unknown; restored from __doc__
        """ registerEngine(name: str, extension: str, code: str = '') -> bool """
        return False

    def script(self, name): # real signature unknown; restored from __doc__
        """ script(self, name: str) -> PySide2.QtAxContainer.QAxScript """
        pass

    def scriptFileFilter(self): # real signature unknown; restored from __doc__
        """ scriptFileFilter() -> str """
        return ""

    def scriptNames(self): # real signature unknown; restored from __doc__
        """ scriptNames(self) -> typing.List[str] """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000210AAEE9B00>'


class QAxSelect(__PySide2_QtWidgets.QDialog):
    """ QAxSelect(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, flags: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None """
    def clsid(self): # real signature unknown; restored from __doc__
        """ clsid(self) -> str """
        return ""

    def sandboxingLevel(self): # real signature unknown; restored from __doc__
        """ sandboxingLevel(self) -> PySide2.QtAxContainer.QAxSelect.SandboxingLevel """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    SandboxingLevel = None # (!) real value is "<class 'PySide2.QtAxContainer.QAxSelect.SandboxingLevel'>"
    SandboxingLowIntegrity = PySide2.QtAxContainer.QAxSelect.SandboxingLevel.SandboxingLowIntegrity
    SandboxingNone = PySide2.QtAxContainer.QAxSelect.SandboxingLevel.SandboxingNone
    SandboxingProcess = PySide2.QtAxContainer.QAxSelect.SandboxingLevel.SandboxingProcess
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000210AAEE9980>'


class QAxWidget(__PySide2_QtWidgets.QWidget, QAxBase):
    """
    QAxWidget(self, c: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    QAxWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    """
    def changeEvent(self, e): # real signature unknown; restored from __doc__
        """ changeEvent(self, e: PySide2.QtCore.QEvent) -> None """
        pass

    def className(self): # real signature unknown; restored from __doc__
        """ className(self) -> bytes """
        return b""

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def createHostWindow(self, arg__1): # real signature unknown; restored from __doc__
        """
        createHostWindow(self, arg__1: bool) -> bool
        createHostWindow(self, arg__1: bool, arg__2: PySide2.QtCore.QByteArray) -> bool
        """
        return False

    def doVerb(self, verb): # real signature unknown; restored from __doc__
        """ doVerb(self, verb: str) -> bool """
        return False

    def exception(self, *args, **kwargs): # real signature unknown
        pass

    def fallbackMetaObject(self): # real signature unknown; restored from __doc__
        """ fallbackMetaObject(self) -> PySide2.QtCore.QMetaObject """
        pass

    def minimumSizeHint(self): # real signature unknown; restored from __doc__
        """ minimumSizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def propertyChanged(self, *args, **kwargs): # real signature unknown
        pass

    def qObject(self): # real signature unknown; restored from __doc__
        """ qObject(self) -> PySide2.QtCore.QObject """
        pass

    def resizeEvent(self, arg__1): # real signature unknown; restored from __doc__
        """ resizeEvent(self, arg__1: PySide2.QtGui.QResizeEvent) -> None """
        pass

    def signal(self, *args, **kwargs): # real signature unknown
        pass

    def sizeHint(self): # real signature unknown; restored from __doc__
        """ sizeHint(self) -> PySide2.QtCore.QSize """
        pass

    def translateKeyEvent(self, message, keycode): # real signature unknown; restored from __doc__
        """ translateKeyEvent(self, message: int, keycode: int) -> bool """
        return False

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, c, parent, PySide2_QtWidgets_QWidget=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000210AAEEA700>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000210A9FB17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtAxContainer', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000210A9FB17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtAxContainer.cp310-win_amd64.pyd')"

