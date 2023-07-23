# encoding: utf-8
# module PyQt5.QtXml
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtXml.pyd
# by generator 1.147
# no doc

# imports
import sip as __sip


class QDomImplementation(__sip.simplewrapper):
    """
    QDomImplementation()
    QDomImplementation(a0: QDomImplementation)
    """
    def createDocument(self, nsURI, qName, doctype): # real signature unknown; restored from __doc__
        """ createDocument(self, nsURI: str, qName: str, doctype: QDomDocumentType) -> QDomDocument """
        return QDomDocument

    def createDocumentType(self, qName, publicId, systemId): # real signature unknown; restored from __doc__
        """ createDocumentType(self, qName: str, publicId: str, systemId: str) -> QDomDocumentType """
        return QDomDocumentType

    def hasFeature(self, feature, version): # real signature unknown; restored from __doc__
        """ hasFeature(self, feature: str, version: str) -> bool """
        return False

    def invalidDataPolicy(self): # real signature unknown; restored from __doc__
        """ invalidDataPolicy() -> QDomImplementation.InvalidDataPolicy """
        pass

    def isNull(self): # real signature unknown; restored from __doc__
        """ isNull(self) -> bool """
        return False

    def setInvalidDataPolicy(self, policy): # real signature unknown; restored from __doc__
        """ setInvalidDataPolicy(policy: QDomImplementation.InvalidDataPolicy) """
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

    def __init__(self, a0=None): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AcceptInvalidChars = 0
    DropInvalidChars = 1
    ReturnNullNode = 2
    __hash__ = None


