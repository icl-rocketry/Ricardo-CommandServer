from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

TVCarmed_ap = Cmd2ArgumentParser()
@CommandServer.register('TVCarmed',argparse=TVCarmed_ap)
def TVCarmed(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":102,
                        "destination_service":10,
                        "command_id":13,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)