# encoding: utf-8
# module PySide2.QtTest
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtTest.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


# no functions
# classes

class QTest(__Shiboken.Object):
    # no doc
    def addColumnInternal(self, id, name): # real signature unknown; restored from __doc__
        """ addColumnInternal(id: int, name: bytes) -> None """
        pass

    def asciiToKey(self, ascii): # real signature unknown; restored from __doc__
        """ asciiToKey(ascii: int) -> PySide2.QtCore.Qt.Key """
        pass

    def compare_ptr_helper(self, t1, t2, actual, expected, file, line): # real signature unknown; restored from __doc__
        """ compare_ptr_helper(t1: int, t2: int, actual: bytes, expected: bytes, file: bytes, line: int) -> bool """
        return False

    def compare_string_helper(self, t1, t2, actual, expected, file, line): # real signature unknown; restored from __doc__
        """ compare_string_helper(t1: bytes, t2: bytes, actual: bytes, expected: bytes, file: bytes, line: int) -> bool """
        return False

    def createTouchDevice(self, devType=None): # real signature unknown; restored from __doc__
        """ createTouchDevice(devType: PySide2.QtGui.QTouchDevice.DeviceType = PySide2.QtGui.QTouchDevice.DeviceType.TouchScreen) -> PySide2.QtGui.QTouchDevice """
        pass

    def currentAppName(self): # real signature unknown; restored from __doc__
        """ currentAppName() -> bytes """
        return b""

    def currentDataTag(self): # real signature unknown; restored from __doc__
        """ currentDataTag() -> bytes """
        return b""

    def currentTestFailed(self): # real signature unknown; restored from __doc__
        """ currentTestFailed() -> bool """
        return False

    def currentTestFunction(self): # real signature unknown; restored from __doc__
        """ currentTestFunction() -> bytes """
        return b""

    def ignoreMessage(self, type, message): # real signature unknown; restored from __doc__
        """
        ignoreMessage(type: PySide2.QtCore.QtMsgType, message: bytes) -> None
        ignoreMessage(type: PySide2.QtCore.QtMsgType, messagePattern: PySide2.QtCore.QRegularExpression) -> None
        """
        pass

    def keyClick(self, widget, key, modifier=None, delay=-1): # real signature unknown; restored from __doc__
        """
        keyClick(widget: PySide2.QtWidgets.QWidget, key: PySide2.QtCore.Qt.Key, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyClick(widget: PySide2.QtWidgets.QWidget, key: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyClick(window: PySide2.QtGui.QWindow, key: PySide2.QtCore.Qt.Key, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyClick(window: PySide2.QtGui.QWindow, key: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        """
        pass

    def keyClicks(self, widget, sequence, modifier=None, delay=-1): # real signature unknown; restored from __doc__
        """ keyClicks(widget: PySide2.QtWidgets.QWidget, sequence: str, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None """
        pass

    def keyEvent(self, action, widget, ascii, modifier=None, delay=-1): # real signature unknown; restored from __doc__
        """
        keyEvent(action: PySide2.QtTest.QTest.KeyAction, widget: PySide2.QtWidgets.QWidget, ascii: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyEvent(action: PySide2.QtTest.QTest.KeyAction, widget: PySide2.QtWidgets.QWidget, key: PySide2.QtCore.Qt.Key, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyEvent(action: PySide2.QtTest.QTest.KeyAction, window: PySide2.QtGui.QWindow, ascii: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyEvent(action: PySide2.QtTest.QTest.KeyAction, window: PySide2.QtGui.QWindow, key: PySide2.QtCore.Qt.Key, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        """
        pass

    def keyPress(self, widget, key, modifier=None, delay=-1): # real signature unknown; restored from __doc__
        """
        keyPress(widget: PySide2.QtWidgets.QWidget, key: PySide2.QtCore.Qt.Key, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyPress(widget: PySide2.QtWidgets.QWidget, key: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyPress(window: PySide2.QtGui.QWindow, key: PySide2.QtCore.Qt.Key, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyPress(window: PySide2.QtGui.QWindow, key: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        """
        pass

    def keyRelease(self, widget, key, modifier=None, delay=-1): # real signature unknown; restored from __doc__
        """
        keyRelease(widget: PySide2.QtWidgets.QWidget, key: PySide2.QtCore.Qt.Key, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyRelease(widget: PySide2.QtWidgets.QWidget, key: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyRelease(window: PySide2.QtGui.QWindow, key: PySide2.QtCore.Qt.Key, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        keyRelease(window: PySide2.QtGui.QWindow, key: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers = PySide2.QtCore.Qt.KeyboardModifier.NoModifier, delay: int = -1) -> None
        """
        pass

    def keySequence(self, widget, keySequence): # real signature unknown; restored from __doc__
        """
        keySequence(widget: PySide2.QtWidgets.QWidget, keySequence: PySide2.QtGui.QKeySequence) -> None
        keySequence(window: PySide2.QtGui.QWindow, keySequence: PySide2.QtGui.QKeySequence) -> None
        """
        pass

    def keyToAscii(self, key): # real signature unknown; restored from __doc__
        """ keyToAscii(key: PySide2.QtCore.Qt.Key) -> int """
        return 0

    def mouseClick(self, widget, button, stateKey=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        mouseClick(widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers = Default(Qt.KeyboardModifiers), pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        mouseClick(window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers = Default(Qt.KeyboardModifiers), pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        """
        pass

    def mouseDClick(self, widget, button, stateKey=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        mouseDClick(widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers = Default(Qt.KeyboardModifiers), pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        mouseDClick(window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers = Default(Qt.KeyboardModifiers), pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        """
        pass

    def mouseEvent(self, action, widget, button, stateKey, pos, delay=-1): # real signature unknown; restored from __doc__
        """
        mouseEvent(action: PySide2.QtTest.QTest.MouseAction, widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers, pos: PySide2.QtCore.QPoint, delay: int = -1) -> None
        mouseEvent(action: PySide2.QtTest.QTest.MouseAction, window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers, pos: PySide2.QtCore.QPoint, delay: int = -1) -> None
        """
        pass

    def mouseMove(self, widget, pos=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        mouseMove(widget: PySide2.QtWidgets.QWidget, pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        mouseMove(window: PySide2.QtGui.QWindow, pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        """
        pass

    def mousePress(self, widget, button, stateKey=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        mousePress(widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers = Default(Qt.KeyboardModifiers), pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        mousePress(window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers = Default(Qt.KeyboardModifiers), pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        """
        pass

    def mouseRelease(self, widget, button, stateKey=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        mouseRelease(widget: PySide2.QtWidgets.QWidget, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers = Default(Qt.KeyboardModifiers), pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        mouseRelease(window: PySide2.QtGui.QWindow, button: PySide2.QtCore.Qt.MouseButton, stateKey: PySide2.QtCore.Qt.KeyboardModifiers = Default(Qt.KeyboardModifiers), pos: PySide2.QtCore.QPoint = Default(QPoint), delay: int = -1) -> None
        """
        pass

    def qCleanup(self): # real signature unknown; restored from __doc__
        """ qCleanup() -> None """
        pass

    def qElementData(self, elementName, metaTypeId): # real signature unknown; restored from __doc__
        """ qElementData(elementName: bytes, metaTypeId: int) -> int """
        return 0

    def qExpectFail(self, dataIndex, comment, mode, file, line): # real signature unknown; restored from __doc__
        """ qExpectFail(dataIndex: bytes, comment: bytes, mode: PySide2.QtTest.QTest.TestFailMode, file: bytes, line: int) -> bool """
        return False

    def qFindTestData(self, basepath, file, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        qFindTestData(basepath: str, file: typing.Optional[bytes] = None, line: int = 0, builddir: typing.Optional[bytes] = None) -> str
        qFindTestData(basepath: bytes, file: typing.Optional[bytes] = None, line: int = 0, builddir: typing.Optional[bytes] = None) -> str
        """
        pass

    def qGlobalData(self, tagName, typeId): # real signature unknown; restored from __doc__
        """ qGlobalData(tagName: bytes, typeId: int) -> int """
        return 0

    def qRun(self): # real signature unknown; restored from __doc__
        """ qRun() -> int """
        return 0

    def qSkip(self, message, file, line): # real signature unknown; restored from __doc__
        """ qSkip(message: bytes, file: bytes, line: int) -> None """
        pass

    def qWaitForWindowActive(self, widget, timeout=5000): # real signature unknown; restored from __doc__
        """ qWaitForWindowActive(widget: PySide2.QtWidgets.QWidget, timeout: int = 5000) -> bool """
        return False

    def qWaitForWindowExposed(self, widget, timeout=5000): # real signature unknown; restored from __doc__
        """ qWaitForWindowExposed(widget: PySide2.QtWidgets.QWidget, timeout: int = 5000) -> bool """
        return False

    def sendKeyEvent(self, action, widget, code, ascii, modifier, delay=-1): # real signature unknown; restored from __doc__
        """
        sendKeyEvent(action: PySide2.QtTest.QTest.KeyAction, widget: PySide2.QtWidgets.QWidget, code: PySide2.QtCore.Qt.Key, ascii: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers, delay: int = -1) -> None
        sendKeyEvent(action: PySide2.QtTest.QTest.KeyAction, widget: PySide2.QtWidgets.QWidget, code: PySide2.QtCore.Qt.Key, text: str, modifier: PySide2.QtCore.Qt.KeyboardModifiers, delay: int = -1) -> None
        sendKeyEvent(action: PySide2.QtTest.QTest.KeyAction, window: PySide2.QtGui.QWindow, code: PySide2.QtCore.Qt.Key, ascii: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers, delay: int = -1) -> None
        sendKeyEvent(action: PySide2.QtTest.QTest.KeyAction, window: PySide2.QtGui.QWindow, code: PySide2.QtCore.Qt.Key, text: str, modifier: PySide2.QtCore.Qt.KeyboardModifiers, delay: int = -1) -> None
        """
        pass

    def setBenchmarkResult(self, result, metric): # real signature unknown; restored from __doc__
        """ setBenchmarkResult(result: float, metric: PySide2.QtTest.QTest.QBenchmarkMetric) -> None """
        pass

    def setMainSourcePath(self, file, builddir, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setMainSourcePath(file: bytes, builddir: typing.Optional[bytes] = None) -> None """
        pass

    def simulateEvent(self, widget, press, code, modifier, text, repeat, delay=-1): # real signature unknown; restored from __doc__
        """
        simulateEvent(widget: PySide2.QtWidgets.QWidget, press: bool, code: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers, text: str, repeat: bool, delay: int = -1) -> None
        simulateEvent(window: PySide2.QtGui.QWindow, press: bool, code: int, modifier: PySide2.QtCore.Qt.KeyboardModifiers, text: str, repeat: bool, delay: int = -1) -> None
        """
        pass

    def testObject(self): # real signature unknown; restored from __doc__
        """ testObject() -> PySide2.QtCore.QObject """
        pass

    def toPrettyCString(self, unicode, length): # real signature unknown; restored from __doc__
        """ toPrettyCString(unicode: bytes, length: int) -> bytes """
        return b""

    def touchEvent(self, widget, device, autoCommit=True): # real signature unknown; restored from __doc__
        """
        touchEvent(widget: PySide2.QtWidgets.QWidget, device: PySide2.QtGui.QTouchDevice, autoCommit: bool = True) -> PySide2.QtTest.QTest.QTouchEventSequence
        touchEvent(window: PySide2.QtGui.QWindow, device: PySide2.QtGui.QTouchDevice, autoCommit: bool = True) -> PySide2.QtTest.QTest.QTouchEventSequence
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Abort = PySide2.QtTest.QTest.TestFailMode.Abort
    AlignmentFaults = PySide2.QtTest.QTest.QBenchmarkMetric.AlignmentFaults
    BitsPerSecond = PySide2.QtTest.QTest.QBenchmarkMetric.BitsPerSecond
    BranchInstructions = PySide2.QtTest.QTest.QBenchmarkMetric.BranchInstructions
    BranchMisses = PySide2.QtTest.QTest.QBenchmarkMetric.BranchMisses
    BusCycles = PySide2.QtTest.QTest.QBenchmarkMetric.BusCycles
    BytesAllocated = PySide2.QtTest.QTest.QBenchmarkMetric.BytesAllocated
    BytesPerSecond = PySide2.QtTest.QTest.QBenchmarkMetric.BytesPerSecond
    CacheMisses = PySide2.QtTest.QTest.QBenchmarkMetric.CacheMisses
    CachePrefetches = PySide2.QtTest.QTest.QBenchmarkMetric.CachePrefetches
    CachePrefetchMisses = PySide2.QtTest.QTest.QBenchmarkMetric.CachePrefetchMisses
    CacheReadMisses = PySide2.QtTest.QTest.QBenchmarkMetric.CacheReadMisses
    CacheReads = PySide2.QtTest.QTest.QBenchmarkMetric.CacheReads
    CacheReferences = PySide2.QtTest.QTest.QBenchmarkMetric.CacheReferences
    CacheWriteMisses = PySide2.QtTest.QTest.QBenchmarkMetric.CacheWriteMisses
    CacheWrites = PySide2.QtTest.QTest.QBenchmarkMetric.CacheWrites
    Click = PySide2.QtTest.QTest.KeyAction.Click
    ContextSwitches = PySide2.QtTest.QTest.QBenchmarkMetric.ContextSwitches
    Continue = PySide2.QtTest.QTest.TestFailMode.Continue
    CPUCycles = PySide2.QtTest.QTest.QBenchmarkMetric.CPUCycles
    CPUMigrations = PySide2.QtTest.QTest.QBenchmarkMetric.CPUMigrations
    CPUTicks = PySide2.QtTest.QTest.QBenchmarkMetric.CPUTicks
    EmulationFaults = PySide2.QtTest.QTest.QBenchmarkMetric.EmulationFaults
    Events = PySide2.QtTest.QTest.QBenchmarkMetric.Events
    FramesPerSecond = PySide2.QtTest.QTest.QBenchmarkMetric.FramesPerSecond
    InstructionReads = PySide2.QtTest.QTest.QBenchmarkMetric.InstructionReads
    Instructions = PySide2.QtTest.QTest.QBenchmarkMetric.Instructions
    KeyAction = None # (!) real value is "<class 'PySide2.QtTest.QTest.KeyAction'>"
    MajorPageFaults = PySide2.QtTest.QTest.QBenchmarkMetric.MajorPageFaults
    MinorPageFaults = PySide2.QtTest.QTest.QBenchmarkMetric.MinorPageFaults
    MouseAction = None # (!) real value is "<class 'PySide2.QtTest.QTest.MouseAction'>"
    MouseClick = PySide2.QtTest.QTest.MouseAction.MouseClick
    MouseDClick = PySide2.QtTest.QTest.MouseAction.MouseDClick
    mouseDoubleClickInterval = 500
    MouseMove = PySide2.QtTest.QTest.MouseAction.MouseMove
    MousePress = PySide2.QtTest.QTest.MouseAction.MousePress
    MouseRelease = PySide2.QtTest.QTest.MouseAction.MouseRelease
    PageFaults = PySide2.QtTest.QTest.QBenchmarkMetric.PageFaults
    Press = PySide2.QtTest.QTest.KeyAction.Press
    QBenchmarkMetric = None # (!) real value is "<class 'PySide2.QtTest.QTest.QBenchmarkMetric'>"
    QTouchEventSequence = None # (!) real value is "<class 'PySide2.QtTest.QTest.QTouchEventSequence'>"
    RefCPUCycles = PySide2.QtTest.QTest.QBenchmarkMetric.RefCPUCycles
    Release = PySide2.QtTest.QTest.KeyAction.Release
    Shortcut = PySide2.QtTest.QTest.KeyAction.Shortcut
    StalledCycles = PySide2.QtTest.QTest.QBenchmarkMetric.StalledCycles
    TestFailMode = None # (!) real value is "<class 'PySide2.QtTest.QTest.TestFailMode'>"
    WalltimeMilliseconds = PySide2.QtTest.QTest.QBenchmarkMetric.WalltimeMilliseconds
    WalltimeNanoseconds = PySide2.QtTest.QTest.QBenchmarkMetric.WalltimeNanoseconds


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E93DD417B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtTest', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001E93DD417B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtTest.cp310-win_amd64.pyd')"

