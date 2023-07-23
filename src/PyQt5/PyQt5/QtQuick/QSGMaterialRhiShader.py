# encoding: utf-8
# module PyQt5.QtQuick
# from D:\Maya2024\Python\lib\site-packages\PyQt5\QtQuick.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui
import PyQt5.QtQml as __PyQt5_QtQml
import sip as __sip


from .QSGMaterialShader import QSGMaterialShader

class QSGMaterialRhiShader(QSGMaterialShader):
    """ QSGMaterialRhiShader() """
    def compile(self, *args, **kwargs): # real signature unknown
        pass

    def flags(self): # real signature unknown; restored from __doc__
        """ flags(self) -> QSGMaterialRhiShader.Flags """
        pass

    def fragmentShader(self, *args, **kwargs): # real signature unknown
        pass

    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def setFlag(self, flags, QSGMaterialRhiShader_Flags=None, QSGMaterialRhiShader_Flag=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ setFlag(self, flags: Union[QSGMaterialRhiShader.Flags, QSGMaterialRhiShader.Flag], on: bool = True) """
        pass

    def setShaderSourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def setShaderSourceFiles(self, *args, **kwargs): # real signature unknown
        pass

    def updateGraphicsPipelineState(self, state, ps, newMaterial, oldMaterial): # real signature unknown; restored from __doc__
        """ updateGraphicsPipelineState(self, state: QSGMaterialRhiShader.RenderState, ps: QSGMaterialRhiShader.GraphicsPipelineState, newMaterial: QSGMaterial, oldMaterial: QSGMaterial) -> bool """
        return False

    def updateSampledImage(self, state, binding, newMaterial, oldMaterial): # real signature unknown; restored from __doc__
        """ updateSampledImage(self, state: QSGMaterialRhiShader.RenderState, binding: int, newMaterial: QSGMaterial, oldMaterial: QSGMaterial) -> QSGTexture """
        return QSGTexture

    def updateUniformData(self, state, newMaterial, oldMaterial): # real signature unknown; restored from __doc__
        """ updateUniformData(self, state: QSGMaterialRhiShader.RenderState, newMaterial: QSGMaterial, oldMaterial: QSGMaterial) -> bool """
        return False

    def vertexShader(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    UpdatesGraphicsPipelineState = 1


