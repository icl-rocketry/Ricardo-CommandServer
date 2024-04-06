from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

enterflight_ap = Cmd2ArgumentParser()
enterflight_ap.add_argument("--argument",type=int,required=True)
@CommandServer.register('enterflight',argparse=enterflight_ap)
def enterflight(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":args['argument'],
                        "destination_service":2,
                        "command_id":104,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)