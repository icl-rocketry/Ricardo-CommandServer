from CommandServer.commandserver import CommandServer

from . import restartlogicpdu0
from . import restartlogicpdu1

@CommandServer.register('restartlogic')
def restartlogic(instance,args):
    restartlogic_args = {"argument":5000}
    
    restartlogicpdu0.restartlogicpdu0(instance,restartlogic_args)
    restartlogicpdu1.restartlogicpdu1(instance,restartlogic_args)