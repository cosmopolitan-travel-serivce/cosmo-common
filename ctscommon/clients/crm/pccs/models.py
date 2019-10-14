from pydantic import BaseModel


class PccBase(BaseModel):
    gds: str = None
    country: str = None


class PccCreate(PccBase):
    code: str


class Pcc(PccBase):
    country: str = None
    code: str
    gds: str = None
    booking: bool = False
    ticketing: bool = False


class PccGet(PccBase):
    id: int
    country: str = None
    code: str
    gds: str = None
    booking: bool = False
    ticketing: bool = False


class PccUpdate(PccBase):
    country: str = None
    code: str
    gds: str = None
    booking: bool = False
    ticketing: bool = False
