from pydantic import BaseModel
from typing import Set, List
from datetime import date
from enum import Enum


class RequestTypeEnum(str, Enum):
    r200 = "200ITINS"
    r50 = "50ITINS"
    ad1 = "AD1"
    ad3 = "AD3"
    ad7 = "AD7"


class Itinerary(BaseModel):
    origin: str
    destination: str
    departureDate: date


class SearchOption(BaseModel):
    requestType: RequestTypeEnum = RequestTypeEnum.r50
    agencyId: str
    excludeBasicEconomy: bool
    maxConnection: int
    baggagePref: bool
    adult: int
    child: int
    infant: int
    csv: str
    pcc: str
    alternatePcc: Set[str] = set()
    preferredAirlines: Set[str] = set()
    itineraries: List[Itinerary]
