from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

movefuelsrvthanos_ap = Cmd2ArgumentParser()
movefuelsrvthanos_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('movefuelsrvthanos',argparse=movefuelsrvthanos_ap)
def movefuelsrvthanos(instance,args):

    command_packet_args = {"source":1,
                        "source_service":2,
                        "destination":7,
                        "destination_service":10,
                        "command_id":6,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)