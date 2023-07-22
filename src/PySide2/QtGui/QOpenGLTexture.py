# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLTexture(__Shiboken.Object):
    """
    QOpenGLTexture(self, image: PySide2.QtGui.QImage, genMipMaps: PySide2.QtGui.QOpenGLTexture.MipMapGeneration = PySide2.QtGui.QOpenGLTexture.MipMapGeneration.GenerateMipMaps) -> None
    QOpenGLTexture(self, target: PySide2.QtGui.QOpenGLTexture.Target) -> None
    """
    def allocateStorage(self): # real signature unknown; restored from __doc__
        """
        allocateStorage(self) -> None
        allocateStorage(self, pixelFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, pixelType: PySide2.QtGui.QOpenGLTexture.PixelType) -> None
        """
        pass

    def bind(self): # real signature unknown; restored from __doc__
        """
        bind(self) -> None
        bind(self, unit: int, reset: PySide2.QtGui.QOpenGLTexture.TextureUnitReset = PySide2.QtGui.QOpenGLTexture.TextureUnitReset.DontResetTextureUnit) -> None
        """
        pass

    def borderColor(self): # real signature unknown; restored from __doc__
        """ borderColor(self) -> PySide2.QtGui.QColor """
        pass

    def boundTextureId(self, target): # real signature unknown; restored from __doc__
        """
        boundTextureId(target: PySide2.QtGui.QOpenGLTexture.BindingTarget) -> int
        boundTextureId(unit: int, target: PySide2.QtGui.QOpenGLTexture.BindingTarget) -> int
        """
        return 0

    def comparisonFunction(self): # real signature unknown; restored from __doc__
        """ comparisonFunction(self) -> PySide2.QtGui.QOpenGLTexture.ComparisonFunction """
        pass

    def comparisonMode(self): # real signature unknown; restored from __doc__
        """ comparisonMode(self) -> PySide2.QtGui.QOpenGLTexture.ComparisonMode """
        pass

    def create(self): # real signature unknown; restored from __doc__
        """ create(self) -> bool """
        return False

    def createTextureView(self, target, viewFormat, minimumMipmapLevel, maximumMipmapLevel, minimumLayer, maximumLayer): # real signature unknown; restored from __doc__
        """ createTextureView(self, target: PySide2.QtGui.QOpenGLTexture.Target, viewFormat: PySide2.QtGui.QOpenGLTexture.TextureFormat, minimumMipmapLevel: int, maximumMipmapLevel: int, minimumLayer: int, maximumLayer: int) -> PySide2.QtGui.QOpenGLTexture """
        pass

    def depth(self): # real signature unknown; restored from __doc__
        """ depth(self) -> int """
        return 0

    def depthStencilMode(self): # real signature unknown; restored from __doc__
        """ depthStencilMode(self) -> PySide2.QtGui.QOpenGLTexture.DepthStencilMode """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) -> None """
        pass

    def faces(self): # real signature unknown; restored from __doc__
        """ faces(self) -> int """
        return 0

    def format(self): # real signature unknown; restored from __doc__
        """ format(self) -> PySide2.QtGui.QOpenGLTexture.TextureFormat """
        pass

    def generateMipMaps(self): # real signature unknown; restored from __doc__
        """
        generateMipMaps(self) -> None
        generateMipMaps(self, baseLevel: int, resetBaseLevel: bool = True) -> None
        """
        pass

    def hasFeature(self, feature): # real signature unknown; restored from __doc__
        """ hasFeature(feature: PySide2.QtGui.QOpenGLTexture.Feature) -> bool """
        return False

    def height(self): # real signature unknown; restored from __doc__
        """ height(self) -> int """
        return 0

    def isAutoMipMapGenerationEnabled(self): # real signature unknown; restored from __doc__
        """ isAutoMipMapGenerationEnabled(self) -> bool """
        return False

    def isBound(self): # real signature unknown; restored from __doc__
        """
        isBound(self) -> bool
        isBound(self, unit: int) -> bool
        """
        return False

    def isCreated(self): # real signature unknown; restored from __doc__
        """ isCreated(self) -> bool """
        return False

    def isFixedSamplePositions(self): # real signature unknown; restored from __doc__
        """ isFixedSamplePositions(self) -> bool """
        return False

    def isStorageAllocated(self): # real signature unknown; restored from __doc__
        """ isStorageAllocated(self) -> bool """
        return False

    def isTextureView(self): # real signature unknown; restored from __doc__
        """ isTextureView(self) -> bool """
        return False

    def layers(self): # real signature unknown; restored from __doc__
        """ layers(self) -> int """
        return 0

    def levelofDetailBias(self): # real signature unknown; restored from __doc__
        """ levelofDetailBias(self) -> float """
        return 0.0

    def levelOfDetailRange(self): # real signature unknown; restored from __doc__
        """ levelOfDetailRange(self) -> typing.Tuple[float, float] """
        pass

    def magnificationFilter(self): # real signature unknown; restored from __doc__
        """ magnificationFilter(self) -> PySide2.QtGui.QOpenGLTexture.Filter """
        pass

    def maximumAnisotropy(self): # real signature unknown; restored from __doc__
        """ maximumAnisotropy(self) -> float """
        return 0.0

    def maximumLevelOfDetail(self): # real signature unknown; restored from __doc__
        """ maximumLevelOfDetail(self) -> float """
        return 0.0

    def maximumMipLevels(self): # real signature unknown; restored from __doc__
        """ maximumMipLevels(self) -> int """
        return 0

    def minificationFilter(self): # real signature unknown; restored from __doc__
        """ minificationFilter(self) -> PySide2.QtGui.QOpenGLTexture.Filter """
        pass

    def minimumLevelOfDetail(self): # real signature unknown; restored from __doc__
        """ minimumLevelOfDetail(self) -> float """
        return 0.0

    def minMagFilters(self): # real signature unknown; restored from __doc__
        """ minMagFilters(self) -> typing.Tuple[PySide2.QtGui.QOpenGLTexture.Filter, PySide2.QtGui.QOpenGLTexture.Filter] """
        pass

    def mipBaseLevel(self): # real signature unknown; restored from __doc__
        """ mipBaseLevel(self) -> int """
        return 0

    def mipLevelRange(self): # real signature unknown; restored from __doc__
        """ mipLevelRange(self) -> typing.Tuple[int, int] """
        pass

    def mipLevels(self): # real signature unknown; restored from __doc__
        """ mipLevels(self) -> int """
        return 0

    def mipMaxLevel(self): # real signature unknown; restored from __doc__
        """ mipMaxLevel(self) -> int """
        return 0

    def release(self): # real signature unknown; restored from __doc__
        """
        release(self) -> None
        release(self, unit: int, reset: PySide2.QtGui.QOpenGLTexture.TextureUnitReset = PySide2.QtGui.QOpenGLTexture.TextureUnitReset.DontResetTextureUnit) -> None
        """
        pass

    def samples(self): # real signature unknown; restored from __doc__
        """ samples(self) -> int """
        return 0

    def setAutoMipMapGenerationEnabled(self, enabled): # real signature unknown; restored from __doc__
        """ setAutoMipMapGenerationEnabled(self, enabled: bool) -> None """
        pass

    def setBorderColor(self, color): # real signature unknown; restored from __doc__
        """
        setBorderColor(self, color: PySide2.QtGui.QColor) -> None
        setBorderColor(self, r: float, g: float, b: float, a: float) -> None
        setBorderColor(self, r: int, g: int, b: int, a: int) -> None
        setBorderColor(self, r: int, g: int, b: int, a: int) -> None
        """
        pass

    def setComparisonFunction(self, function): # real signature unknown; restored from __doc__
        """ setComparisonFunction(self, function: PySide2.QtGui.QOpenGLTexture.ComparisonFunction) -> None """
        pass

    def setComparisonMode(self, mode): # real signature unknown; restored from __doc__
        """ setComparisonMode(self, mode: PySide2.QtGui.QOpenGLTexture.ComparisonMode) -> None """
        pass

    def setCompressedData(self, dataSize, data, options, PySide2_QtGui_QOpenGLPixelTransferOptions=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        setCompressedData(self, dataSize: int, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setCompressedData(self, mipLevel: int, dataSize: int, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setCompressedData(self, mipLevel: int, layer: int, cubeFace: PySide2.QtGui.QOpenGLTexture.CubeMapFace, dataSize: int, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setCompressedData(self, mipLevel: int, layer: int, dataSize: int, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setCompressedData(self, mipLevel: int, layer: int, layerCount: int, cubeFace: PySide2.QtGui.QOpenGLTexture.CubeMapFace, dataSize: int, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        """
        pass

    def setData(self, image, genMipMaps=None): # real signature unknown; restored from __doc__
        """
        setData(self, image: PySide2.QtGui.QImage, genMipMaps: PySide2.QtGui.QOpenGLTexture.MipMapGeneration = PySide2.QtGui.QOpenGLTexture.MipMapGeneration.GenerateMipMaps) -> None
        setData(self, mipLevel: int, layer: int, cubeFace: PySide2.QtGui.QOpenGLTexture.CubeMapFace, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setData(self, mipLevel: int, layer: int, layerCount: int, cubeFace: PySide2.QtGui.QOpenGLTexture.CubeMapFace, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setData(self, mipLevel: int, layer: int, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setData(self, mipLevel: int, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setData(self, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setData(self, xOffset: int, yOffset: int, zOffset: int, width: int, height: int, depth: int, mipLevel: int, layer: int, cubeFace: PySide2.QtGui.QOpenGLTexture.CubeMapFace, layerCount: int, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setData(self, xOffset: int, yOffset: int, zOffset: int, width: int, height: int, depth: int, mipLevel: int, layer: int, cubeFace: PySide2.QtGui.QOpenGLTexture.CubeMapFace, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setData(self, xOffset: int, yOffset: int, zOffset: int, width: int, height: int, depth: int, mipLevel: int, layer: int, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        setData(self, xOffset: int, yOffset: int, zOffset: int, width: int, height: int, depth: int, sourceFormat: PySide2.QtGui.QOpenGLTexture.PixelFormat, sourceType: PySide2.QtGui.QOpenGLTexture.PixelType, data: int, options: typing.Optional[PySide2.QtGui.QOpenGLPixelTransferOptions] = None) -> None
        """
        pass

    def setDepthStencilMode(self, mode): # real signature unknown; restored from __doc__
        """ setDepthStencilMode(self, mode: PySide2.QtGui.QOpenGLTexture.DepthStencilMode) -> None """
        pass

    def setFixedSamplePositions(self, fixed): # real signature unknown; restored from __doc__
        """ setFixedSamplePositions(self, fixed: bool) -> None """
        pass

    def setFormat(self, format): # real signature unknown; restored from __doc__
        """ setFormat(self, format: PySide2.QtGui.QOpenGLTexture.TextureFormat) -> None """
        pass

    def setLayers(self, layers): # real signature unknown; restored from __doc__
        """ setLayers(self, layers: int) -> None """
        pass

    def setLevelofDetailBias(self, bias): # real signature unknown; restored from __doc__
        """ setLevelofDetailBias(self, bias: float) -> None """
        pass

    def setLevelOfDetailRange(self, min, max): # real signature unknown; restored from __doc__
        """ setLevelOfDetailRange(self, min: float, max: float) -> None """
        pass

    def setMagnificationFilter(self, filter): # real signature unknown; restored from __doc__
        """ setMagnificationFilter(self, filter: PySide2.QtGui.QOpenGLTexture.Filter) -> None """
        pass

    def setMaximumAnisotropy(self, anisotropy): # real signature unknown; restored from __doc__
        """ setMaximumAnisotropy(self, anisotropy: float) -> None """
        pass

    def setMaximumLevelOfDetail(self, value): # real signature unknown; restored from __doc__
        """ setMaximumLevelOfDetail(self, value: float) -> None """
        pass

    def setMinificationFilter(self, filter): # real signature unknown; restored from __doc__
        """ setMinificationFilter(self, filter: PySide2.QtGui.QOpenGLTexture.Filter) -> None """
        pass

    def setMinimumLevelOfDetail(self, value): # real signature unknown; restored from __doc__
        """ setMinimumLevelOfDetail(self, value: float) -> None """
        pass

    def setMinMagFilters(self, minificationFilter, magnificationFilter): # real signature unknown; restored from __doc__
        """ setMinMagFilters(self, minificationFilter: PySide2.QtGui.QOpenGLTexture.Filter, magnificationFilter: PySide2.QtGui.QOpenGLTexture.Filter) -> None """
        pass

    def setMipBaseLevel(self, baseLevel): # real signature unknown; restored from __doc__
        """ setMipBaseLevel(self, baseLevel: int) -> None """
        pass

    def setMipLevelRange(self, baseLevel, maxLevel): # real signature unknown; restored from __doc__
        """ setMipLevelRange(self, baseLevel: int, maxLevel: int) -> None """
        pass

    def setMipLevels(self, levels): # real signature unknown; restored from __doc__
        """ setMipLevels(self, levels: int) -> None """
        pass

    def setMipMaxLevel(self, maxLevel): # real signature unknown; restored from __doc__
        """ setMipMaxLevel(self, maxLevel: int) -> None """
        pass

    def setSamples(self, samples): # real signature unknown; restored from __doc__
        """ setSamples(self, samples: int) -> None """
        pass

    def setSize(self, width, height=1, depth=1): # real signature unknown; restored from __doc__
        """ setSize(self, width: int, height: int = 1, depth: int = 1) -> None """
        pass

    def setSwizzleMask(self, component, value): # real signature unknown; restored from __doc__
        """
        setSwizzleMask(self, component: PySide2.QtGui.QOpenGLTexture.SwizzleComponent, value: PySide2.QtGui.QOpenGLTexture.SwizzleValue) -> None
        setSwizzleMask(self, r: PySide2.QtGui.QOpenGLTexture.SwizzleValue, g: PySide2.QtGui.QOpenGLTexture.SwizzleValue, b: PySide2.QtGui.QOpenGLTexture.SwizzleValue, a: PySide2.QtGui.QOpenGLTexture.SwizzleValue) -> None
        """
        pass

    def setWrapMode(self, direction, mode): # real signature unknown; restored from __doc__
        """
        setWrapMode(self, direction: PySide2.QtGui.QOpenGLTexture.CoordinateDirection, mode: PySide2.QtGui.QOpenGLTexture.WrapMode) -> None
        setWrapMode(self, mode: PySide2.QtGui.QOpenGLTexture.WrapMode) -> None
        """
        pass

    def swizzleMask(self, component): # real signature unknown; restored from __doc__
        """ swizzleMask(self, component: PySide2.QtGui.QOpenGLTexture.SwizzleComponent) -> PySide2.QtGui.QOpenGLTexture.SwizzleValue """
        pass

    def target(self): # real signature unknown; restored from __doc__
        """ target(self) -> PySide2.QtGui.QOpenGLTexture.Target """
        pass

    def textureId(self): # real signature unknown; restored from __doc__
        """ textureId(self) -> int """
        return 0

    def width(self): # real signature unknown; restored from __doc__
        """ width(self) -> int """
        return 0

    def wrapMode(self, direction): # real signature unknown; restored from __doc__
        """ wrapMode(self, direction: PySide2.QtGui.QOpenGLTexture.CoordinateDirection) -> PySide2.QtGui.QOpenGLTexture.WrapMode """
        pass

    def __init__(self, image, genMipMaps=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    Alpha = PySide2.QtGui.QOpenGLTexture.PixelFormat.Alpha
    AlphaFormat = PySide2.QtGui.QOpenGLTexture.TextureFormat.AlphaFormat
    AlphaValue = PySide2.QtGui.QOpenGLTexture.SwizzleValue.AlphaValue
    AnisotropicFiltering = PySide2.QtGui.QOpenGLTexture.Feature.AnisotropicFiltering
    BGR = PySide2.QtGui.QOpenGLTexture.PixelFormat.BGR
    BGRA = PySide2.QtGui.QOpenGLTexture.PixelFormat.BGRA
    BGRA_Integer = PySide2.QtGui.QOpenGLTexture.PixelFormat.BGRA_Integer
    BGR_Integer = PySide2.QtGui.QOpenGLTexture.PixelFormat.BGR_Integer
    BindingTarget = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.BindingTarget'>"
    BindingTarget1D = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTarget1D
    BindingTarget1DArray = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTarget1DArray
    BindingTarget2D = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTarget2D
    BindingTarget2DArray = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTarget2DArray
    BindingTarget2DMultisample = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTarget2DMultisample
    BindingTarget2DMultisampleArray = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTarget2DMultisampleArray
    BindingTarget3D = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTarget3D
    BindingTargetBuffer = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTargetBuffer
    BindingTargetCubeMap = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTargetCubeMap
    BindingTargetCubeMapArray = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTargetCubeMapArray
    BindingTargetRectangle = PySide2.QtGui.QOpenGLTexture.BindingTarget.BindingTargetRectangle
    BlueValue = PySide2.QtGui.QOpenGLTexture.SwizzleValue.BlueValue
    ClampToBorder = PySide2.QtGui.QOpenGLTexture.WrapMode.ClampToBorder
    ClampToEdge = PySide2.QtGui.QOpenGLTexture.WrapMode.ClampToEdge
    CommpareNotEqual = PySide2.QtGui.QOpenGLTexture.ComparisonFunction.CommpareNotEqual
    CompareAlways = PySide2.QtGui.QOpenGLTexture.ComparisonFunction.CompareAlways
    CompareEqual = PySide2.QtGui.QOpenGLTexture.ComparisonFunction.CompareEqual
    CompareGreater = PySide2.QtGui.QOpenGLTexture.ComparisonFunction.CompareGreater
    CompareGreaterEqual = PySide2.QtGui.QOpenGLTexture.ComparisonFunction.CompareGreaterEqual
    CompareLess = PySide2.QtGui.QOpenGLTexture.ComparisonFunction.CompareLess
    CompareLessEqual = PySide2.QtGui.QOpenGLTexture.ComparisonFunction.CompareLessEqual
    CompareNever = PySide2.QtGui.QOpenGLTexture.ComparisonFunction.CompareNever
    CompareNone = PySide2.QtGui.QOpenGLTexture.ComparisonMode.CompareNone
    CompareRefToTexture = PySide2.QtGui.QOpenGLTexture.ComparisonMode.CompareRefToTexture
    ComparisonFunction = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.ComparisonFunction'>"
    ComparisonMode = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.ComparisonMode'>"
    CoordinateDirection = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.CoordinateDirection'>"
    CubeMapFace = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.CubeMapFace'>"
    CubeMapNegativeX = PySide2.QtGui.QOpenGLTexture.CubeMapFace.CubeMapNegativeX
    CubeMapNegativeY = PySide2.QtGui.QOpenGLTexture.CubeMapFace.CubeMapNegativeY
    CubeMapNegativeZ = PySide2.QtGui.QOpenGLTexture.CubeMapFace.CubeMapNegativeZ
    CubeMapPositiveX = PySide2.QtGui.QOpenGLTexture.CubeMapFace.CubeMapPositiveX
    CubeMapPositiveY = PySide2.QtGui.QOpenGLTexture.CubeMapFace.CubeMapPositiveY
    CubeMapPositiveZ = PySide2.QtGui.QOpenGLTexture.CubeMapFace.CubeMapPositiveZ
    D16 = PySide2.QtGui.QOpenGLTexture.TextureFormat.D16
    D24 = PySide2.QtGui.QOpenGLTexture.TextureFormat.D24
    D24S8 = PySide2.QtGui.QOpenGLTexture.TextureFormat.D24S8
    D32 = PySide2.QtGui.QOpenGLTexture.TextureFormat.D32
    D32F = PySide2.QtGui.QOpenGLTexture.TextureFormat.D32F
    D32FS8X24 = PySide2.QtGui.QOpenGLTexture.TextureFormat.D32FS8X24
    Depth = PySide2.QtGui.QOpenGLTexture.PixelFormat.Depth
    DepthFormat = PySide2.QtGui.QOpenGLTexture.TextureFormat.DepthFormat
    DepthMode = PySide2.QtGui.QOpenGLTexture.DepthStencilMode.DepthMode
    DepthStencil = PySide2.QtGui.QOpenGLTexture.PixelFormat.DepthStencil
    DepthStencilMode = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.DepthStencilMode'>"
    DirectionR = PySide2.QtGui.QOpenGLTexture.CoordinateDirection.DirectionR
    DirectionS = PySide2.QtGui.QOpenGLTexture.CoordinateDirection.DirectionS
    DirectionT = PySide2.QtGui.QOpenGLTexture.CoordinateDirection.DirectionT
    DontGenerateMipMaps = PySide2.QtGui.QOpenGLTexture.MipMapGeneration.DontGenerateMipMaps
    DontResetTextureUnit = PySide2.QtGui.QOpenGLTexture.TextureUnitReset.DontResetTextureUnit
    Feature = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.Feature'>"
    Features = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.Features'>"
    Filter = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.Filter'>"
    Float16 = PySide2.QtGui.QOpenGLTexture.PixelType.Float16
    Float16OES = PySide2.QtGui.QOpenGLTexture.PixelType.Float16OES
    Float32 = PySide2.QtGui.QOpenGLTexture.PixelType.Float32
    Float32_D32_UInt32_S8_X24 = PySide2.QtGui.QOpenGLTexture.PixelType.Float32_D32_UInt32_S8_X24
    FormatClass_128Bit = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_128Bit
    FormatClass_16Bit = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_16Bit
    FormatClass_24Bit = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_24Bit
    FormatClass_32Bit = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_32Bit
    FormatClass_48Bit = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_48Bit
    FormatClass_64Bit = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_64Bit
    FormatClass_8Bit = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_8Bit
    FormatClass_96Bit = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_96Bit
    FormatClass_BPTC_Float = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_BPTC_Float
    FormatClass_BPTC_Unorm = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_BPTC_Unorm
    FormatClass_RGTC1_R = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_RGTC1_R
    FormatClass_RGTC2_RG = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_RGTC2_RG
    FormatClass_S3TC_DXT1_RGB = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_S3TC_DXT1_RGB
    FormatClass_S3TC_DXT1_RGBA = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_S3TC_DXT1_RGBA
    FormatClass_S3TC_DXT3_RGBA = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_S3TC_DXT3_RGBA
    FormatClass_S3TC_DXT5_RGBA = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_S3TC_DXT5_RGBA
    FormatClass_Unique = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.FormatClass_Unique
    GenerateMipMaps = PySide2.QtGui.QOpenGLTexture.MipMapGeneration.GenerateMipMaps
    GreenValue = PySide2.QtGui.QOpenGLTexture.SwizzleValue.GreenValue
    ImmutableMultisampleStorage = PySide2.QtGui.QOpenGLTexture.Feature.ImmutableMultisampleStorage
    ImmutableStorage = PySide2.QtGui.QOpenGLTexture.Feature.ImmutableStorage
    Int16 = PySide2.QtGui.QOpenGLTexture.PixelType.Int16
    Int32 = PySide2.QtGui.QOpenGLTexture.PixelType.Int32
    Int8 = PySide2.QtGui.QOpenGLTexture.PixelType.Int8
    Linear = PySide2.QtGui.QOpenGLTexture.Filter.Linear
    LinearMipMapLinear = PySide2.QtGui.QOpenGLTexture.Filter.LinearMipMapLinear
    LinearMipMapNearest = PySide2.QtGui.QOpenGLTexture.Filter.LinearMipMapNearest
    Luminance = PySide2.QtGui.QOpenGLTexture.PixelFormat.Luminance
    LuminanceAlpha = PySide2.QtGui.QOpenGLTexture.PixelFormat.LuminanceAlpha
    LuminanceAlphaFormat = PySide2.QtGui.QOpenGLTexture.TextureFormat.LuminanceAlphaFormat
    LuminanceFormat = PySide2.QtGui.QOpenGLTexture.TextureFormat.LuminanceFormat
    MaxFeatureFlag = PySide2.QtGui.QOpenGLTexture.Feature.MaxFeatureFlag
    MipMapGeneration = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.MipMapGeneration'>"
    MirroredRepeat = PySide2.QtGui.QOpenGLTexture.WrapMode.MirroredRepeat
    Nearest = PySide2.QtGui.QOpenGLTexture.Filter.Nearest
    NearestMipMapLinear = PySide2.QtGui.QOpenGLTexture.Filter.NearestMipMapLinear
    NearestMipMapNearest = PySide2.QtGui.QOpenGLTexture.Filter.NearestMipMapNearest
    NoFormat = PySide2.QtGui.QOpenGLTexture.TextureFormat.NoFormat
    NoFormatClass = PySide2.QtGui.QOpenGLTexture.TextureFormatClass.NoFormatClass
    NoPixelType = PySide2.QtGui.QOpenGLTexture.PixelType.NoPixelType
    NoSourceFormat = PySide2.QtGui.QOpenGLTexture.PixelFormat.NoSourceFormat
    NPOTTextureRepeat = PySide2.QtGui.QOpenGLTexture.Feature.NPOTTextureRepeat
    NPOTTextures = PySide2.QtGui.QOpenGLTexture.Feature.NPOTTextures
    OneValue = PySide2.QtGui.QOpenGLTexture.SwizzleValue.OneValue
    PixelFormat = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.PixelFormat'>"
    PixelType = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.PixelType'>"
    R11_EAC_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.R11_EAC_SNorm
    R11_EAC_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.R11_EAC_UNorm
    R16F = PySide2.QtGui.QOpenGLTexture.TextureFormat.R16F
    R16I = PySide2.QtGui.QOpenGLTexture.TextureFormat.R16I
    R16U = PySide2.QtGui.QOpenGLTexture.TextureFormat.R16U
    R16_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.R16_SNorm
    R16_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.R16_UNorm
    R32F = PySide2.QtGui.QOpenGLTexture.TextureFormat.R32F
    R32I = PySide2.QtGui.QOpenGLTexture.TextureFormat.R32I
    R32U = PySide2.QtGui.QOpenGLTexture.TextureFormat.R32U
    R5G6B5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.R5G6B5
    R8I = PySide2.QtGui.QOpenGLTexture.TextureFormat.R8I
    R8U = PySide2.QtGui.QOpenGLTexture.TextureFormat.R8U
    R8_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.R8_SNorm
    R8_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.R8_UNorm
    Red = PySide2.QtGui.QOpenGLTexture.PixelFormat.Red
    RedValue = PySide2.QtGui.QOpenGLTexture.SwizzleValue.RedValue
    Red_Integer = PySide2.QtGui.QOpenGLTexture.PixelFormat.Red_Integer
    Repeat = PySide2.QtGui.QOpenGLTexture.WrapMode.Repeat
    ResetTextureUnit = PySide2.QtGui.QOpenGLTexture.TextureUnitReset.ResetTextureUnit
    RG = PySide2.QtGui.QOpenGLTexture.PixelFormat.RG
    RG11B10F = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG11B10F
    RG11_EAC_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG11_EAC_SNorm
    RG11_EAC_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG11_EAC_UNorm
    RG16F = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG16F
    RG16I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG16I
    RG16U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG16U
    RG16_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG16_SNorm
    RG16_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG16_UNorm
    RG32F = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG32F
    RG32I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG32I
    RG32U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG32U
    RG3B2 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG3B2
    RG8I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG8I
    RG8U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG8U
    RG8_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG8_SNorm
    RG8_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG8_UNorm
    RGB = PySide2.QtGui.QOpenGLTexture.PixelFormat.RGB
    RGB10A2 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB10A2
    RGB16F = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB16F
    RGB16I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB16I
    RGB16U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB16U
    RGB16_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB16_SNorm
    RGB16_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB16_UNorm
    RGB32F = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB32F
    RGB32I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB32I
    RGB32U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB32U
    RGB5A1 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB5A1
    RGB8I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB8I
    RGB8U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB8U
    RGB8_ETC1 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB8_ETC1
    RGB8_ETC2 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB8_ETC2
    RGB8_PunchThrough_Alpha1_ETC2 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB8_PunchThrough_Alpha1_ETC2
    RGB8_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB8_SNorm
    RGB8_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB8_UNorm
    RGB9E5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB9E5
    RGBA = PySide2.QtGui.QOpenGLTexture.PixelFormat.RGBA
    RGBA16F = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA16F
    RGBA16I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA16I
    RGBA16U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA16U
    RGBA16_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA16_SNorm
    RGBA16_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA16_UNorm
    RGBA32F = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA32F
    RGBA32I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA32I
    RGBA32U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA32U
    RGBA4 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA4
    RGBA8I = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA8I
    RGBA8U = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA8U
    RGBA8_ETC2_EAC = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA8_ETC2_EAC
    RGBA8_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA8_SNorm
    RGBA8_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA8_UNorm
    RGBAFormat = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBAFormat
    RGBA_ASTC_10x10 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_10x10
    RGBA_ASTC_10x5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_10x5
    RGBA_ASTC_10x6 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_10x6
    RGBA_ASTC_10x8 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_10x8
    RGBA_ASTC_12x10 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_12x10
    RGBA_ASTC_12x12 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_12x12
    RGBA_ASTC_4x4 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_4x4
    RGBA_ASTC_5x4 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_5x4
    RGBA_ASTC_5x5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_5x5
    RGBA_ASTC_6x5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_6x5
    RGBA_ASTC_6x6 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_6x6
    RGBA_ASTC_8x5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_8x5
    RGBA_ASTC_8x6 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_8x6
    RGBA_ASTC_8x8 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_ASTC_8x8
    RGBA_DXT1 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_DXT1
    RGBA_DXT3 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_DXT3
    RGBA_DXT5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBA_DXT5
    RGBA_Integer = PySide2.QtGui.QOpenGLTexture.PixelFormat.RGBA_Integer
    RGBFormat = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGBFormat
    RGB_BP_SIGNED_FLOAT = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB_BP_SIGNED_FLOAT
    RGB_BP_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB_BP_UNorm
    RGB_BP_UNSIGNED_FLOAT = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB_BP_UNSIGNED_FLOAT
    RGB_DXT1 = PySide2.QtGui.QOpenGLTexture.TextureFormat.RGB_DXT1
    RGB_Integer = PySide2.QtGui.QOpenGLTexture.PixelFormat.RGB_Integer
    RG_ATI2N_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG_ATI2N_SNorm
    RG_ATI2N_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.RG_ATI2N_UNorm
    RG_Integer = PySide2.QtGui.QOpenGLTexture.PixelFormat.RG_Integer
    R_ATI1N_SNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.R_ATI1N_SNorm
    R_ATI1N_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.R_ATI1N_UNorm
    S8 = PySide2.QtGui.QOpenGLTexture.TextureFormat.S8
    SRGB8 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8
    SRGB8_Alpha8 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8
    SRGB8_Alpha8_ASTC_10x10 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_10x10
    SRGB8_Alpha8_ASTC_10x5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_10x5
    SRGB8_Alpha8_ASTC_10x6 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_10x6
    SRGB8_Alpha8_ASTC_10x8 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_10x8
    SRGB8_Alpha8_ASTC_12x10 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_12x10
    SRGB8_Alpha8_ASTC_12x12 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_12x12
    SRGB8_Alpha8_ASTC_4x4 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_4x4
    SRGB8_Alpha8_ASTC_5x4 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_5x4
    SRGB8_Alpha8_ASTC_5x5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_5x5
    SRGB8_Alpha8_ASTC_6x5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_6x5
    SRGB8_Alpha8_ASTC_6x6 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_6x6
    SRGB8_Alpha8_ASTC_8x5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_8x5
    SRGB8_Alpha8_ASTC_8x6 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_8x6
    SRGB8_Alpha8_ASTC_8x8 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ASTC_8x8
    SRGB8_Alpha8_ETC2_EAC = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_Alpha8_ETC2_EAC
    SRGB8_ETC2 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_ETC2
    SRGB8_PunchThrough_Alpha1_ETC2 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB8_PunchThrough_Alpha1_ETC2
    SRGB_Alpha_DXT1 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB_Alpha_DXT1
    SRGB_Alpha_DXT3 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB_Alpha_DXT3
    SRGB_Alpha_DXT5 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB_Alpha_DXT5
    SRGB_BP_UNorm = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB_BP_UNorm
    SRGB_DXT1 = PySide2.QtGui.QOpenGLTexture.TextureFormat.SRGB_DXT1
    Stencil = PySide2.QtGui.QOpenGLTexture.PixelFormat.Stencil
    StencilMode = PySide2.QtGui.QOpenGLTexture.DepthStencilMode.StencilMode
    StencilTexturing = PySide2.QtGui.QOpenGLTexture.Feature.StencilTexturing
    Swizzle = PySide2.QtGui.QOpenGLTexture.Feature.Swizzle
    SwizzleAlpha = PySide2.QtGui.QOpenGLTexture.SwizzleComponent.SwizzleAlpha
    SwizzleBlue = PySide2.QtGui.QOpenGLTexture.SwizzleComponent.SwizzleBlue
    SwizzleComponent = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.SwizzleComponent'>"
    SwizzleGreen = PySide2.QtGui.QOpenGLTexture.SwizzleComponent.SwizzleGreen
    SwizzleRed = PySide2.QtGui.QOpenGLTexture.SwizzleComponent.SwizzleRed
    SwizzleValue = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.SwizzleValue'>"
    Target = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.Target'>"
    Target1D = PySide2.QtGui.QOpenGLTexture.Target.Target1D
    Target1DArray = PySide2.QtGui.QOpenGLTexture.Target.Target1DArray
    Target2D = PySide2.QtGui.QOpenGLTexture.Target.Target2D
    Target2DArray = PySide2.QtGui.QOpenGLTexture.Target.Target2DArray
    Target2DMultisample = PySide2.QtGui.QOpenGLTexture.Target.Target2DMultisample
    Target2DMultisampleArray = PySide2.QtGui.QOpenGLTexture.Target.Target2DMultisampleArray
    Target3D = PySide2.QtGui.QOpenGLTexture.Target.Target3D
    TargetBuffer = PySide2.QtGui.QOpenGLTexture.Target.TargetBuffer
    TargetCubeMap = PySide2.QtGui.QOpenGLTexture.Target.TargetCubeMap
    TargetCubeMapArray = PySide2.QtGui.QOpenGLTexture.Target.TargetCubeMapArray
    TargetRectangle = PySide2.QtGui.QOpenGLTexture.Target.TargetRectangle
    Texture1D = PySide2.QtGui.QOpenGLTexture.Feature.Texture1D
    Texture3D = PySide2.QtGui.QOpenGLTexture.Feature.Texture3D
    TextureArrays = PySide2.QtGui.QOpenGLTexture.Feature.TextureArrays
    TextureBuffer = PySide2.QtGui.QOpenGLTexture.Feature.TextureBuffer
    TextureComparisonOperators = PySide2.QtGui.QOpenGLTexture.Feature.TextureComparisonOperators
    TextureCubeMapArrays = PySide2.QtGui.QOpenGLTexture.Feature.TextureCubeMapArrays
    TextureFormat = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.TextureFormat'>"
    TextureFormatClass = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.TextureFormatClass'>"
    TextureMipMapLevel = PySide2.QtGui.QOpenGLTexture.Feature.TextureMipMapLevel
    TextureMultisample = PySide2.QtGui.QOpenGLTexture.Feature.TextureMultisample
    TextureRectangle = PySide2.QtGui.QOpenGLTexture.Feature.TextureRectangle
    TextureUnitReset = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.TextureUnitReset'>"
    UInt16 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt16
    UInt16_R5G6B5 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt16_R5G6B5
    UInt16_R5G6B5_Rev = PySide2.QtGui.QOpenGLTexture.PixelType.UInt16_R5G6B5_Rev
    UInt16_RGB5A1 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt16_RGB5A1
    UInt16_RGB5A1_Rev = PySide2.QtGui.QOpenGLTexture.PixelType.UInt16_RGB5A1_Rev
    UInt16_RGBA4 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt16_RGBA4
    UInt16_RGBA4_Rev = PySide2.QtGui.QOpenGLTexture.PixelType.UInt16_RGBA4_Rev
    UInt32 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt32
    UInt32_D24S8 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt32_D24S8
    UInt32_RG11B10F = PySide2.QtGui.QOpenGLTexture.PixelType.UInt32_RG11B10F
    UInt32_RGB10A2 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt32_RGB10A2
    UInt32_RGB10A2_Rev = PySide2.QtGui.QOpenGLTexture.PixelType.UInt32_RGB10A2_Rev
    UInt32_RGB9_E5 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt32_RGB9_E5
    UInt32_RGBA8 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt32_RGBA8
    UInt32_RGBA8_Rev = PySide2.QtGui.QOpenGLTexture.PixelType.UInt32_RGBA8_Rev
    UInt8 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt8
    UInt8_RG3B2 = PySide2.QtGui.QOpenGLTexture.PixelType.UInt8_RG3B2
    UInt8_RG3B2_Rev = PySide2.QtGui.QOpenGLTexture.PixelType.UInt8_RG3B2_Rev
    WrapMode = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLTexture.WrapMode'>"
    ZeroValue = PySide2.QtGui.QOpenGLTexture.SwizzleValue.ZeroValue


