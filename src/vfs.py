fs = {
    "root": {
        "documents": {}
    }
}

path = ["root"]

extensions = [".txt"] # w i p

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
        if isinstance(f, dict):
            tree(f, pre + " ")

def ls():
    dir = _rd()
    for name in dir:
        print(name)


def pwd():
    return "/" + "/".join(path)

def cd(f):
    dir = _rd()
    if f == "..":
        if path != ["root"]:
            path.pop()
    elif f in dir:
        path.append(f)
    else:
        print(f"file not found: {_rd}/{f}")

def touch(f): # w i p (makes folders only for now)
    dir = _rd()
    if path == ["root"]:
        print(f"cannot create folder at /root: {f}")
    elif f in dir:
        print(f"{f} already exists")
    else:
        dir[f] = {}


# w i p
def write(f, c):
    pass

def cat(f):
    pass

