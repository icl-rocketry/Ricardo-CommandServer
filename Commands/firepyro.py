from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

firepyro_ap = Cmd2ArgumentParser()
firepyro_ap.add_argument("--destinationnode",type=int,required=True)
firepyro_ap.add_argument("--destinationservice",type=int,required=True)
firepyro_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('firepyro',argparse=firepyro_ap)
def firepyro(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['destination'],
                        "destination_service":args['destination_service'],
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)