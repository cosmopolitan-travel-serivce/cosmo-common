from pydantic import BaseModel
from typing import List
from ctscommon.clients.accounting.contract.models import ContractGet
from enum import Enum


class RULETYPE(str, Enum):
    Markup = 'M'
    Reward = 'R'
    Dropnet = 'D'
    Discount = 'DC'
    CORPCC = 'CC'
    Exchange = 'EX'
    Refund = 'RE'
    TAFP = 'TP'


class OWRTTYPE(str, Enum):
    ONEWAY = 'OW'
    ROUNDTRIP = 'RT'
    CIRCLE = 'CR'
    OPENJAW = 'OJ'
    OTHER = 'O'
    ANY = 'AN'
    ALL = ''


class Deal(BaseModel):
    pax_type: str = None
    fare_type: str = None
    airline: str = None
    owrt: OWRTTYPE
    rule_type: RULETYPE
    value: str = None
    customer: str = None
    group: str = None


class DealCreate(Deal):
    contract: str


class DealUpdate(Deal):
    contract_id: int = None


class DealDelete(Deal):
    contract_id: int = None


class DealGet(Deal):
    id: int
    owrt: str
    rule_type: str
    contract: ContractGet


class Itinerary(BaseModel):
    origin: str = None
    destination: str = None
    departureDate: str = None


class Itineraries(BaseModel):
    itineraries: List[Itinerary]
    adult: int = 0
    child: int = 0
    infant: int = 0
    csv: str = None
    pcc: str = None
    alternatePcc: List[str] = []
    requestType: str = None
    interfaceId: str = None
    customer: str


class MatchingDeal(BaseModel):
    markup: List[DealGet] = None
    reward: List[DealGet] = None
    agency: List[DealGet] = None
    owrt: str = None
