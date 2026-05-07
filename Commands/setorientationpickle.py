from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

setorientationpickle_ap = Cmd2ArgumentParser()
setorientationpickle_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('setorientationpickle',argparse=setorientationpickle_ap)
def setorientationpickle(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['argument'],
                        "destination_service":2,
                        "command_id":44,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)