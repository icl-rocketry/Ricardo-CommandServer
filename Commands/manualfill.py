from CommandServer.commandserver import CommandServer
import movesrvprss, movesrvoxvent, movesrvfuelvent

@CommandServer.register('manualfill')
def manualfill(instance,args):
    movesrvprss.movesrvprss(instance,args)
    movesrvfuelvent.movesrvfuelvent(instance,args)
    movesrvoxvent.movesrvoxvent(instance,args)