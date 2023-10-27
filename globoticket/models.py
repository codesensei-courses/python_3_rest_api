import decimal
from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declarative_base,
    mapped_column,
    reconstructor,
    relationship,
)

from globoticket.frontmatter import get_frontmatter

Base: DeclarativeBase = declarative_base()


class DBCategory(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    events: Mapped[list["DBEvent"]] = relationship(back_populates="category")


class DBEvent(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_code: Mapped[str] = mapped_column(unique=True)
    date: Mapped[date]
    price: Mapped[decimal.Decimal]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["DBCategory"] = relationship(back_populates="events")

    @reconstructor
    def _get_frontmatter(self):
        frontmatter = get_frontmatter(self.product_code)
        for k, v in frontmatter.items():
            if not hasattr(self, k):
                setattr(self, k, v)
