import datetime
import decimal

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    # product_code: str
    date: datetime.date
    price: decimal.Decimal
    artist: str
    name: str
    content: str
    image: str
