from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

disarmsolenoid_ap = Cmd2ArgumentParser()
disarmsolenoid_ap.add_argument("--channel",type=int,required=True)
@CommandServer.register('disarmsolenoid')
def disarmsolenoid(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":111,
                        "destination_service":args['channel'], # 11 through 13
                        "command_id":4,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)