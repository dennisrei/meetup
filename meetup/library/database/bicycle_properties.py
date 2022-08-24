import dataclasses


@dataclasses.dataclass
class BicycleProperties:
    password: str
    user: str
    connection_string: str
