from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.travelers.models import TravelerCreate, TravelerUpdate, TravelerGet
from typing import List
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class CRMTravelers(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COSMO-CRM", "/api/travelers")

    def read_travelers(self) -> List[TravelerGet]:
        """
        The read travelers router get
        a travelers from the database
        :return json list
        """
        response = self._get_url("/")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read all travelers")

    def add_traveler(self, traveler_in: TravelerCreate) -> TravelerGet:
        """
        This router is used to create a new
        traveler to the db
        :param traveler_in: the traveler schemas
        :return json object
        """
        response = self._post_url("/", traveler_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on add traveler")

    def read_traveler(self, traveler_id: int) -> TravelerGet:
        """
        This router is used to get
        a traveler by giving the id
        :param traveler_id: the traveler to get
        :return json object
        """
        response = self._get_url(f"/{traveler_id}")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read traveler")

    def search_travelers(self, first_name: str, last_name: str, email: str) -> List[TravelerGet]:
        """
        The read traveler router get
        a travelers from the database
        :first_name search by first_name
        :last_name search by last_name
        :email search by email
        :return json list
        """
        params = {"first_name": first_name, "last_name": last_name, "email": email}
        response = self._get_url(f"/search/", params=params)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on search travelers")

    def update_traveler(self, traveler_id: int, traveler_in: TravelerUpdate):
        """
        This router update a given traveler
        :param traveler_id: the given traveler
        :param traveler_in: the new data
        :return json object
        """
        response = self._put_url(f"/{traveler_id}", traveler_in.dict())
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on update traveler")

    def delete_traveler(self, traveler_id: int):
        """
        To delete a given traveler
        :param traveler_id: the given traveler
        :return 204 status code
        """
        response = self._delete_url(f"/{traveler_id}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on delete travelers")
