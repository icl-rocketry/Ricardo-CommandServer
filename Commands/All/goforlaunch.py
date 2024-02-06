from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

goforlaunch_ap = Cmd2ArgumentParser()
goforlaunch_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('goforlaunch',argparse=goforlaunch_ap)
def goforlaunch(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['argument'],
                        "destination_service":2,
                        "command_id":1,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)