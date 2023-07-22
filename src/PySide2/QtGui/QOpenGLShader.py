# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLShader(__PySide2_QtCore.QObject):
    """ QOpenGLShader(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def compileSourceCode(self, source): # real signature unknown; restored from __doc__
        """
        compileSourceCode(self, source: PySide2.QtCore.QByteArray) -> bool
        compileSourceCode(self, source: str) -> bool
        compileSourceCode(self, source: bytes) -> bool
        """
        return False

    def compileSourceFile(self, fileName): # real signature unknown; restored from __doc__
        """ compileSourceFile(self, fileName: str) -> bool """
        return False

    def hasOpenGLShaders(self, type, context, PySide2_QtGui_QOpenGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasOpenGLShaders(type: PySide2.QtGui.QOpenGLShader.ShaderType, context: typing.Optional[PySide2.QtGui.QOpenGLContext] = None) -> bool """
        pass

    def isCompiled(self): # real signature unknown; restored from __doc__
        """ isCompiled(self) -> bool """
        return False

    def log(self): # real signature unknown; restored from __doc__
        """ log(self) -> str """
        return ""

    def shaderId(self): # real signature unknown; restored from __doc__
        """ shaderId(self) -> int """
        return 0

    def shaderType(self): # real signature unknown; restored from __doc__
        """ shaderType(self) -> PySide2.QtGui.QOpenGLShader.ShaderType """
        pass

    def sourceCode(self): # real signature unknown; restored from __doc__
        """ sourceCode(self) -> PySide2.QtCore.QByteArray """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __init__(self, type, parent, PySide2_QtCore_QObject=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    Compute = PySide2.QtGui.QOpenGLShader.ShaderTypeBit.Compute
    Fragment = PySide2.QtGui.QOpenGLShader.ShaderTypeBit.Fragment
    Geometry = PySide2.QtGui.QOpenGLShader.ShaderTypeBit.Geometry
    ShaderType = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLShader.ShaderType'>"
    ShaderTypeBit = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLShader.ShaderTypeBit'>"
    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00854340>'
    TessellationControl = PySide2.QtGui.QOpenGLShader.ShaderTypeBit.TessellationControl
    TessellationEvaluation = PySide2.QtGui.QOpenGLShader.ShaderTypeBit.TessellationEvaluation
    Vertex = PySide2.QtGui.QOpenGLShader.ShaderTypeBit.Vertex


