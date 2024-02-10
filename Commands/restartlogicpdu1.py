from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

restartlogicpdu1_ap = Cmd2ArgumentParser()
restartlogicpdu1_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('restartlogicpdu1',argparse=restartlogicpdu1_ap)
def restartlogicpdu1(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":105,
                        "destination_service":2,
                        "command_id":3,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)