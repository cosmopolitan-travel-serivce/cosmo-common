from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.deals.models import DealGet, DealCreate, DealUpdate, MatchingDeal, Itineraries
from typing import List
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class AccountingDeals(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "ACCOUNTING", "/api/deals")

    def read_deals(self, customer: str = None, rule_type: str = None, group: str = None) -> List[DealGet]:
        """
        Retreive all deals
        : return json list
        """
        params = {"customer": customer, "rule_type": rule_type, "group": group}
        response = self._get_url("/", params=params)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read all deals")

    def create_deal(self, deal_to_create: DealCreate) -> DealGet:
        """
        methode to create a deal
        :return a deal
        """
        response = self._post_url("/", deal_to_create.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on create deal")

    def read_deal(self, code: str) -> DealGet:
        """
        Retreive a deal
        :param code: the deal code
        : return a json
        """
        response = self._get_url(f"/{code}")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read deal")

    def update_deal(self, code: str, deal_to_update: DealUpdate):
        """
        methode to update a deal
        :param code : the deal code
        deal_to_update: deal update schema
        :return a deal updated
        """
        response = self._put_url(f"/{code}", deal_to_update)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on update deal")

    def remove_deal(self, code: str):
        """
        Remove a deal
        :param code : the deal code
        """
        response = self._delete_url(f"/{code}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on delete deal")

    def valid_deals(self, itineraries: Itineraries) -> MatchingDeal:
        """
        methode to get valid deals
        :return list deals
        """
        response = self._post_url("/", itineraries.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on valid deal")
