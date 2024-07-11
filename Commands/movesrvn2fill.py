from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

movesrvn2fill_ap = Cmd2ArgumentParser()
movesrvn2fill_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('movesrvn2fill',argparse=movesrvn2fill_ap)
def movesrvn2fill(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":104,
                        "destination_service":11,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)
