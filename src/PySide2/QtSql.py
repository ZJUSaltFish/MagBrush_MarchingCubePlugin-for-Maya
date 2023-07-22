# encoding: utf-8
# module PySide2.QtSql
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtSql.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import PySide2.QtWidgets as __PySide2_QtWidgets
import Shiboken as __Shiboken


# no functions
# classes

class QSql(__Shiboken.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AfterLastRow = PySide2.QtSql.QSql.Location.AfterLastRow
    AllTables = PySide2.QtSql.QSql.TableType.AllTables
    BeforeFirstRow = PySide2.QtSql.QSql.Location.BeforeFirstRow
    Binary = PySide2.QtSql.QSql.ParamTypeFlag.Binary
    HighPrecision = PySide2.QtSql.QSql.NumericalPrecisionPolicy.HighPrecision
    In = PySide2.QtSql.QSql.ParamTypeFlag.In
    InOut = PySide2.QtSql.QSql.ParamTypeFlag.InOut
    Location = None # (!) real value is "<class 'PySide2.QtSql.QSql.Location'>"
    LowPrecisionDouble = PySide2.QtSql.QSql.NumericalPrecisionPolicy.LowPrecisionDouble
    LowPrecisionInt32 = PySide2.QtSql.QSql.NumericalPrecisionPolicy.LowPrecisionInt32
    LowPrecisionInt64 = PySide2.QtSql.QSql.NumericalPrecisionPolicy.LowPrecisionInt64
    NumericalPrecisionPolicy = None # (!) real value is "<class 'PySide2.QtSql.QSql.NumericalPrecisionPolicy'>"
    Out = PySide2.QtSql.QSql.ParamTypeFlag.Out
    ParamType = None # (!) real value is "<class 'PySide2.QtSql.QSql.ParamType'>"
    ParamTypeFlag = None # (!) real value is "<class 'PySide2.QtSql.QSql.ParamTypeFlag'>"
    SystemTables = PySide2.QtSql.QSql.TableType.SystemTables
    Tables = PySide2.QtSql.QSql.TableType.Tables
    TableType = None # (!) real value is "<class 'PySide2.QtSql.QSql.TableType'>"
    Views = PySide2.QtSql.QSql.TableType.Views


class QSqlDatabase(__Shiboken.Object):
    """
    QSqlDatabase(self) -> None
    QSqlDatabase(self, driver: PySide2.QtSql.QSqlDriver) -> None
    QSqlDatabase(self, other: PySide2.QtSql.QSqlDatabase) -> None
    QSqlDatabase(self, type: str) -> None
    """
    def addDatabase(self, driver, connectionName='qt_sql_default_connection'): # real signature unknown; restored from __doc__
        """
        addDatabase(driver: PySide2.QtSql.QSqlDriver, connectionName: str = 'qt_sql_default_connection') -> PySide2.QtSql.QSqlDatabase
        addDatabase(type: str, connectionName: str = 'qt_sql_default_connection') -> PySide2.QtSql.QSqlDatabase
        """
        pass

    def cloneDatabase(self, other, connectionName): # real signature unknown; restored from __doc__
        """
        cloneDatabase(other: PySide2.QtSql.QSqlDatabase, connectionName: str) -> PySide2.QtSql.QSqlDatabase
        cloneDatabase(other: str, connectionName: str) -> PySide2.QtSql.QSqlDatabase
        """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def commit(self): # real signature unknown; restored from __doc__
        """ commit(self) -> bool """
        return False

    def connectionName(self): # real signature unknown; restored from __doc__
        """ connectionName(self) -> str """
        return ""

    def connectionNames(self): # real signature unknown; restored from __doc__
        """ connectionNames() -> typing.List[str] """
        pass

    def connectOptions(self): # real signature unknown; restored from __doc__
        """ connectOptions(self) -> str """
        return ""

    def contains(self, connectionName='qt_sql_default_connection'): # real signature unknown; restored from __doc__
        """ contains(connectionName: str = 'qt_sql_default_connection') -> bool """
        return False

    def database(self, connectionName='qt_sql_default_connection', open=True): # real signature unknown; restored from __doc__
        """ database(connectionName: str = 'qt_sql_default_connection', open: bool = True) -> PySide2.QtSql.QSqlDatabase """
        pass

    def databaseName(self): # real signature unknown; restored from __doc__
        """ databaseName(self) -> str """
        return ""

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> PySide2.QtSql.QSqlDriver """
        pass

    def driverName(self): # real signature unknown; restored from __doc__
        """ driverName(self) -> str """
        return ""

    def drivers(self): # real signature unknown; restored from __doc__
        """ drivers() -> typing.List[str] """
        pass

    def exec_(self, query=''): # real signature unknown; restored from __doc__
        """ exec_(self, query: str = '') -> PySide2.QtSql.QSqlQuery """
        pass

    def hostName(self): # real signature unknown; restored from __doc__
        """ hostName(self) -> str """
        return ""

    def isDriverAvailable(self, name): # real signature unknown; restored from __doc__
        """ isDriverAvailable(name: str) -> bool """
        return False

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isOpenError(self): # real signature unknown; restored from __doc__
        """ isOpenError(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> PySide2.QtSql.QSqlError """
        pass

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> PySide2.QtSql.QSql.NumericalPrecisionPolicy """
        pass

    def open(self): # real signature unknown; restored from __doc__
        """
        open(self) -> bool
        open(self, user: str, password: str) -> bool
        """
        return False

    def password(self): # real signature unknown; restored from __doc__
        """ password(self) -> str """
        return ""

    def port(self): # real signature unknown; restored from __doc__
        """ port(self) -> int """
        return 0

    def primaryIndex(self, tablename): # real signature unknown; restored from __doc__
        """ primaryIndex(self, tablename: str) -> PySide2.QtSql.QSqlIndex """
        pass

    def record(self, tablename): # real signature unknown; restored from __doc__
        """ record(self, tablename: str) -> PySide2.QtSql.QSqlRecord """
        pass

    def registerSqlDriver(self, name, creator): # real signature unknown; restored from __doc__
        """ registerSqlDriver(name: str, creator: PySide2.QtSql.QSqlDriverCreatorBase) -> None """
        pass

    def removeDatabase(self, connectionName): # real signature unknown; restored from __doc__
        """ removeDatabase(connectionName: str) -> None """
        pass

    def rollback(self): # real signature unknown; restored from __doc__
        """ rollback(self) -> bool """
        return False

    def setConnectOptions(self, options=''): # real signature unknown; restored from __doc__
        """ setConnectOptions(self, options: str = '') -> None """
        pass

    def setDatabaseName(self, name): # real signature unknown; restored from __doc__
        """ setDatabaseName(self, name: str) -> None """
        pass

    def setHostName(self, host): # real signature unknown; restored from __doc__
        """ setHostName(self, host: str) -> None """
        pass

    def setNumericalPrecisionPolicy(self, precisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, precisionPolicy: PySide2.QtSql.QSql.NumericalPrecisionPolicy) -> None """
        pass

    def setPassword(self, password): # real signature unknown; restored from __doc__
        """ setPassword(self, password: str) -> None """
        pass

    def setPort(self, p): # real signature unknown; restored from __doc__
        """ setPort(self, p: int) -> None """
        pass

    def setUserName(self, name): # real signature unknown; restored from __doc__
        """ setUserName(self, name: str) -> None """
        pass

    def tables(self, type=None): # real signature unknown; restored from __doc__
        """ tables(self, type: PySide2.QtSql.QSql.TableType = PySide2.QtSql.QSql.TableType.Tables) -> typing.List[str] """
        pass

    def transaction(self): # real signature unknown; restored from __doc__
        """ transaction(self) -> bool """
        return False

    def userName(self): # real signature unknown; restored from __doc__
        """ userName(self) -> str """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    defaultConnection = 'qt_sql_default_connection'


class QSqlDriver(__PySide2_QtCore.QObject):
    """ QSqlDriver(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def beginTransaction(self): # real signature unknown; restored from __doc__
        """ beginTransaction(self) -> bool """
        return False

    def cancelQuery(self): # real signature unknown; restored from __doc__
        """ cancelQuery(self) -> bool """
        return False

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) -> None """
        pass

    def commitTransaction(self): # real signature unknown; restored from __doc__
        """ commitTransaction(self) -> bool """
        return False

    def createResult(self): # real signature unknown; restored from __doc__
        """ createResult(self) -> PySide2.QtSql.QSqlResult """
        pass

    def dbmsType(self): # real signature unknown; restored from __doc__
        """ dbmsType(self) -> PySide2.QtSql.QSqlDriver.DbmsType """
        pass

    def escapeIdentifier(self, identifier, type): # real signature unknown; restored from __doc__
        """ escapeIdentifier(self, identifier: str, type: PySide2.QtSql.QSqlDriver.IdentifierType) -> str """
        return ""

    def formatValue(self, field, trimStrings=False): # real signature unknown; restored from __doc__
        """ formatValue(self, field: PySide2.QtSql.QSqlField, trimStrings: bool = False) -> str """
        return ""

    def hasFeature(self, f): # real signature unknown; restored from __doc__
        """ hasFeature(self, f: PySide2.QtSql.QSqlDriver.DriverFeature) -> bool """
        return False

    def isIdentifierEscaped(self, identifier, type): # real signature unknown; restored from __doc__
        """ isIdentifierEscaped(self, identifier: str, type: PySide2.QtSql.QSqlDriver.IdentifierType) -> bool """
        return False

    def isOpen(self): # real signature unknown; restored from __doc__
        """ isOpen(self) -> bool """
        return False

    def isOpenError(self): # real signature unknown; restored from __doc__
        """ isOpenError(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> PySide2.QtSql.QSqlError """
        pass

    def notification(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> PySide2.QtSql.QSql.NumericalPrecisionPolicy """
        pass

    def open(self, db, user='', password='', host='', port=-1, connOpts=''): # real signature unknown; restored from __doc__
        """ open(self, db: str, user: str = '', password: str = '', host: str = '', port: int = -1, connOpts: str = '') -> bool """
        return False

    def primaryIndex(self, tableName): # real signature unknown; restored from __doc__
        """ primaryIndex(self, tableName: str) -> PySide2.QtSql.QSqlIndex """
        pass

    def record(self, tableName): # real signature unknown; restored from __doc__
        """ record(self, tableName: str) -> PySide2.QtSql.QSqlRecord """
        pass

    def rollbackTransaction(self): # real signature unknown; restored from __doc__
        """ rollbackTransaction(self) -> bool """
        return False

    def setLastError(self, e): # real signature unknown; restored from __doc__
        """ setLastError(self, e: PySide2.QtSql.QSqlError) -> None """
        pass

    def setNumericalPrecisionPolicy(self, precisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, precisionPolicy: PySide2.QtSql.QSql.NumericalPrecisionPolicy) -> None """
        pass

    def setOpen(self, o): # real signature unknown; restored from __doc__
        """ setOpen(self, o: bool) -> None """
        pass

    def setOpenError(self, e): # real signature unknown; restored from __doc__
        """ setOpenError(self, e: bool) -> None """
        pass

    def sqlStatement(self, type, tableName, rec, preparedStatement): # real signature unknown; restored from __doc__
        """ sqlStatement(self, type: PySide2.QtSql.QSqlDriver.StatementType, tableName: str, rec: PySide2.QtSql.QSqlRecord, preparedStatement: bool) -> str """
        return ""

    def stripDelimiters(self, identifier, type): # real signature unknown; restored from __doc__
        """ stripDelimiters(self, identifier: str, type: PySide2.QtSql.QSqlDriver.IdentifierType) -> str """
        return ""

    def subscribedToNotifications(self): # real signature unknown; restored from __doc__
        """ subscribedToNotifications(self) -> typing.List[str] """
        pass

    def subscribeToNotification(self, name): # real signature unknown; restored from __doc__
        """ subscribeToNotification(self, name: str) -> bool """
        return False

    def tables(self, tableType): # real signature unknown; restored from __doc__
        """ tables(self, tableType: PySide2.QtSql.QSql.TableType) -> typing.List[str] """
        pass

    def unsubscribeFromNotification(self, name): # real signature unknown; restored from __doc__
        """ unsubscribeFromNotification(self, name: str) -> bool """
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

    BatchOperations = PySide2.QtSql.QSqlDriver.DriverFeature.BatchOperations
    BLOB = PySide2.QtSql.QSqlDriver.DriverFeature.BLOB
    CancelQuery = PySide2.QtSql.QSqlDriver.DriverFeature.CancelQuery
    DB2 = PySide2.QtSql.QSqlDriver.DbmsType.DB2
    DbmsType = None # (!) real value is "<class 'PySide2.QtSql.QSqlDriver.DbmsType'>"
    DeleteStatement = PySide2.QtSql.QSqlDriver.StatementType.DeleteStatement
    DriverFeature = None # (!) real value is "<class 'PySide2.QtSql.QSqlDriver.DriverFeature'>"
    EventNotifications = PySide2.QtSql.QSqlDriver.DriverFeature.EventNotifications
    FieldName = PySide2.QtSql.QSqlDriver.IdentifierType.FieldName
    FinishQuery = PySide2.QtSql.QSqlDriver.DriverFeature.FinishQuery
    IdentifierType = None # (!) real value is "<class 'PySide2.QtSql.QSqlDriver.IdentifierType'>"
    InsertStatement = PySide2.QtSql.QSqlDriver.StatementType.InsertStatement
    Interbase = PySide2.QtSql.QSqlDriver.DbmsType.Interbase
    LastInsertId = PySide2.QtSql.QSqlDriver.DriverFeature.LastInsertId
    LowPrecisionNumbers = PySide2.QtSql.QSqlDriver.DriverFeature.LowPrecisionNumbers
    MSSqlServer = PySide2.QtSql.QSqlDriver.DbmsType.MSSqlServer
    MultipleResultSets = PySide2.QtSql.QSqlDriver.DriverFeature.MultipleResultSets
    MySqlServer = PySide2.QtSql.QSqlDriver.DbmsType.MySqlServer
    NamedPlaceholders = PySide2.QtSql.QSqlDriver.DriverFeature.NamedPlaceholders
    NotificationSource = None # (!) real value is "<class 'PySide2.QtSql.QSqlDriver.NotificationSource'>"
    Oracle = PySide2.QtSql.QSqlDriver.DbmsType.Oracle
    OtherSource = PySide2.QtSql.QSqlDriver.NotificationSource.OtherSource
    PositionalPlaceholders = PySide2.QtSql.QSqlDriver.DriverFeature.PositionalPlaceholders
    PostgreSQL = PySide2.QtSql.QSqlDriver.DbmsType.PostgreSQL
    PreparedQueries = PySide2.QtSql.QSqlDriver.DriverFeature.PreparedQueries
    QuerySize = PySide2.QtSql.QSqlDriver.DriverFeature.QuerySize
    SelectStatement = PySide2.QtSql.QSqlDriver.StatementType.SelectStatement
    SelfSource = PySide2.QtSql.QSqlDriver.NotificationSource.SelfSource
    SimpleLocking = PySide2.QtSql.QSqlDriver.DriverFeature.SimpleLocking
    SQLite = PySide2.QtSql.QSqlDriver.DbmsType.SQLite
    StatementType = None # (!) real value is "<class 'PySide2.QtSql.QSqlDriver.StatementType'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000016EF7A0E300>'
    Sybase = PySide2.QtSql.QSqlDriver.DbmsType.Sybase
    TableName = PySide2.QtSql.QSqlDriver.IdentifierType.TableName
    Transactions = PySide2.QtSql.QSqlDriver.DriverFeature.Transactions
    Unicode = PySide2.QtSql.QSqlDriver.DriverFeature.Unicode
    UnknownDbms = PySide2.QtSql.QSqlDriver.DbmsType.UnknownDbms
    UnknownSource = PySide2.QtSql.QSqlDriver.NotificationSource.UnknownSource
    UpdateStatement = PySide2.QtSql.QSqlDriver.StatementType.UpdateStatement
    WhereStatement = PySide2.QtSql.QSqlDriver.StatementType.WhereStatement


class QSqlDriverCreatorBase(__Shiboken.Object):
    """ QSqlDriverCreatorBase(self) -> None """
    def createObject(self): # real signature unknown; restored from __doc__
        """ createObject(self) -> PySide2.QtSql.QSqlDriver """
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


class QSqlError(__Shiboken.Object):
    """
    QSqlError(self, driverText: str, databaseText: str, type: PySide2.QtSql.QSqlError.ErrorType, number: int) -> None
    QSqlError(self, driverText: str = '', databaseText: str = '', type: PySide2.QtSql.QSqlError.ErrorType = PySide2.QtSql.QSqlError.ErrorType.NoError, errorCode: str = '') -> None
    QSqlError(self, other: PySide2.QtSql.QSqlError) -> None
    """
    def databaseText(self): # real signature unknown; restored from __doc__
        """ databaseText(self) -> str """
        return ""

    def driverText(self): # real signature unknown; restored from __doc__
        """ driverText(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def nativeErrorCode(self): # real signature unknown; restored from __doc__
        """ nativeErrorCode(self) -> str """
        return ""

    def number(self): # real signature unknown; restored from __doc__
        """ number(self) -> int """
        return 0

    def setDatabaseText(self, databaseText): # real signature unknown; restored from __doc__
        """ setDatabaseText(self, databaseText: str) -> None """
        pass

    def setDriverText(self, driverText): # real signature unknown; restored from __doc__
        """ setDriverText(self, driverText: str) -> None """
        pass

    def setNumber(self, number): # real signature unknown; restored from __doc__
        """ setNumber(self, number: int) -> None """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: PySide2.QtSql.QSqlError.ErrorType) -> None """
        pass

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtSql.QSqlError) -> None """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> PySide2.QtSql.QSqlError.ErrorType """
        pass

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

    def __init__(self, driverText, databaseText, type, number): # real signature unknown; restored from __doc__
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    ConnectionError = PySide2.QtSql.QSqlError.ErrorType.ConnectionError
    ErrorType = None # (!) real value is "<class 'PySide2.QtSql.QSqlError.ErrorType'>"
    NoError = PySide2.QtSql.QSqlError.ErrorType.NoError
    StatementError = PySide2.QtSql.QSqlError.ErrorType.StatementError
    TransactionError = PySide2.QtSql.QSqlError.ErrorType.TransactionError
    UnknownError = PySide2.QtSql.QSqlError.ErrorType.UnknownError
    __hash__ = None


class QSqlField(__Shiboken.Object):
    """
    QSqlField(self, fieldName: str, type: type, tableName: str) -> None
    QSqlField(self, fieldName: str = '', type: type = {}) -> None
    QSqlField(self, other: PySide2.QtSql.QSqlField) -> None
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def defaultValue(self): # real signature unknown; restored from __doc__
        """ defaultValue(self) -> typing.Any """
        pass

    def isAutoValue(self): # real signature unknown; restored from __doc__
        """ isAutoValue(self) -> bool """
        return False

    def isGenerated(self): # real signature unknown; restored from __doc__
        """ isGenerated(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isReadOnly(self): # real signature unknown; restored from __doc__
        """ isReadOnly(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def length(self): # real signature unknown; restored from __doc__
        """ length(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def precision(self): # real signature unknown; restored from __doc__
        """ precision(self) -> int """
        return 0

    def requiredStatus(self): # real signature unknown; restored from __doc__
        """ requiredStatus(self) -> PySide2.QtSql.QSqlField.RequiredStatus """
        pass

    def setAutoValue(self, autoVal): # real signature unknown; restored from __doc__
        """ setAutoValue(self, autoVal: bool) -> None """
        pass

    def setDefaultValue(self, value): # real signature unknown; restored from __doc__
        """ setDefaultValue(self, value: typing.Any) -> None """
        pass

    def setGenerated(self, gen): # real signature unknown; restored from __doc__
        """ setGenerated(self, gen: bool) -> None """
        pass

    def setLength(self, fieldLength): # real signature unknown; restored from __doc__
        """ setLength(self, fieldLength: int) -> None """
        pass

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def setPrecision(self, precision): # real signature unknown; restored from __doc__
        """ setPrecision(self, precision: int) -> None """
        pass

    def setReadOnly(self, readOnly): # real signature unknown; restored from __doc__
        """ setReadOnly(self, readOnly: bool) -> None """
        pass

    def setRequired(self, required): # real signature unknown; restored from __doc__
        """ setRequired(self, required: bool) -> None """
        pass

    def setRequiredStatus(self, status): # real signature unknown; restored from __doc__
        """ setRequiredStatus(self, status: PySide2.QtSql.QSqlField.RequiredStatus) -> None """
        pass

    def setSqlType(self, type): # real signature unknown; restored from __doc__
        """ setSqlType(self, type: int) -> None """
        pass

    def setTableName(self, tableName): # real signature unknown; restored from __doc__
        """ setTableName(self, tableName: str) -> None """
        pass

    def setType(self, type): # real signature unknown; restored from __doc__
        """ setType(self, type: type) -> None """
        pass

    def setValue(self, value): # real signature unknown; restored from __doc__
        """ setValue(self, value: typing.Any) -> None """
        pass

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
        return ""

    def type(self): # real signature unknown; restored from __doc__
        """ type(self) -> type """
        return type(*(), **{})

    def typeID(self): # real signature unknown; restored from __doc__
        """ typeID(self) -> int """
        return 0

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> typing.Any """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

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

    def __init__(self, fieldName, type, tableName): # real signature unknown; restored from __doc__
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Optional = PySide2.QtSql.QSqlField.RequiredStatus.Optional
    Required = PySide2.QtSql.QSqlField.RequiredStatus.Required
    RequiredStatus = None # (!) real value is "<class 'PySide2.QtSql.QSqlField.RequiredStatus'>"
    Unknown = PySide2.QtSql.QSqlField.RequiredStatus.Unknown
    __hash__ = None


class QSqlRecord(__Shiboken.Object):
    """
    QSqlRecord(self) -> None
    QSqlRecord(self, other: PySide2.QtSql.QSqlRecord) -> None
    """
    def append(self, field): # real signature unknown; restored from __doc__
        """ append(self, field: PySide2.QtSql.QSqlField) -> None """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def clearValues(self): # real signature unknown; restored from __doc__
        """ clearValues(self) -> None """
        pass

    def contains(self, name): # real signature unknown; restored from __doc__
        """ contains(self, name: str) -> bool """
        return False

    def count(self): # real signature unknown; restored from __doc__
        """ count(self) -> int """
        return 0

    def field(self, i): # real signature unknown; restored from __doc__
        """
        field(self, i: int) -> PySide2.QtSql.QSqlField
        field(self, name: str) -> PySide2.QtSql.QSqlField
        """
        pass

    def fieldName(self, i): # real signature unknown; restored from __doc__
        """ fieldName(self, i: int) -> str """
        return ""

    def indexOf(self, name): # real signature unknown; restored from __doc__
        """ indexOf(self, name: str) -> int """
        return 0

    def insert(self, pos, field): # real signature unknown; restored from __doc__
        """ insert(self, pos: int, field: PySide2.QtSql.QSqlField) -> None """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isGenerated(self, i): # real signature unknown; restored from __doc__
        """
        isGenerated(self, i: int) -> bool
        isGenerated(self, name: str) -> bool
        """
        return False

    def isNull(self, i): # real signature unknown; restored from __doc__
        """
        isNull(self, i: int) -> bool
        isNull(self, name: str) -> bool
        """
        return False

    def keyValues(self, keyFields): # real signature unknown; restored from __doc__
        """ keyValues(self, keyFields: PySide2.QtSql.QSqlRecord) -> PySide2.QtSql.QSqlRecord """
        pass

    def remove(self, pos): # real signature unknown; restored from __doc__
        """ remove(self, pos: int) -> None """
        pass

    def replace(self, pos, field): # real signature unknown; restored from __doc__
        """ replace(self, pos: int, field: PySide2.QtSql.QSqlField) -> None """
        pass

    def setGenerated(self, i, generated): # real signature unknown; restored from __doc__
        """
        setGenerated(self, i: int, generated: bool) -> None
        setGenerated(self, name: str, generated: bool) -> None
        """
        pass

    def setNull(self, i): # real signature unknown; restored from __doc__
        """
        setNull(self, i: int) -> None
        setNull(self, name: str) -> None
        """
        pass

    def setValue(self, i, val): # real signature unknown; restored from __doc__
        """
        setValue(self, i: int, val: typing.Any) -> None
        setValue(self, name: str, val: typing.Any) -> None
        """
        pass

    def value(self, i): # real signature unknown; restored from __doc__
        """
        value(self, i: int) -> typing.Any
        value(self, name: str) -> typing.Any
        """
        pass

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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __hash__ = None


class QSqlIndex(QSqlRecord):
    """
    QSqlIndex(self, cursorName: str = '', name: str = '') -> None
    QSqlIndex(self, other: PySide2.QtSql.QSqlIndex) -> None
    """
    def append(self, field): # real signature unknown; restored from __doc__
        """
        append(self, field: PySide2.QtSql.QSqlField) -> None
        append(self, field: PySide2.QtSql.QSqlField, desc: bool) -> None
        """
        pass

    def cursorName(self): # real signature unknown; restored from __doc__
        """ cursorName(self) -> str """
        return ""

    def isDescending(self, i): # real signature unknown; restored from __doc__
        """ isDescending(self, i: int) -> bool """
        return False

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def setCursorName(self, cursorName): # real signature unknown; restored from __doc__
        """ setCursorName(self, cursorName: str) -> None """
        pass

    def setDescending(self, i, desc): # real signature unknown; restored from __doc__
        """ setDescending(self, i: int, desc: bool) -> None """
        pass

    def setName(self, name): # real signature unknown; restored from __doc__
        """ setName(self, name: str) -> None """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self, cursorName='', name=''): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QSqlQuery(__Shiboken.Object):
    """
    QSqlQuery(self, db: PySide2.QtSql.QSqlDatabase) -> None
    QSqlQuery(self, other: PySide2.QtSql.QSqlQuery) -> None
    QSqlQuery(self, query: str = '', db: PySide2.QtSql.QSqlDatabase = Default(QSqlDatabase)) -> None
    QSqlQuery(self, r: PySide2.QtSql.QSqlResult) -> None
    """
    def addBindValue(self, val, type=None): # real signature unknown; restored from __doc__
        """ addBindValue(self, val: typing.Any, type: PySide2.QtSql.QSql.ParamType = PySide2.QtSql.QSql.ParamTypeFlag.In) -> None """
        pass

    def at(self): # real signature unknown; restored from __doc__
        """ at(self) -> int """
        return 0

    def bindValue(self, placeholder, val, type=None): # real signature unknown; restored from __doc__
        """
        bindValue(self, placeholder: str, val: typing.Any, type: PySide2.QtSql.QSql.ParamType = PySide2.QtSql.QSql.ParamTypeFlag.In) -> None
        bindValue(self, pos: int, val: typing.Any, type: PySide2.QtSql.QSql.ParamType = PySide2.QtSql.QSql.ParamTypeFlag.In) -> None
        """
        pass

    def boundValue(self, placeholder): # real signature unknown; restored from __doc__
        """
        boundValue(self, placeholder: str) -> typing.Any
        boundValue(self, pos: int) -> typing.Any
        """
        pass

    def boundValues(self): # real signature unknown; restored from __doc__
        """ boundValues(self) -> typing.Dict[str, typing.Any] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> PySide2.QtSql.QSqlDriver """
        pass

    def execBatch(self, mode=None): # real signature unknown; restored from __doc__
        """ execBatch(self, mode: PySide2.QtSql.QSqlQuery.BatchExecutionMode = PySide2.QtSql.QSqlQuery.BatchExecutionMode.ValuesAsRows) -> bool """
        return False

    def executedQuery(self): # real signature unknown; restored from __doc__
        """ executedQuery(self) -> str """
        return ""

    def exec_(self): # real signature unknown; restored from __doc__
        """
        exec_(self) -> bool
        exec_(self, query: str) -> bool
        """
        return False

    def finish(self): # real signature unknown; restored from __doc__
        """ finish(self) -> None """
        pass

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isForwardOnly(self): # real signature unknown; restored from __doc__
        """ isForwardOnly(self) -> bool """
        return False

    def isNull(self, field): # real signature unknown; restored from __doc__
        """
        isNull(self, field: int) -> bool
        isNull(self, name: str) -> bool
        """
        return False

    def isSelect(self): # real signature unknown; restored from __doc__
        """ isSelect(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def last(self): # real signature unknown; restored from __doc__
        """ last(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> PySide2.QtSql.QSqlError """
        pass

    def lastInsertId(self): # real signature unknown; restored from __doc__
        """ lastInsertId(self) -> typing.Any """
        pass

    def lastQuery(self): # real signature unknown; restored from __doc__
        """ lastQuery(self) -> str """
        return ""

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

    def nextResult(self): # real signature unknown; restored from __doc__
        """ nextResult(self) -> bool """
        return False

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> PySide2.QtSql.QSql.NumericalPrecisionPolicy """
        pass

    def numRowsAffected(self): # real signature unknown; restored from __doc__
        """ numRowsAffected(self) -> int """
        return 0

    def prepare(self, query): # real signature unknown; restored from __doc__
        """ prepare(self, query: str) -> bool """
        return False

    def previous(self): # real signature unknown; restored from __doc__
        """ previous(self) -> bool """
        return False

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> PySide2.QtSql.QSqlRecord """
        pass

    def result(self): # real signature unknown; restored from __doc__
        """ result(self) -> PySide2.QtSql.QSqlResult """
        pass

    def seek(self, i, relative=False): # real signature unknown; restored from __doc__
        """ seek(self, i: int, relative: bool = False) -> bool """
        return False

    def setForwardOnly(self, forward): # real signature unknown; restored from __doc__
        """ setForwardOnly(self, forward: bool) -> None """
        pass

    def setNumericalPrecisionPolicy(self, precisionPolicy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, precisionPolicy: PySide2.QtSql.QSql.NumericalPrecisionPolicy) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def value(self, i): # real signature unknown; restored from __doc__
        """
        value(self, i: int) -> typing.Any
        value(self, name: str) -> typing.Any
        """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self, db): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BatchExecutionMode = None # (!) real value is "<class 'PySide2.QtSql.QSqlQuery.BatchExecutionMode'>"
    ValuesAsColumns = PySide2.QtSql.QSqlQuery.BatchExecutionMode.ValuesAsColumns
    ValuesAsRows = PySide2.QtSql.QSqlQuery.BatchExecutionMode.ValuesAsRows


class QSqlQueryModel(__PySide2_QtCore.QAbstractTableModel):
    """ QSqlQueryModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def beginInsertColumns(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginInsertColumns(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
        pass

    def beginInsertRows(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginInsertRows(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
        pass

    def beginRemoveColumns(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginRemoveColumns(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
        pass

    def beginRemoveRows(self, parent, first, last): # real signature unknown; restored from __doc__
        """ beginRemoveRows(self, parent: PySide2.QtCore.QModelIndex, first: int, last: int) -> None """
        pass

    def beginResetModel(self): # real signature unknown; restored from __doc__
        """ beginResetModel(self) -> None """
        pass

    def canFetchMore(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ canFetchMore(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def columnCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ columnCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def data(self, item, role=None): # real signature unknown; restored from __doc__
        """ data(self, item: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def endInsertColumns(self): # real signature unknown; restored from __doc__
        """ endInsertColumns(self) -> None """
        pass

    def endInsertRows(self): # real signature unknown; restored from __doc__
        """ endInsertRows(self) -> None """
        pass

    def endRemoveColumns(self): # real signature unknown; restored from __doc__
        """ endRemoveColumns(self) -> None """
        pass

    def endRemoveRows(self): # real signature unknown; restored from __doc__
        """ endRemoveRows(self) -> None """
        pass

    def endResetModel(self): # real signature unknown; restored from __doc__
        """ endResetModel(self) -> None """
        pass

    def fetchMore(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ fetchMore(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> None """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def indexInQuery(self, item): # real signature unknown; restored from __doc__
        """ indexInQuery(self, item: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def insertColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> PySide2.QtSql.QSqlError """
        pass

    def query(self): # real signature unknown; restored from __doc__
        """ query(self) -> PySide2.QtSql.QSqlQuery """
        pass

    def queryChange(self): # real signature unknown; restored from __doc__
        """ queryChange(self) -> None """
        pass

    def record(self): # real signature unknown; restored from __doc__
        """
        record(self) -> PySide2.QtSql.QSqlRecord
        record(self, row: int) -> PySide2.QtSql.QSqlRecord
        """
        pass

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def roleNames(self): # real signature unknown; restored from __doc__
        """ roleNames(self) -> typing.Dict[int, PySide2.QtCore.QByteArray] """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def setHeaderData(self, section, orientation, value, role=None): # real signature unknown; restored from __doc__
        """ setHeaderData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setLastError(self, error): # real signature unknown; restored from __doc__
        """ setLastError(self, error: PySide2.QtSql.QSqlError) -> None """
        pass

    def setQuery(self, query): # real signature unknown; restored from __doc__
        """
        setQuery(self, query: PySide2.QtSql.QSqlQuery) -> None
        setQuery(self, query: str, db: PySide2.QtSql.QSqlDatabase = Default(QSqlDatabase)) -> None
        """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000016EF7A0E700>'


class QSqlRelation(__Shiboken.Object):
    """
    QSqlRelation(self) -> None
    QSqlRelation(self, QSqlRelation: PySide2.QtSql.QSqlRelation) -> None
    QSqlRelation(self, aTableName: str, indexCol: str, displayCol: str) -> None
    """
    def displayColumn(self): # real signature unknown; restored from __doc__
        """ displayColumn(self) -> str """
        return ""

    def indexColumn(self): # real signature unknown; restored from __doc__
        """ indexColumn(self) -> str """
        return ""

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtSql.QSqlRelation) -> None """
        pass

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
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


class QSqlRelationalDelegate(__PySide2_QtWidgets.QItemDelegate):
    """ QSqlRelationalDelegate(self, aParent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def createEditor(self, aParent, option, index): # real signature unknown; restored from __doc__
        """ createEditor(self, aParent: PySide2.QtWidgets.QWidget, option: PySide2.QtWidgets.QStyleOptionViewItem, index: PySide2.QtCore.QModelIndex) -> PySide2.QtWidgets.QWidget """
        pass

    def setEditorData(self, editor, index): # real signature unknown; restored from __doc__
        """ setEditorData(self, editor: PySide2.QtWidgets.QWidget, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def setModelData(self, editor, model, index): # real signature unknown; restored from __doc__
        """ setModelData(self, editor: PySide2.QtWidgets.QWidget, model: PySide2.QtCore.QAbstractItemModel, index: PySide2.QtCore.QModelIndex) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, aParent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000016EF7A0E480>'


class QSqlTableModel(QSqlQueryModel):
    """ QSqlTableModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None, db: PySide2.QtSql.QSqlDatabase = Default(QSqlDatabase)) -> None """
    def beforeDelete(self, *args, **kwargs): # real signature unknown
        pass

    def beforeInsert(self, *args, **kwargs): # real signature unknown
        pass

    def beforeUpdate(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def data(self, idx, role=None): # real signature unknown; restored from __doc__
        """ data(self, idx: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def database(self): # real signature unknown; restored from __doc__
        """ database(self) -> PySide2.QtSql.QSqlDatabase """
        pass

    def deleteRowFromTable(self, row): # real signature unknown; restored from __doc__
        """ deleteRowFromTable(self, row: int) -> bool """
        return False

    def editStrategy(self): # real signature unknown; restored from __doc__
        """ editStrategy(self) -> PySide2.QtSql.QSqlTableModel.EditStrategy """
        pass

    def fieldIndex(self, fieldName): # real signature unknown; restored from __doc__
        """ fieldIndex(self, fieldName: str) -> int """
        return 0

    def filter(self): # real signature unknown; restored from __doc__
        """ filter(self) -> str """
        return ""

    def flags(self, index): # real signature unknown; restored from __doc__
        """ flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags """
        pass

    def headerData(self, section, orientation, role=None): # real signature unknown; restored from __doc__
        """ headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def indexInQuery(self, item): # real signature unknown; restored from __doc__
        """ indexInQuery(self, item: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.QModelIndex """
        pass

    def insertRecord(self, row, record): # real signature unknown; restored from __doc__
        """ insertRecord(self, row: int, record: PySide2.QtSql.QSqlRecord) -> bool """
        return False

    def insertRowIntoTable(self, values): # real signature unknown; restored from __doc__
        """ insertRowIntoTable(self, values: PySide2.QtSql.QSqlRecord) -> bool """
        return False

    def insertRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ insertRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def isDirty(self): # real signature unknown; restored from __doc__
        """
        isDirty(self) -> bool
        isDirty(self, index: PySide2.QtCore.QModelIndex) -> bool
        """
        return False

    def orderByClause(self): # real signature unknown; restored from __doc__
        """ orderByClause(self) -> str """
        return ""

    def primaryKey(self): # real signature unknown; restored from __doc__
        """ primaryKey(self) -> PySide2.QtSql.QSqlIndex """
        pass

    def primaryValues(self, row): # real signature unknown; restored from __doc__
        """ primaryValues(self, row: int) -> PySide2.QtSql.QSqlRecord """
        pass

    def primeInsert(self, *args, **kwargs): # real signature unknown
        pass

    def record(self): # real signature unknown; restored from __doc__
        """
        record(self) -> PySide2.QtSql.QSqlRecord
        record(self, row: int) -> PySide2.QtSql.QSqlRecord
        """
        pass

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def removeRows(self, row, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeRows(self, row: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) -> None """
        pass

    def revertAll(self): # real signature unknown; restored from __doc__
        """ revertAll(self) -> None """
        pass

    def revertRow(self, row): # real signature unknown; restored from __doc__
        """ revertRow(self, row: int) -> None """
        pass

    def rowCount(self, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ rowCount(self, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> int """
        pass

    def select(self): # real signature unknown; restored from __doc__
        """ select(self) -> bool """
        return False

    def selectRow(self, row): # real signature unknown; restored from __doc__
        """ selectRow(self, row: int) -> bool """
        return False

    def selectStatement(self): # real signature unknown; restored from __doc__
        """ selectStatement(self) -> str """
        return ""

    def setData(self, index, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setEditStrategy(self, strategy): # real signature unknown; restored from __doc__
        """ setEditStrategy(self, strategy: PySide2.QtSql.QSqlTableModel.EditStrategy) -> None """
        pass

    def setFilter(self, filter): # real signature unknown; restored from __doc__
        """ setFilter(self, filter: str) -> None """
        pass

    def setPrimaryKey(self, key): # real signature unknown; restored from __doc__
        """ setPrimaryKey(self, key: PySide2.QtSql.QSqlIndex) -> None """
        pass

    def setQuery(self, query): # real signature unknown; restored from __doc__
        """ setQuery(self, query: PySide2.QtSql.QSqlQuery) -> None """
        pass

    def setRecord(self, row, record): # real signature unknown; restored from __doc__
        """ setRecord(self, row: int, record: PySide2.QtSql.QSqlRecord) -> bool """
        return False

    def setSort(self, column, order): # real signature unknown; restored from __doc__
        """ setSort(self, column: int, order: PySide2.QtCore.Qt.SortOrder) -> None """
        pass

    def setTable(self, tableName): # real signature unknown; restored from __doc__
        """ setTable(self, tableName: str) -> None """
        pass

    def sort(self, column, order): # real signature unknown; restored from __doc__
        """ sort(self, column: int, order: PySide2.QtCore.Qt.SortOrder) -> None """
        pass

    def submit(self): # real signature unknown; restored from __doc__
        """ submit(self) -> bool """
        return False

    def submitAll(self): # real signature unknown; restored from __doc__
        """ submitAll(self) -> bool """
        return False

    def tableName(self): # real signature unknown; restored from __doc__
        """ tableName(self) -> str """
        return ""

    def updateRowInTable(self, row, values): # real signature unknown; restored from __doc__
        """ updateRowInTable(self, row: int, values: PySide2.QtSql.QSqlRecord) -> bool """
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

    EditStrategy = None # (!) real value is "<class 'PySide2.QtSql.QSqlTableModel.EditStrategy'>"
    OnFieldChange = PySide2.QtSql.QSqlTableModel.EditStrategy.OnFieldChange
    OnManualSubmit = PySide2.QtSql.QSqlTableModel.EditStrategy.OnManualSubmit
    OnRowChange = PySide2.QtSql.QSqlTableModel.EditStrategy.OnRowChange
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000016EF7A0F0C0>'


class QSqlRelationalTableModel(QSqlTableModel):
    """ QSqlRelationalTableModel(self, parent: typing.Optional[PySide2.QtCore.QObject] = None, db: PySide2.QtSql.QSqlDatabase = Default(QSqlDatabase)) -> None """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def data(self, item, role=None): # real signature unknown; restored from __doc__
        """ data(self, item: PySide2.QtCore.QModelIndex, role: int = PySide2.QtCore.Qt.ItemDataRole.DisplayRole) -> typing.Any """
        pass

    def insertRowIntoTable(self, values): # real signature unknown; restored from __doc__
        """ insertRowIntoTable(self, values: PySide2.QtSql.QSqlRecord) -> bool """
        return False

    def orderByClause(self): # real signature unknown; restored from __doc__
        """ orderByClause(self) -> str """
        return ""

    def relation(self, column): # real signature unknown; restored from __doc__
        """ relation(self, column: int) -> PySide2.QtSql.QSqlRelation """
        pass

    def relationModel(self, column): # real signature unknown; restored from __doc__
        """ relationModel(self, column: int) -> PySide2.QtSql.QSqlTableModel """
        pass

    def removeColumns(self, column, count, parent=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ removeColumns(self, column: int, count: int, parent: PySide2.QtCore.QModelIndex = Invalid(PySide2.QtCore.QModelIndex)) -> bool """
        pass

    def revertRow(self, row): # real signature unknown; restored from __doc__
        """ revertRow(self, row: int) -> None """
        pass

    def select(self): # real signature unknown; restored from __doc__
        """ select(self) -> bool """
        return False

    def selectStatement(self): # real signature unknown; restored from __doc__
        """ selectStatement(self) -> str """
        return ""

    def setData(self, item, value, role=None): # real signature unknown; restored from __doc__
        """ setData(self, item: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = PySide2.QtCore.Qt.ItemDataRole.EditRole) -> bool """
        return False

    def setJoinMode(self, joinMode): # real signature unknown; restored from __doc__
        """ setJoinMode(self, joinMode: PySide2.QtSql.QSqlRelationalTableModel.JoinMode) -> None """
        pass

    def setRelation(self, column, relation): # real signature unknown; restored from __doc__
        """ setRelation(self, column: int, relation: PySide2.QtSql.QSqlRelation) -> None """
        pass

    def setTable(self, tableName): # real signature unknown; restored from __doc__
        """ setTable(self, tableName: str) -> None """
        pass

    def updateRowInTable(self, row, values): # real signature unknown; restored from __doc__
        """ updateRowInTable(self, row: int, values: PySide2.QtSql.QSqlRecord) -> bool """
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

    InnerJoin = PySide2.QtSql.QSqlRelationalTableModel.JoinMode.InnerJoin
    JoinMode = None # (!) real value is "<class 'PySide2.QtSql.QSqlRelationalTableModel.JoinMode'>"
    LeftJoin = PySide2.QtSql.QSqlRelationalTableModel.JoinMode.LeftJoin
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000016EF7A0F540>'


class QSqlResult(__Shiboken.Object):
    """ QSqlResult(self, db: PySide2.QtSql.QSqlDriver) -> None """
    def addBindValue(self, val, type): # real signature unknown; restored from __doc__
        """ addBindValue(self, val: typing.Any, type: PySide2.QtSql.QSql.ParamType) -> None """
        pass

    def at(self): # real signature unknown; restored from __doc__
        """ at(self) -> int """
        return 0

    def bindingSyntax(self): # real signature unknown; restored from __doc__
        """ bindingSyntax(self) -> PySide2.QtSql.QSqlResult.BindingSyntax """
        pass

    def bindValue(self, placeholder, val, type): # real signature unknown; restored from __doc__
        """
        bindValue(self, placeholder: str, val: typing.Any, type: PySide2.QtSql.QSql.ParamType) -> None
        bindValue(self, pos: int, val: typing.Any, type: PySide2.QtSql.QSql.ParamType) -> None
        """
        pass

    def bindValueType(self, placeholder): # real signature unknown; restored from __doc__
        """
        bindValueType(self, placeholder: str) -> PySide2.QtSql.QSql.ParamType
        bindValueType(self, pos: int) -> PySide2.QtSql.QSql.ParamType
        """
        pass

    def boundValue(self, placeholder): # real signature unknown; restored from __doc__
        """
        boundValue(self, placeholder: str) -> typing.Any
        boundValue(self, pos: int) -> typing.Any
        """
        pass

    def boundValueCount(self): # real signature unknown; restored from __doc__
        """ boundValueCount(self) -> int """
        return 0

    def boundValueName(self, pos): # real signature unknown; restored from __doc__
        """ boundValueName(self, pos: int) -> str """
        return ""

    def boundValues(self): # real signature unknown; restored from __doc__
        """ boundValues(self) -> typing.List[typing.Any] """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def data(self, i): # real signature unknown; restored from __doc__
        """ data(self, i: int) -> typing.Any """
        pass

    def detachFromResultSet(self): # real signature unknown; restored from __doc__
        """ detachFromResultSet(self) -> None """
        pass

    def driver(self): # real signature unknown; restored from __doc__
        """ driver(self) -> PySide2.QtSql.QSqlDriver """
        pass

    def execBatch(self, arrayBind=False): # real signature unknown; restored from __doc__
        """ execBatch(self, arrayBind: bool = False) -> bool """
        return False

    def executedQuery(self): # real signature unknown; restored from __doc__
        """ executedQuery(self) -> str """
        return ""

    def exec_(self): # real signature unknown; restored from __doc__
        """ exec_(self) -> bool """
        return False

    def fetch(self, i): # real signature unknown; restored from __doc__
        """ fetch(self, i: int) -> bool """
        return False

    def fetchFirst(self): # real signature unknown; restored from __doc__
        """ fetchFirst(self) -> bool """
        return False

    def fetchLast(self): # real signature unknown; restored from __doc__
        """ fetchLast(self) -> bool """
        return False

    def fetchNext(self): # real signature unknown; restored from __doc__
        """ fetchNext(self) -> bool """
        return False

    def fetchPrevious(self): # real signature unknown; restored from __doc__
        """ fetchPrevious(self) -> bool """
        return False

    def handle(self): # real signature unknown; restored from __doc__
        """ handle(self) -> typing.Any """
        pass

    def hasOutValues(self): # real signature unknown; restored from __doc__
        """ hasOutValues(self) -> bool """
        return False

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isForwardOnly(self): # real signature unknown; restored from __doc__
        """ isForwardOnly(self) -> bool """
        return False

    def isNull(self, i): # real signature unknown; restored from __doc__
        """ isNull(self, i: int) -> bool """
        return False

    def isSelect(self): # real signature unknown; restored from __doc__
        """ isSelect(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def lastError(self): # real signature unknown; restored from __doc__
        """ lastError(self) -> PySide2.QtSql.QSqlError """
        pass

    def lastInsertId(self): # real signature unknown; restored from __doc__
        """ lastInsertId(self) -> typing.Any """
        pass

    def lastQuery(self): # real signature unknown; restored from __doc__
        """ lastQuery(self) -> str """
        return ""

    def nextResult(self): # real signature unknown; restored from __doc__
        """ nextResult(self) -> bool """
        return False

    def numericalPrecisionPolicy(self): # real signature unknown; restored from __doc__
        """ numericalPrecisionPolicy(self) -> PySide2.QtSql.QSql.NumericalPrecisionPolicy """
        pass

    def numRowsAffected(self): # real signature unknown; restored from __doc__
        """ numRowsAffected(self) -> int """
        return 0

    def prepare(self, query): # real signature unknown; restored from __doc__
        """ prepare(self, query: str) -> bool """
        return False

    def record(self): # real signature unknown; restored from __doc__
        """ record(self) -> PySide2.QtSql.QSqlRecord """
        pass

    def reset(self, sqlquery): # real signature unknown; restored from __doc__
        """ reset(self, sqlquery: str) -> bool """
        return False

    def resetBindCount(self): # real signature unknown; restored from __doc__
        """ resetBindCount(self) -> None """
        pass

    def savePrepare(self, sqlquery): # real signature unknown; restored from __doc__
        """ savePrepare(self, sqlquery: str) -> bool """
        return False

    def setActive(self, a): # real signature unknown; restored from __doc__
        """ setActive(self, a: bool) -> None """
        pass

    def setAt(self, at): # real signature unknown; restored from __doc__
        """ setAt(self, at: int) -> None """
        pass

    def setForwardOnly(self, forward): # real signature unknown; restored from __doc__
        """ setForwardOnly(self, forward: bool) -> None """
        pass

    def setLastError(self, e): # real signature unknown; restored from __doc__
        """ setLastError(self, e: PySide2.QtSql.QSqlError) -> None """
        pass

    def setNumericalPrecisionPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setNumericalPrecisionPolicy(self, policy: PySide2.QtSql.QSql.NumericalPrecisionPolicy) -> None """
        pass

    def setQuery(self, query): # real signature unknown; restored from __doc__
        """ setQuery(self, query: str) -> None """
        pass

    def setSelect(self, s): # real signature unknown; restored from __doc__
        """ setSelect(self, s: bool) -> None """
        pass

    def size(self): # real signature unknown; restored from __doc__
        """ size(self) -> int """
        return 0

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, db): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    BindingSyntax = None # (!) real value is "<class 'PySide2.QtSql.QSqlResult.BindingSyntax'>"
    NamedBinding = PySide2.QtSql.QSqlResult.BindingSyntax.NamedBinding
    PositionalBinding = PySide2.QtSql.QSqlResult.BindingSyntax.PositionalBinding


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016EF6AB17B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtSql', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016EF6AB17B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtSql.cp310-win_amd64.pyd')"

