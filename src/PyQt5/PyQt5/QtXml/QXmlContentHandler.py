# encoding: utf-8
# module PyQt5.QtXml
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QXmlContentHandler(__sip.simplewrapper):
    """
    QXmlContentHandler()
    QXmlContentHandler(a0: QXmlContentHandler)
    """
    def characters(self, ch): # real signature unknown; restored from __doc__
        """ characters(self, ch: str) -> bool """
        return False

    def endDocument(self): # real signature unknown; restored from __doc__
        """ endDocument(self) -> bool """
        return False

    def endElement(self, namespaceURI, localName, qName): # real signature unknown; restored from __doc__
        """ endElement(self, namespaceURI: str, localName: str, qName: str) -> bool """
        return False

    def endPrefixMapping(self, prefix): # real signature unknown; restored from __doc__
        """ endPrefixMapping(self, prefix: str) -> bool """
        return False

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def ignorableWhitespace(self, ch): # real signature unknown; restored from __doc__
        """ ignorableWhitespace(self, ch: str) -> bool """
        return False

    def processingInstruction(self, target, data): # real signature unknown; restored from __doc__
        """ processingInstruction(self, target: str, data: str) -> bool """
        return False

    def setDocumentLocator(self, locator): # real signature unknown; restored from __doc__
        """ setDocumentLocator(self, locator: QXmlLocator) """
        pass

    def skippedEntity(self, name): # real signature unknown; restored from __doc__
        """ skippedEntity(self, name: str) -> bool """
        return False

    def startDocument(self): # real signature unknown; restored from __doc__
        """ startDocument(self) -> bool """
        return False

    def startElement(self, namespaceURI, localName, qName, atts): # real signature unknown; restored from __doc__
        """ startElement(self, namespaceURI: str, localName: str, qName: str, atts: QXmlAttributes) -> bool """
        return False

    def startPrefixMapping(self, prefix, uri): # real signature unknown; restored from __doc__
        """ startPrefixMapping(self, prefix: str, uri: str) -> bool """
        return False

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



