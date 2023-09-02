from CommandServer.commandserver import CommandServer
import time

@CommandServer.register('disarmsrvprss')
def disarmsrvprss(instance,args):

    command_packet_args = {"source":1,
                        "source_service":2,
                        "destination":9,
                        "destination_service":11,
                        "command_id":4,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)
