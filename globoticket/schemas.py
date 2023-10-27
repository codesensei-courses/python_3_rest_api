import datetime
import decimal

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    date: datetime.date
    price: decimal.Decimal
