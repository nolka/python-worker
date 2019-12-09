import multiprocessing

from command.commands.shell_exec import ShellExecCommand
from command.responses.response import BaseResponse
from command.command import CommandFactory, Invoker
from command.source import get_stdin

def worker_func(job):
    cmdmap = {
        'shell.exec': ShellExecCommand
    }

    invoker = Invoker(cmdmap)
    for x in range(1000000000):
        pass
    result = invoker.invoke('shell.exec', dict(uuid=job))
    print(result.code)
    print(result.uuid)

def main():
    with multiprocessing.Pool(processes=4) as p:
        for cmd in get_stdin():
            if cmd == 'qq':
                break
            p.map_async(worker_func, (cmd, ))


if __name__ == '__main__':
    main()
