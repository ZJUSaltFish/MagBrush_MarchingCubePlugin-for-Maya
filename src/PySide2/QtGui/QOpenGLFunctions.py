# encoding: utf-8
# module PySide2.QtGui
# from D:\Maya2024\Python\lib\site-packages\PySide2\QtGui.cp310-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import PySide2.QtCore as __PySide2_QtCore
import Shiboken as __Shiboken


class QOpenGLFunctions(__Shiboken.Object):
    """
    QOpenGLFunctions(self) -> None
    QOpenGLFunctions(self, context: PySide2.QtGui.QOpenGLContext) -> None
    """
    def glActiveTexture(self, texture): # real signature unknown; restored from __doc__
        """ glActiveTexture(self, texture: int) -> None """
        pass

    def glAttachShader(self, program, shader): # real signature unknown; restored from __doc__
        """ glAttachShader(self, program: int, shader: int) -> None """
        pass

    def glBindAttribLocation(self, program, index, name): # real signature unknown; restored from __doc__
        """ glBindAttribLocation(self, program: int, index: int, name: bytes) -> None """
        pass

    def glBindBuffer(self, target, buffer): # real signature unknown; restored from __doc__
        """ glBindBuffer(self, target: int, buffer: int) -> None """
        pass

    def glBindFramebuffer(self, target, framebuffer): # real signature unknown; restored from __doc__
        """ glBindFramebuffer(self, target: int, framebuffer: int) -> None """
        pass

    def glBindRenderbuffer(self, target, renderbuffer): # real signature unknown; restored from __doc__
        """ glBindRenderbuffer(self, target: int, renderbuffer: int) -> None """
        pass

    def glBindTexture(self, target, texture): # real signature unknown; restored from __doc__
        """ glBindTexture(self, target: int, texture: int) -> None """
        pass

    def glBlendColor(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ glBlendColor(self, red: float, green: float, blue: float, alpha: float) -> None """
        pass

    def glBlendEquation(self, mode): # real signature unknown; restored from __doc__
        """ glBlendEquation(self, mode: int) -> None """
        pass

    def glBlendEquationSeparate(self, modeRGB, modeAlpha): # real signature unknown; restored from __doc__
        """ glBlendEquationSeparate(self, modeRGB: int, modeAlpha: int) -> None """
        pass

    def glBlendFunc(self, sfactor, dfactor): # real signature unknown; restored from __doc__
        """ glBlendFunc(self, sfactor: int, dfactor: int) -> None """
        pass

    def glBlendFuncSeparate(self, srcRGB, dstRGB, srcAlpha, dstAlpha): # real signature unknown; restored from __doc__
        """ glBlendFuncSeparate(self, srcRGB: int, dstRGB: int, srcAlpha: int, dstAlpha: int) -> None """
        pass

    def glCheckFramebufferStatus(self, target): # real signature unknown; restored from __doc__
        """ glCheckFramebufferStatus(self, target: int) -> int """
        return 0

    def glClear(self, mask): # real signature unknown; restored from __doc__
        """ glClear(self, mask: int) -> None """
        pass

    def glClearColor(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ glClearColor(self, red: float, green: float, blue: float, alpha: float) -> None """
        pass

    def glClearDepthf(self, depth): # real signature unknown; restored from __doc__
        """ glClearDepthf(self, depth: float) -> None """
        pass

    def glClearStencil(self, s): # real signature unknown; restored from __doc__
        """ glClearStencil(self, s: int) -> None """
        pass

    def glColorMask(self, red, green, blue, alpha): # real signature unknown; restored from __doc__
        """ glColorMask(self, red: int, green: int, blue: int, alpha: int) -> None """
        pass

    def glCompileShader(self, shader): # real signature unknown; restored from __doc__
        """ glCompileShader(self, shader: int) -> None """
        pass

    def glCompressedTexImage2D(self, target, level, internalformat, width, height, border, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, imageSize: int, data: int) -> None """
        pass

    def glCompressedTexSubImage2D(self, target, level, xoffset, yoffset, width, height, format, imageSize, data): # real signature unknown; restored from __doc__
        """ glCompressedTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, imageSize: int, data: int) -> None """
        pass

    def glCopyTexImage2D(self, target, level, internalformat, x, y, width, height, border): # real signature unknown; restored from __doc__
        """ glCopyTexImage2D(self, target: int, level: int, internalformat: int, x: int, y: int, width: int, height: int, border: int) -> None """
        pass

    def glCopyTexSubImage2D(self, target, level, xoffset, yoffset, x, y, width, height): # real signature unknown; restored from __doc__
        """ glCopyTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, x: int, y: int, width: int, height: int) -> None """
        pass

    def glCreateProgram(self): # real signature unknown; restored from __doc__
        """ glCreateProgram(self) -> int """
        return 0

    def glCreateShader(self, type): # real signature unknown; restored from __doc__
        """ glCreateShader(self, type: int) -> int """
        return 0

    def glCullFace(self, mode): # real signature unknown; restored from __doc__
        """ glCullFace(self, mode: int) -> None """
        pass

    def glDeleteBuffers(self, n, buffers, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteBuffers(self, n: int, buffers: typing.Sequence[int]) -> None """
        pass

    def glDeleteFramebuffers(self, n, framebuffers, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteFramebuffers(self, n: int, framebuffers: typing.Sequence[int]) -> None """
        pass

    def glDeleteProgram(self, program): # real signature unknown; restored from __doc__
        """ glDeleteProgram(self, program: int) -> None """
        pass

    def glDeleteRenderbuffers(self, n, renderbuffers, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteRenderbuffers(self, n: int, renderbuffers: typing.Sequence[int]) -> None """
        pass

    def glDeleteShader(self, shader): # real signature unknown; restored from __doc__
        """ glDeleteShader(self, shader: int) -> None """
        pass

    def glDeleteTextures(self, n, textures, p_int=None): # real signature unknown; restored from __doc__
        """ glDeleteTextures(self, n: int, textures: typing.Sequence[int]) -> None """
        pass

    def glDepthFunc(self, func): # real signature unknown; restored from __doc__
        """ glDepthFunc(self, func: int) -> None """
        pass

    def glDepthMask(self, flag): # real signature unknown; restored from __doc__
        """ glDepthMask(self, flag: int) -> None """
        pass

    def glDepthRangef(self, zNear, zFar): # real signature unknown; restored from __doc__
        """ glDepthRangef(self, zNear: float, zFar: float) -> None """
        pass

    def glDetachShader(self, program, shader): # real signature unknown; restored from __doc__
        """ glDetachShader(self, program: int, shader: int) -> None """
        pass

    def glDisable(self, cap): # real signature unknown; restored from __doc__
        """ glDisable(self, cap: int) -> None """
        pass

    def glDisableVertexAttribArray(self, index): # real signature unknown; restored from __doc__
        """ glDisableVertexAttribArray(self, index: int) -> None """
        pass

    def glDrawArrays(self, mode, first, count): # real signature unknown; restored from __doc__
        """ glDrawArrays(self, mode: int, first: int, count: int) -> None """
        pass

    def glDrawElements(self, mode, count, type, indices): # real signature unknown; restored from __doc__
        """ glDrawElements(self, mode: int, count: int, type: int, indices: int) -> None """
        pass

    def glEnable(self, cap): # real signature unknown; restored from __doc__
        """ glEnable(self, cap: int) -> None """
        pass

    def glEnableVertexAttribArray(self, index): # real signature unknown; restored from __doc__
        """ glEnableVertexAttribArray(self, index: int) -> None """
        pass

    def glFinish(self): # real signature unknown; restored from __doc__
        """ glFinish(self) -> None """
        pass

    def glFlush(self): # real signature unknown; restored from __doc__
        """ glFlush(self) -> None """
        pass

    def glFramebufferRenderbuffer(self, target, attachment, renderbuffertarget, renderbuffer): # real signature unknown; restored from __doc__
        """ glFramebufferRenderbuffer(self, target: int, attachment: int, renderbuffertarget: int, renderbuffer: int) -> None """
        pass

    def glFramebufferTexture2D(self, target, attachment, textarget, texture, level): # real signature unknown; restored from __doc__
        """ glFramebufferTexture2D(self, target: int, attachment: int, textarget: int, texture: int, level: int) -> None """
        pass

    def glFrontFace(self, mode): # real signature unknown; restored from __doc__
        """ glFrontFace(self, mode: int) -> None """
        pass

    def glGenBuffers(self, n, buffers, p_int=None): # real signature unknown; restored from __doc__
        """ glGenBuffers(self, n: int, buffers: typing.Sequence[int]) -> None """
        pass

    def glGenerateMipmap(self, target): # real signature unknown; restored from __doc__
        """ glGenerateMipmap(self, target: int) -> None """
        pass

    def glGenFramebuffers(self, n, framebuffers, p_int=None): # real signature unknown; restored from __doc__
        """ glGenFramebuffers(self, n: int, framebuffers: typing.Sequence[int]) -> None """
        pass

    def glGenRenderbuffers(self, n, renderbuffers, p_int=None): # real signature unknown; restored from __doc__
        """ glGenRenderbuffers(self, n: int, renderbuffers: typing.Sequence[int]) -> None """
        pass

    def glGenTextures(self, n, textures, p_int=None): # real signature unknown; restored from __doc__
        """ glGenTextures(self, n: int, textures: typing.Sequence[int]) -> None """
        pass

    def glGetAttachedShaders(self, program, maxcount, count, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ glGetAttachedShaders(self, program: int, maxcount: int, count: typing.Sequence[int], shaders: typing.Sequence[int]) -> None """
        pass

    def glGetAttribLocation(self, program, name): # real signature unknown; restored from __doc__
        """ glGetAttribLocation(self, program: int, name: bytes) -> int """
        return 0

    def glGetBufferParameteriv(self, target, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetBufferParameteriv(self, target: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetError(self): # real signature unknown; restored from __doc__
        """ glGetError(self) -> int """
        return 0

    def glGetFloatv(self, pname, params, p_float=None): # real signature unknown; restored from __doc__
        """ glGetFloatv(self, pname: int, params: typing.Sequence[float]) -> None """
        pass

    def glGetFramebufferAttachmentParameteriv(self, target, attachment, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetFramebufferAttachmentParameteriv(self, target: int, attachment: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetIntegerv(self, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetIntegerv(self, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetProgramiv(self, program, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetProgramiv(self, program: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetRenderbufferParameteriv(self, target, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetRenderbufferParameteriv(self, target: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetShaderiv(self, shader, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetShaderiv(self, shader: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetShaderPrecisionFormat(self, shadertype, precisiontype, range, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ glGetShaderPrecisionFormat(self, shadertype: int, precisiontype: int, range: typing.Sequence[int], precision: typing.Sequence[int]) -> None """
        pass

    def glGetString(self, name): # real signature unknown; restored from __doc__
        """ glGetString(self, name: int) -> bytes """
        return b""

    def glGetTexParameterfv(self, target, pname, params, p_float=None): # real signature unknown; restored from __doc__
        """ glGetTexParameterfv(self, target: int, pname: int, params: typing.Sequence[float]) -> None """
        pass

    def glGetTexParameteriv(self, target, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetTexParameteriv(self, target: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetUniformfv(self, program, location, params, p_float=None): # real signature unknown; restored from __doc__
        """ glGetUniformfv(self, program: int, location: int, params: typing.Sequence[float]) -> None """
        pass

    def glGetUniformiv(self, program, location, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetUniformiv(self, program: int, location: int, params: typing.Sequence[int]) -> None """
        pass

    def glGetUniformLocation(self, program, name): # real signature unknown; restored from __doc__
        """ glGetUniformLocation(self, program: int, name: bytes) -> int """
        return 0

    def glGetVertexAttribfv(self, index, pname, params, p_float=None): # real signature unknown; restored from __doc__
        """ glGetVertexAttribfv(self, index: int, pname: int, params: typing.Sequence[float]) -> None """
        pass

    def glGetVertexAttribiv(self, index, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glGetVertexAttribiv(self, index: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glHint(self, target, mode): # real signature unknown; restored from __doc__
        """ glHint(self, target: int, mode: int) -> None """
        pass

    def glIsBuffer(self, buffer): # real signature unknown; restored from __doc__
        """ glIsBuffer(self, buffer: int) -> int """
        return 0

    def glIsEnabled(self, cap): # real signature unknown; restored from __doc__
        """ glIsEnabled(self, cap: int) -> int """
        return 0

    def glIsFramebuffer(self, framebuffer): # real signature unknown; restored from __doc__
        """ glIsFramebuffer(self, framebuffer: int) -> int """
        return 0

    def glIsProgram(self, program): # real signature unknown; restored from __doc__
        """ glIsProgram(self, program: int) -> int """
        return 0

    def glIsRenderbuffer(self, renderbuffer): # real signature unknown; restored from __doc__
        """ glIsRenderbuffer(self, renderbuffer: int) -> int """
        return 0

    def glIsShader(self, shader): # real signature unknown; restored from __doc__
        """ glIsShader(self, shader: int) -> int """
        return 0

    def glIsTexture(self, texture): # real signature unknown; restored from __doc__
        """ glIsTexture(self, texture: int) -> int """
        return 0

    def glLineWidth(self, width): # real signature unknown; restored from __doc__
        """ glLineWidth(self, width: float) -> None """
        pass

    def glLinkProgram(self, program): # real signature unknown; restored from __doc__
        """ glLinkProgram(self, program: int) -> None """
        pass

    def glPixelStorei(self, pname, param): # real signature unknown; restored from __doc__
        """ glPixelStorei(self, pname: int, param: int) -> None """
        pass

    def glPolygonOffset(self, factor, units): # real signature unknown; restored from __doc__
        """ glPolygonOffset(self, factor: float, units: float) -> None """
        pass

    def glReadPixels(self, x, y, width, height, format, type, pixels): # real signature unknown; restored from __doc__
        """ glReadPixels(self, x: int, y: int, width: int, height: int, format: int, type: int, pixels: int) -> None """
        pass

    def glReleaseShaderCompiler(self): # real signature unknown; restored from __doc__
        """ glReleaseShaderCompiler(self) -> None """
        pass

    def glRenderbufferStorage(self, target, internalformat, width, height): # real signature unknown; restored from __doc__
        """ glRenderbufferStorage(self, target: int, internalformat: int, width: int, height: int) -> None """
        pass

    def glSampleCoverage(self, value, invert): # real signature unknown; restored from __doc__
        """ glSampleCoverage(self, value: float, invert: int) -> None """
        pass

    def glScissor(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ glScissor(self, x: int, y: int, width: int, height: int) -> None """
        pass

    def glShaderBinary(self, n, shaders, p_int=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ glShaderBinary(self, n: int, shaders: typing.Sequence[int], binaryformat: int, binary: int, length: int) -> None """
        pass

    def glStencilFunc(self, func, ref, mask): # real signature unknown; restored from __doc__
        """ glStencilFunc(self, func: int, ref: int, mask: int) -> None """
        pass

    def glStencilFuncSeparate(self, face, func, ref, mask): # real signature unknown; restored from __doc__
        """ glStencilFuncSeparate(self, face: int, func: int, ref: int, mask: int) -> None """
        pass

    def glStencilMask(self, mask): # real signature unknown; restored from __doc__
        """ glStencilMask(self, mask: int) -> None """
        pass

    def glStencilMaskSeparate(self, face, mask): # real signature unknown; restored from __doc__
        """ glStencilMaskSeparate(self, face: int, mask: int) -> None """
        pass

    def glStencilOp(self, fail, zfail, zpass): # real signature unknown; restored from __doc__
        """ glStencilOp(self, fail: int, zfail: int, zpass: int) -> None """
        pass

    def glStencilOpSeparate(self, face, fail, zfail, zpass): # real signature unknown; restored from __doc__
        """ glStencilOpSeparate(self, face: int, fail: int, zfail: int, zpass: int) -> None """
        pass

    def glTexImage2D(self, target, level, internalformat, width, height, border, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexImage2D(self, target: int, level: int, internalformat: int, width: int, height: int, border: int, format: int, type: int, pixels: int) -> None """
        pass

    def glTexParameterf(self, target, pname, param): # real signature unknown; restored from __doc__
        """ glTexParameterf(self, target: int, pname: int, param: float) -> None """
        pass

    def glTexParameterfv(self, target, pname, params, p_float=None): # real signature unknown; restored from __doc__
        """ glTexParameterfv(self, target: int, pname: int, params: typing.Sequence[float]) -> None """
        pass

    def glTexParameteri(self, target, pname, param): # real signature unknown; restored from __doc__
        """ glTexParameteri(self, target: int, pname: int, param: int) -> None """
        pass

    def glTexParameteriv(self, target, pname, params, p_int=None): # real signature unknown; restored from __doc__
        """ glTexParameteriv(self, target: int, pname: int, params: typing.Sequence[int]) -> None """
        pass

    def glTexSubImage2D(self, target, level, xoffset, yoffset, width, height, format, type, pixels): # real signature unknown; restored from __doc__
        """ glTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int, format: int, type: int, pixels: int) -> None """
        pass

    def glUniform1f(self, location, x): # real signature unknown; restored from __doc__
        """ glUniform1f(self, location: int, x: float) -> None """
        pass

    def glUniform1fv(self, location, count, v, p_float=None): # real signature unknown; restored from __doc__
        """ glUniform1fv(self, location: int, count: int, v: typing.Sequence[float]) -> None """
        pass

    def glUniform1i(self, location, x): # real signature unknown; restored from __doc__
        """ glUniform1i(self, location: int, x: int) -> None """
        pass

    def glUniform1iv(self, location, count, v, p_int=None): # real signature unknown; restored from __doc__
        """ glUniform1iv(self, location: int, count: int, v: typing.Sequence[int]) -> None """
        pass

    def glUniform2f(self, location, x, y): # real signature unknown; restored from __doc__
        """ glUniform2f(self, location: int, x: float, y: float) -> None """
        pass

    def glUniform2fv(self, location, count, v, p_float=None): # real signature unknown; restored from __doc__
        """ glUniform2fv(self, location: int, count: int, v: typing.Sequence[float]) -> None """
        pass

    def glUniform2i(self, location, x, y): # real signature unknown; restored from __doc__
        """ glUniform2i(self, location: int, x: int, y: int) -> None """
        pass

    def glUniform2iv(self, location, count, v, p_int=None): # real signature unknown; restored from __doc__
        """ glUniform2iv(self, location: int, count: int, v: typing.Sequence[int]) -> None """
        pass

    def glUniform3f(self, location, x, y, z): # real signature unknown; restored from __doc__
        """ glUniform3f(self, location: int, x: float, y: float, z: float) -> None """
        pass

    def glUniform3fv(self, location, count, v, p_float=None): # real signature unknown; restored from __doc__
        """ glUniform3fv(self, location: int, count: int, v: typing.Sequence[float]) -> None """
        pass

    def glUniform3i(self, location, x, y, z): # real signature unknown; restored from __doc__
        """ glUniform3i(self, location: int, x: int, y: int, z: int) -> None """
        pass

    def glUniform3iv(self, location, count, v, p_int=None): # real signature unknown; restored from __doc__
        """ glUniform3iv(self, location: int, count: int, v: typing.Sequence[int]) -> None """
        pass

    def glUniform4f(self, location, x, y, z, w): # real signature unknown; restored from __doc__
        """ glUniform4f(self, location: int, x: float, y: float, z: float, w: float) -> None """
        pass

    def glUniform4fv(self, location, count, v, p_float=None): # real signature unknown; restored from __doc__
        """ glUniform4fv(self, location: int, count: int, v: typing.Sequence[float]) -> None """
        pass

    def glUniform4i(self, location, x, y, z, w): # real signature unknown; restored from __doc__
        """ glUniform4i(self, location: int, x: int, y: int, z: int, w: int) -> None """
        pass

    def glUniform4iv(self, location, count, v, p_int=None): # real signature unknown; restored from __doc__
        """ glUniform4iv(self, location: int, count: int, v: typing.Sequence[int]) -> None """
        pass

    def glUniformMatrix2fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix2fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUniformMatrix3fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix3fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUniformMatrix4fv(self, location, count, transpose, value, p_float=None): # real signature unknown; restored from __doc__
        """ glUniformMatrix4fv(self, location: int, count: int, transpose: int, value: typing.Sequence[float]) -> None """
        pass

    def glUseProgram(self, program): # real signature unknown; restored from __doc__
        """ glUseProgram(self, program: int) -> None """
        pass

    def glValidateProgram(self, program): # real signature unknown; restored from __doc__
        """ glValidateProgram(self, program: int) -> None """
        pass

    def glVertexAttrib1f(self, indx, x): # real signature unknown; restored from __doc__
        """ glVertexAttrib1f(self, indx: int, x: float) -> None """
        pass

    def glVertexAttrib1fv(self, indx, values, p_float=None): # real signature unknown; restored from __doc__
        """ glVertexAttrib1fv(self, indx: int, values: typing.Sequence[float]) -> None """
        pass

    def glVertexAttrib2f(self, indx, x, y): # real signature unknown; restored from __doc__
        """ glVertexAttrib2f(self, indx: int, x: float, y: float) -> None """
        pass

    def glVertexAttrib2fv(self, indx, values, p_float=None): # real signature unknown; restored from __doc__
        """ glVertexAttrib2fv(self, indx: int, values: typing.Sequence[float]) -> None """
        pass

    def glVertexAttrib3f(self, indx, x, y, z): # real signature unknown; restored from __doc__
        """ glVertexAttrib3f(self, indx: int, x: float, y: float, z: float) -> None """
        pass

    def glVertexAttrib3fv(self, indx, values, p_float=None): # real signature unknown; restored from __doc__
        """ glVertexAttrib3fv(self, indx: int, values: typing.Sequence[float]) -> None """
        pass

    def glVertexAttrib4f(self, indx, x, y, z, w): # real signature unknown; restored from __doc__
        """ glVertexAttrib4f(self, indx: int, x: float, y: float, z: float, w: float) -> None """
        pass

    def glVertexAttrib4fv(self, indx, values, p_float=None): # real signature unknown; restored from __doc__
        """ glVertexAttrib4fv(self, indx: int, values: typing.Sequence[float]) -> None """
        pass

    def glVertexAttribPointer(self, indx, size, type, normalized, stride, ptr): # real signature unknown; restored from __doc__
        """ glVertexAttribPointer(self, indx: int, size: int, type: int, normalized: int, stride: int, ptr: int) -> None """
        pass

    def glViewport(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ glViewport(self, x: int, y: int, width: int, height: int) -> None """
        pass

    def hasOpenGLFeature(self, feature): # real signature unknown; restored from __doc__
        """ hasOpenGLFeature(self, feature: PySide2.QtGui.QOpenGLFunctions.OpenGLFeature) -> bool """
        return False

    def initializeOpenGLFunctions(self): # real signature unknown; restored from __doc__
        """ initializeOpenGLFunctions(self) -> None """
        pass

    def openGLFeatures(self): # real signature unknown; restored from __doc__
        """ openGLFeatures(self) -> PySide2.QtGui.QOpenGLFunctions.OpenGLFeatures """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BlendColor = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.BlendColor
    BlendEquation = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.BlendEquation
    BlendEquationAdvanced = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.BlendEquationAdvanced
    BlendEquationSeparate = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.BlendEquationSeparate
    BlendFuncSeparate = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.BlendFuncSeparate
    BlendSubtract = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.BlendSubtract
    Buffers = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.Buffers
    CompressedTextures = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.CompressedTextures
    FixedFunctionPipeline = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.FixedFunctionPipeline
    Framebuffers = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.Framebuffers
    MultipleRenderTargets = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.MultipleRenderTargets
    Multisample = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.Multisample
    Multitexture = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.Multitexture
    NPOTTextureRepeat = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.NPOTTextureRepeat
    NPOTTextures = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.NPOTTextures
    OpenGLFeature = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLFunctions.OpenGLFeature'>"
    OpenGLFeatures = None # (!) real value is "<class 'PySide2.QtGui.QOpenGLFunctions.OpenGLFeatures'>"
    Shaders = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.Shaders
    StencilSeparate = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.StencilSeparate
    TextureRGFormats = PySide2.QtGui.QOpenGLFunctions.OpenGLFeature.TextureRGFormats


