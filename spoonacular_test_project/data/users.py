import dataclasses


@dataclasses.dataclass
class User:
    login: str
    email: str
    password: str

