# encoding: utf-8
# module PySide2.QtCore
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtCore.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QXmlStreamReader(__Shiboken.Object):
    """
    QXmlStreamReader(self) -> None
    QXmlStreamReader(self, data: PySide2.QtCore.QByteArray) -> None
    QXmlStreamReader(self, data: str) -> None
    QXmlStreamReader(self, data: bytes) -> None
    QXmlStreamReader(self, device: PySide2.QtCore.QIODevice) -> None
    """
    def addData(self, data): # real signature unknown; restored from __doc__
        """
        addData(self, data: PySide2.QtCore.QByteArray) -> None
        addData(self, data: str) -> None
        addData(self, data: bytes) -> None
        """
        pass

    def addExtraNamespaceDeclaration(self, extraNamespaceDeclaraction): # real signature unknown; restored from __doc__
        """ addExtraNamespaceDeclaration(self, extraNamespaceDeclaraction: PySide2.QtCore.QXmlStreamNamespaceDeclaration) -> None """
        pass

    def addExtraNamespaceDeclarations(self, extraNamespaceDeclaractions, PySide2_QtCore_QXmlStreamNamespaceDeclaration=None): # real signature unknown; restored from __doc__
        """ addExtraNamespaceDeclarations(self, extraNamespaceDeclaractions: typing.List[PySide2.QtCore.QXmlStreamNamespaceDeclaration]) -> None """
        pass

    def atEnd(self): # real signature unknown; restored from __doc__
        """ atEnd(self) -> bool """
        return False

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> PySide2.QtCore.QXmlStreamAttributes """
        pass

    def characterOffset(self): # real signature unknown; restored from __doc__
        """ characterOffset(self) -> int """
        return 0

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def device(self): # real signature unknown; restored from __doc__
        """ device(self) -> PySide2.QtCore.QIODevice """
        pass

    def documentEncoding(self): # real signature unknown; restored from __doc__
        """ documentEncoding(self) -> str """
        return ""

    def documentVersion(self): # real signature unknown; restored from __doc__
        """ documentVersion(self) -> str """
        return ""

    def dtdName(self): # real signature unknown; restored from __doc__
        """ dtdName(self) -> str """
        return ""

    def dtdPublicId(self): # real signature unknown; restored from __doc__
        """ dtdPublicId(self) -> str """
        return ""

    def dtdSystemId(self): # real signature unknown; restored from __doc__
        """ dtdSystemId(self) -> str """
        return ""

    def entityDeclarations(self): # real signature unknown; restored from __doc__
        """ entityDeclarations(self) -> typing.List[PySide2.QtCore.QXmlStreamEntityDeclaration] """
        pass

    def entityExpansionLimit(self): # real signature unknown; restored from __doc__
        """ entityExpansionLimit(self) -> int """
        return 0

    def entityResolver(self): # real signature unknown; restored from __doc__
        """ entityResolver(self) -> PySide2.QtCore.QXmlStreamEntityResolver """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtCore.QXmlStreamReader.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def hasError(self): # real signature unknown; restored from __doc__
        """ hasError(self) -> bool """
        return False

    def isCDATA(self): # real signature unknown; restored from __doc__
        """ isCDATA(self) -> bool """
        return False

    def isCharacters(self): # real signature unknown; restored from __doc__
        """ isCharacters(self) -> bool """
        return False

    def isComment(self): # real signature unknown; restored from __doc__
        """ isComment(self) -> bool """
        return False

    def isDTD(self): # real signature unknown; restored from __doc__
        """ isDTD(self) -> bool """
        return False

    def isEndDocument(self): # real signature unknown; restored from __doc__
        """ isEndDocument(self) -> bool """
        return False

    def isEndElement(self): # real signature unknown; restored from __doc__
        """ isEndElement(self) -> bool """
        return False

    def isEntityReference(self): # real signature unknown; restored from __doc__
        """ isEntityReference(self) -> bool """
        return False

    def isProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ isProcessingInstruction(self) -> bool """
        return False

    def isStandaloneDocument(self): # real signature unknown; restored from __doc__
        """ isStandaloneDocument(self) -> bool """
        return False

    def isStartDocument(self): # real signature unknown; restored from __doc__
        """ isStartDocument(self) -> bool """
        return False

    def isStartElement(self): # real signature unknown; restored from __doc__
        """ isStartElement(self) -> bool """
        return False

    def isWhitespace(self): # real signature unknown; restored from __doc__
        """ isWhitespace(self) -> bool """
        return False

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def name(self): # real signature unknown; restored from __doc__
        """ name(self) -> str """
        return ""

    def namespaceDeclarations(self): # real signature unknown; restored from __doc__
        """ namespaceDeclarations(self) -> typing.List[PySide2.QtCore.QXmlStreamNamespaceDeclaration] """
        pass

    def namespaceProcessing(self): # real signature unknown; restored from __doc__
        """ namespaceProcessing(self) -> bool """
        return False

    def namespaceUri(self): # real signature unknown; restored from __doc__
        """ namespaceUri(self) -> str """
        return ""

    def notationDeclarations(self): # real signature unknown; restored from __doc__
        """ notationDeclarations(self) -> typing.List[PySide2.QtCore.QXmlStreamNotationDeclaration] """
        pass

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def processingInstructionData(self): # real signature unknown; restored from __doc__
        """ processingInstructionData(self) -> str """
        return ""

    def processingInstructionTarget(self): # real signature unknown; restored from __doc__
        """ processingInstructionTarget(self) -> str """
        return ""

    def qualifiedName(self): # real signature unknown; restored from __doc__
        """ qualifiedName(self) -> str """
        return ""

    def raiseError(self, message=''): # real signature unknown; restored from __doc__
        """ raiseError(self, message: str = '') -> None """
        pass

    def readElementText(self, behaviour=None): # real signature unknown; restored from __doc__
        """ readElementText(self, behaviour: PySide2.QtCore.QXmlStreamReader.ReadElementTextBehaviour = PySide2.QtCore.QXmlStreamReader.ReadElementTextBehaviour.ErrorOnUnexpectedElement) -> str """
        return ""

    def readNext(self): # real signature unknown; restored from __doc__
        """ readNext(self) -> PySide2.QtCore.QXmlStreamReader.TokenType """
        pass

    def readNextStartElement(self): # real signature unknown; restored from __doc__
        """ readNextStartElement(self) -> bool """
        return False

    def setDevice(self, device): # real signature unknown; restored from __doc__
        """ setDevice(self, device: PySide2.QtCore.QIODevice) -> None """
        pass

    def setEntityExpansionLimit(self, limit): # real signature unknown; restored from __doc__
        """ setEntityExpansionLimit(self, limit: int) -> None """
        pass

    def setEntityResolver(self, resolver): # real signature unknown; restored from __doc__
        """ setEntityResolver(self, resolver: PySide2.QtCore.QXmlStreamEntityResolver) -> None """
        pass

    def setNamespaceProcessing(self, arg__1): # real signature unknown; restored from __doc__
        """ setNamespaceProcessing(self, arg__1: bool) -> None """
        pass

    def skipCurrentElement(self): # real signature unknown; restored from __doc__
        """ skipCurrentElement(self) -> None """
        pass

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def tokenString(self): # real signature unknown; restored from __doc__
        """ tokenString(self) -> str """
        return ""

    def tokenType(self): # real signature unknown; restored from __doc__
        """ tokenType(self) -> PySide2.QtCore.QXmlStreamReader.TokenType """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Characters = PySide2.QtCore.QXmlStreamReader.TokenType.Characters
    Comment = PySide2.QtCore.QXmlStreamReader.TokenType.Comment
    CustomError = PySide2.QtCore.QXmlStreamReader.Error.CustomError
    DTD = PySide2.QtCore.QXmlStreamReader.TokenType.DTD
    EndDocument = PySide2.QtCore.QXmlStreamReader.TokenType.EndDocument
    EndElement = PySide2.QtCore.QXmlStreamReader.TokenType.EndElement
    EntityReference = PySide2.QtCore.QXmlStreamReader.TokenType.EntityReference
    Error = None # (!) real value is "<class 'PySide2.QtCore.QXmlStreamReader.Error'>"
    ErrorOnUnexpectedElement = PySide2.QtCore.QXmlStreamReader.ReadElementTextBehaviour.ErrorOnUnexpectedElement
    IncludeChildElements = PySide2.QtCore.QXmlStreamReader.ReadElementTextBehaviour.IncludeChildElements
    Invalid = PySide2.QtCore.QXmlStreamReader.TokenType.Invalid
    NoError = PySide2.QtCore.QXmlStreamReader.Error.NoError
    NoToken = PySide2.QtCore.QXmlStreamReader.TokenType.NoToken
    NotWellFormedError = PySide2.QtCore.QXmlStreamReader.Error.NotWellFormedError
    PrematureEndOfDocumentError = PySide2.QtCore.QXmlStreamReader.Error.PrematureEndOfDocumentError
    ProcessingInstruction = PySide2.QtCore.QXmlStreamReader.TokenType.ProcessingInstruction
    ReadElementTextBehaviour = None # (!) real value is "<class 'PySide2.QtCore.QXmlStreamReader.ReadElementTextBehaviour'>"
    SkipChildElements = PySide2.QtCore.QXmlStreamReader.ReadElementTextBehaviour.SkipChildElements
    StartDocument = PySide2.QtCore.QXmlStreamReader.TokenType.StartDocument
    StartElement = PySide2.QtCore.QXmlStreamReader.TokenType.StartElement
    TokenType = None # (!) real value is "<class 'PySide2.QtCore.QXmlStreamReader.TokenType'>"
    UnexpectedElementError = PySide2.QtCore.QXmlStreamReader.Error.UnexpectedElementError


