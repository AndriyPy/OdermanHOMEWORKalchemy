from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column

DB = "sqlite:///app.db"
engine = create_engine(DB, echo=True)

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    ...

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(240), nullable=True)
    pizzaname: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"Pizzaname:{self.pizzaname}, description:{self.description}"

def create_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)
