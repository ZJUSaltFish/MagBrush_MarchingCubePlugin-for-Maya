# encoding: utf-8
# module PySide2.QtXml
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtXml.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import Shiboken as __Shiboken


class QDomNode(__Shiboken.Object):
    """
    QDomNode(self) -> None
    QDomNode(self, arg__1: PySide2.QtXml.QDomNode) -> None
    """
    def appendChild(self, newChild): # real signature unknown; restored from __doc__
        """ appendChild(self, newChild: PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode """
        pass

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> PySide2.QtXml.QDomNamedNodeMap """
        pass

    def childNodes(self): # real signature unknown; restored from __doc__
        """ childNodes(self) -> PySide2.QtXml.QDomNodeList """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) -> None """
        pass

    def cloneNode(self, deep=True): # real signature unknown; restored from __doc__
        """ cloneNode(self, deep: bool = True) -> PySide2.QtXml.QDomNode """
        pass

    def columnNumber(self): # real signature unknown; restored from __doc__
        """ columnNumber(self) -> int """
        return 0

    def firstChild(self): # real signature unknown; restored from __doc__
        """ firstChild(self) -> PySide2.QtXml.QDomNode """
        pass

    def firstChildElement(self, tagName=''): # real signature unknown; restored from __doc__
        """ firstChildElement(self, tagName: str = '') -> PySide2.QtXml.QDomElement """
        pass

    def hasAttributes(self): # real signature unknown; restored from __doc__
        """ hasAttributes(self) -> bool """
        return False

    def hasChildNodes(self): # real signature unknown; restored from __doc__
        """ hasChildNodes(self) -> bool """
        return False

    def insertAfter(self, newChild, refChild): # real signature unknown; restored from __doc__
        """ insertAfter(self, newChild: PySide2.QtXml.QDomNode, refChild: PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode """
        pass

    def insertBefore(self, newChild, refChild): # real signature unknown; restored from __doc__
        """ insertBefore(self, newChild: PySide2.QtXml.QDomNode, refChild: PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode """
        pass

    def isAttr(self): # real signature unknown; restored from __doc__
        """ isAttr(self) -> bool """
        return False

    def isCDATASection(self): # real signature unknown; restored from __doc__
        """ isCDATASection(self) -> bool """
        return False

    def isCharacterData(self): # real signature unknown; restored from __doc__
        """ isCharacterData(self) -> bool """
        return False

    def isComment(self): # real signature unknown; restored from __doc__
        """ isComment(self) -> bool """
        return False

    def isDocument(self): # real signature unknown; restored from __doc__
        """ isDocument(self) -> bool """
        return False

    def isDocumentFragment(self): # real signature unknown; restored from __doc__
        """ isDocumentFragment(self) -> bool """
        return False

    def isDocumentType(self): # real signature unknown; restored from __doc__
        """ isDocumentType(self) -> bool """
        return False

    def isElement(self): # real signature unknown; restored from __doc__
        """ isElement(self) -> bool """
        return False

    def isEntity(self): # real signature unknown; restored from __doc__
        """ isEntity(self) -> bool """
        return False

    def isEntityReference(self): # real signature unknown; restored from __doc__
        """ isEntityReference(self) -> bool """
        return False

    def isNotation(self): # real signature unknown; restored from __doc__
        """ isNotation(self) -> bool """
        return False

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def isProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ isProcessingInstruction(self) -> bool """
        return False

    def isSupported(self, feature, version): # real signature unknown; restored from __doc__
        """ isSupported(self, feature: str, version: str) -> bool """
        return False

    def isText(self): # real signature unknown; restored from __doc__
        """ isText(self) -> bool """
        return False

    def lastChild(self): # real signature unknown; restored from __doc__
        """ lastChild(self) -> PySide2.QtXml.QDomNode """
        pass

    def lastChildElement(self, tagName=''): # real signature unknown; restored from __doc__
        """ lastChildElement(self, tagName: str = '') -> PySide2.QtXml.QDomElement """
        pass

    def lineNumber(self): # real signature unknown; restored from __doc__
        """ lineNumber(self) -> int """
        return 0

    def localName(self): # real signature unknown; restored from __doc__
        """ localName(self) -> str """
        return ""

    def namedItem(self, name): # real signature unknown; restored from __doc__
        """ namedItem(self, name: str) -> PySide2.QtXml.QDomNode """
        pass

    def namespaceURI(self): # real signature unknown; restored from __doc__
        """ namespaceURI(self) -> str """
        return ""

    def nextSibling(self): # real signature unknown; restored from __doc__
        """ nextSibling(self) -> PySide2.QtXml.QDomNode """
        pass

    def nextSiblingElement(self, taName=''): # real signature unknown; restored from __doc__
        """ nextSiblingElement(self, taName: str = '') -> PySide2.QtXml.QDomElement """
        pass

    def nodeName(self): # real signature unknown; restored from __doc__
        """ nodeName(self) -> str """
        return ""

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> PySide2.QtXml.QDomNode.NodeType """
        pass

    def nodeValue(self): # real signature unknown; restored from __doc__
        """ nodeValue(self) -> str """
        return ""

    def normalize(self): # real signature unknown; restored from __doc__
        """ normalize(self) -> None """
        pass

    def ownerDocument(self): # real signature unknown; restored from __doc__
        """ ownerDocument(self) -> PySide2.QtXml.QDomDocument """
        pass

    def parentNode(self): # real signature unknown; restored from __doc__
        """ parentNode(self) -> PySide2.QtXml.QDomNode """
        pass

    def prefix(self): # real signature unknown; restored from __doc__
        """ prefix(self) -> str """
        return ""

    def previousSibling(self): # real signature unknown; restored from __doc__
        """ previousSibling(self) -> PySide2.QtXml.QDomNode """
        pass

    def previousSiblingElement(self, tagName=''): # real signature unknown; restored from __doc__
        """ previousSiblingElement(self, tagName: str = '') -> PySide2.QtXml.QDomElement """
        pass

    def removeChild(self, oldChild): # real signature unknown; restored from __doc__
        """ removeChild(self, oldChild: PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode """
        pass

    def replaceChild(self, newChild, oldChild): # real signature unknown; restored from __doc__
        """ replaceChild(self, newChild: PySide2.QtXml.QDomNode, oldChild: PySide2.QtXml.QDomNode) -> PySide2.QtXml.QDomNode """
        pass

    def save(self, arg__1, arg__2, arg__3=None): # real signature unknown; restored from __doc__
        """ save(self, arg__1: PySide2.QtCore.QTextStream, arg__2: int, arg__3: PySide2.QtXml.QDomNode.EncodingPolicy = PySide2.QtXml.QDomNode.EncodingPolicy.EncodingFromDocument) -> None """
        pass

    def setNodeValue(self, arg__1): # real signature unknown; restored from __doc__
        """ setNodeValue(self, arg__1: str) -> None """
        pass

    def setPrefix(self, pre): # real signature unknown; restored from __doc__
        """ setPrefix(self, pre: str) -> None """
        pass

    def toAttr(self): # real signature unknown; restored from __doc__
        """ toAttr(self) -> PySide2.QtXml.QDomAttr """
        pass

    def toCDATASection(self): # real signature unknown; restored from __doc__
        """ toCDATASection(self) -> PySide2.QtXml.QDomCDATASection """
        pass

    def toCharacterData(self): # real signature unknown; restored from __doc__
        """ toCharacterData(self) -> PySide2.QtXml.QDomCharacterData """
        pass

    def toComment(self): # real signature unknown; restored from __doc__
        """ toComment(self) -> PySide2.QtXml.QDomComment """
        pass

    def toDocument(self): # real signature unknown; restored from __doc__
        """ toDocument(self) -> PySide2.QtXml.QDomDocument """
        pass

    def toDocumentFragment(self): # real signature unknown; restored from __doc__
        """ toDocumentFragment(self) -> PySide2.QtXml.QDomDocumentFragment """
        pass

    def toDocumentType(self): # real signature unknown; restored from __doc__
        """ toDocumentType(self) -> PySide2.QtXml.QDomDocumentType """
        pass

    def toElement(self): # real signature unknown; restored from __doc__
        """ toElement(self) -> PySide2.QtXml.QDomElement """
        pass

    def toEntity(self): # real signature unknown; restored from __doc__
        """ toEntity(self) -> PySide2.QtXml.QDomEntity """
        pass

    def toEntityReference(self): # real signature unknown; restored from __doc__
        """ toEntityReference(self) -> PySide2.QtXml.QDomEntityReference """
        pass

    def toNotation(self): # real signature unknown; restored from __doc__
        """ toNotation(self) -> PySide2.QtXml.QDomNotation """
        pass

    def toProcessingInstruction(self): # real signature unknown; restored from __doc__
        """ toProcessingInstruction(self) -> PySide2.QtXml.QDomProcessingInstruction """
        pass

    def toText(self): # real signature unknown; restored from __doc__
        """ toText(self) -> PySide2.QtXml.QDomText """
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

    def __lshift__(self, arg__1): # real signature unknown; restored from __doc__
        """
        __lshift__(self, arg__1: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream
        
        Return self<<value.
        """
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

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    AttributeNode = PySide2.QtXml.QDomNode.NodeType.AttributeNode
    BaseNode = PySide2.QtXml.QDomNode.NodeType.BaseNode
    CDATASectionNode = PySide2.QtXml.QDomNode.NodeType.CDATASectionNode
    CharacterDataNode = PySide2.QtXml.QDomNode.NodeType.CharacterDataNode
    CommentNode = PySide2.QtXml.QDomNode.NodeType.CommentNode
    DocumentFragmentNode = PySide2.QtXml.QDomNode.NodeType.DocumentFragmentNode
    DocumentNode = PySide2.QtXml.QDomNode.NodeType.DocumentNode
    DocumentTypeNode = PySide2.QtXml.QDomNode.NodeType.DocumentTypeNode
    ElementNode = PySide2.QtXml.QDomNode.NodeType.ElementNode
    EncodingFromDocument = PySide2.QtXml.QDomNode.EncodingPolicy.EncodingFromDocument
    EncodingFromTextStream = PySide2.QtXml.QDomNode.EncodingPolicy.EncodingFromTextStream
    EncodingPolicy = None # (!) real value is "<class 'PySide2.QtXml.QDomNode.EncodingPolicy'>"
    EntityNode = PySide2.QtXml.QDomNode.NodeType.EntityNode
    EntityReferenceNode = PySide2.QtXml.QDomNode.NodeType.EntityReferenceNode
    NodeType = None # (!) real value is "<class 'PySide2.QtXml.QDomNode.NodeType'>"
    NotationNode = PySide2.QtXml.QDomNode.NodeType.NotationNode
    ProcessingInstructionNode = PySide2.QtXml.QDomNode.NodeType.ProcessingInstructionNode
    TextNode = PySide2.QtXml.QDomNode.NodeType.TextNode
    __hash__ = None


