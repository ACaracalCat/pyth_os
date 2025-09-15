from typing import Dict, Any

Folder = Dict[str, Any]

fs: Folder = {
    "root": {
        "documents": {},
        "downloads": {}
    }
}

path = ["root"]
extensions = [".txt"]

def _rd():
    dir = fs
    for p in path:
        dir = dir[p]
    return dir

def tree(d=None, pre=""):
    if d is None:
        d = fs
    for name, f in d.items():
        print(pre + name)
        if isinstance(f, dict) and "content" not in f:
            tree(f, pre + "  ")

def ls():
    for name in _rd():
        print(name)

def pwd():
    return "/" + "/".join(path)

def cd(f: str):
    dir = _rd()
    if f == "..":
        if path != ["root"]:
            path.pop()
        return
    if f not in dir:
        print(f"pyth_os: cd: {f}: No such file or directory")
        return
    if "content" in dir[f]:
        print(f"pyth_os: cd: {f}: Not a directory")
        return
    path.append(f)

def touch(f: str):
    dir = _rd()
    if path == ["root"]:
        print(f"pyth_os: touch: cannot create file '{f}' in '/root'")
        return
    if f in dir:
        print(f"pyth_os: touch: cannot create file '{f}': File exists")
        return
    if not any(f.endswith(e) for e in extensions):
        print(f"pyth_os: touch: unknown file type '{f}'")
        return
    dir[f] = {"content": ""}

def mkdir(f: str):
    dir = _rd()
    if path == ["root"]:
        print(f"pyth_os: mkdir: cannot create directory '{f}' in '/root'")
        return
    if f in dir:
        print(f"pyth_os: mkdir: cannot create directory '{f}': File exists")
        return
    if any(f.endswith(e) for e in extensions):
        print(f"pyth_os: mkdir: invalid directory name '{f}'")
        return
    dir[f] = {}

def write(f: str, c: str):
    dir = _rd()
    if f not in dir:
        print(f"pyth_os: {f}: No such file")
        return
    if "content" not in dir[f]:
        print(f"pyth_os: {f}: Is a directory")
        return
    dir[f]["content"] = c

def cat(f: str):
    dir = _rd()
    if f not in dir:
        print(f"pyth_os: cat: {f}: No such file or directory")
        return
    if "content" not in dir[f]:
        print(f"pyth_os: cat: {f}: Is a directory")
        return
    print(dir[f]["content"])

def rm(f: str, t=None):
    dir = _rd()
    if f not in dir:
        print(f"pyth_os: rm: cannot remove '{f}': No such file or directory")
        return
    if "content" not in dir[f]:
        if t == "-r" or not dir[f]:
            del dir[f]
        else:
            print(f"pyth_os: rm: cannot remove '{f}': Is a directory")
        return
    del dir[f]

def rmdir(f: str):
    dir = _rd()
    if f not in dir:
        print(f"pyth_os: rmdir: failed to remove '{f}': No such file or directory")
        return
    if "content" in dir[f]:
        print(f"pyth_os: rmdir: failed to remove '{f}': Not a directory")
        return
    if dir[f]:
        print(f"pyth_os: rmdir: failed to remove '{f}': Directory not empty")
        return
    del dir[f]
