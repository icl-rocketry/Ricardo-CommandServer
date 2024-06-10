from CommandServer.commandserver import CommandServer
# import movesrvprss, movesrvoxvent, movesrvfuelvent

from . import armsrvoxfill
from . import armsrvoxhosevent

@CommandServer.register('armgroundvalves')
def armgroundvalves(instance,args):
    armsrvoxfill.armsrvoxfill(instance,args)
    armsrvoxhosevent.armsrvoxhosevent(instance,args)