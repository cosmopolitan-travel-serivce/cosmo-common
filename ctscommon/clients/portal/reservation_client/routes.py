from ctscommon.clients import MicroServiceClient
from ctscommon.clients.portal.reservation.models import DisplayPnr, PassengerType, SearchPriceQuote, DetailDeals, DetailPassengers, CustomerIdentifier, CreatePnr
from typing import List


class ReservationClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "PORTAL", "/api/reservation")