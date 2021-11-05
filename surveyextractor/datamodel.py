""" Models for data """

from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum, auto
import datetime

@dataclass
class RawClass:

    def __post_init__(self):
        for key, value in self.__dataclass_fields__.items():
            if getattr(self, key) == '':
                setattr(self, key, 'Null')

            if value.type == float:
                key_copy = getattr(self, key).replace(',', '.')
                setattr(self, key, key_copy.replace(',', '.'))



@dataclass
class Answer1b(RawClass):
    """ Answer from participant """

    # answer_id: int
    survey: int
    respondentid: int
    organization: int
    statinternal_1: int
    statinternal_2: int
    statinternal_3: int
    statinternal_4: int
    statinternal_5: int
    statinternal_6: int
    statinternal_7: int
    statinternal_8: int
    statinternal_9: int
    statinternal_10: int
    statinternal_11: int
    statinternal_12: int
    statinternal_13: int
    statinternal_14: int
    statinternal_15: int
    statinternal_16: int
    statinternal_17: int
    statinternal_18: int
    statinternal_19: int
    statinternal_20: int
    created: datetime.datetime
    modified: datetime.datetime
    closetime: datetime.datetime
    starttime: datetime.datetime
    difftime: float
    responsecollectsessions: int
    numberofreturnedmail: int
    importgroup: int
    distributionschedule: str
    email: str
    digitaldistributionstatus: str
    digitaldistributionerrormessage: str
    risikovurdering: int
    anbefalinger: int
    hast_revurdering: int
    nyviden: int
    opmaerksomhedsniveau: int
    overhold_fremover: int
    andrebilister: int
    uddyb_evaluering: int
    situation1: int
    strategi1: int
    situation2: int
    strategi2: int
    situation3: int
    strategi3: int
    strategi_tekstfelt: str
    strategimail: int
    strategireminder: int
    email_strategi: str
    slutkommentar_1b: str
    id: str
    gr: str
    s: int
    statcompletion_1: int
    statcompletion_2: int
    statcompletion_3: int
    statcreation_1: int
    statcreation_2: int
    statcreation_3: int
    statcreation_4: int
    statcreation_5: int
    statcreation_6: int
    statcreation_7: int
    statdistribution_1: int
    statdistribution_2: int
    statdistribution_3: int
    statdistribution_4: int
    statdistribution_5: int
    statsource_1: int
    statsource_2: int
    statsource_3: int
    statsource_4: int
    statsource_5: int
    statsource_6: int
    statcollect_1: int
    statcollect_2: int
    statcollect_3: int
    statcollect_4: int
    statoverall_1: int
    statoverall_2: int
    statoverall_3: int
    statoverall_4: int
    statoverall_5: int

@dataclass
class Survey(RawClass):
    """Survey Base"""

    survey_id: int
    name: str
    answers: List[Answer1b] = field(default_factory=lambda: [])
