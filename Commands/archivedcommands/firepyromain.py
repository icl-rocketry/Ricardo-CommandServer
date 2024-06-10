from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

firepyromain_ap = Cmd2ArgumentParser()
firepyromain_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('firepyromain',argparse=firepyromain_ap)
def firepyromain(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":17,
                        "destination_service":11,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)