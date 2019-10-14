from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.deals.models import DealGet, DealCreate, DealUpdate, MatchingDeal, Itineraries
from typing import List


class AccountingDeals(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "ACCOUNTING", "/api/deals")

    def read_deals(self, customer: str = None, rule_type: str = None, group: str = None) -> List[DealGet]:
        params = {"customer": customer, "rule_type": rule_type, "group": group}
        response = self._get_url("/", params=params)
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def create_deal(self, deal_to_create: DealCreate) -> DealGet:

        response = self._post_url("/", deal_to_create.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def read_deal(self, code: str) -> DealGet:
        return self._get_url(f"/{code}")

    def update_deal(self, code: str, deal_to_update: DealUpdate):
        return self._put_url(f"/{code}", deal_to_update)

    def remove_deal(self, code: str):
        return self._delete_url(f"/{code}", data=None)

    def valid_deals(self, itineraries: Itineraries) -> MatchingDeal:
        response = self._post_url("/", itineraries.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}
