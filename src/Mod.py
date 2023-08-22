from typing import Dict, Tuple, List
import os.path

def stringify(v: str) -> str:
    return repr(v).replace("'", "\x00").replace('"', "'").replace('\x00', '"')

class TraditionCategory(object):
    def __init__(self, name: str, tree: str):
        self.name = name
        self.tree = tree
        self.desc = None
        self.tradition_adopt = None
        self.tradition_1 = None
        self.tradition_2 = None
        self.tradition_3 = None
        self.tradition_4 = None
        self.tradition_5 = None
        self.tradition_finish = None

    def get_traditions(self) -> List[str]:
        return [self.tradition_1, self.tradition_2, self.tradition_3, self.tradition_4, self.tradition_5]

class Tradition(object):
    def __init__(self, name: str, status: str = None, of: TraditionCategory = None):
        assert(status in [None, "adopt", "finish"])
        self.name = name
        self.status = status
        self.of = of

    def dup_with_status(self, status: str, mod):
        assert(status in [None, "adopt", "finish"])
        if mod is not None:
            assert(status not in mod.traditions)
        tr = Tradition(self.name, status, self.of)
        return tr

    def get_name(self) -> str:
        if self.status is None:
            return self.name
        elif self.status == "adopt":
            return self.name + "_adopt"
        elif self.status == "finish":
            return self.name + "_finish"

class Technology(object):
    def __init__(self, name: str, domain: str, category: str):
        self.name = name
        self.domain = domain
        self.category = category

class Mod(object):
    def __init__(self, name: str):
        self.name: str = name
        self.game_version: Tuple[int, int, int] = (3, 8, 4)
        self.mod_version: Tuple[int, int, int] = (1, 0, 0)
        self.tags: List[str] = []
        self.require_traditions: List[str] = []
        self.tradition_categories: Dict[str, TraditionCategory] = {}
        self.traditions: Dict[str, Tradition] = {}
        self.technology: Dict[str, Technology] = {}

    def set_game_version(self, game_version: Tuple[int, int, int]):
        self.game_version = game_version

    def set_mod_version(self, mod_version: Tuple[int, int, int]):
        self.mod_version = mod_version

    def add_technology(self, name: str, domain: str, category: str):
        self.technology[name] = Technology(name, domain, category)

    def add_tradition(self, name: str, status: str = None, of: TraditionCategory = None):
        tr = Tradition(name, status, of)
        pretrad = name + "_adopt"
        preftrad = name + "_finish"
        self.traditions[tr.get_name()] = tr

    def set_tradition_for_categories(self, cat: str, trad: str, pos: int):
        assert(pos >= -1 and pos <= 5) # 0 = adopt, -1 = finish, 1~5 as expected
        if pos == 0:
            pretrad = trad + "_adopt"
            preftrad = trad + "_finish"
            if pretrad not in self.traditions:
                if pretrad not in self.require_traditions:
                    if trad in self.traditions:
                        tr = self.traditions[trad].dup_with_status("adopt", self)
                        assert(tr.get_name() == pretrad)
                        self.traditions[pretrad] = tr
                    elif preftrad in self.traditions:
                        tr = self.traditions[preftrad].dup_with_status("adopt", self)
                        assert(tr.get_name() == pretrad)
                        self.traditions[pretrad] = tr
                    else:
                        self.require_traditions.append(pretrad)
            self.tradition_categories[cat].tradition_adopt = pretrad
        elif pos == -1:
            pretrad = trad + "_adopt"
            preftrad = trad + "_finish"
            if preftrad not in self.traditions:
                if preftrad not in self.require_traditions:
                    if trad in self.traditions:
                        tr = self.traditions[trad].dup_with_status("finish", self)
                        assert(tr.get_name() == preftrad)
                        self.traditions[preftrad] = tr
                    elif pretrad in self.traditions:
                        tr = self.traditions[pretrad].dup_with_status("finish", self)
                        assert(tr.get_name() == preftrad)
                        self.traditions[preftrad] = tr
                    else:
                        self.require_traditions.append(preftrad)
            self.tradition_categories[cat].tradition_finish = preftrad
        else:
            pretrad = trad + "_adopt"
            preftrad = trad + "_finish"
            if trad not in self.traditions:
                if trad not in self.require_traditions:
                    if preftrad in self.traditions:
                        tr = self.traditions[preftrad].dup_with_status(None, self)
                        assert(tr.get_name() == trad)
                        self.traditions[trad] = tr
                    elif pretrad in self.traditions:
                        tr = self.traditions[pretrad].dup_with_status(None, self)
                        assert(tr.get_name() == trad)
                        self.traditions[trad] = tr
                    else:
                        self.require_traditions.append(trad)
            setattr(self.tradition_categories[cat], "tradition_" + {
                1:"1", 2:"2", 3:"3", 4:"4", 5:"5"
            }[pos], trad)

    def add_tradition_categories(self, name: str, tree: str):
        self.tradition_categories[name] = TraditionCategory(name, tree)

    def add_tags(self, tag: str) -> bool:
        if tag not in self.tags:
            self.tags.append(tag)
        else:
            print("duplicate tag :", repr(tag))

    def generate_descriptor(self) -> str:
        return ("name=" + repr(self.name) + "\n" + \
                "tags={\n" + \
                "\t" + "\n\t".join(map(lambda x:repr(x.capitalize()), self.tags)) + "\n" + \
                "}\n" + \
                "version=" + repr(".".join(map(str, self.mod_version if self.mod_version else (1, 0, 0)))) + "\n" + \
                "supported_version=" + repr(".".join(map(str, self.game_version if self.game_version else (3, 8, 4)))) + "\n" + \
                "\n").replace("'", '"')

    def tradition_name(self, name: str) -> str:
        return f"tr_{self.name}_{name}"

    def tradition_categories_name(self, name: str) -> str:
        return f"tradition_{self.name}_{name}"

    def generate_tradition_category(self, name: str) -> str:
        trad = self.tradition_categories[name]
        return\
            self.tradition_categories_name(name) + " = {\n" + \
            f"\ttree_template = {stringify(trad.tree)}\n" + \
            f"\tadoptation_bonus = {stringify(self.tradition_name(trad.tradition_adopt))}\n" + \
            f"\tfinish_bonus = {stringify(self.tradition_name(trad.tradition_finish))}\n" + \
            "\ttraditions = {\n" + \
            f"\t\t{stringify(self.tradition_name(trad.tradition_1))}\n" + \
            f"\t\t{stringify(self.tradition_name(trad.tradition_2))}\n" + \
            f"\t\t{stringify(self.tradition_name(trad.tradition_3))}\n" + \
            f"\t\t{stringify(self.tradition_name(trad.tradition_4))}\n" + \
            f"\t\t{stringify(self.tradition_name(trad.tradition_5))}\n" + \
            "\t}\n" + \
            "}"

    def generate_tradition_categories(self) -> str:
        return "\n\n".join([self.generate_tradition_category(name) for name in self.tradition_categories])

    def generate_tradition(self, name: str) -> str:
        return self.tradition_name(name) + " = {\n" + \
            "}"

    def generate_traditions(self) -> str:
        return "\n\n".join([self.generate_tradition(name) for name in self.traditions])

    def fname(self) -> str:
        return f"00_{self.name}.txt"

    def generate_governments(self) -> str:
        return {}

    def generate_interface(self) -> str:
        return {}

    def generate_gfx(self) -> str:
        return {}

    def generate_localisation(self) -> str:
        return {}

    def generate_events(self) -> str:
        return {}


    def generate_common(self) -> Dict[str, str]:
        return {
            os.path.join("tradition_categories", self.fname()): self.generate_tradition_categories(),
            os.path.join("traditions", self.fname()): self.generate_traditions(),
            **{os.path.join("governments", file_name): content for file_name, content in self.generate_governments().items() if content}
        }

    def generate_all_the_data(self) -> Dict[str, str]:
        print(self.require_traditions)
        return {
            "descriptor.mod": self.generate_descriptor(),
            **{os.path.join("common", file_name): content for file_name, content in self.generate_common().items() if content},
            **{os.path.join("interface", file_name): content for file_name, content in self.generate_interface().items() if content},
            **{os.path.join("gfx", file_name): content for file_name, content in self.generate_gfx().items() if content},
            **{os.path.join("localisation", file_name): content for file_name, content in self.generate_localisation().items() if content},
            **{os.path.join("events", file_name): content for file_name, content in self.generate_events().items() if content},
        }