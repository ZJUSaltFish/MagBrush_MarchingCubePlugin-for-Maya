# encoding: utf-8
# module PyQt5.QtCore
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


class QMetaObject(__sip.simplewrapper):
    """
    QMetaObject()
    QMetaObject(a0: QMetaObject)
    """
    def checkConnectArgs(self, signal, method): # real signature unknown; restored from __doc__ with multiple overloads
        """
        checkConnectArgs(signal: str, method: str) -> bool
        checkConnectArgs(signal: QMetaMethod, method: QMetaMethod) -> bool
        """
        return False

    def classInfo(self, index): # real signature unknown; restored from __doc__
        """ classInfo(self, index: int) -> QMetaClassInfo """
        return QMetaClassInfo

    def classInfoCount(self): # real signature unknown; restored from __doc__
        """ classInfoCount(self) -> int """
        return 0

    def classInfoOffset(self): # real signature unknown; restored from __doc__
        """ classInfoOffset(self) -> int """
        return 0

    def className(self): # real signature unknown; restored from __doc__
        """ className(self) -> str """
        return ""

    def connectSlotsByName(self, o): # real signature unknown; restored from __doc__
        """ connectSlotsByName(o: QObject) """
        pass

    def constructor(self, index): # real signature unknown; restored from __doc__
        """ constructor(self, index: int) -> QMetaMethod """
        return QMetaMethod

    def constructorCount(self): # real signature unknown; restored from __doc__
        """ constructorCount(self) -> int """
        return 0

    def enumerator(self, index): # real signature unknown; restored from __doc__
        """ enumerator(self, index: int) -> QMetaEnum """
        return QMetaEnum

    def enumeratorCount(self): # real signature unknown; restored from __doc__
        """ enumeratorCount(self) -> int """
        return 0

    def enumeratorOffset(self): # real signature unknown; restored from __doc__
        """ enumeratorOffset(self) -> int """
        return 0

    def indexOfClassInfo(self, name): # real signature unknown; restored from __doc__
        """ indexOfClassInfo(self, name: str) -> int """
        return 0

    def indexOfConstructor(self, constructor): # real signature unknown; restored from __doc__
        """ indexOfConstructor(self, constructor: str) -> int """
        return 0

    def indexOfEnumerator(self, name): # real signature unknown; restored from __doc__
        """ indexOfEnumerator(self, name: str) -> int """
        return 0

    def indexOfMethod(self, method): # real signature unknown; restored from __doc__
        """ indexOfMethod(self, method: str) -> int """
        return 0

    def indexOfProperty(self, name): # real signature unknown; restored from __doc__
        """ indexOfProperty(self, name: str) -> int """
        return 0

    def indexOfSignal(self, signal): # real signature unknown; restored from __doc__
        """ indexOfSignal(self, signal: str) -> int """
        return 0

    def indexOfSlot(self, slot): # real signature unknown; restored from __doc__
        """ indexOfSlot(self, slot: str) -> int """
        return 0

    def inherits(self, metaObject): # real signature unknown; restored from __doc__
        """ inherits(self, metaObject: QMetaObject) -> bool """
        return False

    def invokeMethod(self, obj, member, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        invokeMethod(obj: QObject, member: str, type: Qt.ConnectionType, ret: QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object
        invokeMethod(obj: QObject, member: str, ret: QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object
        invokeMethod(obj: QObject, member: str, type: Qt.ConnectionType, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object
        invokeMethod(obj: QObject, member: str, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object
        """
        pass

    def method(self, index): # real signature unknown; restored from __doc__
        """ method(self, index: int) -> QMetaMethod """
        return QMetaMethod

    def methodCount(self): # real signature unknown; restored from __doc__
        """ methodCount(self) -> int """
        return 0

    def methodOffset(self): # real signature unknown; restored from __doc__
        """ methodOffset(self) -> int """
        return 0

    def normalizedSignature(self, method): # real signature unknown; restored from __doc__
        """ normalizedSignature(method: str) -> QByteArray """
        return QByteArray

    def normalizedType(self, type): # real signature unknown; restored from __doc__
        """ normalizedType(type: str) -> QByteArray """
        return QByteArray

    def property(self, index): # real signature unknown; restored from __doc__
        """ property(self, index: int) -> QMetaProperty """
        return QMetaProperty

    def propertyCount(self): # real signature unknown; restored from __doc__
        """ propertyCount(self) -> int """
        return 0

    def propertyOffset(self): # real signature unknown; restored from __doc__
        """ propertyOffset(self) -> int """
        return 0

    def superClass(self): # real signature unknown; restored from __doc__
        """ superClass(self) -> QMetaObject """
        return QMetaObject

    def userProperty(self): # real signature unknown; restored from __doc__
        """ userProperty(self) -> QMetaProperty """
        return QMetaProperty

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""




