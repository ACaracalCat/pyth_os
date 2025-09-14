import os

from . import vfs
from .version import VERSION

cmds = {
    "exit": lambda args: exit(),
    "clear": lambda args: os.system("cls" if os.name == "nt" else "clear"),
    "echo": lambda args: print(" ".join(args)),
    "ver": lambda args: print(f"{VERSION}"),
    "tree": lambda args: vfs.tree(),
    "ls": lambda args: vfs.ls(),
    "pwd": lambda args: print(vfs.pwd()),
    "cd": lambda args: vfs.cd(args[0]) if args else print("cd <folder>"),
    "touch": lambda args: vfs.touch(args[0]) if args else print("touch <file>"),
    "mkdir": lambda args: vfs.mkdir(args[0]) if args else print("mkdir <folder>"),
    "write": lambda args: vfs.write(args[0], args[1]) if len(args) > 2 else print("write <file> <content>"),
    "cat": lambda args: vfs.cat(args[0]) if args else print("cat <file>")
}

cmds["help"] = lambda args: print(", ".join(cmds.keys()))