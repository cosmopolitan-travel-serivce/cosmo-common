from fastapi import APIRouter
from portal.reservation.reservation_controller import ReservationController
from portal.reservation.reservation_schema import SearchPriceQuote, CreatePnr
from portal.reservation.reservation_utils import get_region_name
from starlette.responses import Response


class ReservationClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "PORTAL", "/api/reservation")
        
    def get_reservation(self, pnr: str, message_id: str = None, close_session: bool = True):
        return self._get_url("/")

