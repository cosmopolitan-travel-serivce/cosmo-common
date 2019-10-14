from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.pccs.models import PccCreate, PccUpdate, Pcc
from typing import List


class CRMPcc(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COSMO-CRM", "/api/pccs")

    def read_pccs(self) -> List[Pcc]:
        return self._get_url("/")

    def add_pcc(self, pcc: PccCreate) -> Pcc:
        response = self._post_url("/", pcc.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def read_pcc(self, code: str) -> Pcc:
        return self._get_url(f"/{code}")

    def update_pcc(self, code: str, gds: str, pcc_in: PccUpdate):
        return self._put_url(f"/{gds}/{code}", pcc_in.dict())

    def delete_pcc(self, code: str, gds: str):
        return self._delete_url(f"/{gds}/{code}", data=None)
