import os

from . import vfs

cmds = {
    "exit": lambda args: exit(),
    "clear": lambda args: os.system("cls" if os.name == "nt" else "clear"),
    "echo": lambda args: print(" ".join(args)),
    "tree": lambda args: vfs.tree(),
    "ls": lambda args: vfs.ls(),
    "pwd": lambda args: print(vfs.pwd()),
    "cd": lambda args: vfs.cd(args[0]) if args else print("cd <folder>"),
    "touch": lambda args: vfs.touch(args[0]) if args else print("touch <file>")
}

cmds["help"] = lambda args: print(", ".join(cmds.keys()))