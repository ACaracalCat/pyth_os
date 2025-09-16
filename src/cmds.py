import os

from . import vfs

cmds = {
    "exit": lambda args: exit(),
    "clear": lambda args: os.system("cls" if os.name == "nt" else "clear"),
    "echo": lambda args: print(" ".join(args)),
    "ls": lambda args: vfs.ls(),
    "pwd": lambda args: print(vfs.pwd()),
    "cd": lambda args: vfs.cd(args[0]) if args else print("cd <folder>"),
    "touch": lambda args: vfs.touch(args[0]) if args else print("touch <file>"),
    "mkdir": lambda args: vfs.mkdir(args[0]) if args else print("mkdir <folder>"),
    "write": lambda args: vfs.write(args[0], " ".join(args[1:])) if len(args) >= 2 else print("write <file> <content>"),
    "cat": lambda args: vfs.cat(args[0]) if args else print("cat <file>"),
    "rm": lambda args: vfs.rm(args[0], args[1] if len(args) > 1 else None) if args else print("rm <node> <flag>"),
    "rmdir": lambda args: vfs.rmdir(args[0]) if args else print("rmdir <folder>"),
}

cmds["help"] = lambda args: print(", ".join(cmds.keys()))
