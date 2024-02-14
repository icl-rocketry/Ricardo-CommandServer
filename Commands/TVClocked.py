from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

TVClocked_ap = Cmd2ArgumentParser()
@CommandServer.register('TVClocked',argparse=TVClocked_ap)
def TVClocked(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":102,
                        "destination_service":10,
                        "command_id":10,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)