from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

disarmpyro_ap = Cmd2ArgumentParser()
disarmpyro_ap.add_argument("--destinationnode",type=int,required=True)
disarmpyro_ap.add_argument("--destinationservice",type=int,required=True)
@CommandServer.register('disarmpyro',argparse=disarmpyro_ap)
def disarmpyro(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":4,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)