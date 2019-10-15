from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.offices.models_office import OfficeCreate, OfficeGet, OfficeUpdate, OfficeFind
from ctscommon.clients.crm.offices.models_office_pcc import OfficePccCreate
from typing import List
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class CRMOffices(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COSMO-CRM", "/api/offices")

    def read_offices(self) -> List[OfficeFind]:
        """
        This router retrives offices
        :return json list
        """
        response = self._get_url("/")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read all offices")

    def add_offices(self, office_in: OfficeCreate) -> OfficeFind:
        """
        This router create a new office
        :param office_in Office schemas
        :return json object
        """
        response = self._post_url("/", office_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on add office")

    def read_office(self, code: str) -> OfficeGet:
        """
        Read_office is used to get a
        office object.
        :param code: code of the office
        :return json object
        """
        response = self._get_url(f"/{code}")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read office")

    def search_offices(self, code: str, name: str) -> List[OfficeFind]:
        """
        The search router search
        offices by name or code
        :name search by name
        :code search by code
        :return json list
        """
        params = {"code": code, "name": name}
        response = self._get_url(f"/search/", params=params)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on search office")

    def update_office(self, code: str, office_in: OfficeUpdate):
        """
        This router is used to update offfice
        :param code code of office to update
        :return json object
        """
        response = self._put_url(f"/{code}", office_in.dict())
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on update office")

    def delete_office(self, code: str):
        """
        Delete Office router remove a
        office given in param
        :param code of office to delete
        :return 204 status code
        """
        response = self._delete_url(f"/{code}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on delete office")

    def add_pccs(self, office_code: str, pccs_in: OfficePccCreate):
        """
        This router is used to add
        a pccs for a given office
        :param office_code: the given office
        :param pccs_in: list pccs to add
        :return json list
        """
        response = self._post_url(f"/{office_code}/pccs", pccs_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on add pccs")

    def update_pccs(self, office_code: str, pccs_in: OfficePccCreate):
        """
        This router update pccs for a given office
        :param office_code: the given office
        :param pccs_in: the new data
        :return json list
        """
        response = self._put_url(f"/{office_code}/pccs", pccs_in.dict())
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on update pccs")

    def delete_pccs(self, office_code: str):
        """
        To delete pccs for a given office
        :param office: the given office
        :return 204 status code
        """
        response = self._delete_url(f"/{office_code}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on delete pccs")
