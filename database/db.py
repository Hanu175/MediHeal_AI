from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Float,
)
from sqlalchemy.orm import declarative_base, sessionmaker

from config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Interaction(Base):

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)

    agent = Column(String, nullable=False)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow,
    )

    execution_time = Column(Float)

    status = Column(String, default="SUCCESS")

    user_input = Column(Text)

    response = Column(Text)


def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized")


def save_interaction(
    agent,
    user_input,
    response,
    execution_time=None,
    status="SUCCESS",
):

    session = SessionLocal()

    interaction = Interaction(
        agent=agent,
        timestamp=datetime.utcnow(),
        execution_time=execution_time,
        status=status,
        user_input=user_input,
        response=response,
    )

    session.add(interaction)

    session.commit()

    session.close()


def get_history():

    session = SessionLocal()

    rows = (
        session.query(Interaction)
        .order_by(Interaction.id.desc())
        .all()
    )

    session.close()

    return rows