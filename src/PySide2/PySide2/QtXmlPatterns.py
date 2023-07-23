# encoding: utf-8
# module PySide2.QtXmlPatterns
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtXmlPatterns.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QAbstractMessageHandler(__PySide2_QtCore.QObject):
    """ QAbstractMessageHandler(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def handleMessage(self, type, description, identifier, sourceLocation): # real signature unknown; restored from __doc__
        """ handleMessage(self, type: PySide2.QtCore.QtMsgType, description: str, identifier: PySide2.QtCore.QUrl, sourceLocation: PySide2.QtXmlPatterns.QSourceLocation) -> None """
        pass

    def message(self, type, description, identifier=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ message(self, type: PySide2.QtCore.QtMsgType, description: str, identifier: PySide2.QtCore.QUrl = Default(QUrl), sourceLocation: PySide2.QtXmlPatterns.QSourceLocation = Default(QSourceLocation)) -> None """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000016139985AC0>'


class QAbstractUriResolver(__PySide2_QtCore.QObject):
    """ QAbstractUriResolver(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def resolve(self, relative, baseURI): # real signature unknown; restored from __doc__
        """ resolve(self, relative: PySide2.QtCore.QUrl, baseURI: PySide2.QtCore.QUrl) -> PySide2.QtCore.QUrl """
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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x00000161399859C0>'


class QAbstractXmlNodeModel(__Shiboken.Object):
    """ QAbstractXmlNodeModel(self) -> None """
    def attributes(self, element): # real signature unknown; restored from __doc__
        """ attributes(self, element: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.List[PySide2.QtXmlPatterns.QXmlNodeModelIndex] """
        pass

    def baseUri(self, ni): # real signature unknown; restored from __doc__
        """ baseUri(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtCore.QUrl """
        pass

    def compareOrder(self, ni1, ni2): # real signature unknown; restored from __doc__
        """ compareOrder(self, ni1: PySide2.QtXmlPatterns.QXmlNodeModelIndex, ni2: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder """
        pass

    def createIndex(self, data): # real signature unknown; restored from __doc__
        """
        createIndex(self, data: int) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
        createIndex(self, data: int, additionalData: int) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
        createIndex(self, pointer: int, additionalData: int = 0) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex
        """
        pass

    def documentUri(self, ni): # real signature unknown; restored from __doc__
        """ documentUri(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtCore.QUrl """
        pass

    def elementById(self, NCName): # real signature unknown; restored from __doc__
        """ elementById(self, NCName: PySide2.QtXmlPatterns.QXmlName) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex """
        pass

    def isDeepEqual(self, ni1, ni2): # real signature unknown; restored from __doc__
        """ isDeepEqual(self, ni1: PySide2.QtXmlPatterns.QXmlNodeModelIndex, ni2: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> bool """
        return False

    def kind(self, ni): # real signature unknown; restored from __doc__
        """ kind(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind """
        pass

    def name(self, ni): # real signature unknown; restored from __doc__
        """ name(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlName """
        pass

    def namespaceBindings(self, n): # real signature unknown; restored from __doc__
        """ namespaceBindings(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.List[PySide2.QtXmlPatterns.QXmlName] """
        pass

    def namespaceForPrefix(self, ni, prefix, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ namespaceForPrefix(self, ni: PySide2.QtXmlPatterns.QXmlNodeModelIndex, prefix: Missing("PySide2.QtXmlPatterns.QXmlName.PrefixCode")) -> Missing("PySide2.QtXmlPatterns.QXmlName.NamespaceCode") """
        pass

    def nextFromSimpleAxis(self, axis, origin): # real signature unknown; restored from __doc__
        """ nextFromSimpleAxis(self, axis: PySide2.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis, origin: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex """
        pass

    def nodesByIdref(self, NCName): # real signature unknown; restored from __doc__
        """ nodesByIdref(self, NCName: PySide2.QtXmlPatterns.QXmlName) -> typing.List[PySide2.QtXmlPatterns.QXmlNodeModelIndex] """
        pass

    def root(self, n): # real signature unknown; restored from __doc__
        """ root(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex """
        pass

    def sendNamespaces(self, n, receiver): # real signature unknown; restored from __doc__
        """ sendNamespaces(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex, receiver: PySide2.QtXmlPatterns.QAbstractXmlReceiver) -> None """
        pass

    def sourceLocation(self, index): # real signature unknown; restored from __doc__
        """ sourceLocation(self, index: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> PySide2.QtXmlPatterns.QSourceLocation """
        pass

    def stringValue(self, n): # real signature unknown; restored from __doc__
        """ stringValue(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> str """
        return ""

    def typedValue(self, n): # real signature unknown; restored from __doc__
        """ typedValue(self, n: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> typing.Any """
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

    FirstChild = PySide2.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis.FirstChild
    InheritNamespaces = PySide2.QtXmlPatterns.QAbstractXmlNodeModel.NodeCopySetting.InheritNamespaces
    NextSibling = PySide2.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis.NextSibling
    NodeCopySetting = None # (!) real value is "<class 'PySide2.QtXmlPatterns.QAbstractXmlNodeModel.NodeCopySetting'>"
    Parent = PySide2.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis.Parent
    PreserveNamespaces = PySide2.QtXmlPatterns.QAbstractXmlNodeModel.NodeCopySetting.PreserveNamespaces
    PreviousSibling = PySide2.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis.PreviousSibling
    SimpleAxis = None # (!) real value is "<class 'PySide2.QtXmlPatterns.QAbstractXmlNodeModel.SimpleAxis'>"


class QAbstractXmlReceiver(__Shiboken.Object):
    """ QAbstractXmlReceiver(self) -> None """
    def atomicValue(self, value): # real signature unknown; restored from __doc__
        """ atomicValue(self, value: typing.Any) -> None """
        pass

    def attribute(self, name, value): # real signature unknown; restored from __doc__
        """ attribute(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None """
        pass

    def characters(self, value): # real signature unknown; restored from __doc__
        """ characters(self, value: str) -> None """
        pass

    def comment(self, value): # real signature unknown; restored from __doc__
        """ comment(self, value: str) -> None """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) -> None """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) -> None """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) -> None """
        pass

    def namespaceBinding(self, name): # real signature unknown; restored from __doc__
        """ namespaceBinding(self, name: PySide2.QtXmlPatterns.QXmlName) -> None """
        pass

    def processingInstruction(self, target, value): # real signature unknown; restored from __doc__
        """ processingInstruction(self, target: PySide2.QtXmlPatterns.QXmlName, value: str) -> None """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) -> None """
        pass

    def startElement(self, name): # real signature unknown; restored from __doc__
        """ startElement(self, name: PySide2.QtXmlPatterns.QXmlName) -> None """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) -> None """
        pass

    def whitespaceOnly(self, value): # real signature unknown; restored from __doc__
        """ whitespaceOnly(self, value: str) -> None """
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


class QSourceLocation(__Shiboken.Object):
    """
    QSourceLocation(self) -> None
    QSourceLocation(self, other: PySide2.QtXmlPatterns.QSourceLocation) -> None
    QSourceLocation(self, uri: PySide2.QtCore.QUrl, line: int = -1, column: int = -1) -> None
    """
    def column(self): # real signature unknown; restored from __doc__
        """ column(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def line(self): # real signature unknown; restored from __doc__
        """ line(self) -> int """
        return 0

    def setColumn(self, newColumn): # real signature unknown; restored from __doc__
        """ setColumn(self, newColumn: int) -> None """
        pass

    def setLine(self, newLine): # real signature unknown; restored from __doc__
        """ setLine(self, newLine: int) -> None """
        pass

    def setUri(self, newUri): # real signature unknown; restored from __doc__
        """ setUri(self, newUri: PySide2.QtCore.QUrl) -> None """
        pass

    def uri(self): # real signature unknown; restored from __doc__
        """ uri(self) -> PySide2.QtCore.QUrl """
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


class QXmlSerializer(QAbstractXmlReceiver):
    """ QXmlSerializer(self, query: PySide2.QtXmlPatterns.QXmlQuery, outputDevice: PySide2.QtCore.QIODevice) -> None """
    def atomicValue(self, value): # real signature unknown; restored from __doc__
        """ atomicValue(self, value: typing.Any) -> None """
        pass

    def attribute(self, name, value): # real signature unknown; restored from __doc__
        """ attribute(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None """
        pass

    def characters(self, value): # real signature unknown; restored from __doc__
        """ characters(self, value: str) -> None """
        pass

    def codec(self): # real signature unknown; restored from __doc__
        """ codec(self) -> PySide2.QtCore.QTextCodec """
        pass

    def comment(self, value): # real signature unknown; restored from __doc__
        """ comment(self, value: str) -> None """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) -> None """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) -> None """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) -> None """
        pass

    def namespaceBinding(self, nb): # real signature unknown; restored from __doc__
        """ namespaceBinding(self, nb: PySide2.QtXmlPatterns.QXmlName) -> None """
        pass

    def outputDevice(self): # real signature unknown; restored from __doc__
        """ outputDevice(self) -> PySide2.QtCore.QIODevice """
        pass

    def processingInstruction(self, name, value): # real signature unknown; restored from __doc__
        """ processingInstruction(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None """
        pass

    def setCodec(self, codec): # real signature unknown; restored from __doc__
        """ setCodec(self, codec: PySide2.QtCore.QTextCodec) -> None """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) -> None """
        pass

    def startElement(self, name): # real signature unknown; restored from __doc__
        """ startElement(self, name: PySide2.QtXmlPatterns.QXmlName) -> None """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, query, outputDevice): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QXmlFormatter(QXmlSerializer):
    """ QXmlFormatter(self, query: PySide2.QtXmlPatterns.QXmlQuery, outputDevice: PySide2.QtCore.QIODevice) -> None """
    def atomicValue(self, value): # real signature unknown; restored from __doc__
        """ atomicValue(self, value: typing.Any) -> None """
        pass

    def attribute(self, name, value): # real signature unknown; restored from __doc__
        """ attribute(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None """
        pass

    def characters(self, value): # real signature unknown; restored from __doc__
        """ characters(self, value: str) -> None """
        pass

    def comment(self, value): # real signature unknown; restored from __doc__
        """ comment(self, value: str) -> None """
        pass

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) -> None """
        pass

    def endElement(self): # real signature unknown; restored from __doc__
        """ endElement(self) -> None """
        pass

    def endOfSequence(self): # real signature unknown; restored from __doc__
        """ endOfSequence(self) -> None """
        pass

    def indentationDepth(self): # real signature unknown; restored from __doc__
        """ indentationDepth(self) -> int """
        return 0

    def processingInstruction(self, name, value): # real signature unknown; restored from __doc__
        """ processingInstruction(self, name: PySide2.QtXmlPatterns.QXmlName, value: str) -> None """
        pass

    def setIndentationDepth(self, depth): # real signature unknown; restored from __doc__
        """ setIndentationDepth(self, depth: int) -> None """
        pass

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) -> None """
        pass

    def startElement(self, name): # real signature unknown; restored from __doc__
        """ startElement(self, name: PySide2.QtXmlPatterns.QXmlName) -> None """
        pass

    def startOfSequence(self): # real signature unknown; restored from __doc__
        """ startOfSequence(self) -> None """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, query, outputDevice): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class QXmlItem(__Shiboken.Object):
    """
    QXmlItem(self) -> None
    QXmlItem(self, atomicValue: typing.Any) -> None
    QXmlItem(self, node: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> None
    QXmlItem(self, other: PySide2.QtXmlPatterns.QXmlItem) -> None
    """
    def isAtomicValue(self): # real signature unknown; restored from __doc__
        """ isAtomicValue(self) -> bool """
        return False

    def isNode(self): # real signature unknown; restored from __doc__
        """ isNode(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def toAtomicValue(self): # real signature unknown; restored from __doc__
        """ toAtomicValue(self) -> typing.Any """
        pass

    def toNodeModelIndex(self): # real signature unknown; restored from __doc__
        """ toNodeModelIndex(self) -> PySide2.QtXmlPatterns.QXmlNodeModelIndex """
        pass

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


class QXmlName(__Shiboken.Object):
    """
    QXmlName(self) -> None
    QXmlName(self, namePool: PySide2.QtXmlPatterns.QXmlNamePool, localName: str, namespaceURI: str = '', prefix: str = '') -> None
    QXmlName(self, other: PySide2.QtXmlPatterns.QXmlName) -> None
    """
    def fromClarkName(self, clarkName, namePool): # real signature unknown; restored from __doc__
        """ fromClarkName(clarkName: str, namePool: PySide2.QtXmlPatterns.QXmlNamePool) -> PySide2.QtXmlPatterns.QXmlName """
        pass

    def isNCName(self, candidate): # real signature unknown; restored from __doc__
        """ isNCName(candidate: str) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def localName(self, query): # real signature unknown; restored from __doc__
        """ localName(self, query: PySide2.QtXmlPatterns.QXmlNamePool) -> str """
        return ""

    def namespaceUri(self, query): # real signature unknown; restored from __doc__
        """ namespaceUri(self, query: PySide2.QtXmlPatterns.QXmlNamePool) -> str """
        return ""

    def prefix(self, query): # real signature unknown; restored from __doc__
        """ prefix(self, query: PySide2.QtXmlPatterns.QXmlNamePool) -> str """
        return ""

    def toClarkName(self, query): # real signature unknown; restored from __doc__
        """ toClarkName(self, query: PySide2.QtXmlPatterns.QXmlNamePool) -> str """
        return ""

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


class QXmlNamePool(__Shiboken.Object):
    """
    QXmlNamePool(self) -> None
    QXmlNamePool(self, other: PySide2.QtXmlPatterns.QXmlNamePool) -> None
    """
    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__() -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QXmlNodeModelIndex(__Shiboken.Object):
    """
    QXmlNodeModelIndex(self) -> None
    QXmlNodeModelIndex(self, other: PySide2.QtXmlPatterns.QXmlNodeModelIndex) -> None
    """
    def additionalData(self): # real signature unknown; restored from __doc__
        """ additionalData(self) -> int """
        return 0

    def data(self): # real signature unknown; restored from __doc__
        """ data(self) -> int """
        return 0

    def internalPointer(self): # real signature unknown; restored from __doc__
        """ internalPointer(self) -> int """
        return 0

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def model(self): # real signature unknown; restored from __doc__
        """ model(self) -> PySide2.QtXmlPatterns.QAbstractXmlNodeModel """
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

    Attribute = PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Attribute
    Comment = PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Comment
    Document = PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Document
    DocumentOrder = None # (!) real value is "<class 'PySide2.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder'>"
    Element = PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Element
    Follows = PySide2.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder.Follows
    Is = PySide2.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder.Is
    Namespace = PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Namespace
    NodeKind = None # (!) real value is "<class 'PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind'>"
    Precedes = PySide2.QtXmlPatterns.QXmlNodeModelIndex.DocumentOrder.Precedes
    ProcessingInstruction = PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.ProcessingInstruction
    Text = PySide2.QtXmlPatterns.QXmlNodeModelIndex.NodeKind.Text
    __hash__ = None


class QXmlQuery(__Shiboken.Object):
    """
    QXmlQuery(self) -> None
    QXmlQuery(self, np: PySide2.QtXmlPatterns.QXmlNamePool) -> None
    QXmlQuery(self, other: PySide2.QtXmlPatterns.QXmlQuery) -> None
    QXmlQuery(self, queryLanguage: PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage, np: PySide2.QtXmlPatterns.QXmlNamePool = Default(QXmlNamePool)) -> None
    """
    def bindVariable(self, localName, arg__2): # real signature unknown; restored from __doc__
        """
        bindVariable(self, localName: str, arg__2: PySide2.QtCore.QIODevice) -> None
        bindVariable(self, localName: str, query: PySide2.QtXmlPatterns.QXmlQuery) -> None
        bindVariable(self, localName: str, value: PySide2.QtXmlPatterns.QXmlItem) -> None
        bindVariable(self, name: PySide2.QtXmlPatterns.QXmlName, arg__2: PySide2.QtCore.QIODevice) -> None
        bindVariable(self, name: PySide2.QtXmlPatterns.QXmlName, query: PySide2.QtXmlPatterns.QXmlQuery) -> None
        bindVariable(self, name: PySide2.QtXmlPatterns.QXmlName, value: PySide2.QtXmlPatterns.QXmlItem) -> None
        """
        pass

    def evaluateTo(self, callback): # real signature unknown; restored from __doc__
        """
        evaluateTo(self, callback: PySide2.QtXmlPatterns.QAbstractXmlReceiver) -> bool
        evaluateTo(self, result: PySide2.QtXmlPatterns.QXmlResultItems) -> None
        evaluateTo(self, target: PySide2.QtCore.QIODevice) -> bool
        """
        return False

    def initialTemplateName(self): # real signature unknown; restored from __doc__
        """ initialTemplateName(self) -> PySide2.QtXmlPatterns.QXmlName """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler """
        pass

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool """
        pass

    def queryLanguage(self): # real signature unknown; restored from __doc__
        """ queryLanguage(self) -> PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage """
        pass

    def setFocus(self, document): # real signature unknown; restored from __doc__
        """
        setFocus(self, document: PySide2.QtCore.QIODevice) -> bool
        setFocus(self, documentURI: PySide2.QtCore.QUrl) -> bool
        setFocus(self, focus: str) -> bool
        setFocus(self, item: PySide2.QtXmlPatterns.QXmlItem) -> None
        """
        return False

    def setInitialTemplateName(self, name): # real signature unknown; restored from __doc__
        """
        setInitialTemplateName(self, name: PySide2.QtXmlPatterns.QXmlName) -> None
        setInitialTemplateName(self, name: str) -> None
        """
        pass

    def setMessageHandler(self, messageHandler): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, messageHandler: PySide2.QtXmlPatterns.QAbstractMessageHandler) -> None """
        pass

    def setQuery(self, queryURI, baseURI=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        setQuery(self, queryURI: PySide2.QtCore.QUrl, baseURI: PySide2.QtCore.QUrl = Default(QUrl)) -> None
        setQuery(self, sourceCode: PySide2.QtCore.QIODevice, documentURI: PySide2.QtCore.QUrl = Default(QUrl)) -> None
        setQuery(self, sourceCode: str, documentURI: PySide2.QtCore.QUrl = Default(QUrl)) -> None
        """
        pass

    def setUriResolver(self, resolver): # real signature unknown; restored from __doc__
        """ setUriResolver(self, resolver: PySide2.QtXmlPatterns.QAbstractUriResolver) -> None """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver """
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

    QueryLanguage = None # (!) real value is "<class 'PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage'>"
    XmlSchema11IdentityConstraintField = PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage.XmlSchema11IdentityConstraintField
    XmlSchema11IdentityConstraintSelector = PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage.XmlSchema11IdentityConstraintSelector
    XPath20 = PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage.XPath20
    XQuery10 = PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage.XQuery10
    XSLT20 = PySide2.QtXmlPatterns.QXmlQuery.QueryLanguage.XSLT20


class QXmlResultItems(__Shiboken.Object):
    """ QXmlResultItems(self) -> None """
    def current(self): # real signature unknown; restored from __doc__
        """ current(self) -> PySide2.QtXmlPatterns.QXmlItem """
        pass

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> PySide2.QtXmlPatterns.QXmlItem """
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


class QXmlSchema(__Shiboken.Object):
    """
    QXmlSchema(self) -> None
    QXmlSchema(self, other: PySide2.QtXmlPatterns.QXmlSchema) -> None
    """
    def documentUri(self): # real signature unknown; restored from __doc__
        """ documentUri(self) -> PySide2.QtCore.QUrl """
        pass

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def load(self, data, documentUri=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        load(self, data: PySide2.QtCore.QByteArray, documentUri: PySide2.QtCore.QUrl = Default(QUrl)) -> bool
        load(self, source: PySide2.QtCore.QIODevice, documentUri: PySide2.QtCore.QUrl = Default(QUrl)) -> bool
        load(self, source: PySide2.QtCore.QUrl) -> bool
        """
        pass

    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler """
        pass

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool """
        pass

    def setMessageHandler(self, handler): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, handler: PySide2.QtXmlPatterns.QAbstractMessageHandler) -> None """
        pass

    def setUriResolver(self, resolver): # real signature unknown; restored from __doc__
        """ setUriResolver(self, resolver: PySide2.QtXmlPatterns.QAbstractUriResolver) -> None """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QXmlSchemaValidator(__Shiboken.Object):
    """
    QXmlSchemaValidator(self) -> None
    QXmlSchemaValidator(self, schema: PySide2.QtXmlPatterns.QXmlSchema) -> None
    """
    def messageHandler(self): # real signature unknown; restored from __doc__
        """ messageHandler(self) -> PySide2.QtXmlPatterns.QAbstractMessageHandler """
        pass

    def namePool(self): # real signature unknown; restored from __doc__
        """ namePool(self) -> PySide2.QtXmlPatterns.QXmlNamePool """
        pass

    def schema(self): # real signature unknown; restored from __doc__
        """ schema(self) -> PySide2.QtXmlPatterns.QXmlSchema """
        pass

    def setMessageHandler(self, handler): # real signature unknown; restored from __doc__
        """ setMessageHandler(self, handler: PySide2.QtXmlPatterns.QAbstractMessageHandler) -> None """
        pass

    def setSchema(self, schema): # real signature unknown; restored from __doc__
        """ setSchema(self, schema: PySide2.QtXmlPatterns.QXmlSchema) -> None """
        pass

    def setUriResolver(self, resolver): # real signature unknown; restored from __doc__
        """ setUriResolver(self, resolver: PySide2.QtXmlPatterns.QAbstractUriResolver) -> None """
        pass

    def uriResolver(self): # real signature unknown; restored from __doc__
        """ uriResolver(self) -> PySide2.QtXmlPatterns.QAbstractUriResolver """
        pass

    def validate(self, data, documentUri=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        validate(self, data: PySide2.QtCore.QByteArray, documentUri: PySide2.QtCore.QUrl = Default(QUrl)) -> bool
        validate(self, source: PySide2.QtCore.QIODevice, documentUri: PySide2.QtCore.QUrl = Default(QUrl)) -> bool
        validate(self, source: PySide2.QtCore.QUrl) -> bool
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016138E017B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='PySide2.QtXmlPatterns', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016138E017B0>, origin='D:\\\\Maya2024\\\\Python\\\\lib\\\\site-packages\\\\PySide2\\\\QtXmlPatterns.cp310-win_amd64.pyd')"

