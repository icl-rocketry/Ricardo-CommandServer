from CommandServer.commandserver import CommandServer
import time

@CommandServer.register('armsrvn2fill')
def armsrvn2fill(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":104,
                        "destination_service":11,
                        "command_id":3,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)

