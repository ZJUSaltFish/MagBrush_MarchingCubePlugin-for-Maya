# encoding: utf-8
# module PyQt5.QtXml
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QDomNode import QDomNode

class QDomDocument(QDomNode):
    """
    QDomDocument()
    QDomDocument(name: str)
    QDomDocument(doctype: QDomDocumentType)
    QDomDocument(x: QDomDocument)
    """
    def createAttribute(self, name): # real signature unknown; restored from __doc__
        """ createAttribute(self, name: str) -> QDomAttr """
        return QDomAttr

    def createAttributeNS(self, nsURI, qName): # real signature unknown; restored from __doc__
        """ createAttributeNS(self, nsURI: str, qName: str) -> QDomAttr """
        return QDomAttr

    def createCDATASection(self, data): # real signature unknown; restored from __doc__
        """ createCDATASection(self, data: str) -> QDomCDATASection """
        return QDomCDATASection

    def createComment(self, data): # real signature unknown; restored from __doc__
        """ createComment(self, data: str) -> QDomComment """
        return QDomComment

    def createDocumentFragment(self): # real signature unknown; restored from __doc__
        """ createDocumentFragment(self) -> QDomDocumentFragment """
        return QDomDocumentFragment

    def createElement(self, tagName): # real signature unknown; restored from __doc__
        """ createElement(self, tagName: str) -> QDomElement """
        return QDomElement

    def createElementNS(self, nsURI, qName): # real signature unknown; restored from __doc__
        """ createElementNS(self, nsURI: str, qName: str) -> QDomElement """
        return QDomElement

    def createEntityReference(self, name): # real signature unknown; restored from __doc__
        """ createEntityReference(self, name: str) -> QDomEntityReference """
        return QDomEntityReference

    def createProcessingInstruction(self, target, data): # real signature unknown; restored from __doc__
        """ createProcessingInstruction(self, target: str, data: str) -> QDomProcessingInstruction """
        return QDomProcessingInstruction

    def createTextNode(self, data): # real signature unknown; restored from __doc__
        """ createTextNode(self, data: str) -> QDomText """
        return QDomText

    def doctype(self): # real signature unknown; restored from __doc__
        """ doctype(self) -> QDomDocumentType """
        return QDomDocumentType

    def documentElement(self): # real signature unknown; restored from __doc__
        """ documentElement(self) -> QDomElement """
        return QDomElement

    def elementById(self, elementId): # real signature unknown; restored from __doc__
        """ elementById(self, elementId: str) -> QDomElement """
        return QDomElement

    def elementsByTagName(self, tagname): # real signature unknown; restored from __doc__
        """ elementsByTagName(self, tagname: str) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, nsURI, localName): # real signature unknown; restored from __doc__
        """ elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList """
        return QDomNodeList

    def implementation(self): # real signature unknown; restored from __doc__
        """ implementation(self) -> QDomImplementation """
        return QDomImplementation

    def importNode(self, importedNode, deep): # real signature unknown; restored from __doc__
        """ importNode(self, importedNode: QDomNode, deep: bool) -> QDomNode """
        return QDomNode

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> QDomNode.NodeType """
        pass

    def setContent(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setContent(self, text: Union[QByteArray, bytes, bytearray], namespaceProcessing: bool) -> Tuple[bool, str, int, int]
        setContent(self, text: str, namespaceProcessing: bool) -> Tuple[bool, str, int, int]
        setContent(self, dev: QIODevice, namespaceProcessing: bool) -> Tuple[bool, str, int, int]
        setContent(self, source: QXmlInputSource, namespaceProcessing: bool) -> Tuple[bool, str, int, int]
        setContent(self, text: Union[QByteArray, bytes, bytearray]) -> Tuple[bool, str, int, int]
        setContent(self, text: str) -> Tuple[bool, str, int, int]
        setContent(self, dev: QIODevice) -> Tuple[bool, str, int, int]
        setContent(self, source: QXmlInputSource, reader: QXmlReader) -> Tuple[bool, str, int, int]
        setContent(self, reader: QXmlStreamReader, namespaceProcessing: bool) -> Tuple[bool, str, int, int]
        """
        pass

    def toByteArray(self, indent=1): # real signature unknown; restored from __doc__
        """ toByteArray(self, indent: int = 1) -> QByteArray """
        pass

    def toString(self, indent=1): # real signature unknown; restored from __doc__
        """ toString(self, indent: int = 1) -> str """
        return ""

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass


