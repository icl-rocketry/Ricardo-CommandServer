import cmd2
from threading import Thread


class CmdUI(cmd2.Cmd):
    pass

if __name__ == '__main__':
    app = CmdUI()
    t = Thread(target=app.cmdloop())
    t.run()