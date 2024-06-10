from CommandServer.commandserver import CommandServer
# import movesrvprss, movesrvoxvent, movesrvfuelvent

from . import disarmsrvoxfill
from . import disarmsrvoxhosevent

@CommandServer.register('disarmgroundvalves')
def disarmgroundvalves(instance,args):
    disarmsrvoxfill.disarmsrvoxfill(instance,args)
    disarmsrvoxhosevent.disarmsrvoxhosevent(instance,args)