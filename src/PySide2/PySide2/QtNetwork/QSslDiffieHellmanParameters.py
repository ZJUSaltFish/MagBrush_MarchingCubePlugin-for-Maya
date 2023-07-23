# encoding: utf-8
# module PySide2.QtNetwork
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtNetwork.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QSslDiffieHellmanParameters(__Shiboken.Object):
    """
    QSslDiffieHellmanParameters(self) -> None
    QSslDiffieHellmanParameters(self, other: PySide2.QtNetwork.QSslDiffieHellmanParameters) -> None
    """
    def defaultParameters(self): # real signature unknown; restored from __doc__
        """ defaultParameters() -> PySide2.QtNetwork.QSslDiffieHellmanParameters """
        pass

    def error(self): # real signature unknown; restored from __doc__
        """ error(self) -> PySide2.QtNetwork.QSslDiffieHellmanParameters.Error """
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fromEncoded(self, device, format=None): # real signature unknown; restored from __doc__
        """
        fromEncoded(device: PySide2.QtCore.QIODevice, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem) -> PySide2.QtNetwork.QSslDiffieHellmanParameters
        fromEncoded(encoded: PySide2.QtCore.QByteArray, format: PySide2.QtNetwork.QSsl.EncodingFormat = PySide2.QtNetwork.QSsl.EncodingFormat.Pem) -> PySide2.QtNetwork.QSslDiffieHellmanParameters
        """
        pass

    def isEmpty(self): # real signature unknown; restored from __doc__
        """ isEmpty(self) -> bool """
        return False

    def isValid(self): # real signature unknown; restored from __doc__
        """ isValid(self) -> bool """
        return False

    def swap(self, other): # real signature unknown; restored from __doc__
        """ swap(self, other: PySide2.QtNetwork.QSslDiffieHellmanParameters) -> None """
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

    Error = None # (!) real value is "<class 'PySide2.QtNetwork.QSslDiffieHellmanParameters.Error'>"
    InvalidInputDataError = PySide2.QtNetwork.QSslDiffieHellmanParameters.Error.InvalidInputDataError
    NoError = PySide2.QtNetwork.QSslDiffieHellmanParameters.Error.NoError
    UnsafeParametersError = PySide2.QtNetwork.QSslDiffieHellmanParameters.Error.UnsafeParametersError
    __hash__ = None


