from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

movesrvfuelvent_ap = Cmd2ArgumentParser()
movesrvfuelvent_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('movesrvfuelvent',args=movesrvfuelvent_ap)
def movesrvfuelvent(instance,args):

    command_packet_args = {"source":1,
                        "source_service":2,
                        "destination":9,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)
