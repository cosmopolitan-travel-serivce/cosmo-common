from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.offices.models_office import OfficeCreate, OfficeGet, OfficeUpdate, OfficeFind
from ctscommon.clients.crm.offices.models_office_pcc import OfficePccCreate
from typing import List


class CRMOffices(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COSMO-CRM", "/api/offices")

    def read_offices(self) -> List[OfficeFind]:
        return self._get_url("/")

    def add_offices(self, office_in: OfficeCreate) -> OfficeFind:
        response = self._post_url("/", office_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def read_office(self, code: str) -> OfficeGet:
        return self._get_url(f"/{code}")

    def search_offices(self, code: str, name: str) -> List[OfficeFind]:
        return self._get_url(f"/search/", code, name)

    def update_office(self, code: str, office_in: OfficeUpdate):
        return self._put_url(f"/{code}", office_in.dict())

    def delete_office(self, code: str):
        return self._delete_url(f"/{code}", data=None)

    def add_pccs(self, office_code: str, pccs_in: OfficePccCreate):
        response = self._post_url(f"/{office_code}/pccs", pccs_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def update_pccs(self, office_code: str, pccs_in: OfficePccCreate):
        return self._put_url(f"/{office_code}/pccs", pccs_in.dict())

    def delete_pccs(self, office_code: str):
        return self._delete_url(f"/{office_code}", data=None)
