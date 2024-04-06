from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

@CommandServer.register('disarmall')
def disarmall(instance,args):

    args['destination'] = 5
    args['destination_service'] = 10
    instance.disarmpyro(args)

    args['destination'] = 6
    args['destination_service'] = 10
    instance.disarmpyro(args)

    args['destination'] = 5
    args['destination_service'] = 11
    instance.disarmpyro(args)

    args['destination'] = 6
    args['destination_service'] = 11
    instance.disarmpyro(args)

    args['destination'] = 5
    args['destination_service'] = 12
    instance.disarmpyro(args)

    args['destination'] = 6
    args['destination_service'] = 12
    instance.disarmpyro(args)