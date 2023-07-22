# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


from .QOpenGLFunctions import QOpenGLFunctions

class QOpenGLExtraFunctions(QOpenGLFunctions):
    """
    QOpenGLExtraFunctions(self) -> None
    QOpenGLExtraFunctions(self, context: PySide2.QtGui.QOpenGLContext) -> None
    """
    def glActiveShaderProgram(self, pipeline, program): # real signature unknown; restored from __doc__
        """ glActiveShaderProgram(self, pipeline: int, program: int) -> None """
        pass

    def glBeginQuery(self, target, id): # real signature unknown; restored from __doc__
        """ glBeginQuery(self, target: int, id: int) -> None """
        pass

    def glBeginTransformFeedback(self, primitiveMode): # real signature unknown; restored from __doc__
        """ glBeginTransformFeedback(self, primitiveMode: int) -> None """
        pass

    def glBindBufferBase(self, target, index, buffer): # real signature unknown; restored from __doc__
        """ glBindBufferBase(self, target: int, index: int, buffer: int) -> None """
        pass

    def glBindImageTexture(self, unit, texture, level, layered, layer, access, format): # real signature unknown; restored from __doc__
        """ glBindImageTexture(self, unit: int, texture: int, level: int, layered: int, layer: int, access: int, format: int) -> None """
        pass

    def glBindProgramPipeline(self, pipeline): # real signature unknown; restored from __doc__
        """ glBindProgramPipeline(self, pipeline: int) -> None """
        pass

    def glBindSampler(self, unit, sampler): # real signature unknown; restored from __doc__
        """ glBindSampler(self, unit: int, sampler: int) -> None """
        pass

    def glBindTransformFeedback(self, target, id): # real signature unknown; restored from __doc__
        """ glBindTransformFeedback(self, target: int, id: int) -> None """
        pass

    def glBindVertexArray(self, array): # real signature unknown; restored from __doc__
        """ glBindVertexArray(self, array: int) -> None """
        pass

    def glBlendBarrier(self): # real signature unknown; restored from __doc__
        """ glBlendBarrier(self) -> None """
        pass

    def glBlendEquationi(self, buf, mode): # real signature unknown; restored from __doc__
        """ glBlendEquationi(self, buf: int, mode: int) -> None """
        pass

    def glBlendEquationSeparatei(self, buf, modeRGB, modeAlpha): # real signature unknown; restored from __doc__
        """ glBlendEquationSeparatei(self, buf: int, modeRGB: int, modeAlpha: int) -> None """
        pass

    def glBlendFunci(self, buf, src, dst): # real signature unknown; restored from __doc__
        """ glBlendFunci(self, buf: int, src: int, dst: int) -> None """
        pass

    def glBlendFuncSeparatei(self, buf, srcRGB, dstRGB, srcAlpha, dstAlpha): # real signature unknown; restored from __doc__
        """ glBlendFuncSeparatei(self, buf: int, srcRGB: int, dstRGB: int, srcAlpha: int, dstAlpha: int) -> None """
        pass

    def glBlitFramebuffer(self, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter): # real signature unknown; restored from __doc__
        """ glBlitFramebuffer(self, srcX0: int, srcY0: int, srcX1: int, srcY1: int, dstX0: int, dstY0: int, dstX1: int, dstY1: int, mask: int, filter: int) -> None """
        pass

    def glClearBufferfi(self, buffer, drawbuffer, depth, stencil): # real signature unknown; restored from __doc__
        """ glClearBufferfi(self, buffer: int, drawbuffer: int, depth: float, stencil: int) -> None """
        pass

    def glClearBufferfv(self, buffer, drawbuffer, value, p_float=None): # real signature unknown; restored from __doc__
        """ glClearBufferfv(self, buffer: int, drawbuffer: int, value: typing.Sequence[float]) -> None """
        pass

    def glClearBufferiv(self, buffer, drawbuffer, value, p_int=None): # real signature unknown; restored from __doc__
        """ glClearBufferiv(self, buffer: int, drawbuffer: int, value: typing.Sequence[int]) -> None """
        pass

    def glClearBufferuiv(self, buffer, drawbuffer, value, p_int=None): # real signature unknown; restored from __doc__
        """ glClearBufferuiv(self, buffer: int, drawbuffer: int, value: typing.Sequence[int]) -> None """
        pass

    def glColorMaski(self, index, r, g, b, a): # real signature unknown; restored from __doc__
        """ glColorMaski(self, index: int, r: int, g: int, b: int, a: int) -> None """
        pass

    def glCompressedTexImage3D(self, target, level, internalformat, width, height, depth, border, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexImage3D(self, target: int, level: int, internalformat: int, width: int, height: int, depth: int, border: int, imageSize: int, data: int) -> None """
        pass

    def glCompressedTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, format: int, imageSize: int, data: int) -> None """
        pass

    def glCopyImageSubData(self, srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth): # real signature unknown; restored from __doc__
        """ glCopyImageSubData(self, srcName: int, srcTarget: int, srcLevel: int, srcX: int, srcY: int, srcZ: int, dstName: int, dstTarget: int, dstLevel: int, dstX: int, dstY: int, dstZ: int, srcWidth: int, srcHeight: int, srcDepth: int) -> None """
        pass

    def glCopyTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, x, y, width, height): # real signature unknown; restored from __doc__
        """ glCopyTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, x: int, y: int, width: int, height: int) -> None """
        pass

    def glDebugMessageControl(self, source, type, severity, count, ids, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ glDebugMessageControl(self, source: int, type: int, severity: int, count: int, ids: typing.Sequence[int], enabled: int) -> None """
        pass

    def glDebugMessageInsert(self, source, type, id, severity, length, buf): # real signature unknown; restored from __doc__
        """ glDebugMessageInsert(self, source: int, type: int, id: int, severity: int, length: int, buf: bytes) -> None """
        pass

    def glDeleteProgramPipelines(self, n, pipelines, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteProgramPipelines(self, n: int, pipelines: typing.Sequence[int]) -> None """
        pass

    def glDeleteQueries(self, n, ids, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteQueries(self, n: int, ids: typing.Sequence[int]) -> None """
        pass

    def glDeleteSamplers(self, count, samplers, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteSamplers(self, count: int, samplers: typing.Sequence[int]) -> None """
        pass

    def glDeleteTransformFeedbacks(self, n, ids, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteTransformFeedbacks(self, n: int, ids: typing.Sequence[int]) -> None """
        pass

    def glDeleteVertexArrays(self, n, arrays, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteVertexArrays(self, n: int, arrays: typing.Sequence[int]) -> None """
        pass

    def glDisablei(self, target, index): # real signature unknown; restored from __doc__
        """ glDisablei(self, target: int, index: int) -> None """
        pass

    def glDispatchCompute(self, num_groups_x, num_groups_y, num_groups_z): # real signature unknown; restored from __doc__
        """ glDispatchCompute(self, num_groups_x: int, num_groups_y: int, num_groups_z: int) -> None """
        pass

    def glDrawArraysIndirect(self, mode, indirect): # real signature unknown; restored from __doc__
        """ glDrawArraysIndirect(self, mode: int, indirect: int) -> None """
        pass

    def glDrawArraysInstanced(self, mode, first, count, instancecount): # real signature unknown; restored from __doc__
        """ glDrawArraysInstanced(self, mode: int, first: int, count: int, instancecount: int) -> None """
        pass

    def glDrawBuffers(self, n, bufs, p_int=None): # real signature unknown; restored from __doc__
        """ glDrawBuffers(self, n: int, bufs: typing.Sequence[int]) -> None """
        pass

    def glDrawElementsBaseVertex(self, mode, count, type, indices, basevertex): # real signature unknown; restored from __doc__
        """ glDrawElementsBaseVertex(self, mode: int, count: int, type: int, indices: int, basevertex: int) -> None """
        pass

    def glDrawElementsIndirect(self, mode, type, indirect): # real signature unknown; restored from __doc__
        """ glDrawElementsIndirect(self, mode: int, type: int, indirect: int) -> None """
        pass

    def glDrawElementsInstanced(self, mode, count, type, indices, instancecount): # real signature unknown; restored from __doc__
        """ glDrawElementsInstanced(self, mode: int, count: int, type: int, indices: int, instancecount: int) -> None """
        pass

    def glDrawElementsInstancedBaseVertex(self, mode, count, type, indices, instancecount, basevertex): # real signature unknown; restored from __doc__
        """ glDrawElementsInstancedBaseVertex(self, mode: int, count: int, type: int, indices: int, instancecount: int, basevertex: int) -> None """
        pass

    def glDrawRangeElements(self, mode, start, end, count, type, indices): # real signature unknown; restored from __doc__
        """ glDrawRangeElements(self, mode: int, start: int, end: int, count: int, type: int, indices: int) -> None """
        pass

    def glDrawRangeElementsBaseVertex(self, mode, start, end, count, type, indices, basevertex): # real signature unknown; restored from __doc__
        """ glDrawRangeElementsBaseVertex(self, mode: int, start: int, end: int, count: int, type: int, indices: int, basevertex: int) -> None """
        pass

    def glEnablei(self, target, index): # real signature unknown; restored from __doc__
        """ glEnablei(self, target: int, index: int) -> None """
        pass

    def glEndQuery(self, target): # real signature unknown; restored from __doc__
        """ glEndQuery(self, target: int) -> None """
        pass

    def glFramebufferParameteri(self, target, pname, param): # real signature unknown; restored from __doc__
        """ glFramebufferParameteri(self, target: int, pname: int, param: int) -> None """
        pass

    def glFramebufferTexture(self, target, attachment, texture, level): # real signature unknown; restored from __doc__
        """ glFramebufferTexture(self, target: int, attachment: int, texture: int, level: int) -> None """
        pass

    def glFramebufferTextureLayer(self, target, attachment, texture, level, layer): # real signature unknown; restored from __doc__
        """ glFramebufferTextureLayer(self, target: int, attachment: int, texture: int, level: int, layer: int) -> None """
        pass

    def glGenProgramPipelines(self, n, pipelines, p_int=None): # real signature unknown; restored from __doc__
        """ glGenProgramPipelines(self, n: int, pipelines: typing.Sequence[int]) -> None """
        pass

    def glGenQueries(self, n, ids, p_int=None): # real signature unknown; restored from __doc__
        """ glGenQueries(self, n: int, ids: typing.Sequence[int]) -> None """
        pass

    def glGenSamplers(self, count, samplers, p_int=None): # real signature unknown; restored from __doc__
        """ glGenSamplers(self, count: int, samplers: typing.Sequence[int]) -> None """
        pass

    def glGenTransformFeedbacks(self, n, ids, p_int=None): # real signature unknown; restored from __doc__
        """ glGenTransformFeedbacks(self, n: int, ids: typing.Sequence[int]) -> None """
        pass

    def glGenVertexArrays(self, n, arrays, p_int=None): # real signature unknown; restored from __doc__
        """ glGenVertexArrays(self, n: int, arrays: typing.Sequence[int]) -> None """
        pass

    def glGetActiveUniformBlockiv(self, program, uniformBlockIndex, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetActiveUniformBlockiv(self, program: int, uniformBlockIndex: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetActiveUniformsiv(self, program, uniformCount, uniformIndices, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ glGetActiveUniformsiv(self, program: int, uniformCount: int, uniformIndices: typing.Sequence[int], pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetBufferParameteri64v(self, target, pname): # real signature unknown; restored from __doc__
        """ glGetBufferParameteri64v(self, target: int, pname: int) -> int """
        return 0

    def glGetFragDataLocation(self, program, name): # real signature unknown; restored from __doc__
        """ glGetFragDataLocation(self, program: int, name: bytes) -> int """
        return 0

    def glGetFramebufferParameteriv(self, target, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetFramebufferParameteriv(self, target: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetGraphicsResetStatus(self): # real signature unknown; restored from __doc__
        """ glGetGraphicsResetStatus(self) -> int """
        return 0

    def glGetInteger64i_v(self, target, index): # real signature unknown; restored from __doc__
        """ glGetInteger64i_v(self, target: int, index: int) -> int """
        return 0

    def glGetInteger64v(self, pname): # real signature unknown; restored from __doc__
        """ glGetInteger64v(self, pname: int) -> int """
        return 0

    def glGetIntegeri_v(self, target, index, data, p_int=None): # real signature unknown; restored from __doc__
        """ glGetIntegeri_v(self, target: int, index: int, data: typing.Sequence[int]) -> None """
        pass

    def glGetInternalformativ(self, target, internalformat, pname, bufSize, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetInternalformativ(self, target: int, internalformat: int, pname: int, bufSize: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetMultisamplefv(self, pname, index, val, p_float=None): # real signature unknown; restored from __doc__
        """ glGetMultisamplefv(self, pname: int, index: int, val: typing.Sequence[float]) -> None """
        pass

    def glGetnUniformfv(self, program, location, bufSize): # real signature unknown; restored from __doc__
        """ glGetnUniformfv(self, program: int, location: int, bufSize: int) -> float """
        return 0.0

    def glGetnUniformiv(self, program, location, bufSize): # real signature unknown; restored from __doc__
        """ glGetnUniformiv(self, program: int, location: int, bufSize: int) -> int """
        return 0

    def glGetnUniformuiv(self, program, location, bufSize): # real signature unknown; restored from __doc__
        """ glGetnUniformuiv(self, program: int, location: int, bufSize: int) -> int """
        return 0

    def glGetProgramBinary(self, program, bufSize, binary): # real signature unknown; restored from __doc__
        """ glGetProgramBinary(self, program: int, bufSize: int, binary: int) -> typing.Tuple[int, int] """
        pass

    def glGetProgramInterfaceiv(self, program, programInterface, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetProgramInterfaceiv(self, program: int, programInterface: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetProgramPipelineiv(self, pipeline, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetProgramPipelineiv(self, pipeline: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetProgramResourceIndex(self, program, programInterface, name): # real signature unknown; restored from __doc__
        """ glGetProgramResourceIndex(self, program: int, programInterface: int, name: bytes) -> int """
        return 0

    def glGetProgramResourceiv(self, program, programInterface, index, propCount, props, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ glGetProgramResourceiv(self, program: int, programInterface: int, index: int, propCount: int, props: typing.Sequence[int], bufSize: int, length: typing.Sequence[int], params: typing.Sequence[int]) -> None """
        pass

    def glGetProgramResourceLocation(self, program, programInterface, name): # real signature unknown; restored from __doc__
        """ glGetProgramResourceLocation(self, program: int, programInterface: int, name: bytes) -> int """
        return 0

    def glGetQueryiv(self, target, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetQueryiv(self, target: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetQueryObjectuiv(self, id, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetQueryObjectuiv(self, id: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetSamplerParameterfv(self, sampler, pname, params, p_float=None): # real signature unknown; restored from __doc__
        """ glGetSamplerParameterfv(self, sampler: int, pname: int, params: typing.Sequence[float]) -> None """
        pass

    def glGetSamplerParameterIiv(self, sampler, pname): # real signature unknown; restored from __doc__
        """ glGetSamplerParameterIiv(self, sampler: int, pname: int) -> int """
        return 0

    def glGetSamplerParameterIuiv(self, sampler, pname): # real signature unknown; restored from __doc__
        """ glGetSamplerParameterIuiv(self, sampler: int, pname: int) -> int """
        return 0

    def glGetSamplerParameteriv(self, sampler, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetSamplerParameteriv(self, sampler: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetStringi(self, name, index): # real signature unknown; restored from __doc__
        """ glGetStringi(self, name: int, index: int) -> bytes """
        return b""

    def glGetTexLevelParameterfv(self, target, level, pname, params, p_float=None): # real signature unknown; restored from __doc__
        """ glGetTexLevelParameterfv(self, target: int, level: int, pname: int, params: typing.Sequence[float]) -> None """
        pass

    def glGetTexLevelParameteriv(self, target, level, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetTexLevelParameteriv(self, target: int, level: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetTexParameterIiv(self, target, pname): # real signature unknown; restored from __doc__
        """ glGetTexParameterIiv(self, target: int, pname: int) -> int """
        return 0

    def glGetTexParameterIuiv(self, target, pname): # real signature unknown; restored from __doc__
        """ glGetTexParameterIuiv(self, target: int, pname: int) -> int """
        return 0

    def glGetUniformBlockIndex(self, program, uniformBlockName): # real signature unknown; restored from __doc__
        """ glGetUniformBlockIndex(self, program: int, uniformBlockName: bytes) -> int """
        return 0

    def glGetUniformuiv(self, program, location, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetUniformuiv(self, program: int, location: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetVertexAttribIiv(self, index, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetVertexAttribIiv(self, index: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetVertexAttribIuiv(self, index, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetVertexAttribIuiv(self, index: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glInvalidateFramebuffer(self, target, numAttachments, attachments, p_int=None): # real signature unknown; restored from __doc__
        """ glInvalidateFramebuffer(self, target: int, numAttachments: int, attachments: typing.Sequence[int]) -> None """
        pass

    def glInvalidateSubFramebuffer(self, target, numAttachments, attachments, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ glInvalidateSubFramebuffer(self, target: int, numAttachments: int, attachments: typing.Sequence[int], x: int, y: int, width: int, height: int) -> None """
        pass

    def glIsEnabledi(self, target, index): # real signature unknown; restored from __doc__
        """ glIsEnabledi(self, target: int, index: int) -> int """
        return 0

    def glIsProgramPipeline(self, pipeline): # real signature unknown; restored from __doc__
        """ glIsProgramPipeline(self, pipeline: int) -> int """
        return 0

    def glIsQuery(self, id): # real signature unknown; restored from __doc__
        """ glIsQuery(self, id: int) -> int """
        return 0

    def glIsSampler(self, sampler): # real signature unknown; restored from __doc__
        """ glIsSampler(self, sampler: int) -> int """
        return 0

    def glIsTransformFeedback(self, id): # real signature unknown; restored from __doc__
        """ glIsTransformFeedback(self, id: int) -> int """
        return 0

    def glIsVertexArray(self, array): # real signature unknown; restored from __doc__
        """ glIsVertexArray(self, array: int) -> int """
        return 0

    def glMemoryBarrier(self, barriers): # real signature unknown; restored from __doc__
        """ glMemoryBarrier(self, barriers: int) -> None """
        pass

    def glMemoryBarrierByRegion(self, barriers): # real signature unknown; restored from __doc__
        """ glMemoryBarrierByRegion(self, barriers: int) -> None """
        pass

    def glMinSampleShading(self, value): # real signature unknown; restored from __doc__
        """ glMinSampleShading(self, value: float) -> None """
        pass

    def glObjectLabel(self, identifier, name, length, label): # real signature unknown; restored from __doc__
        """ glObjectLabel(self, identifier: int, name: int, length: int, label: bytes) -> None """
        pass

    def glObjectPtrLabel(self, ptr, length, label): # real signature unknown; restored from __doc__
        """ glObjectPtrLabel(self, ptr: int, length: int, label: bytes) -> None """
        pass

    def glPatchParameteri(self, pname, value): # real signature unknown; restored from __doc__
        """ glPatchParameteri(self, pname: int, value: int) -> None """
        pass

    def glPopDebugGroup(self): # real signature unknown; restored from __doc__
        """ glPopDebugGroup(self) -> None """
        pass

    def glPrimitiveBoundingBox(self, minX, minY, minZ, minW, maxX, maxY, maxZ, maxW): # real signature unknown; restored from __doc__
        """ glPrimitiveBoundingBox(self, minX: float, minY: float, minZ: float, minW: float, maxX: float, maxY: float, maxZ: float, maxW: float) -> None """
        pass

    def glProgramBinary(self, program, binaryFormat, binary, length): # real signature unknown; restored from __doc__
        """ glProgramBinary(self, program: int, binaryFormat: int, binary: int, length: int) -> None """
        pass

    def glProgramParameteri(self, program, pname, value): # real signature unknown; restored from __doc__
        """ glProgramParameteri(self, program: int, pname: int, value: int) -> None """
        pass

    def glProgramUniform1f(self, program, location, v0): # real signature unknown; restored from __doc__
        """ glProgramUniform1f(self, program: int, location: int, v0: float) -> None """
        pass

    def glProgramUniform1fv(self, program, location, count, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniform1fv(self, program: int, location: int, count: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniform1i(self, program, location, v0): # real signature unknown; restored from __doc__
        """ glProgramUniform1i(self, program: int, location: int, v0: int) -> None """
        pass

    def glProgramUniform1iv(self, program, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glProgramUniform1iv(self, program: int, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glProgramUniform1ui(self, program, location, v0): # real signature unknown; restored from __doc__
        """ glProgramUniform1ui(self, program: int, location: int, v0: int) -> None """
        pass

    def glProgramUniform1uiv(self, program, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glProgramUniform1uiv(self, program: int, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glProgramUniform2f(self, program, location, v0, v1): # real signature unknown; restored from __doc__
        """ glProgramUniform2f(self, program: int, location: int, v0: float, v1: float) -> None """
        pass

    def glProgramUniform2fv(self, program, location, count, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniform2fv(self, program: int, location: int, count: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniform2i(self, program, location, v0, v1): # real signature unknown; restored from __doc__
        """ glProgramUniform2i(self, program: int, location: int, v0: int, v1: int) -> None """
        pass

    def glProgramUniform2iv(self, program, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glProgramUniform2iv(self, program: int, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glProgramUniform2ui(self, program, location, v0, v1): # real signature unknown; restored from __doc__
        """ glProgramUniform2ui(self, program: int, location: int, v0: int, v1: int) -> None """
        pass

    def glProgramUniform2uiv(self, program, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glProgramUniform2uiv(self, program: int, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glProgramUniform3f(self, program, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glProgramUniform3f(self, program: int, location: int, v0: float, v1: float, v2: float) -> None """
        pass

    def glProgramUniform3fv(self, program, location, count, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniform3fv(self, program: int, location: int, count: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniform3i(self, program, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glProgramUniform3i(self, program: int, location: int, v0: int, v1: int, v2: int) -> None """
        pass

    def glProgramUniform3iv(self, program, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glProgramUniform3iv(self, program: int, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glProgramUniform3ui(self, program, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glProgramUniform3ui(self, program: int, location: int, v0: int, v1: int, v2: int) -> None """
        pass

    def glProgramUniform3uiv(self, program, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glProgramUniform3uiv(self, program: int, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glProgramUniform4f(self, program, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glProgramUniform4f(self, program: int, location: int, v0: float, v1: float, v2: float, v3: float) -> None """
        pass

    def glProgramUniform4fv(self, program, location, count, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniform4fv(self, program: int, location: int, count: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniform4i(self, program, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glProgramUniform4i(self, program: int, location: int, v0: int, v1: int, v2: int, v3: int) -> None """
        pass

    def glProgramUniform4iv(self, program, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glProgramUniform4iv(self, program: int, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glProgramUniform4ui(self, program, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glProgramUniform4ui(self, program: int, location: int, v0: int, v1: int, v2: int, v3: int) -> None """
        pass

    def glProgramUniform4uiv(self, program, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glProgramUniform4uiv(self, program: int, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glProgramUniformMatrix2fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix2fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniformMatrix2x3fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix2x3fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniformMatrix2x4fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix2x4fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniformMatrix3fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix3fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniformMatrix3x2fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix3x2fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniformMatrix3x4fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix3x4fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniformMatrix4fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix4fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniformMatrix4x2fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix4x2fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glProgramUniformMatrix4x3fv(self, program, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glProgramUniformMatrix4x3fv(self, program: int, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glPushDebugGroup(self, source, id, length, message): # real signature unknown; restored from __doc__
        """ glPushDebugGroup(self, source: int, id: int, length: int, message: bytes) -> None """
        pass

    def glReadBuffer(self, mode): # real signature unknown; restored from __doc__
        """ glReadBuffer(self, mode: int) -> None """
        pass

    def glReadnPixels(self, x, y, width, height, format, type, bufSize, data): # real signature unknown; restored from __doc__
        """ glReadnPixels(self, x: int, y: int, width: int, height: int, format: int, type: int, bufSize: int, data: int) -> None """
        pass

    def glRenderbufferStorageMultisample(self, target, samples, internalformat, width, height): # real signature unknown; restored from __doc__
        """ glRenderbufferStorageMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int) -> None """
        pass

    def glSampleMaski(self, maskNumber, mask): # real signature unknown; restored from __doc__
        """ glSampleMaski(self, maskNumber: int, mask: int) -> None """
        pass

    def glSamplerParameterf(self, sampler, pname, param): # real signature unknown; restored from __doc__
        """ glSamplerParameterf(self, sampler: int, pname: int, param: float) -> None """
        pass

    def glSamplerParameterfv(self, sampler, pname, param, p_float=None): # real signature unknown; restored from __doc__
        """ glSamplerParameterfv(self, sampler: int, pname: int, param: typing.Sequence[float]) -> None """
        pass

    def glSamplerParameteri(self, sampler, pname, param): # real signature unknown; restored from __doc__
        """ glSamplerParameteri(self, sampler: int, pname: int, param: int) -> None """
        pass

    def glSamplerParameterIiv(self, sampler, pname, param, p_int=None): # real signature unknown; restored from __doc__
        """ glSamplerParameterIiv(self, sampler: int, pname: int, param: typing.Sequence[int]) -> None """
        pass

    def glSamplerParameterIuiv(self, sampler, pname, param, p_int=None): # real signature unknown; restored from __doc__
        """ glSamplerParameterIuiv(self, sampler: int, pname: int, param: typing.Sequence[int]) -> None """
        pass

    def glSamplerParameteriv(self, sampler, pname, param, p_int=None): # real signature unknown; restored from __doc__
        """ glSamplerParameteriv(self, sampler: int, pname: int, param: typing.Sequence[int]) -> None """
        pass

    def glTexBuffer(self, target, internalformat, buffer): # real signature unknown; restored from __doc__
        """ glTexBuffer(self, target: int, internalformat: int, buffer: int) -> None """
        pass

    def glTexImage3D(self, target, level, internalformat, width, height, depth, border, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexImage3D(self, target: int, level: int, internalformat: int, width: int, height: int, depth: int, border: int, format: int, type: int, pixels: int) -> None """
        pass

    def glTexParameterIiv(self, target, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glTexParameterIiv(self, target: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glTexParameterIuiv(self, target, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glTexParameterIuiv(self, target: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glTexStorage2D(self, target, levels, internalformat, width, height): # real signature unknown; restored from __doc__
        """ glTexStorage2D(self, target: int, levels: int, internalformat: int, width: int, height: int) -> None """
        pass

    def glTexStorage2DMultisample(self, target, samples, internalformat, width, height, fixedsamplelocations): # real signature unknown; restored from __doc__
        """ glTexStorage2DMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int, fixedsamplelocations: int) -> None """
        pass

    def glTexStorage3D(self, target, levels, internalformat, width, height, depth): # real signature unknown; restored from __doc__
        """ glTexStorage3D(self, target: int, levels: int, internalformat: int, width: int, height: int, depth: int) -> None """
        pass

    def glTexStorage3DMultisample(self, target, samples, internalformat, width, height, depth, fixedsamplelocations): # real signature unknown; restored from __doc__
        """ glTexStorage3DMultisample(self, target: int, samples: int, internalformat: int, width: int, height: int, depth: int, fixedsamplelocations: int) -> None """
        pass

    def glTexSubImage3D(self, target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexSubImage3D(self, target: int, level: int, xoffset: int, yoffset: int, zoffset: int, width: int, height: int, depth: int, format: int, type: int, pixels: int) -> None """
        pass

    def glUniform1ui(self, location, v0): # real signature unknown; restored from __doc__
        """ glUniform1ui(self, location: int, v0: int) -> None """
        pass

    def glUniform1uiv(self, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glUniform1uiv(self, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glUniform2ui(self, location, v0, v1): # real signature unknown; restored from __doc__
        """ glUniform2ui(self, location: int, v0: int, v1: int) -> None """
        pass

    def glUniform2uiv(self, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glUniform2uiv(self, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glUniform3ui(self, location, v0, v1, v2): # real signature unknown; restored from __doc__
        """ glUniform3ui(self, location: int, v0: int, v1: int, v2: int) -> None """
        pass

    def glUniform3uiv(self, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glUniform3uiv(self, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glUniform4ui(self, location, v0, v1, v2, v3): # real signature unknown; restored from __doc__
        """ glUniform4ui(self, location: int, v0: int, v1: int, v2: int, v3: int) -> None """
        pass

    def glUniform4uiv(self, location, count, value, p_int=None): # real signature unknown; restored from __doc__
        """ glUniform4uiv(self, location: int, count: int, value: typing.Sequence[int]) -> None """
        pass

    def glUniformBlockBinding(self, program, uniformBlockIndex, uniformBlockBinding): # real signature unknown; restored from __doc__
        """ glUniformBlockBinding(self, program: int, uniformBlockIndex: int, uniformBlockBinding: int) -> None """
        pass

    def glUniformMatrix2x3fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix2x3fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUniformMatrix2x4fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix2x4fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUniformMatrix3x2fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix3x2fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUniformMatrix3x4fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix3x4fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUniformMatrix4x2fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix4x2fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUniformMatrix4x3fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix4x3fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUnmapBuffer(self, target): # real signature unknown; restored from __doc__
        """ glUnmapBuffer(self, target: int) -> int """
        return 0

    def glUseProgramStages(self, pipeline, stages, program): # real signature unknown; restored from __doc__
        """ glUseProgramStages(self, pipeline: int, stages: int, program: int) -> None """
        pass

    def glValidateProgramPipeline(self, pipeline): # real signature unknown; restored from __doc__
        """ glValidateProgramPipeline(self, pipeline: int) -> None """
        pass

    def glVertexAttribBinding(self, attribindex, bindingindex): # real signature unknown; restored from __doc__
        """ glVertexAttribBinding(self, attribindex: int, bindingindex: int) -> None """
        pass

    def glVertexAttribDivisor(self, index, divisor): # real signature unknown; restored from __doc__
        """ glVertexAttribDivisor(self, index: int, divisor: int) -> None """
        pass

    def glVertexAttribFormat(self, attribindex, size, type, normalized, relativeoffset): # real signature unknown; restored from __doc__
        """ glVertexAttribFormat(self, attribindex: int, size: int, type: int, normalized: int, relativeoffset: int) -> None """
        pass

    def glVertexAttribI4i(self, index, x, y, z, w): # real signature unknown; restored from __doc__
        """ glVertexAttribI4i(self, index: int, x: int, y: int, z: int, w: int) -> None """
        pass

    def glVertexAttribI4iv(self, index, v, p_int=None): # real signature unknown; restored from __doc__
        """ glVertexAttribI4iv(self, index: int, v: typing.Sequence[int]) -> None """
        pass

    def glVertexAttribI4ui(self, index, x, y, z, w): # real signature unknown; restored from __doc__
        """ glVertexAttribI4ui(self, index: int, x: int, y: int, z: int, w: int) -> None """
        pass

    def glVertexAttribI4uiv(self, index, v, p_int=None): # real signature unknown; restored from __doc__
        """ glVertexAttribI4uiv(self, index: int, v: typing.Sequence[int]) -> None """
        pass

    def glVertexAttribIFormat(self, attribindex, size, type, relativeoffset): # real signature unknown; restored from __doc__
        """ glVertexAttribIFormat(self, attribindex: int, size: int, type: int, relativeoffset: int) -> None """
        pass

    def glVertexAttribIPointer(self, index, size, type, stride, pointer): # real signature unknown; restored from __doc__
        """ glVertexAttribIPointer(self, index: int, size: int, type: int, stride: int, pointer: int) -> None """
        pass

    def glVertexBindingDivisor(self, bindingindex, divisor): # real signature unknown; restored from __doc__
        """ glVertexBindingDivisor(self, bindingindex: int, divisor: int) -> None """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


