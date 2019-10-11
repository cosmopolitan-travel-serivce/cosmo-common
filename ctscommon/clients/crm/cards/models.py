from pydantic import BaseModel
from enum import Enum


class CardType(str, Enum):
    FrequentFlyer = 'FF'
    CreditCard = 'CC'
    ff_numbers = 'FN'
    frequent_guest_numbers = 'FGN'


class CardBase(BaseModel):
    card_type: CardType
    exp_date: str = None
    card_name: str = None
    card_description: str = None
    issued_by: str = None
    aprox_miles: str = None
    card_limit: str = None
    merge_to_pnr: str = None


class CardCreate(CardBase):
    card_number: str = None


class CardUpdate(CardBase):
    pass


class CardGet(CardBase):
    id: int
    card_number: str = None
    card_type: str = None
