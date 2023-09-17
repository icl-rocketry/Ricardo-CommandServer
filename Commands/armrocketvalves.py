from CommandServer.commandserver import CommandServer
# import movesrvprss, movesrvoxvent, movesrvfuelvent

from . import armsrvfuelvent
from . import armsrvoxvent
from . import armsrvprss

@CommandServer.register('armrocketvalves')
def armrocketvalves(instance,args):

    armsrvfuelvent.armsrvfuelvent(instance)
    armsrvoxvent.armsrvoxvent(instance)
    armsrvprss.armsrvprss(instance)