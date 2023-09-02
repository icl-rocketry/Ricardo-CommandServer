from CommandServer.commandserver import CommandServer
import time


@CommandServer.register('golivepdu')
def golivepdu(instance,args):

    command_packet_args = {"source":1,
                        "source_service":2,
                        "destination":11,
                        "destination_service":2,
                        "command_id":2,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)