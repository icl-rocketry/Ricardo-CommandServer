from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

firepyrodelu_ap = Cmd2ArgumentParser()
firepyrodelu_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('firepyrodelu',argparse=firepyrodelu_ap)
def firepyrodelu(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":107,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)