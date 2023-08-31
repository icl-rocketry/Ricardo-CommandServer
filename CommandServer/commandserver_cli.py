import cmd2
from cmd2.decorators import with_argparser
import time

class CommandServerCLI(cmd2.Cmd):
    def __init__(self):
        super().__init__(allow_cli_args=False)

    def run(self):
        return self._cmdloop_reimplementation()
        
    #literally stolen from cmd2 cmdloop and _cmdloop implementation with the addition of time.sleep(0) so that 
    #we can run this in a thread lol

    def _cmdloop_reimplementation(self):
        # Register a SIGINT signal handler for Ctrl+C

        # Grab terminal lock before the command line prompt has been drawn by readline
        self.terminal_lock.acquire()

        # Always run the preloop first
        for func in self._preloop_hooks:
            func()
        self.preloop()


        stop = False
        saved_readline_settings = None

        try:
            # Get sigint protection while we set up readline for cmd2
            with self.sigint_protection:
                saved_readline_settings = self._set_up_cmd2_readline()

            # Run startup commands
            stop = self.runcmds_plus_hooks(self._startup_commands)
            self._startup_commands.clear()

            while not stop:
                # Get commands from user
                try:
                    line = self._read_command_line(self.prompt)
                except KeyboardInterrupt:
                    self.poutput('^C')
                    line = ''

                # Run the command along with all associated pre and post hooks
                stop = self.onecmd_plus_hooks(line)
                time.sleep(0)
        finally:
            # Get sigint protection while we restore readline settings
            with self.sigint_protection:
                if saved_readline_settings is not None:
                    self._restore_readline(saved_readline_settings)

        # Run the postloop() no matter what
        for func in self._postloop_hooks:
            func()
        self.postloop()

        # Release terminal lock now that postloop code should have stopped any terminal updater threads
        # This will also zero the lock count in case cmdloop() is called again
        self.terminal_lock.release()

        return self.exit_code


    #this is a classmethod so we add new member functions before the class is instantiated, so that
    #cmd2 correctly processes the new member functions
    @classmethod
    def register_command(cls,command_name:str = None, parser = None,command_func = None):

        if command_name is None: 
            raise Exception('command_name cannot be empty')
        
        if command_func is None: 
            raise Exception('command_func cannot be empty')
        
        cli_command_name = "do_" + command_name

        def wrapper(instance,args=None):
            #command_func expects args as a dict, so we need to convert the namespace
            command_func(vars(args))
        
        if parser is not None:
            #register command with argparser
            wrapper = with_argparser(parser=parser)(wrapper)

        #add this new wrapped command as a member function with the "do" prefix so cmd2 registers this as a command
        setattr(cls,cli_command_name,wrapper)
