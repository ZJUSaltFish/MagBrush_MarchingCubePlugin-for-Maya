# encoding: utf-8
# module PySide2.QtXml
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtXml.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


from .QDomNode import QDomNode

class QDomDocument(QDomNode):
    """
    QDomDocument(self) -> None
    QDomDocument(self, doctype: PySide2.QtXml.QDomDocumentType) -> None
    QDomDocument(self, name: str) -> None
    QDomDocument(self, x: PySide2.QtXml.QDomDocument) -> None
    """
    def createAttribute(self, name): # real signature unknown; restored from __doc__
        """ createAttribute(self, name: str) -> PySide2.QtXml.QDomAttr """
        pass

    def createAttributeNS(self, nsURI, qName): # real signature unknown; restored from __doc__
        """ createAttributeNS(self, nsURI: str, qName: str) -> PySide2.QtXml.QDomAttr """
        pass

    def createCDATASection(self, data): # real signature unknown; restored from __doc__
        """ createCDATASection(self, data: str) -> PySide2.QtXml.QDomCDATASection """
        pass

    def createComment(self, data): # real signature unknown; restored from __doc__
        """ createComment(self, data: str) -> PySide2.QtXml.QDomComment """
        pass

    def createDocumentFragment(self): # real signature unknown; restored from __doc__
        """ createDocumentFragment(self) -> PySide2.QtXml.QDomDocumentFragment """
        pass

    def createElement(self, tagName): # real signature unknown; restored from __doc__
        """ createElement(self, tagName: str) -> PySide2.QtXml.QDomElement """
        pass

    def createElementNS(self, nsURI, qName): # real signature unknown; restored from __doc__
        """ createElementNS(self, nsURI: str, qName: str) -> PySide2.QtXml.QDomElement """
        pass

    def createEntityReference(self, name): # real signature unknown; restored from __doc__
        """ createEntityReference(self, name: str) -> PySide2.QtXml.QDomEntityReference """
        pass

    def createProcessingInstruction(self, target, data): # real signature unknown; restored from __doc__
        """ createProcessingInstruction(self, target: str, data: str) -> PySide2.QtXml.QDomProcessingInstruction """
        pass

    def createTextNode(self, data): # real signature unknown; restored from __doc__
        """ createTextNode(self, data: str) -> PySide2.QtXml.QDomText """
        pass

    def doctype(self): # real signature unknown; restored from __doc__
        """ doctype(self) -> PySide2.QtXml.QDomDocumentType """
        pass

    def documentElement(self): # real signature unknown; restored from __doc__
        """ documentElement(self) -> PySide2.QtXml.QDomElement """
        pass

    def elementById(self, elementId): # real signature unknown; restored from __doc__
        """ elementById(self, elementId: str) -> PySide2.QtXml.QDomElement """
        pass

    def elementsByTagName(self, tagname): # real signature unknown; restored from __doc__
        """ elementsByTagName(self, tagname: str) -> PySide2.QtXml.QDomNodeList """
        pass

    def elementsByTagNameNS(self, nsURI, localName): # real signature unknown; restored from __doc__
        """ elementsByTagNameNS(self, nsURI: str, localName: str) -> PySide2.QtXml.QDomNodeList """
        pass

    def implementation(self): # real signature unknown; restored from __doc__
        """ implementation(self) -> PySide2.QtXml.QDomImplementation """
        pass

    def importNode(self, importedNode, deep): # real signature unknown; restored from __doc__
        """ importNode(self, importedNode: PySide2.QtXml.QDomNode, deep: bool) -> PySide2.QtXml.QDomNode """
        pass

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> PySide2.QtXml.QDomNode.NodeType """
        pass

    def setContent(self, dev): # real signature unknown; restored from __doc__
        """
        setContent(self, dev: PySide2.QtCore.QIODevice) -> typing.Tuple[bool, str, int, int]
        setContent(self, dev: PySide2.QtCore.QIODevice, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]
        setContent(self, reader: PySide2.QtCore.QXmlStreamReader, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]
        setContent(self, source: PySide2.QtXml.QXmlInputSource, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]
        setContent(self, source: PySide2.QtXml.QXmlInputSource, reader: PySide2.QtXml.QXmlReader) -> typing.Tuple[bool, str, int, int]
        setContent(self, text: PySide2.QtCore.QByteArray) -> typing.Tuple[bool, str, int, int]
        setContent(self, text: PySide2.QtCore.QByteArray, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]
        setContent(self, text: str) -> typing.Tuple[bool, str, int, int]
        setContent(self, text: str, namespaceProcessing: bool) -> typing.Tuple[bool, str, int, int]
        """
        pass

    def toByteArray(self, arg__1=1): # real signature unknown; restored from __doc__
        """ toByteArray(self, arg__1: int = 1) -> PySide2.QtCore.QByteArray """
        pass

    def toString(self, arg__1=1): # real signature unknown; restored from __doc__
        """ toString(self, arg__1: int = 1) -> str """
        return ""

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


