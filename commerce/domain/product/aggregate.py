import copy
from entities.item_filter import (
    FilterItemBrand,
    FilterItemName,
    FilterItemRegion,
    ItemFilter,
)
from entities.item import Item
from typing import Any, Dict


class ProductAggregate:
    is_valid: bool
    error: ValueError

    # ---- factory method ----#
    def __init__(
        self,
        name: str,
        brand: str,
        region: str,
        stock: int,
        price: float,
    ):
        self.__product: Item = Item(name=name, brand=brand, region=region, stock=stock)
        self.__price: float = price
        self.__quantity: int = 0
        self.__product_filter: Dict[str, ItemFilter] = {}

    @classmethod
    def from_filter_only(cls) -> "ProductAggregate":
        instance: ProductAggregate = cls.__new__(cls)
        instance.__product = Item()
        instance.__price = 0.0
        instance.__product_filter = {}
        return instance

    @classmethod
    def from_including_id(
        cls, id: int, name: str, brand: str, region: str, stock: int, price: float
    ) -> "ProductAggregate":
        instance = cls.__new__(cls)
        instance.__product = Item(
            id=id,
            name=name,
            brand=brand,
            region=region,
            stock=stock,
        )
        instance.__price = price
        return instance

    # ---- property method ----#
    @property
    def product(self):
        return copy.deepcopy(self.__product)

    @property
    def product_filter(self) -> Dict[str, ItemFilter]:
        return copy.deepcopy(self.__product_filter)

    @property
    def price(self) -> float:
        return copy.deepcopy(self.__price)

    @property
    def quantity(self) -> int:
        return copy.deepcopy(self.__quantity)

    # ---- business method ----#
    def addItemFilter(self, filterName: str, filterValue: str):
        if filterName not in ["name", "brand", "region"]:
            return
        filterMapping: Dict[str, ItemFilter] = {
            "name": FilterItemName(filterValue),
            "brand": FilterItemBrand(filterValue),
            "region": FilterItemRegion(filterValue),
        }
        itemFilter: ItemFilter | None = filterMapping.get(filterName)
        if itemFilter is not None:
            self.__product_filter.update({filterName: itemFilter.value})

    # -- serializer -- #
    def toDict(self) -> Dict[str, Any]:
        return {
            "id": self.__product.id,
            "name": self.__product.name,
            "brand": self.__product.brand,
            "region": self.__product.region,
            "stock": self.__product.stock,
            "price": self.__price,
        }
