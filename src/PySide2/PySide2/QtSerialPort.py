# encoding: utf-8
# module PySide2.QtSerialPort
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSerialPort.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QSerialPort(__PySide2_QtCore.QIODevice):
    """
    QSerialPort(self, info: PySide2.QtSerialPort.QSerialPortInfo, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSerialPort(self, name: str, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    QSerialPort(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """
    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def baudRate(self, directions=None): # real signature unknown; restored from __doc__
        """ baudRate(self, directions: PySide2.QtSerialPort.QSerialPort.Directions = PySide2.QtSerialPort.QSerialPort.Direction.AllDirections) -> int """
        return 0

    def baudRateChanged(self, *args, **kwargs): # real signature unknown
        pass

    def breakEnabledChanged(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self): # real signature unknown; restored from __doc__
        """ bytesAvailable(self) -> int """
        return 0

    def bytesToWrite(self): # real signature unknown; restored from __doc__
        """ bytesToWrite(self) -> int """
        return 0

    def canReadLine(self): # real signature unknown; restored from __doc__
        """ canReadLine(self) -> bool """
        return False

    def clear(self, directions=None): # real signature unknown; restored from __doc__
        """ clear(self, directions: PySide2.QtSerialPort.QSerialPort.Directions = PySide2.QtSerialPort.QSerialPort.Direction.AllDirections) -> bool """
        return False

    def clearError(self): # real signature unknown; restored from __doc__
        """ clearError(self) -> None """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def dataBits(self): # real signature unknown; restored from __doc__
        """ dataBits(self) -> PySide2.QtSerialPort.QSerialPort.DataBits """
        pass

    def dataBitsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dataErrorPolicy(self): # real signature unknown; restored from __doc__
        """ dataErrorPolicy(self) -> PySide2.QtSerialPort.QSerialPort.DataErrorPolicy """
        pass

    def dataErrorPolicyChanged(self, *args, **kwargs): # real signature unknown
        pass

    def dataTerminalReadyChanged(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def error.overload(self, *args, **kwargs): # real signature unknown
        """ error(self) -> PySide2.QtSerialPort.QSerialPort.SerialPortError """
        pass

    def errorOccurred(self, *args, **kwargs): # real signature unknown
        pass

    def flowControl(self): # real signature unknown; restored from __doc__
        """ flowControl(self) -> PySide2.QtSerialPort.QSerialPort.FlowControl """
        pass

    def flowControlChanged(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> int """
        return 0

    def isBreakEnabled(self): # real signature unknown; restored from __doc__
        """ isBreakEnabled(self) -> bool """
        return False

    def isDataTerminalReady(self): # real signature unknown; restored from __doc__
        """ isDataTerminalReady(self) -> bool """
        return False

    def isRequestToSend(self): # real signature unknown; restored from __doc__
        """ isRequestToSend(self) -> bool """
        return False

    def isSequential(self): # real signature unknown; restored from __doc__
        """ isSequential(self) -> bool """
        return False

    def open(self, mode): # real signature unknown; restored from __doc__
        """ open(self, mode: PySide2.QtCore.QIODevice.OpenMode) -> bool """
        return False

    def parity(self): # real signature unknown; restored from __doc__
        """ parity(self) -> PySide2.QtSerialPort.QSerialPort.Parity """
        pass

    def parityChanged(self, *args, **kwargs): # real signature unknown
        pass

    def pinoutSignals(self): # real signature unknown; restored from __doc__
        """ pinoutSignals(self) -> PySide2.QtSerialPort.QSerialPort.PinoutSignals """
        pass

    def portName(self): # real signature unknown; restored from __doc__
        """ portName(self) -> str """
        return ""

    def readBufferSize(self): # real signature unknown; restored from __doc__
        """ readBufferSize(self) -> int """
        return 0

    def readData(self, data, maxSize): # real signature unknown; restored from __doc__
        """ readData(self, data: bytes, maxSize: int) -> int """
        return 0

    def readLineData(self, data, maxSize): # real signature unknown; restored from __doc__
        """ readLineData(self, data: bytes, maxSize: int) -> int """
        return 0

    def requestToSendChanged(self, *args, **kwargs): # real signature unknown
        pass

    def sendBreak(self, duration=0): # real signature unknown; restored from __doc__
        """ sendBreak(self, duration: int = 0) -> bool """
        return False

    def setBaudRate(self, baudRate, directions=None): # real signature unknown; restored from __doc__
        """ setBaudRate(self, baudRate: int, directions: PySide2.QtSerialPort.QSerialPort.Directions = PySide2.QtSerialPort.QSerialPort.Direction.AllDirections) -> bool """
        return False

    def setBreakEnabled(self, set=True): # real signature unknown; restored from __doc__
        """ setBreakEnabled(self, set: bool = True) -> bool """
        return False

    def setDataBits(self, dataBits): # real signature unknown; restored from __doc__
        """ setDataBits(self, dataBits: PySide2.QtSerialPort.QSerialPort.DataBits) -> bool """
        return False

    def setDataErrorPolicy(self, policy=None): # real signature unknown; restored from __doc__
        """ setDataErrorPolicy(self, policy: PySide2.QtSerialPort.QSerialPort.DataErrorPolicy = PySide2.QtSerialPort.QSerialPort.DataErrorPolicy.IgnorePolicy) -> bool """
        return False

    def setDataTerminalReady(self, set): # real signature unknown; restored from __doc__
        """ setDataTerminalReady(self, set: bool) -> bool """
        return False

    def setFlowControl(self, flowControl): # real signature unknown; restored from __doc__
        """ setFlowControl(self, flowControl: PySide2.QtSerialPort.QSerialPort.FlowControl) -> bool """
        return False

    def setParity(self, parity): # real signature unknown; restored from __doc__
        """ setParity(self, parity: PySide2.QtSerialPort.QSerialPort.Parity) -> bool """
        return False

    def setPort(self, info): # real signature unknown; restored from __doc__
        """ setPort(self, info: PySide2.QtSerialPort.QSerialPortInfo) -> None """
        pass

    def setPortName(self, name): # real signature unknown; restored from __doc__
        """ setPortName(self, name: str) -> None """
        pass

    def setReadBufferSize(self, size): # real signature unknown; restored from __doc__
        """ setReadBufferSize(self, size: int) -> None """
        pass

    def setRequestToSend(self, set): # real signature unknown; restored from __doc__
        """ setRequestToSend(self, set: bool) -> bool """
        return False

    def setSettingsRestoredOnClose(self, restore): # real signature unknown; restored from __doc__
        """ setSettingsRestoredOnClose(self, restore: bool) -> None """
        pass

    def setStopBits(self, stopBits): # real signature unknown; restored from __doc__
        """ setStopBits(self, stopBits: PySide2.QtSerialPort.QSerialPort.StopBits) -> bool """
        return False

    def settingsRestoredOnClose(self): # real signature unknown; restored from __doc__
        """ settingsRestoredOnClose(self) -> bool """
        return False

    def settingsRestoredOnCloseChanged(self, *args, **kwargs): # real signature unknown
        pass

    def stopBits(self): # real signature unknown; restored from __doc__
        """ stopBits(self) -> PySide2.QtSerialPort.QSerialPort.StopBits """
        pass

    def stopBitsChanged(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForBytesWritten(self, msecs: int = 30000) -> bool """
        return False

    def waitForReadyRead(self, msecs=30000): # real signature unknown; restored from __doc__
        """ waitForReadyRead(self, msecs: int = 30000) -> bool """
        return False

    def writeData(self, data, maxSize): # real signature unknown; restored from __doc__
        """ writeData(self, data: bytes, maxSize: int) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, info, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    AllDirections = PySide2.QtSerialPort.QSerialPort.Direction.AllDirections
    Baud115200 = PySide2.QtSerialPort.QSerialPort.BaudRate.Baud115200
    Baud1200 = PySide2.QtSerialPort.QSerialPort.BaudRate.Baud1200
    Baud19200 = PySide2.QtSerialPort.QSerialPort.BaudRate.Baud19200
    Baud2400 = PySide2.QtSerialPort.QSerialPort.BaudRate.Baud2400
    Baud38400 = PySide2.QtSerialPort.QSerialPort.BaudRate.Baud38400
    Baud4800 = PySide2.QtSerialPort.QSerialPort.BaudRate.Baud4800
    Baud57600 = PySide2.QtSerialPort.QSerialPort.BaudRate.Baud57600
    Baud9600 = PySide2.QtSerialPort.QSerialPort.BaudRate.Baud9600
    BaudRate = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.BaudRate'>"
    BreakConditionError = PySide2.QtSerialPort.QSerialPort.SerialPortError.BreakConditionError
    ClearToSendSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.ClearToSendSignal
    Data5 = PySide2.QtSerialPort.QSerialPort.DataBits.Data5
    Data6 = PySide2.QtSerialPort.QSerialPort.DataBits.Data6
    Data7 = PySide2.QtSerialPort.QSerialPort.DataBits.Data7
    Data8 = PySide2.QtSerialPort.QSerialPort.DataBits.Data8
    DataBits = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.DataBits'>"
    DataCarrierDetectSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.DataCarrierDetectSignal
    DataErrorPolicy = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.DataErrorPolicy'>"
    DataSetReadySignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.DataSetReadySignal
    DataTerminalReadySignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.DataTerminalReadySignal
    DeviceNotFoundError = PySide2.QtSerialPort.QSerialPort.SerialPortError.DeviceNotFoundError
    Direction = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.Direction'>"
    Directions = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.Directions'>"
    EvenParity = PySide2.QtSerialPort.QSerialPort.Parity.EvenParity
    FlowControl = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.FlowControl'>"
    FramingError = PySide2.QtSerialPort.QSerialPort.SerialPortError.FramingError
    HardwareControl = PySide2.QtSerialPort.QSerialPort.FlowControl.HardwareControl
    IgnorePolicy = PySide2.QtSerialPort.QSerialPort.DataErrorPolicy.IgnorePolicy
    Input = PySide2.QtSerialPort.QSerialPort.Direction.Input
    MarkParity = PySide2.QtSerialPort.QSerialPort.Parity.MarkParity
    NoError = PySide2.QtSerialPort.QSerialPort.SerialPortError.NoError
    NoFlowControl = PySide2.QtSerialPort.QSerialPort.FlowControl.NoFlowControl
    NoParity = PySide2.QtSerialPort.QSerialPort.Parity.NoParity
    NoSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.NoSignal
    NotOpenError = PySide2.QtSerialPort.QSerialPort.SerialPortError.NotOpenError
    OddParity = PySide2.QtSerialPort.QSerialPort.Parity.OddParity
    OneAndHalfStop = PySide2.QtSerialPort.QSerialPort.StopBits.OneAndHalfStop
    OneStop = PySide2.QtSerialPort.QSerialPort.StopBits.OneStop
    OpenError = PySide2.QtSerialPort.QSerialPort.SerialPortError.OpenError
    Output = PySide2.QtSerialPort.QSerialPort.Direction.Output
    Parity = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.Parity'>"
    ParityError = PySide2.QtSerialPort.QSerialPort.SerialPortError.ParityError
    PassZeroPolicy = PySide2.QtSerialPort.QSerialPort.DataErrorPolicy.PassZeroPolicy
    PermissionError = PySide2.QtSerialPort.QSerialPort.SerialPortError.PermissionError
    PinoutSignal = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.PinoutSignal'>"
    PinoutSignals = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.PinoutSignals'>"
    ReadError = PySide2.QtSerialPort.QSerialPort.SerialPortError.ReadError
    ReceivedDataSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.ReceivedDataSignal
    RequestToSendSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.RequestToSendSignal
    ResourceError = PySide2.QtSerialPort.QSerialPort.SerialPortError.ResourceError
    RingIndicatorSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.RingIndicatorSignal
    SecondaryReceivedDataSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.SecondaryReceivedDataSignal
    SecondaryTransmittedDataSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.SecondaryTransmittedDataSignal
    SerialPortError = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.SerialPortError'>"
    SkipPolicy = PySide2.QtSerialPort.QSerialPort.DataErrorPolicy.SkipPolicy
    SoftwareControl = PySide2.QtSerialPort.QSerialPort.FlowControl.SoftwareControl
    SpaceParity = PySide2.QtSerialPort.QSerialPort.Parity.SpaceParity
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000169D6FA6200>'
    StopBits = None # (!) real value is "<class 'PySide2.QtSerialPort.QSerialPort.StopBits'>"
    StopReceivingPolicy = PySide2.QtSerialPort.QSerialPort.DataErrorPolicy.StopReceivingPolicy
    TimeoutError = PySide2.QtSerialPort.QSerialPort.SerialPortError.TimeoutError
    TransmittedDataSignal = PySide2.QtSerialPort.QSerialPort.PinoutSignal.TransmittedDataSignal
    TwoStop = PySide2.QtSerialPort.QSerialPort.StopBits.TwoStop
    UnknownBaud = PySide2.QtSerialPort.QSerialPort.BaudRate.UnknownBaud
    UnknownDataBits = PySide2.QtSerialPort.QSerialPort.DataBits.UnknownDataBits
    UnknownError = PySide2.QtSerialPort.QSerialPort.SerialPortError.UnknownError
    UnknownFlowControl = PySide2.QtSerialPort.QSerialPort.FlowControl.UnknownFlowControl
    UnknownParity = PySide2.QtSerialPort.QSerialPort.Parity.UnknownParity
    UnknownPolicy = PySide2.QtSerialPort.QSerialPort.DataErrorPolicy.UnknownPolicy
    UnknownStopBits = PySide2.QtSerialPort.QSerialPort.StopBits.UnknownStopBits
    UnsupportedOperationError = PySide2.QtSerialPort.QSerialPort.SerialPortError.UnsupportedOperationError
    WriteError = PySide2.QtSerialPort.QSerialPort.SerialPortError.WriteError


class QSerialPortInfo(__Shiboken.Object):
    """
    QSerialPortInfo(self) -> None
    QSerialPortInfo(self, name: str) -> None
    QSerialPortInfo(self, other: PySide2.QtSerialPort.QSerialPortInfo) -> None
    QSerialPortInfo(self, port: PySide2.QtSerialPort.QSerialPort) -> None
    """
    def availablePorts(self): # real signature unknown; restored from __doc__
        """ availablePorts() -> typing.List[PySide2.QtSerialPort.QSerialPortInfo] """
        pass

    def description(self): # real signature unknown; restored from __doc__
        """ description(self) -> str """
        return ""

    def hasProductIdentifier(self): # real signature unknown; restored from __doc__
        """ hasProductIdentifier(self) -> bool """
        return False

    def hasVendorIdentifier(self): # real signature unknown; restored from __doc__
        """ hasVendorIdentifier(self) -> bool """
        return False

    def isBusy(self): # real signature unknown; restored from __doc__
        """ isBusy(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def manufacturer(self): # real signature unknown; restored from __doc__
        """ manufacturer(self) -> str """
        return ""

    def portName(self): # real signature unknown; restored from __doc__
        """ portName(self) -> str """
        return ""

    def productIdentifier(self): # real signature unknown; restored from __doc__
        """ productIdentifier(self) -> int """
        return 0

    def serialNumber(self): # real signature unknown; restored from __doc__
        """ serialNumber(self) -> str """
        return ""

    def standardBaudRates(self): # real signature unknown; restored from __doc__
        """ standardBaudRates() -> typing.List[int] """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtSerialPort.QSerialPortInfo) -> None """
        pass

    def systemLocation(self): # real signature unknown; restored from __doc__
        """ systemLocation(self) -> str """
        return ""

    def vendorIdentifier(self): # real signature unknown; restored from __doc__
        """ vendorIdentifier(self) -> int """
        return 0

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
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


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000169D63C17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtSerialPort', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000169D63C17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtSerialPort.cp310-win_amd64.pyd')"

