from ctscommon.clients import MicroServiceClient
from ctscommon.clients.portal.airlines_client.models_airlines import AirlineUpdateSchemas, AirlineCreateSchemas, MaxMarkupBase, SeasonalityBase
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class AirlinesClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "PORTAL", "/api/airlines")

    def get_airlines(self, airline_code: str):
        return self._get_url("/")

    def add_airline(self, airline: AirlineCreateSchemas):
        response = self._post_url("/", airline.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on added airline")

    def get_airline(self, airline_id: str):
        return self._get_url(f"/{airline_id}")

    def update_airline(self, airline_id: str, airline: AirlineUpdateSchemas):
        response = self._put_url(f"/{airline_id}", airline.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on updated airline")

    def remove_airline(self, airline_id: str):
        return self._delete_url(f"/{airline_id}")
