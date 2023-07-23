from dataclasses import dataclass


@dataclass
class ItemFilter:
    value: str or int or float

    def __init__(self, value: str or int or float) -> None:
        self.value = value


class FilterItemName(ItemFilter):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class FilterItemBrand(ItemFilter):
    def __init__(self, value: str) -> None:
        super().__init__(value)


class FilterItemRegion(ItemFilter):
    def __init__(self, value: str) -> None:
        super().__init__(value)
