from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

firepyroeng_ap = Cmd2ArgumentParser()
firepyroeng_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('firepyroeng',argparse=firepyroeng_ap)
def firepyroeng(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":107,
<<<<<<< HEAD
<<<<<<< HEAD
                        "destination_service":12,
=======
                        "destination_service":10,
>>>>>>> 81c1bab (hotfire - 9/2/24 v1)
=======
                        "destination_service":12,
>>>>>>> eabd863 (Added More hotfire commands)
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)