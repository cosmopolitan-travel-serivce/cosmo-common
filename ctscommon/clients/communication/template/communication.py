from ctscommon.clients import MicroServiceClient
from ctscommon.clients.communication.contract.models import Contract, ContractCreate, ContractDelete , ContractUpdate
from typing import List


class CommunicationITemplate(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COMMUNICATION", "/api/communication")

    def get_all_contracts(self) -> List[Contract]:
        return self._get_url("/")

    def create_contract(self, contract: ContractCreate) -> Contract:

        response = self._post_url("/", contract.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def get_contract(self, contract: ContractCreate) -> Contract:
        return self._get_url(f"/{contract}")

    def update_contract(self, contract: ContractUpdate) -> Contract:
        return self._put_url(f"/{contract}")

    def remove_contract(self, contract: ContractDelete):
        return self._delete_url(f"/{contract}")