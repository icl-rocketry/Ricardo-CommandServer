from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

TVCpretestcalibration_ap = Cmd2ArgumentParser()
@CommandServer.register('TVCpretestcalibration',argparse=TVCpretestcalibration_ap)
def TVCpretestcalibration(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":102,
                        "destination_service":10,
                        "command_id":2,
                        "command_arg":4}

    instance.send_command_packet(command_packet_args)