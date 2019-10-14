from typing import List

from ctscommon.clients.alternate_worker import ApiResponseError
from ctscommon.urls.schemas import ApiUrl, ApiUrlUpdate, ApiUrlCreate, HttpMethod
from ctscommon.clients import MicroServiceClient


class ApiUrlClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "AUTH", "api/security/urls")

    def create_url(self, service: str, api_url: ApiUrlCreate) -> ApiUrl:
        response = self._post_url(f"/{service}", api_url.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise ApiResponseError(response.status_code, response.payload)

    def batch_create_service_urls(self, service: str, api_urls: List[ApiUrlCreate]) -> List[ApiUrl]:
        data = [api_url.dict(skip_defaults=True) for api_url in api_urls]
        response = self._post_url(f"/{service}/batch-create", data)
        if response.status_code == 201:
            return response.payload
        else:
            raise ApiResponseError(response.status_code, response.payload)

    def get_service_urls(self, service: str) -> List[ApiUrl]:
        response = self._get_url(f"/{service}")
        if response.status_code == 200:
            return response.payload
        else:
            raise ApiResponseError(response.status_code, response.payload)

    def get_all_urls(self) -> List[ApiUrl]:
        response = self._get_url("/")
        if response.status_code == 200:
            return response.payload
        else:
            raise ApiResponseError(response.status_code, response.payload)

    def update_service_url(self, service: str, operation_id: str, method: HttpMethod, url_update: ApiUrlUpdate) -> ApiUrl:
        response = self._put_url(f"/{service}/{operation_id}/{method}", url_update.dict(skip_defaults=True))
        if response.status_code == 202:
            return response.payload
        else:
            raise ApiResponseError(response.status_code, response.payload)

    def get_service_url(self, service: str, operation_id: str, method: HttpMethod) -> ApiUrl:
        response = self._get_url(f"/{service}/{operation_id}/{method}")
        if response.status_code == 200:
            return response.payload
        else:
            raise ApiResponseError(response.status_code, response.payload)

    def delete_service_url(self, service: str, operation_id: str, method: HttpMethod) -> bool:
        response = self._delete_url(f"/{service}/{operation_id}/{method}", None)
        if response.status_code == 202:
            return True
        else:
            raise ApiResponseError(response.status_code, response.payload)
