import maya.cmds as cmds
import maya.mel as mel


# select parent, then child object
selectedPair = cmds.ls(sl=True)
currentObject = selectedPair[1]
currentParent = selectedPair[0]

# create attach group
attachGroup = str(currentObject) + "_attach"
cmds.group( currentObject, n = attachGroup)

# center pivot of attach group
cmds.select(attachGroup, r = True)
mel.eval("CenterPivot")

# select parent, select child, parent constraint options

cmds.select( currentParent, r=True )
cmds.select( attachGroup, add=True )

mel.eval("ParentConstraintOptions")