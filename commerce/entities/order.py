from dataclasses import dataclass
import datetime
import uuid


@dataclass
class Order:
    id: int = 0
    order_id: uuid.UUID = uuid.uuid1()
    name: str = ""
    place_date: datetime.datetime = datetime.datetime.now()
