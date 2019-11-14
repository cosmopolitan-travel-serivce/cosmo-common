from pydantic import BaseModel


class SeasonalityBase(BaseModel):
    Low: list = []
    Hight: list = []
    Shoulder: list = []


class MaxMarkupBase(BaseModel):
    Low: float = None
    Hight: float = None
    Shoulder: float = None
    default = 0.25


class AirlineCreateSchemas(BaseModel):
    AirlineCode: str
    AirlineName: str
    AlternativeBusinessName: str
    logoRect: str
    MaxMarkup: MaxMarkupBase = None
    SeasonalityCode: SeasonalityBase = None
    AllowCtsCreditCard: bool
    AllowCreditCard: bool
    AlternatePaxCodes: str = None


class AirlineUpdateSchemas(BaseModel):
    

    AirlineCode: str = None
    AirlineName: str = None
    AlternativeBusinessName: str = None
    logoRect: str = None
    MaxMarkup: MaxMarkupBase = None
    SeasonalityCode: SeasonalityBase = None
    AllowCtsCreditCard: bool = None
    AllowCreditCard: bool = None
    AlternatePaxCodes: str = None