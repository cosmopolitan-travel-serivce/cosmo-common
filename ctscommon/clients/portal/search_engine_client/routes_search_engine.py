from ctscommon.clients import MicroServiceClient
from ctscommon.clients.portal.search_engine_client.models_search_engine import Itinerary, RequestTypeEnum, SearchOption
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException, Depends
from portal.core.auth import get_current_user_authorizer


class SearchEngineClient(MicroServiceClient):

    def __init__(self):
        MicroServiceClient.__init__(self, "PORTAL", "/api")

    def search_flights(self, options: SearchOption, auth: dict = Depends(get_current_user_authorizer()), flat: bool = False):
        return self._post_url("/searchflights")

    def search_options(self, searchkey: str):
        return self._get_url("/searchoptions")

    def get_brand_classification(self, cabin: str):
        return self._get_url("/brandclassification")
