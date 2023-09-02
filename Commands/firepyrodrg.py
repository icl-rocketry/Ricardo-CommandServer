from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

firepyrodrg_ap = Cmd2ArgumentParser()
firepyrodrg_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('firepyrodrg',argparse=firepyrodrg_ap)
def firepyrodrg(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":15,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)
