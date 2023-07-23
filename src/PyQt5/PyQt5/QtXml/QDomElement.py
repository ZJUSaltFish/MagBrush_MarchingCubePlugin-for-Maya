# encoding: utf-8
# module PyQt5.QtXml
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


from .QDomNode import QDomNode

class QDomElement(QDomNode):
    """
    QDomElement()
    QDomElement(x: QDomElement)
    """
    def attribute(self, name, defaultValue=''): # real signature unknown; restored from __doc__
        """ attribute(self, name: str, defaultValue: str = '') -> str """
        return ""

    def attributeNode(self, name): # real signature unknown; restored from __doc__
        """ attributeNode(self, name: str) -> QDomAttr """
        return QDomAttr

    def attributeNodeNS(self, nsURI, localName): # real signature unknown; restored from __doc__
        """ attributeNodeNS(self, nsURI: str, localName: str) -> QDomAttr """
        return QDomAttr

    def attributeNS(self, nsURI, localName, defaultValue=''): # real signature unknown; restored from __doc__
        """ attributeNS(self, nsURI: str, localName: str, defaultValue: str = '') -> str """
        return ""

    def attributes(self): # real signature unknown; restored from __doc__
        """ attributes(self) -> QDomNamedNodeMap """
        return QDomNamedNodeMap

    def elementsByTagName(self, tagname): # real signature unknown; restored from __doc__
        """ elementsByTagName(self, tagname: str) -> QDomNodeList """
        return QDomNodeList

    def elementsByTagNameNS(self, nsURI, localName): # real signature unknown; restored from __doc__
        """ elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList """
        return QDomNodeList

    def hasAttribute(self, name): # real signature unknown; restored from __doc__
        """ hasAttribute(self, name: str) -> bool """
        return False

    def hasAttributeNS(self, nsURI, localName): # real signature unknown; restored from __doc__
        """ hasAttributeNS(self, nsURI: str, localName: str) -> bool """
        return False

    def nodeType(self): # real signature unknown; restored from __doc__
        """ nodeType(self) -> QDomNode.NodeType """
        pass

    def removeAttribute(self, name): # real signature unknown; restored from __doc__
        """ removeAttribute(self, name: str) """
        pass

    def removeAttributeNode(self, oldAttr): # real signature unknown; restored from __doc__
        """ removeAttributeNode(self, oldAttr: QDomAttr) -> QDomAttr """
        return QDomAttr

    def removeAttributeNS(self, nsURI, localName): # real signature unknown; restored from __doc__
        """ removeAttributeNS(self, nsURI: str, localName: str) """
        pass

    def setAttribute(self, name, value): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttribute(self, name: str, value: str)
        setAttribute(self, name: str, value: int)
        setAttribute(self, name: str, value: int)
        setAttribute(self, name: str, value: float)
        setAttribute(self, name: str, value: int)
        """
        pass

    def setAttributeNode(self, newAttr): # real signature unknown; restored from __doc__
        """ setAttributeNode(self, newAttr: QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNodeNS(self, newAttr): # real signature unknown; restored from __doc__
        """ setAttributeNodeNS(self, newAttr: QDomAttr) -> QDomAttr """
        return QDomAttr

    def setAttributeNS(self, nsURI, qName, value): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setAttributeNS(self, nsURI: str, qName: str, value: str)
        setAttributeNS(self, nsURI: str, qName: str, value: int)
        setAttributeNS(self, nsURI: str, qName: str, value: int)
        setAttributeNS(self, nsURI: str, qName: str, value: float)
        setAttributeNS(self, nsURI: str, qName: str, value: int)
        """
        pass

    def setTagName(self, name): # real signature unknown; restored from __doc__
        """ setTagName(self, name: str) """
        pass

    def tagName(self): # real signature unknown; restored from __doc__
        """ tagName(self) -> str """
        return ""

    def text(self): # real signature unknown; restored from __doc__
        """ text(self) -> str """
        return ""

    def __init__(self, x=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass


