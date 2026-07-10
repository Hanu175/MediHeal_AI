from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Float,
    func,
)

from sqlalchemy.orm import declarative_base, sessionmaker

from config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Interaction(Base):

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)

    agent = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow,
    )

    execution_time = Column(Float)

    status = Column(String)

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


# ===================================================
# Analytics
# ===================================================

def get_total_reports():

    session = SessionLocal()

    count = (
        session.query(Interaction)
        .filter(Interaction.agent.like("%Report%"))
        .count()
    )

    session.close()

    return count


def get_total_medications():

    session = SessionLocal()

    count = (
        session.query(Interaction)
        .filter(Interaction.agent.like("%Medication%"))
        .count()
    )

    session.close()

    return count


def get_success_count():

    session = SessionLocal()

    count = (
        session.query(Interaction)
        .filter(Interaction.status == "SUCCESS")
        .count()
    )

    session.close()

    return count


def get_failed_count():

    session = SessionLocal()

    count = (
        session.query(Interaction)
        .filter(Interaction.status == "FAILED")
        .count()
    )

    session.close()

    return count


def get_average_runtime():

    session = SessionLocal()

    avg = session.query(
        func.avg(Interaction.execution_time)
    ).scalar()

    session.close()

    return round(avg or 0, 2)


def get_latest_activity():

    session = SessionLocal()

    row = (
        session.query(Interaction)
        .order_by(Interaction.id.desc())
        .first()
    )

    session.close()

    return row