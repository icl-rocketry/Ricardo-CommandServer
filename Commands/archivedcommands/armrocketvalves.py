from CommandServer.commandserver import CommandServer
# import movesrvprss, movesrvoxvent, movesrvfuelvent

from . import armsrvfuelvent
from . import armsrvoxvent
from . import armsrvprss

@CommandServer.register('armrocketvalves')
def armrocketvalves(instance,args):

    armsrvfuelvent.armsrvfuelvent(instance,args)
    armsrvoxvent.armsrvoxvent(instance,args)
    armsrvprss.armsrvprss(instance,args)