# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QMetaObject(__Shiboken.Object):
    """ QMetaObject(self) -> None """
    def cast(self, obj): # real signature unknown; restored from __doc__
        """ cast(self, obj: PySide2.QtCore.QObject) -> PySide2.QtCore.QObject """
        pass

    def checkConnectArgs(self, signal, method): # real signature unknown; restored from __doc__
        """
        checkConnectArgs(signal: PySide2.QtCore.QMetaMethod, method: PySide2.QtCore.QMetaMethod) -> bool
        checkConnectArgs(signal: bytes, method: bytes) -> bool
        """
        return False

    def classInfo(self, index): # real signature unknown; restored from __doc__
        """ classInfo(self, index: int) -> PySide2.QtCore.QMetaClassInfo """
        pass

    def classInfoCount(self): # real signature unknown; restored from __doc__
        """ classInfoCount(self) -> int """
        return 0

    def classInfoOffset(self): # real signature unknown; restored from __doc__
        """ classInfoOffset(self) -> int """
        return 0

    def className(self): # real signature unknown; restored from __doc__
        """ className(self) -> bytes """
        return b""

    def connectSlotsByName(self, o): # real signature unknown; restored from __doc__
        """ connectSlotsByName(o: PySide2.QtCore.QObject) -> None """
        pass

    def constructor(self, index): # real signature unknown; restored from __doc__
        """ constructor(self, index: int) -> PySide2.QtCore.QMetaMethod """
        pass

    def constructorCount(self): # real signature unknown; restored from __doc__
        """ constructorCount(self) -> int """
        return 0

    def disconnect(self, sender, signal_index, receiver, method_index): # real signature unknown; restored from __doc__
        """ disconnect(sender: PySide2.QtCore.QObject, signal_index: int, receiver: PySide2.QtCore.QObject, method_index: int) -> bool """
        return False

    def disconnectOne(self, sender, signal_index, receiver, method_index): # real signature unknown; restored from __doc__
        """ disconnectOne(sender: PySide2.QtCore.QObject, signal_index: int, receiver: PySide2.QtCore.QObject, method_index: int) -> bool """
        return False

    def enumerator(self, index): # real signature unknown; restored from __doc__
        """ enumerator(self, index: int) -> PySide2.QtCore.QMetaEnum """
        pass

    def enumeratorCount(self): # real signature unknown; restored from __doc__
        """ enumeratorCount(self) -> int """
        return 0

    def enumeratorOffset(self): # real signature unknown; restored from __doc__
        """ enumeratorOffset(self) -> int """
        return 0

    def indexOfClassInfo(self, name): # real signature unknown; restored from __doc__
        """ indexOfClassInfo(self, name: bytes) -> int """
        return 0

    def indexOfConstructor(self, constructor): # real signature unknown; restored from __doc__
        """ indexOfConstructor(self, constructor: bytes) -> int """
        return 0

    def indexOfEnumerator(self, name): # real signature unknown; restored from __doc__
        """ indexOfEnumerator(self, name: bytes) -> int """
        return 0

    def indexOfMethod(self, method): # real signature unknown; restored from __doc__
        """ indexOfMethod(self, method: bytes) -> int """
        return 0

    def indexOfProperty(self, name): # real signature unknown; restored from __doc__
        """ indexOfProperty(self, name: bytes) -> int """
        return 0

    def indexOfSignal(self, signal): # real signature unknown; restored from __doc__
        """ indexOfSignal(self, signal: bytes) -> int """
        return 0

    def indexOfSlot(self, slot): # real signature unknown; restored from __doc__
        """ indexOfSlot(self, slot: bytes) -> int """
        return 0

    def inherits(self, metaObject): # real signature unknown; restored from __doc__
        """ inherits(self, metaObject: PySide2.QtCore.QMetaObject) -> bool """
        return False

    def invokeMethod(self, obj, member, arg__3, ret, val0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        invokeMethod(obj: PySide2.QtCore.QObject, member: bytes, arg__3: PySide2.QtCore.Qt.ConnectionType, ret: PySide2.QtCore.QGenericReturnArgument, val0: PySide2.QtCore.QGenericArgument = ..., val1: PySide2.QtCore.QGenericArgument = ..., val2: PySide2.QtCore.QGenericArgument = ..., val3: PySide2.QtCore.QGenericArgument = ..., val4: PySide2.QtCore.QGenericArgument = ..., val5: PySide2.QtCore.QGenericArgument = ..., val6: PySide2.QtCore.QGenericArgument = ..., val7: PySide2.QtCore.QGenericArgument = ..., val8: PySide2.QtCore.QGenericArgument = ..., val9: PySide2.QtCore.QGenericArgument = ...) -> bool
        invokeMethod(obj: PySide2.QtCore.QObject, member: bytes, ret: PySide2.QtCore.QGenericReturnArgument, val0: PySide2.QtCore.QGenericArgument = ..., val1: PySide2.QtCore.QGenericArgument = ..., val2: PySide2.QtCore.QGenericArgument = ..., val3: PySide2.QtCore.QGenericArgument = ..., val4: PySide2.QtCore.QGenericArgument = ..., val5: PySide2.QtCore.QGenericArgument = ..., val6: PySide2.QtCore.QGenericArgument = ..., val7: PySide2.QtCore.QGenericArgument = ..., val8: PySide2.QtCore.QGenericArgument = ..., val9: PySide2.QtCore.QGenericArgument = ...) -> bool
        invokeMethod(obj: PySide2.QtCore.QObject, member: bytes, type: PySide2.QtCore.Qt.ConnectionType, val0: PySide2.QtCore.QGenericArgument = ..., val1: PySide2.QtCore.QGenericArgument = ..., val2: PySide2.QtCore.QGenericArgument = ..., val3: PySide2.QtCore.QGenericArgument = ..., val4: PySide2.QtCore.QGenericArgument = ..., val5: PySide2.QtCore.QGenericArgument = ..., val6: PySide2.QtCore.QGenericArgument = ..., val7: PySide2.QtCore.QGenericArgument = ..., val8: PySide2.QtCore.QGenericArgument = ..., val9: PySide2.QtCore.QGenericArgument = ...) -> bool
        invokeMethod(obj: PySide2.QtCore.QObject, member: bytes, val0: PySide2.QtCore.QGenericArgument = ..., val1: PySide2.QtCore.QGenericArgument = ..., val2: PySide2.QtCore.QGenericArgument = ..., val3: PySide2.QtCore.QGenericArgument = ..., val4: PySide2.QtCore.QGenericArgument = ..., val5: PySide2.QtCore.QGenericArgument = ..., val6: PySide2.QtCore.QGenericArgument = ..., val7: PySide2.QtCore.QGenericArgument = ..., val8: PySide2.QtCore.QGenericArgument = ..., val9: PySide2.QtCore.QGenericArgument = ...) -> bool
        """
        pass

    def method(self, index): # real signature unknown; restored from __doc__
        """ method(self, index: int) -> PySide2.QtCore.QMetaMethod """
        pass

    def methodCount(self): # real signature unknown; restored from __doc__
        """ methodCount(self) -> int """
        return 0

    def methodOffset(self): # real signature unknown; restored from __doc__
        """ methodOffset(self) -> int """
        return 0

    def newInstance(self, val0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ newInstance(self, val0: PySide2.QtCore.QGenericArgument = ..., val1: PySide2.QtCore.QGenericArgument = ..., val2: PySide2.QtCore.QGenericArgument = ..., val3: PySide2.QtCore.QGenericArgument = ..., val4: PySide2.QtCore.QGenericArgument = ..., val5: PySide2.QtCore.QGenericArgument = ..., val6: PySide2.QtCore.QGenericArgument = ..., val7: PySide2.QtCore.QGenericArgument = ..., val8: PySide2.QtCore.QGenericArgument = ..., val9: PySide2.QtCore.QGenericArgument = ...) -> PySide2.QtCore.QObject """
        pass

    def normalizedSignature(self, method): # real signature unknown; restored from __doc__
        """ normalizedSignature(method: bytes) -> PySide2.QtCore.QByteArray """
        pass

    def normalizedType(self, type): # real signature unknown; restored from __doc__
        """ normalizedType(type: bytes) -> PySide2.QtCore.QByteArray """
        pass

    def property(self, index): # real signature unknown; restored from __doc__
        """ property(self, index: int) -> PySide2.QtCore.QMetaProperty """
        pass

    def propertyCount(self): # real signature unknown; restored from __doc__
        """ propertyCount(self) -> int """
        return 0

    def propertyOffset(self): # real signature unknown; restored from __doc__
        """ propertyOffset(self) -> int """
        return 0

    def superClass(self): # real signature unknown; restored from __doc__
        """ superClass(self) -> PySide2.QtCore.QMetaObject """
        pass

    def userProperty(self): # real signature unknown; restored from __doc__
        """ userProperty(self) -> PySide2.QtCore.QMetaProperty """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Call = None # (!) real value is "<class 'PySide2.QtCore.QMetaObject.Call'>"
    Connection = None # (!) real value is "<class 'PySide2.QtCore.QMetaObject.Connection'>"
    CreateInstance = PySide2.QtCore.QMetaObject.Call.CreateInstance
    IndexOfMethod = PySide2.QtCore.QMetaObject.Call.IndexOfMethod
    InvokeMetaMethod = PySide2.QtCore.QMetaObject.Call.InvokeMetaMethod
    QueryPropertyDesignable = PySide2.QtCore.QMetaObject.Call.QueryPropertyDesignable
    QueryPropertyEditable = PySide2.QtCore.QMetaObject.Call.QueryPropertyEditable
    QueryPropertyScriptable = PySide2.QtCore.QMetaObject.Call.QueryPropertyScriptable
    QueryPropertyStored = PySide2.QtCore.QMetaObject.Call.QueryPropertyStored
    QueryPropertyUser = PySide2.QtCore.QMetaObject.Call.QueryPropertyUser
    ReadProperty = PySide2.QtCore.QMetaObject.Call.ReadProperty
    RegisterMethodArgumentMetaType = PySide2.QtCore.QMetaObject.Call.RegisterMethodArgumentMetaType
    RegisterPropertyMetaType = PySide2.QtCore.QMetaObject.Call.RegisterPropertyMetaType
    ResetProperty = PySide2.QtCore.QMetaObject.Call.ResetProperty
    WriteProperty = PySide2.QtCore.QMetaObject.Call.WriteProperty


