from typing import Dict, Tuple, List
import os.path

class TraditionCategory(object):
    def __init__(self, name: str, tree: str):
        self.name = name
        self.tree = tree
        self.tradition_adopt = None
        self.tradition_1 = None
        self.tradition_2 = None
        self.tradition_3 = None
        self.tradition_4 = None
        self.tradition_5 = None
        self.tradition_finish = None

class Tradition(object):
    pass

class Mod(object):
    def __init__(self, name: str):
        self.name: str = name
        self.game_version: Tuple[int, int, int] = (3, 8, 4)
        self.mod_version: Tuple[int, int, int] = (1, 0, 0)
        self.tags: List[str] = []
        self.tradition_categories: Dict[str, TraditionCategory] = {}
        self.traditions: Dict[str, Tuple[bool, bool, bool, Tradition]] = {}

    def add_technology(self, name: str, domain: str, category: str):
        pass

    def add_tradition(self, name: str):
        pass

    def set_tradition_for_categories(self, cat: str, trad: str, pos: int):
        assert(pos >= -1 and pos <= 5) # 0 = adopt, -1 = finish, 1~5 as expected

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
                "version=" + repr(".".join(map(str, self.mod_version))) + "\n" + \
                "supported_version=" + repr(".".join(map(str, self.game_version))) + "\n" + \
                "\n").replace("'", '"')

    def generate_tradition_categories(self) -> str:
        return ""

    def generate_traditions(self) -> str:
        return ""

    def generate_common(self) -> Dict[str, str]:
        return {
            os.path.join("tradition_categories", self.name + ".txt"): self.generate_tradition_categories(),
            os.path.join("traditions", self.name + ".txt"): self.generate_traditions(),
        }

    def generate_all_the_data(self) -> Dict[str, str]:
        return {
            "descriptor.mod": self.generate_descriptor(), \
            **{os.path.join("common", file_name): content for file_name, content in self.generate_common().items() if content}
        }