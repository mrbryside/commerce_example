from dataclasses import dataclass


@dataclass
class Customer:
    id: int = 0
    name: str = ""
    email: str = ""
