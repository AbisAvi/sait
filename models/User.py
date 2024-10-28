from dataclasses import dataclass, asdict


@dataclass
class User:
    id: int
    name: str

    def __dict__(self):
        return asdict(self)
