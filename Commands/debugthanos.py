from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

debugthanos_ap = Cmd2ArgumentParser()
debugthanos_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('debugthanos',argparse=debugthanos_ap)
def debugthanos(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":102,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)