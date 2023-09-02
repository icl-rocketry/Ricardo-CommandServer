from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

restartlogic_ap = Cmd2ArgumentParser()
restartlogic_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('restartlogic',argparse=restartlogic_ap)
def restartlogic(instance,args):

    command_packet_args = {"source":1,
                        "source_service":2,
                        "destination":11,
                        "destination_service":2,
                        "command_id":3,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)