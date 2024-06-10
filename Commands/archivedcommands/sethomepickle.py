from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

sethomepickle_ap = Cmd2ArgumentParser()
sethomepickle_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('sethomepickle',argparse=sethomepickle_ap)
def sethomepickle(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['argument'],
                        "destination_service":2,
                        "command_id":4,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)