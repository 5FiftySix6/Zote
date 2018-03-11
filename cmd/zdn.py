from qoid import *
import random
import time

print("########################")
print("    Zote, The Mighty")
print("by Conrad @the_complexor")
print("########################\n")

print("Initializing...")
start = time.time()

dir_logs = "data/log/"
if not os.path.exists(dir_logs):
    os.mkdir(dir_logs)


class ImgChannel:

    def __init__(self, name: str, links: list, tagged: bool):
        self.name = name
        self.tagged = tagged
        self.q = Qoid(tag=name)
        if tagged:
            for e in links:
                sp = e.split(":", 1)
                self.q.append(Property(tag=sp[0], val=sp[1].strip()))
        else:
            for e in links:
                self.q.append(Property(tag=e))
        self.current = Qoid(tag=name, val=list(self.q.val))

    def __getitem__(self, item):
        return self.q[item]

    def __len__(self):
        return len(self.q)

    def add(self, item):
        if isinstance(item, (Property, str)):
            to_add = item if isinstance(item, Property) else Property(tag=item, val=None)
            self.q.append(to_add)
            self.current.append(to_add)
            with open(f"img/{self.name}.cxr", "a") as f:
                f.write(str(to_add))
                f.write("\n")

    def remove(self, item):
        out = self.q.remove(item)
        with open(f"img/{self.name}.cxr", "w") as f:
            for e in self.q:
                f.write(f"{e}\n")
        return out

    def get_qoid(self):
        return self.q

    def r(self):
        if len(self.current) == 0:
            self.current = Qoid(tag=self.q.tag, val=list(self.q.val))
        elif len(self.current) == 1:
            next_img = self.current.pop(0)
            return next_img
        selection = random.randint(0, len(self.current) - 1)
        next_img = self.current.pop(selection)
        return next_img

    def tag(self):
        return self.q.tag


class ImgServer:

    def __init__(self):
        self.channels = Qoid(tag="img")

    def add(self, ch: ImgChannel):
        self.channels.append(Property(tag=ch.tag(), val=ch))

    def add_to(self, ch: str, to_add):
        if isinstance(to_add, Property):
            self[ch].add(to_add)
        elif isinstance(to_add, str):
            self[ch].add(Property(tag=to_add, val=None))

    def __getitem__(self, tag: str):
        return self.channels.get(tag=tag).val

    def __len__(self):
        return len(self.channels)


config = Index.open("data/config.cxr")

# blacklist = []
# with open("data/blacklist.zote", 'r+') as f:
#     for each in f.readlines():
#         blacklist.append(each.replace("\n", ""))
