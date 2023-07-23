import maya.cmds as cmds
import maya.api.OpenMaya as om

def create_mcl_material():
    shader = cmds.shadingNode('lambert', asShader=True)

    sampler = cmds.shadingNode('samplerInfo', asUtility=True)

    # color_grass = cmds.shadingNode('colorConstant', asUtility=True)
    # cmds.setAttr(color_grass + '.colorR', 0.388)
    # cmds.setAttr(color_grass + '.colorG', 1.00)
    # cmds.setAttr(color_grass + '.colorB', 0.101)
    #
    # color_dirt = cmds.shadingNode('colorConstant', asUtility=True)
    # cmds.setAttr(color_dirt + '.colorR', 0.530)
    # cmds.setAttr(color_dirt + '.colorG', 0.499)
    # cmds.setAttr(color_dirt + '.colorB', 0.179)
    #
    # color_cliff = cmds.shadingNode('colorConstant', asUtility=True)
    # cmds.setAttr(color_cliff + '.colorR', 0.208)
    # cmds.setAttr(color_cliff + '.colorG', 0.211)
    # cmds.setAttr(color_cliff + '.colorB', 0.222)

    color_grass = (0.388, 1.00, 0.101)
    color_dirt = (0.530, 0.499, 0.179)
    color_cliff = (0.208, 0.211, 0.222)

    blend_height = cmds.shadingNode('blendColor', asUtility=True)
    cmds.setAttr(blend_height + '.color1', color_grass[0], color_grass[1], color_grass[2], type='float3')
    cmds.setAttr(blend_height + '.color2', color_dirt[0], color_dirt[1], color_dirt[2], type='float3')

    blend_normal = cmds.shadingNode('blendColor', asUtility=True)

    scale_factor = cmds.shadingNode('multiplyDivide', asUtility=True, operaiton = 2)
    cmds.setAttr(scale_factor + 'input2', 1.0, 1.0, 1.0, type='float3')
    cmds.connectAttr(sampler + '.pointWorldY', scale_factor + '.input1')

    cmds.connectAttr(scale_factor + '.output', blend_height + '.blender')

    cmds.connectAttr(blend_height + '.output', shader + '.color')

    return shader