from pydantic import BaseModel
from typing import Set, List


class DisplayPnr(BaseModel):
    pcc: str = None
    pnr: str
    message_id: str = None
    close_session: bool = True


class PassengerType(BaseModel):
    code: str = None
    quantity: int = 1
    name_select: Set[str] = set()


class SearchPriceQuote(BaseModel):
    message_id: str = None
    pcc: str = None
    pnr: str = None
    passengers_type: List[PassengerType]
    segments_select: Set[int] = set()
    destination: str = None


class DetailDeals(BaseModel):

    cts_reward: float = 0.0
    cts_markup: float = 0.0
    agency_markup: float = 0.0
    agency_discount: float = 0.0

    def __str__(self):
        return f"{self.cts_reward}, {self.cts_markup} {self.agency_markup} {self.agency_discount}"


class DetailPassengers(BaseModel):

    title: str = None
    given_name: str
    surname: str
    middle_name: str = None
    name_number: str
    gender: str
    date_of_birth: str = None
    passenger_type: str
    nationality: str = None
    commission_percent: float = 0.0
    markup: float = 0.0
    total_fare: float
    base_fare: float
    service_fee: float = 0.0
    ticket_designator: str = None
    tour_code: str = None
    address: str = None
    phone: str = None
    email: str = None


class CustomerIdentifier(BaseModel):

    id: int = None
    name: str = None
    interface_id: str
    office: str = None
    code: str


class CreatePnr(BaseModel):

    """This class returns the information to create pnr"""

    customer_identifier: CustomerIdentifier  # TODO: Double check how to get the customer
    user: str
    flight_id: str
    fare_id: str
    pcc: str
    passengers: List[DetailPassengers]
    insurance: dict = None