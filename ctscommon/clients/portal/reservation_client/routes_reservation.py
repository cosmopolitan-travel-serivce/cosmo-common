from ctscommon.clients import MicroServiceClient
from ctscommon.clients.portal.reservation_client.models_reservation import SearchPriceQuote, PassengerType, DisplayPnr, DetailDeals, DetailPassengers, CustomerIdentifier, CreatePnr
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException
from starlette.responses import Response


class ReservationClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "PORTAL", "/api/reservation")

    def create_reservation(self, create_pnr_in: CreatePnr):
        response = self._post_url("/", create_pnr_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on created Pnr")

    def get_reservation(self, pcc: str, pnr: str, message_id: str = None, close_session: bool = True):
        return self._get_url("/")

    def search_prices(self, pq_in: SearchPriceQuote):
        response = self._post_url("/", pq_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on search price")