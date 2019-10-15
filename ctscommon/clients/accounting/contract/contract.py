from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.contract.models import Contract, ContractCreate, ContractUpdate, ContractGet
from typing import List
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class AccountingContract(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "ACCOUNTING", "/api/contracts")

    def read_contracts(self) -> List[Contract]:
        """
        Retreive All contracts
        :return: json list
        """
        response = self._get_url("/")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read all contracts")

    def create_contract(self, contract_to_create: ContractCreate):
        """
        Create a new contract
        :param contract_to_create: a contract object
        :return: a contract object
        """
        response = self._post_url("/", contract_to_create.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on create contract")

    def read_contract(self, code: str) -> Contract:
        """
        Retreive a contract
        :param code: the contract code
        :return: a json
        """
        response = self._get_url(f"/{code}")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read contract")

    def update_contract(self, code: str, contract_to_update: ContractUpdate) -> Contract:
        """
        methode to update a contrcat
        :param code : the contract code
        contract_to_update: contract update schema
        :return a contract updated
        """
        response = self._put_url(f"/{code}", contract_to_update.dict())
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on update contract")

    def remove_contract(self, code: str):
        """
        Remove a contract
        :param code : the contrcat code
        """
        response = self._delete_url(f"/{code}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on delete contract")

    def search_contracts(self, code: str) -> List[ContractGet]:
        """
        The read contract router get
        a contracts from the database
        :name search by name
        :description search by description
        :return json list
        """
        params = {"q": code}
        response = self._get_url(f"/search/", params=params)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on search contracts")
