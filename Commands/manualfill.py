from CommandServer.commandserver import CommandServer
# import movesrvprss, movesrvoxvent, movesrvfuelvent

from . import movesrvprss
from . import movesrvoxvent
from . import movesrvfuelvent

@CommandServer.register('manualfill')
def manualfill(instance,args):
    movesrvprss.movesrvprss(instance,args)
    movesrvfuelvent.movesrvfuelvent(instance,args)
    movesrvoxvent.movesrvoxvent(instance,args)