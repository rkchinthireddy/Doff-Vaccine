import maya.cmds as mc

def delVac(_):
    jobs = mc.scriptJob(lj=True)
    for job in jobs:
        if "leukocyte.antivirus()" in job:
            id = job.split(":")[0]
            if id.isdigit():
                mc.scriptJob(k=int(id), f=True)
    
    script_nodes = mc.ls(["vaccine_gene","breed_gene"], type="script")
    if script_nodes:
        mc.delete(script_nodes)
        print str(script_nodes)+' deleted'
