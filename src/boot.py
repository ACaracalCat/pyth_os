from .cmds import cmds
import src.vfs as vfs

def readln():
    ln = input(f"{vfs.pwd()} pyth_os % ")
    args = ln.split()[1:]
    cmd = ln.split()[0]

    if cmd in cmds:
        cmds[cmd](args)
    else:
        print(f"unknown command: {cmd}")
