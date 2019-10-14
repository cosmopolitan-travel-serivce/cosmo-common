from pydantic import BaseModel
from enum import Enum


class APPLICATIONTYPES(str, Enum):
    ALL = "ALL"
    B2B = "B2B"
    B2C = "B2C"
    TDU = "TDU"
    ANY = ""


class TRIPTYPE(str, Enum):
    Domestic = "D"
    International = "I"
    ANY = ""


class SEASONALITY(str, Enum):
    LOW = "L"
    SHOULDER = "K, J"
    HIGH = "H, P, Q"
    ANY = ""


class INVOICETYPE(str, Enum):
    Sale = "S"
    Refund = "R"
    ANY = ""


class Contract(BaseModel):
    description: str = None
    application_type: APPLICATIONTYPES
    trip_type: TRIPTYPE
    seasonality: SEASONALITY
    inbound_seasonality: SEASONALITY
    outbound_seasonality: SEASONALITY
    invoice_type: INVOICETYPE
    priority: int = None
    active: bool = None
    product_type: str = None
    exclusive: bool = None
    from_base_amount: float = None
    from_total_amount: float = None
    from_com_amount: float = None
    from_base_minus_com_amount: float = None
    to_base_amount: float = None
    to_total_amount: float = None
    to_com_amount: float = None
    to_base_minus_com_amount: float = None
    applies_on_pax: str = None
    pax_group: str = None
    airline_exceptions: str = None
    airline_validating: str = None
    flight_number: str = None
    inboung_flight_number: str = None
    outbound_flight_number: str = None
    fare_code: str = None
    fare_basis: str = None
    fare_basis_exception: str = None
    tour_code: str = None
    tour_code_exception: str = None
    ticket_designator: str = None
    ticket_designator_exception: str = None
    booking_class: str = None
    exception_booking_class: str = None
    booking_class_type: str = None
    inbound_booking_class: str = None
    exception_inbound_booking_class: str = None
    outboun_booking_class: str = None
    exception_outboun_booking_class: str = None
    office_id: str = None
    arc_number: str = None
    exception_arc_number: str = None
    from_city: str = None
    from_exception_city: str = None
    to_city: str = None
    to_exception_city: str = None
    routing_city: str = None
    exception_routing_city: str = None
    routing_country: str = None
    exception_routing_country: str = None
    routing_region: str = None
    exception_routing_region: str = None
    from_country: str = None
    from_exception_country: str = None
    to_country: str = None
    to_exception_country: str = None
    from_region: str = None
    from_exception_region: str = None
    to_region: str = None
    to_exception_region: str = None
    flight_duration: str = None
    inbound_flight_duration: str = None
    outbound_flight_duration: str = None
    top_level: str = None
    depart_from: str = None
    depart_until: str = None
    depart_blackout: str = None
    issued_from: str = None
    issued_until: str = None
    issued_blackout: str = None
    return_from: str = None
    return_until: str = None
    return_blackout: str = None
    claim_half_dropnet: bool = None
    form_of_payment: str = None


class ContractCreate(Contract):
    name: str


class ContractGet(Contract):
    code: str
    name: str


class ContractDelete(Contract):
    name: str


class ContractUpdate(Contract):
    name: str
