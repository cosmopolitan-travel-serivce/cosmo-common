from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.travelers.models import TravelerCreate, TravelerUpdate, TravelerGet
from typing import List


class CRMTravelers(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COSMO-CRM", "/api/travelers")

    def read_travelers(self) -> List[TravelerGet]:
        return self._get_url("/")

    def add_traveler(self, traveler_in: TravelerCreate) -> TravelerGet:
        response = self._post_url("/", traveler_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def read_traveler(self, traveler_id: int) -> TravelerGet:
        return self._get_url(f"/{traveler_id}")

    def search_travelers(self, first_name: str, last_name: str, email: str) -> List[TravelerGet]:
        return self._get_url(f"/search/", first_name, last_name, email)

    def update_traveler(self, traveler_id: int, traveler_in: TravelerUpdate):
        return self._put_url(f"/{traveler_id}", traveler_in.dict())

    def delete_traveler(self, traveler_id: int):
        return self._delete_url(f"/{traveler_id}", data=None)
