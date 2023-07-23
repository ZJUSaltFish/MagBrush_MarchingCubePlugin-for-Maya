# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QIODevice import QIODevice

class QProcess(QIODevice):
    """ QProcess(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def arguments(self): # real signature unknown; restored from __doc__
        """ arguments(self) -> typing.List[str] """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def closeReadChannel(self, channel): # real signature unknown; restored from __doc__
        """ closeReadChannel(self, channel: PySide2.QtCore.QProcess.ProcessChannel) -> None """
        pass

    def closeWriteChannel(self): # real signature unknown; restored from __doc__
        """ closeWriteChannel(self) -> None """
        pass

    def environment(self): # real signature unknown; restored from __doc__
        """ environment(self) -> typing.List[str] """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtCore.QProcess.ProcessError """
        pass

    def errorOccurred(self, *args, **kwargs): # real signature unknown
        pass

    def execute(self, command): # real signature unknown; restored from __doc__
        """
        execute(command: str) -> int
        execute(program: str, arguments: typing.Sequence[str]) -> int
        """
        return 0

    def exitCode(self): # real signature unknown; restored from __doc__
        """ exitCode(self) -> int """
        return 0

    def exitStatus(self): # real signature unknown; restored from __doc__
        """ exitStatus(self) -> PySide2.QtCore.QProcess.ExitStatus """
        pass

    def finished(self, *args, **kwargs): # real signature unknown
        pass

    def inputChannelMode(self): # real signature unknown; restored from __doc__
        """ inputChannelMode(self) -> PySide2.QtCore.QProcess.InputChannelMode """
        pass

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def kill(self): # real signature unknown; restored from __doc__
        """ kill(self) -> None """
        pass

    def nativeArguments(self): # real signature unknown; restored from __doc__
        """ nativeArguments(self) -> str """
        return ""

    def nullDevice(self): # real signature unknown; restored from __doc__
        """ nullDevice() -> str """
        return ""

    def open(self, mode=None): # real signature unknown; restored from __doc__
        """ open(self, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> bool """
        return False

    def pid(self): # real signature unknown; restored from __doc__
        """ pid(self) -> int """
        return 0

    def processChannelMode(self): # real signature unknown; restored from __doc__
        """ processChannelMode(self) -> PySide2.QtCore.QProcess.ProcessChannelMode """
        pass

    def processEnvironment(self): # real signature unknown; restored from __doc__
        """ processEnvironment(self) -> PySide2.QtCore.QProcessEnvironment """
        pass

    def processId(self): # real signature unknown; restored from __doc__
        """ processId(self) -> int """
        return 0

    def program(self): # real signature unknown; restored from __doc__
        """ program(self) -> str """
        return ""

    def readAllStandardError(self): # real signature unknown; restored from __doc__
        """ readAllStandardError(self) -> PySide2.QtCore.QByteArray """
        pass

    def readAllStandardOutput(self): # real signature unknown; restored from __doc__
        """ readAllStandardOutput(self) -> PySide2.QtCore.QByteArray """
        pass

    def readChannel(self): # real signature unknown; restored from __doc__
        """ readChannel(self) -> PySide2.QtCore.QProcess.ProcessChannel """
        pass

    def readData(self, data, maxlen): # real signature unknown; restored from __doc__
        """ readData(self, data: bytes, maxlen: int) -> int """
        return 0

    def readyReadStandardError(self, *args, **kwargs): # real signature unknown
        pass

    def readyReadStandardOutput(self, *args, **kwargs): # real signature unknown
        pass

    def setArguments(self, arguments, p_str=None): # real signature unknown; restored from __doc__
        """ setArguments(self, arguments: typing.Sequence[str]) -> None """
        pass

    def setEnvironment(self, environment, p_str=None): # real signature unknown; restored from __doc__
        """ setEnvironment(self, environment: typing.Sequence[str]) -> None """
        pass

    def setInputChannelMode(self, mode): # real signature unknown; restored from __doc__
        """ setInputChannelMode(self, mode: PySide2.QtCore.QProcess.InputChannelMode) -> None """
        pass

    def setNativeArguments(self, arguments): # real signature unknown; restored from __doc__
        """ setNativeArguments(self, arguments: str) -> None """
        pass

    def setProcessChannelMode(self, mode): # real signature unknown; restored from __doc__
        """ setProcessChannelMode(self, mode: PySide2.QtCore.QProcess.ProcessChannelMode) -> None """
        pass

    def setProcessEnvironment(self, environment): # real signature unknown; restored from __doc__
        """ setProcessEnvironment(self, environment: PySide2.QtCore.QProcessEnvironment) -> None """
        pass

    def setProcessState(self, state): # real signature unknown; restored from __doc__
        """ setProcessState(self, state: PySide2.QtCore.QProcess.ProcessState) -> None """
        pass

    def setProgram(self, program): # real signature unknown; restored from __doc__
        """ setProgram(self, program: str) -> None """
        pass

    def setReadChannel(self, channel): # real signature unknown; restored from __doc__
        """ setReadChannel(self, channel: PySide2.QtCore.QProcess.ProcessChannel) -> None """
        pass

    def setStandardErrorFile(self, fileName, mode=None): # real signature unknown; restored from __doc__
        """ setStandardErrorFile(self, fileName: str, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.Truncate) -> None """
        pass

    def setStandardInputFile(self, fileName): # real signature unknown; restored from __doc__
        """ setStandardInputFile(self, fileName: str) -> None """
        pass

    def setStandardOutputFile(self, fileName, mode=None): # real signature unknown; restored from __doc__
        """ setStandardOutputFile(self, fileName: str, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.Truncate) -> None """
        pass

    def setStandardOutputProcess(self, destination): # real signature unknown; restored from __doc__
        """ setStandardOutputProcess(self, destination: PySide2.QtCore.QProcess) -> None """
        pass

    def setupChildProcess(self): # real signature unknown; restored from __doc__
        """ setupChildProcess(self) -> None """
        pass

    def setWorkingDirectory(self, dir): # real signature unknown; restored from __doc__
        """ setWorkingDirectory(self, dir: str) -> None """
        pass

    def start(self, command, mode=None): # real signature unknown; restored from __doc__
        """
        start(self, command: str, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> None
        start(self, mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> None
        start(self, program: str, arguments: typing.Sequence[str], mode: PySide2.QtCore.QIODevice.OpenMode = PySide2.QtCore.QIODevice.OpenModeFlag.ReadWrite) -> None
        """
        pass

    def startDetached(self, command): # real signature unknown; restored from __doc__
        """
        startDetached(command: str) -> bool
        startDetached(program: str, arguments: typing.Sequence[str]) -> bool
        startDetached(program: str, arguments: typing.Sequence[str], workingDirectory: str) -> typing.Tuple[bool, int]
        startDetached(self) -> typing.Tuple[bool, int]
        """
        return False

    def started(self, *args, **kwargs): # real signature unknown
        pass

    def state(self): # real signature unknown; restored from __doc__
        """ state(self) -> PySide2.QtCore.QProcess.ProcessState """
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def systemEnvironment(self): # real signature unknown; restored from __doc__
        """ systemEnvironment() -> typing.List[str] """
        pass

    def terminate(self): # real signature unknown; restored from __doc__
        """ terminate(self) -> None """
        pass

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForFinished(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForFinished(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def waitForStarted(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForStarted(self, msecs: int = 30000) -> bool """
        return False

    def workingDirectory(self): # real signature unknown; restored from __doc__
        """ workingDirectory(self) -> str """
        return ""

    def writeData(self, data, len): # real signature unknown; restored from __doc__
        """ writeData(self, data: bytes, len: int) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    Crashed = PySide2.QtCore.QProcess.ProcessError.Crashed
    CrashExit = PySide2.QtCore.QProcess.ExitStatus.CrashExit
    ExitStatus = None # (!) real value is "<class 'PySide2.QtCore.QProcess.ExitStatus'>"
    FailedToStart = PySide2.QtCore.QProcess.ProcessError.FailedToStart
    ForwardedChannels = PySide2.QtCore.QProcess.ProcessChannelMode.ForwardedChannels
    ForwardedErrorChannel = PySide2.QtCore.QProcess.ProcessChannelMode.ForwardedErrorChannel
    ForwardedInputChannel = PySide2.QtCore.QProcess.InputChannelMode.ForwardedInputChannel
    ForwardedOutputChannel = PySide2.QtCore.QProcess.ProcessChannelMode.ForwardedOutputChannel
    InputChannelMode = None # (!) real value is "<class 'PySide2.QtCore.QProcess.InputChannelMode'>"
    ManagedInputChannel = PySide2.QtCore.QProcess.InputChannelMode.ManagedInputChannel
    MergedChannels = PySide2.QtCore.QProcess.ProcessChannelMode.MergedChannels
    NormalExit = PySide2.QtCore.QProcess.ExitStatus.NormalExit
    NotRunning = PySide2.QtCore.QProcess.ProcessState.NotRunning
    ProcessChannel = None # (!) real value is "<class 'PySide2.QtCore.QProcess.ProcessChannel'>"
    ProcessChannelMode = None # (!) real value is "<class 'PySide2.QtCore.QProcess.ProcessChannelMode'>"
    ProcessError = None # (!) real value is "<class 'PySide2.QtCore.QProcess.ProcessError'>"
    ProcessState = None # (!) real value is "<class 'PySide2.QtCore.QProcess.ProcessState'>"
    ReadError = PySide2.QtCore.QProcess.ProcessError.ReadError
    Running = PySide2.QtCore.QProcess.ProcessState.Running
    SeparateChannels = PySide2.QtCore.QProcess.ProcessChannelMode.SeparateChannels
    StandardError = PySide2.QtCore.QProcess.ProcessChannel.StandardError
    StandardOutput = PySide2.QtCore.QProcess.ProcessChannel.StandardOutput
    Starting = PySide2.QtCore.QProcess.ProcessState.Starting
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000022221DDC5C0>'
    Timedout = PySide2.QtCore.QProcess.ProcessError.Timedout
    UnknownError = PySide2.QtCore.QProcess.ProcessError.UnknownError
    WriteError = PySide2.QtCore.QProcess.ProcessError.WriteError


