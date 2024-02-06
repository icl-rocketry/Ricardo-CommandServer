from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

moveoxsrvthanos_ap = Cmd2ArgumentParser()
moveoxsrvthanos_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('moveoxsrvthanos',argparse=moveoxsrvthanos_ap)
def moveoxsrvthanos(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":12,
                        "destination_service":10,
                        "command_id":7,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)