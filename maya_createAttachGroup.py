import maya.cmds as cmds

# removes unicode to make a clean string e.g. u['obj'] = 'obj'
def removeUnicode(unicode):
     unicodeString = str(unicode)
     return unicodeString[3:len(unicode)-3]


selected = cmds.ls(sl=True)
currentObject = selected
groupName = removeUnicode(currentObject) + "_attach"

cmds.group( currentObject, n = groupName )
