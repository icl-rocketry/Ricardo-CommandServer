from CommandServer.commandserver import CommandServer
from cmd2 import Cmd2ArgumentParser

GNCprop_ap = Cmd2ArgumentParser()
GNCprop_ap.add_argument("--argument",type=int,required=True)
GNCprop_ap.add_argument("--channel",type=int,required=True)
@CommandServer.register('GNCprop')
def GNCprop(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":103,
                        "destination_service":args['channel'],
                        "command_id":2,
                        "command_arg":args['argument']}

    instance.send_command_packet(command_packet_args)

