from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser
import time

armsolenoid_ap = Cmd2ArgumentParser()
armsolenoid_ap.add_argument("--channel",type=int,required=True)
@CommandServer.register('armsolenoid')
def armsolenoid(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":107,
                        "destination_service":args['channel'], # 11 through 13
                        "command_id":3,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)