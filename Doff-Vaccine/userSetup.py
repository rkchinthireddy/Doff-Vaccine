import maya.OpenMaya as api
import maya.cmds as mc
#doffVaccine ----------------------
from doff import vaccine
saveCallback = api.MSceneMessage.addCallback(api.MSceneMessage.kBeforeSave,vaccine.delVac)
print('Doff Vaccine applied')
