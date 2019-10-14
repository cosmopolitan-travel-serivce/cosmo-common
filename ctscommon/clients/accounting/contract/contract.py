from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.contract.models import Contract, ContractCreate, ContractUpdate, ContractGet
from typing import List


class AccountingContract(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "ACCOUNTING", "/api/contracts")

    def read_contracts(self) -> List[Contract]:
        return self._get_url("/")

    def create_contract(self, contract_to_create: ContractCreate):
        response = self._post_url("/", contract_to_create.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def read_contract(self, code: str) -> Contract:
        return self._get_url(f"/{code}")

    def update_contract(self, code: str, contract_to_update: ContractUpdate) -> Contract:
        return self._put_url(f"/{code}", contract_to_update.dict())

    def remove_contract(self, code: str):
        return self._delete_url(f"/{code}", data=None)

    def search_contracts(self, code: str) -> List[ContractGet]:
        params = {"q": code}
        response = self._get_url(f"/search/", params=params)
        if response.status_code == 201:
            return response.payload
        else:
            return {}
