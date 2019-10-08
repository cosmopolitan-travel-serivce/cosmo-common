from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.models import ContractBase, ContractCreate, ContractGet, ContractUpdate
from typing import List


class Contract(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "CONTRACT", "/api/contracts")

    def get_all_contracts(self) -> List[ContractBase]:
        return self._get_url("/")

    def create_contract(self, contract: ContractCreate) -> ContractBase:

        response = self._post_url("/", contract.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def get_contract(self, contract:ContractCreate) -> ContractBase:
        return self._get_url(f"/{contract}")