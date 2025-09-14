from typing import Union, Dict, Any

File = Dict[str, str]
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
            tree(f, pre + " ")

def ls():
    dir = _rd()
    for name in dir:
        print(name)


def pwd():
    return "/" + "/".join(path)

def cd(f: str):
    dir = _rd()
    if f == "..":
        if path != ["root"]:
            path.pop()
    elif f in dir:
        if "content" not in dir[f]:
            path.append(f)
        else:
            print(f"can't cd into a file: {f}")
    else:
        print(f"file not found: {pwd()}/{f}")

def touch(f):
    dir = _rd()
    if path == ["root"]:
        print(f"cannot create {f} at /root")
    elif f in dir:
        print(f"{f} already exists")
    elif not any(f.endswith(e) for e in extensions):
        print(f"unknown file extension: {f}")
    else:
        dir[f] = {"content": ""}

def mkdir(f):
    dir = _rd()
    if path == ["root"]:
        print(f"cannot create {f} at /root")
    elif f in dir:
        print(f"{f} already exists")
    elif any(f.endswith(e) for e in extensions):
        print(f"folder cannot have file extension: {f}")
    else:
        dir[f] = {}

def write(f, c):
    dir = _rd()
    if any(f.endswith(e) for e in extensions):
        dir[f] = {"content": c}
    else:
        print(f"cannot write to a folder: {f}")

def cat(f: str):
    dir = _rd()
    if f not in dir:
        print(f"file not found: {f}")
        return

    if "content" in dir[f]:
        print(dir[f]["content"])
    else:
        print(f"cannot view content of folder: {f}")


