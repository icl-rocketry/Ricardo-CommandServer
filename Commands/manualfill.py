from CommandServer.commandserver import CommandServer
# import movesrvprss, movesrvoxvent, movesrvfuelvent

from . import movesrvprss
from . import movesrvoxvent
from . import movesrvfuelvent

@CommandServer.register('manualfill')
def manualfill(instance,args):
    movesrvprss_args = {"argument":0}
    movesrvfuelvent_args = {"argument":180}
    
    movesrvprss.movesrvprss(instance,movesrvprss_args)
    movesrvfuelvent.movesrvfuelvent(instance,movesrvfuelvent_args)