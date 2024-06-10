from CommandServer.commandserver import CommandServer
# import movesrvprss, movesrvoxvent, movesrvfuelvent

from . import disarmsrvfuelvent
from . import disarmsrvoxvent
from . import disarmsrvprss

@CommandServer.register('disarmrocketvalves')
def disarmrocketvalves(instance,args):

    disarmsrvfuelvent.disarmsrvfuelvent(instance,args)
    disarmsrvoxvent.disarmsrvoxvent(instance,args)
    disarmsrvprss.disarmsrvprss(instance,args)