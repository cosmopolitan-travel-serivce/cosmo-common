from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.cards.models import CardGet, CardUpdate, CardCreate
from typing import List
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class CRMCards(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "COSMO-CRM", "/api/cards")

    def read_cards(self) -> List[CardGet]:
        """
        This router retrives cards
        :return json list
        """
        response = self._get_url("/")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read all cards")

    def add_card(self, card_in: CardCreate) -> CardGet:
        """
        This router create a new card
        :param card_in Card schemas
        :return json object
        """
        response = self._post_url("/", card_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on add card")

    def read_card(self, card_number: str) -> CardGet:
        """
        Read_card is used to get a
        card object.
        :param card_number: id of the card
        :return json object
        """
        response = self._get_url(f"/{card_number}")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read card")

    def search_cards(self, card_type: str, card_name: str) -> List[CardGet]:
        """
        The search router search
        cards by card_type or card_number
        or card_name
        :card_type search by card_type
        :card_name search by card_name
        :return json list
        """
        params = {"card_type": card_type, "card_name": card_name}
        response = self._get_url(f"/search/", params=params)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on search cards")

    def update_card(self, card_number: str, card_in: CardUpdate):
        """
        This router is used to update card
        :param card_number: number of office to update
        :return json object
        """
        response = self._put_url(f"/{card_number}", card_in.dict())
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on update card")

    def delete_card(self, card_number: str):
        """
        Delete Card router remove a
        card given in param
        :param card_number: of card to delete
        :return 204 status code
        """
        response = self._delete_url(f"/{card_number}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on delete card")
