''' Create database schema for SurveyExact download of EASE project!

by: Pelle Rosenbeck Gøeg, September 2021

'''

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Survey(Base):
    __tablename__ = 'surveys'
    id = Column(Integer(), primary_key=True)
    name = Column(String(255))


class Label(Base):
    __tablename__ = 'labels'
    id = Column(Integer(), primary_key=True)
    organization = Column(Integer())
    survey_id = Column(Integer(), ForeignKey("surveys.id"))
    field_name = Column(String(), nullable=False)
    field_value = Column(Integer(), nullable=False)
    field_text = Column(String(255), nullable=False)

    __table_args__ = (
        UniqueConstraint('field_name', 'field_value'),
    )

class Answer3(Base):
    __tablename__ = 'answers3'
    answer_id = Column(Integer(), primary_key=True)
    survey_id = Column(Integer(), ForeignKey("surveys.id"))
    respondentid = Column(Integer())
    organization = Column(Integer())
    statinternal_1 = Column(Integer())
    statinternal_2 = Column(Integer())
    statinternal_3 = Column(Integer())
    statinternal_4 = Column(Integer())
    statinternal_5 = Column(Integer())
    statinternal_6 = Column(Integer())
    statinternal_7 = Column(Integer())
    statinternal_8 = Column(Integer())
    statinternal_9 = Column(Integer())
    statinternal_10 = Column(Integer())
    statinternal_11 = Column(Integer())
    statinternal_12 = Column(Integer())
    statinternal_13 = Column(Integer())
    statinternal_14 = Column(Integer())
    statinternal_15 = Column(Integer())
    statinternal_16 = Column(Integer())
    statinternal_17 = Column(Integer())
    statinternal_18 = Column(Integer())
    statinternal_19 = Column(Integer())
    statinternal_20 = Column(Integer())
    created = Column(DateTime())
    modified = Column(DateTime())
    closetime = Column(DateTime())
    starttime = Column(DateTime())
    difftime = Column(Float())
    responsecollectsessions = Column(Integer())
    numberofreturnedmail = Column(Integer())
    importgroup = Column(Integer())
    distributionschedule = Column(String())
    email = Column(String())
    digitaldistributionstatus = Column(String())
    digitaldistributionerrormessage = Column(String())
    risikovurdering = Column(Integer())
    anbefalinger = Column(Integer())
    hast_revurdering = Column(Integer())
    nyviden = Column(Integer())
    opmaerksomhedsniveau = Column(Integer())
    overhold_fremover = Column(Integer())
    andrebilister = Column(Integer())
    uddyb_evaluering = Column(Integer())
    situation1 = Column(Integer())
    strategi1 = Column(Integer())
    situation2 = Column(Integer())
    strategi2 = Column(Integer())
    situation3 = Column(Integer())
    strategi3 = Column(Integer())
    strategi_tekstfelt = Column(Text())
    strategimail = Column(Integer())
    strategireminder = Column(Integer())
    email_strategi = Column(String(255))
    slutkommentar_1b = Column(Text())
    id = Column(String(50))
    gr = Column(String(1))
    s = Column(Integer())
    statcompletion_1 = Column(Integer())
    statcompletion_2 = Column(Integer())
    statcompletion_3 = Column(Integer())
    statcreation_1 = Column(Integer())
    statcreation_2 = Column(Integer())
    statcreation_3 = Column(Integer())
    statcreation_4 = Column(Integer())
    statcreation_5 = Column(Integer())
    statcreation_6 = Column(Integer())
    statcreation_7 = Column(Integer())
    statdistribution_1 = Column(Integer())
    statdistribution_2 = Column(Integer())
    statdistribution_3 = Column(Integer())
    statdistribution_4 = Column(Integer())
    statdistribution_5 = Column(Integer())
    statsource_1 = Column(Integer())
    statsource_2 = Column(Integer())
    statsource_3 = Column(Integer())
    statsource_4 = Column(Integer())
    statsource_5 = Column(Integer())
    statsource_6 = Column(Integer())
    statcollect_1 = Column(Integer())
    statcollect_2 = Column(Integer())
    statcollect_3 = Column(Integer())
    statcollect_4 = Column(Integer())
    statoverall_1 = Column(Integer())
    statoverall_2 = Column(Integer())
    statoverall_3 = Column(Integer())
    statoverall_4 = Column(Integer())
    statoverall_5 = Column(Integer())
    strategi_mail_send_first = Column(DateTime(), nullable=True)
    strategi_mail_send_first_failed = Column(DateTime(), nullable=True)
    strategi_mail_send_second = Column(DateTime(), nullable=True)
    strategi_mail_send_second_failed = Column(DateTime(), nullable=True)


if __name__ == '__main__':
    engine = create_engine('sqlite:///main.sqlite3', echo=True)
    # Save database!

    drop = True
    if drop:
        Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(engine)