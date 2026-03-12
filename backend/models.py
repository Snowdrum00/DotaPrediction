from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Date, JSON, DateTime
from database import Base
from datetime import date

class Tournament(Base):
    __tablename__ = "tournaments"

    pageid: Mapped[int] = mapped_column(Integer, primary_key=True)
    pagename: Mapped[str] = mapped_column(String)

    bannerurl: Mapped[str] = mapped_column(String)
    bannerdarkurl: Mapped[str] = mapped_column(String)
    iconurl: Mapped[str] = mapped_column(String)
    icondarkurl: Mapped[str] = mapped_column(String)

    startdate: Mapped[date] = mapped_column(Date)
    enddate: Mapped[date] = mapped_column(Date)
    sortdate: Mapped[date] = mapped_column(Date)

    name: Mapped[str] = mapped_column(String)
    prizepool: Mapped[int] = mapped_column(Integer)
    participantsnumber: Mapped[int] = mapped_column(Integer)
    liquipediatier: Mapped[str] = mapped_column(String)
    format: Mapped[str] = mapped_column(String)

    placementstructure: Mapped[list[str]] = mapped_column(JSON)

class Participant(Base):
    __tablename__ = "participant"

    pageid: Mapped[int] = mapped_column(Integer, primary_key=True)
    pagename: Mapped[str] = mapped_column(String)

    imageurl: Mapped[str] = mapped_column(String)
    imagedarkurl: Mapped[str] = mapped_column(String)

    placement: Mapped[str] = mapped_column(String)
    prizemoney: Mapped[int] = mapped_column(Integer)

    lastvsdata: Mapped[dict] = mapped_column(JSON)

    opponentname: Mapped[str] = mapped_column(String)
    opponentplayers: Mapped[dict] = mapped_column(JSON)

