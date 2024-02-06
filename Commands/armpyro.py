from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

armpyro_ap = Cmd2ArgumentParser()
armpyro_ap.add_argument("--destinationnode",type=int,required=True)
armpyro_ap.add_argument("--destinationservice",type=int,required=True)
@CommandServer.register('armpyro',argparse=armpyro_ap)
def armpyro(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":3,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)