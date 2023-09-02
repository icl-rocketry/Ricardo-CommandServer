from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

ignitethanos_ap = Cmd2ArgumentParser()
ignitethanos_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('ignitethanos',argparse=ignitethanos_ap)
def ignitethanos(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":9,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":1}

    instance.send_command_packet(command_packet_args)