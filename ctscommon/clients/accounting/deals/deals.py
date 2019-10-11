from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.deals.models import DealGet, Deal,DealCreate, DealUpdate, MatchingDeal, DealDelete , Itineraries
from typing import List


class AccountingDeals(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "ACCOUNTING", "/api/contracts")

    def get_all_deals(self) -> List[Deal]:
        return self._get_url("/")

    def create_deal(self, deal: DealCreate) -> Deal:

        response = self._post_url("/", deal.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def get_deal(self, deal:DealGet) -> Deal:
        return self._get_url(f"/{deal}")

    def update_deal(self, deal: DealUpdate) -> Deal:
        return self._put_url(f"/{deal}")

    def remove_deal(self, deal: DealDelete):
        return self._delete_url(f"/{deal}")

    def valid_deals(self, itineraries: Itineraries) -> MatchingDeal:
        response = self._post_url("/", itineraries.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}