# Create Simple Ribbon spines Character Felxibe Rig By Masood Safdarian
# Simple Maya Python Straightforward
import maya.cmds as cmds
import pymel.core as pm

# Create default sirface with 6 Part
cmds.nurbsPlane( n = "ribben", p=[0,0,0], ax = [0,1,0], w=1, lr=6,d=3, u=1, v=6 )
cmds.select('ribben', r=True)

# Create hairsystem
pm.language.Mel.eval("createHair 1 6 5 0 0 0 0 5 0 2 1 1;") 
pm.PyNode("hairSystem1")
# Cleanup 
cmds.delete( 'hairSystem1OutputCurves', 'hairSystem1', 'nucleus1' )

# Create joints
cmds.joint( p=(0, 0, 0) )
cmds.duplicate()
cmds.duplicate()
cmds.duplicate()
cmds.duplicate()
cmds.duplicate()
cmds.parent( 'joint1', 'ribbenFollicle5008' )
cmds.parent( 'joint2', 'ribbenFollicle5025' )
cmds.parent( 'joint3', 'ribbenFollicle5041' )
cmds.parent( 'joint4', 'ribbenFollicle5058' )
cmds.parent( 'joint5', 'ribbenFollicle5074' )
cmds.parent( 'joint6', 'ribbenFollicle5091' )
cmds.setAttr( 'joint6.translateY' , 0 )
cmds.setAttr( 'joint1.translateY' , 0 )
cmds.setAttr( 'joint2.translateY' , 0 )
cmds.setAttr( 'joint3.translateY' , 0 )
cmds.setAttr( 'joint4.translateY' , 0 )
cmds.setAttr( 'joint5.translateY' , 0 )
cmds.select( clear=True )
cmds.joint( p=(0, 0, 0) )
cmds.setAttr( 'joint7.radius', 5 )
cmds.select( clear=True )
cmds.joint( p=(0, 0, 3) )
cmds.setAttr( 'joint8.radius', 5 )
cmds.select( clear=True )
cmds.joint( p=(0, 0, -3) )
cmds.setAttr( 'joint9.radius', 5 )
# Create set selection for Rig
cmds.sets( 'joint7', 'joint8' , 'joint9', 'ribben', n='set1' )
cmds.select( 'set1' )
cmds.ls( selection=True )
# Bind skin
cmds.skinCluster()
# Testing code
cmds.setAttr( 'joint7.translateY' , 2 )
# Now Start Moving/rotate/scale big joint
