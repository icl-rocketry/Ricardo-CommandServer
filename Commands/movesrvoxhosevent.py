from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

movesrvoxhosevent_ap = Cmd2ArgumentParser()
movesrvoxhosevent_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('movesrvoxhosevent',argparse=movesrvoxhosevent_ap)
def movesrvoxhosevent(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":100,
                        "destination_service":11,
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)
