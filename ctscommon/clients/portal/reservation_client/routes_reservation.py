from typing import List
from ctscommon.clients import MicroServiceClient
from ctscommon.clients.portal.reservation_client.models_reservation import SearchPriceQuote, PassengerType, DisplayPnr, DetailDeals, DetailPassengers, CustomerIdentifier, CreatePnr
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class ReservationClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "PORTAL", "/api/reservations")

    def get_reservation(self, pcc: str, pnr: str, message_id: str = None, close_session: bool = True) -> Pnr:
        return self._get_url(f"/{pcc}/{pnr}")

    def search_prices(self, pq_in: SearchPriceQuote) -> :
        return self._post_url(f"/{login}", None)

    def create_reservation(self, create_pnr_in: CreatePnr, response: Response) -> Pnr:

        response = self._post_url("/", user.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on created User")