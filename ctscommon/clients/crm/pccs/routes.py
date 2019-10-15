from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.pccs.models import PccCreate, PccUpdate, Pcc
from typing import List
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class CRMPcc(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COSMO-CRM", "/api/pccs")

    def read_pccs(self) -> List[Pcc]:
        """
        This router retrives pccs
        :return json list
        """
        response = self._get_url("/")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read all pcc")

    def add_pcc(self, pcc: PccCreate) -> Pcc:
        """
        This router create a new pcc
        :param pcc_in Pcc schemas
        :return json object
        """
        response = self._post_url("/", pcc.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on add pcc")

    def read_pcc(self, code: str) -> Pcc:
        """
        Read_pcc is used to get a
        pcc object.
        :param code: code of the office
        :return json object
        """
        response = self._get_url(f"/{code}")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read pcc")

    def update_pcc(self, code: str, gds: str, pcc_in: PccUpdate):
        """
        This router is used to update pcc
        :param code: code of pcc to update
        :return update object
        """
        response = self._put_url(f"/{gds}/{code}", pcc_in.dict())
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on update pcc")

    def delete_pcc(self, code: str, gds: str):
        """
        Delete Pcc router remove a
        pcc given in param
        :param code of pcc to delete
        :return 204 status code
        """
        response = self._delete_url(f"/{gds}/{code}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on delete pcc")
