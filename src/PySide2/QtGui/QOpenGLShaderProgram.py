# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLShaderProgram(__PySide2_QtCore.QObject):
    """ QOpenGLShaderProgram(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None """
    def addCacheableShaderFromSourceCode(self, type, source): # real signature unknown; restored from __doc__
        """
        addCacheableShaderFromSourceCode(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, source: PySide2.QtCore.QByteArray) -> bool
        addCacheableShaderFromSourceCode(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, source: str) -> bool
        addCacheableShaderFromSourceCode(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, source: bytes) -> bool
        """
        return False

    def addCacheableShaderFromSourceFile(self, type, fileName): # real signature unknown; restored from __doc__
        """ addCacheableShaderFromSourceFile(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, fileName: str) -> bool """
        return False

    def addShader(self, shader): # real signature unknown; restored from __doc__
        """ addShader(self, shader: PySide2.QtGui.QOpenGLShader) -> bool """
        return False

    def addShaderFromSourceCode(self, type, source): # real signature unknown; restored from __doc__
        """
        addShaderFromSourceCode(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, source: PySide2.QtCore.QByteArray) -> bool
        addShaderFromSourceCode(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, source: str) -> bool
        addShaderFromSourceCode(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, source: bytes) -> bool
        """
        return False

    def addShaderFromSourceFile(self, type, fileName): # real signature unknown; restored from __doc__
        """ addShaderFromSourceFile(self, type: PySide2.QtGui.QOpenGLShader.ShaderType, fileName: str) -> bool """
        return False

    def attributeLocation(self, name): # real signature unknown; restored from __doc__
        """
        attributeLocation(self, name: PySide2.QtCore.QByteArray) -> int
        attributeLocation(self, name: str) -> int
        attributeLocation(self, name: bytes) -> int
        """
        return 0

    def bind(self): # real signature unknown; restored from __doc__
        """ bind(self) -> bool """
        return False

    def bindAttributeLocation(self, name, location): # real signature unknown; restored from __doc__
        """
        bindAttributeLocation(self, name: PySide2.QtCore.QByteArray, location: int) -> None
        bindAttributeLocation(self, name: str, location: int) -> None
        bindAttributeLocation(self, name: bytes, location: int) -> None
        """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def defaultInnerTessellationLevels(self): # real signature unknown; restored from __doc__
        """ defaultInnerTessellationLevels(self) -> typing.List[float] """
        pass

    def defaultOuterTessellationLevels(self): # real signature unknown; restored from __doc__
        """ defaultOuterTessellationLevels(self) -> typing.List[float] """
        pass

    def disableAttributeArray(self, location): # real signature unknown; restored from __doc__
        """
        disableAttributeArray(self, location: int) -> None
        disableAttributeArray(self, name: bytes) -> None
        """
        pass

    def enableAttributeArray(self, location): # real signature unknown; restored from __doc__
        """
        enableAttributeArray(self, location: int) -> None
        enableAttributeArray(self, name: bytes) -> None
        """
        pass

    def hasOpenGLShaderPrograms(self, context, PySide2_QtGui_QOpenGLContext=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ hasOpenGLShaderPrograms(context: typing.Optional[PySide2.QtGui.QOpenGLContext] = None) -> bool """
        pass

    def isLinked(self): # real signature unknown; restored from __doc__
        """ isLinked(self) -> bool """
        return False

    def link(self): # real signature unknown; restored from __doc__
        """ link(self) -> bool """
        return False

    def log(self): # real signature unknown; restored from __doc__
        """ log(self) -> str """
        return ""

    def maxGeometryOutputVertices(self): # real signature unknown; restored from __doc__
        """ maxGeometryOutputVertices(self) -> int """
        return 0

    def patchVertexCount(self): # real signature unknown; restored from __doc__
        """ patchVertexCount(self) -> int """
        return 0

    def programId(self): # real signature unknown; restored from __doc__
        """ programId(self) -> int """
        return 0

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) -> None """
        pass

    def removeAllShaders(self): # real signature unknown; restored from __doc__
        """ removeAllShaders(self) -> None """
        pass

    def removeShader(self, shader): # real signature unknown; restored from __doc__
        """ removeShader(self, shader: PySide2.QtGui.QOpenGLShader) -> None """
        pass

    def setAttributeArray(self, location, type, values, tupleSize, stride=0): # real signature unknown; restored from __doc__
        """
        setAttributeArray(self, location: int, type: int, values: int, tupleSize: int, stride: int = 0) -> None
        setAttributeArray(self, location: int, values: typing.Sequence[float], tupleSize: int, stride: int = 0) -> None
        setAttributeArray(self, name: bytes, type: int, values: int, tupleSize: int, stride: int = 0) -> None
        setAttributeArray(self, name: bytes, values: typing.Sequence[float], tupleSize: int, stride: int = 0) -> None
        """
        pass

    def setAttributeBuffer(self, location, type, offset, tupleSize, stride=0): # real signature unknown; restored from __doc__
        """
        setAttributeBuffer(self, location: int, type: int, offset: int, tupleSize: int, stride: int = 0) -> None
        setAttributeBuffer(self, name: bytes, type: int, offset: int, tupleSize: int, stride: int = 0) -> None
        """
        pass

    def setAttributeValue(self, location, value): # real signature unknown; restored from __doc__
        """
        setAttributeValue(self, location: int, value: PySide2.QtGui.QColor) -> None
        setAttributeValue(self, location: int, value: PySide2.QtGui.QVector2D) -> None
        setAttributeValue(self, location: int, value: PySide2.QtGui.QVector3D) -> None
        setAttributeValue(self, location: int, value: PySide2.QtGui.QVector4D) -> None
        setAttributeValue(self, location: int, value: float) -> None
        setAttributeValue(self, location: int, values: typing.Sequence[float], columns: int, rows: int) -> None
        setAttributeValue(self, location: int, x: float, y: float) -> None
        setAttributeValue(self, location: int, x: float, y: float, z: float) -> None
        setAttributeValue(self, location: int, x: float, y: float, z: float, w: float) -> None
        setAttributeValue(self, name: bytes, value: PySide2.QtGui.QColor) -> None
        setAttributeValue(self, name: bytes, value: PySide2.QtGui.QVector2D) -> None
        setAttributeValue(self, name: bytes, value: PySide2.QtGui.QVector3D) -> None
        setAttributeValue(self, name: bytes, value: PySide2.QtGui.QVector4D) -> None
        setAttributeValue(self, name: bytes, value: float) -> None
        setAttributeValue(self, name: bytes, values: typing.Sequence[float], columns: int, rows: int) -> None
        setAttributeValue(self, name: bytes, x: float, y: float) -> None
        setAttributeValue(self, name: bytes, x: float, y: float, z: float) -> None
        setAttributeValue(self, name: bytes, x: float, y: float, z: float, w: float) -> None
        """
        pass

    def setDefaultInnerTessellationLevels(self, levels, p_float=None): # real signature unknown; restored from __doc__
        """ setDefaultInnerTessellationLevels(self, levels: typing.List[float]) -> None """
        pass

    def setDefaultOuterTessellationLevels(self, levels, p_float=None): # real signature unknown; restored from __doc__
        """ setDefaultOuterTessellationLevels(self, levels: typing.List[float]) -> None """
        pass

    def setPatchVertexCount(self, count): # real signature unknown; restored from __doc__
        """ setPatchVertexCount(self, count: int) -> None """
        pass

    def setUniformValue(self, location, color): # real signature unknown; restored from __doc__
        """
        setUniformValue(self, location: int, color: PySide2.QtGui.QColor) -> None
        setUniformValue(self, location: int, point: PySide2.QtCore.QPoint) -> None
        setUniformValue(self, location: int, point: PySide2.QtCore.QPointF) -> None
        setUniformValue(self, location: int, size: PySide2.QtCore.QSize) -> None
        setUniformValue(self, location: int, size: PySide2.QtCore.QSizeF) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x2) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x3) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix2x4) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x2) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x3) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix3x4) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x2) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x3) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QMatrix4x4) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QTransform) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QVector2D) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QVector3D) -> None
        setUniformValue(self, location: int, value: PySide2.QtGui.QVector4D) -> None
        setUniformValue(self, location: int, value: float) -> None
        setUniformValue(self, location: int, value: typing.Tuple[typing.Tuple[float, float], typing.Tuple[float, float]]) -> None
        setUniformValue(self, location: int, value: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]]) -> None
        setUniformValue(self, location: int, value: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]]) -> None
        setUniformValue(self, location: int, value: int) -> None
        setUniformValue(self, location: int, value: int) -> None
        setUniformValue(self, location: int, x: float, y: float) -> None
        setUniformValue(self, location: int, x: float, y: float, z: float) -> None
        setUniformValue(self, location: int, x: float, y: float, z: float, w: float) -> None
        setUniformValue(self, name: bytes, color: PySide2.QtGui.QColor) -> None
        setUniformValue(self, name: bytes, point: PySide2.QtCore.QPoint) -> None
        setUniformValue(self, name: bytes, point: PySide2.QtCore.QPointF) -> None
        setUniformValue(self, name: bytes, size: PySide2.QtCore.QSize) -> None
        setUniformValue(self, name: bytes, size: PySide2.QtCore.QSizeF) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix2x2) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix2x3) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix2x4) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix3x2) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix3x3) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix3x4) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix4x2) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix4x3) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QMatrix4x4) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QTransform) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QVector2D) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QVector3D) -> None
        setUniformValue(self, name: bytes, value: PySide2.QtGui.QVector4D) -> None
        setUniformValue(self, name: bytes, value: typing.Tuple[typing.Tuple[float, float], typing.Tuple[float, float]]) -> None
        setUniformValue(self, name: bytes, value: typing.Tuple[typing.Tuple[float, float, float], typing.Tuple[float, float, float], typing.Tuple[float, float, float]]) -> None
        setUniformValue(self, name: bytes, value: typing.Tuple[typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float], typing.Tuple[float, float, float, float]]) -> None
        setUniformValue(self, name: bytes, x: float, y: float) -> None
        setUniformValue(self, name: bytes, x: float, y: float, z: float) -> None
        setUniformValue(self, name: bytes, x: float, y: float, z: float, w: float) -> None
        """
        pass

    def setUniformValue1f(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        setUniformValue1f(self, arg__1: bytes, arg__2: float) -> None
        setUniformValue1f(self, arg__1: int, arg__2: float) -> None
        """
        pass

    def setUniformValue1i(self, arg__1, arg__2): # real signature unknown; restored from __doc__
        """
        setUniformValue1i(self, arg__1: bytes, arg__2: int) -> None
        setUniformValue1i(self, arg__1: int, arg__2: int) -> None
        """
        pass

    def setUniformValueArray(self, location, values, p_float=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        setUniformValueArray(self, location: int, values: typing.Sequence[float], count: int, tupleSize: int) -> None
        setUniformValueArray(self, location: int, values: typing.Sequence[int], count: int) -> None
        setUniformValueArray(self, location: int, values: typing.Sequence[int], count: int) -> None
        setUniformValueArray(self, name: bytes, values: typing.Sequence[float], count: int, tupleSize: int) -> None
        setUniformValueArray(self, name: bytes, values: typing.Sequence[int], count: int) -> None
        setUniformValueArray(self, name: bytes, values: typing.Sequence[int], count: int) -> None
        """
        pass

    def shaders(self): # real signature unknown; restored from __doc__
        """ shaders(self) -> typing.List[PySide2.QtGui.QOpenGLShader] """
        pass

    def uniformLocation(self, name): # real signature unknown; restored from __doc__
        """
        uniformLocation(self, name: PySide2.QtCore.QByteArray) -> int
        uniformLocation(self, name: str) -> int
        uniformLocation(self, name: bytes) -> int
        """
        return 0

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

    staticMetaObject = None # (!) real value is '<PySide2.QtCore.QMetaObject object at 0x0000029F00847BC0>'


