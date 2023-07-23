from dataclasses import dataclass


@dataclass
class Item:
    id: int = 0
    name: str = ""
    brand: str = ""
    region: str = ""
    stock: int = 0
    quantity: int = 0
