from CommandServer.commandserver import CommandServer

@CommandServer.register('armprop1')
def armprop1(instance,args):

    command_packet_args = {"source":1,
                        "source_service":instance.source_service,
                        "destination":103,
                        "destination_service":11,
                        "command_id":3,
                        "command_arg":0}

    instance.send_command_packet(command_packet_args)

