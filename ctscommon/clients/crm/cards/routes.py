from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.cards.models import CardGet,CardUpdate, CardCreate
from typing import List


class CRMCards(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COSMO-CRM", "/api/cards")

    def read_cards(self) -> List[CardGet]:
        return self._get_url("/")

    def add_card(self, card_in: CardCreate) -> CardGet:
        response = self._post_url("/", card_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def read_card(self, card_number: str) -> CardGet:
        return self._get_url(f"/{card_number}")

    def search_cards(self, card_type: str, card_name: str) -> List[CardGet]:
        return self._get_url(f"/search/", card_type, card_name)

    def update_card(self, card_number: str, card_in: CardUpdate):
        return self._put_url(f"/{card_number}", card_in.dict())

    def delete_card(self, card_number: str):
        return self._delete_url(f"/{card_number}", data = None)
