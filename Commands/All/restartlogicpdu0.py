from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

restartlogicpdu0_ap = Cmd2ArgumentParser()
restartlogicpdu0_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('restartlogicpdu0',argparse=restartlogicpdu0_ap)
def restartlogicpdu0(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":6,
                        "destination_service":2,
                        "command_id":3,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)