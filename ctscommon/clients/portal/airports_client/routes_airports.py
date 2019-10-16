from ctscommon.clients import MicroServiceClient
from ctscommon.clients.portal.airports_client.models_airports import AirportBase, AirportUpdateSchema
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from fastapi import HTTPException
from starlette.responses import Response


class AirportsClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "PORTAL", "/api/airports")

    def get_airports(self, airport_code: str):
        return self._get_url("/")

    def add_airport(self, airport: AirportBase):
        response = self._post_url("/", airport.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on added airport")

     def get_airport(self, airport_id: str):
        
        return self._get_url(f"/{airport_id}")

    def update_airport(self, airport_id: str, airport: AirportUpdateSchema):
        response = self._put_url(f"/{airport_id}", airport.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on updated airport")

    def remove_airport(self, airport_id: str):
        return self._delete_url(f"/{airport_id}")