from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.deals.models import DealGet, Deal,DealCreate, DealUpdate, MatchingDeal
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