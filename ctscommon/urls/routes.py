from typing import List

from fastapi import APIRouter
from ctscommon.urls.schemas import ApiUrl,  ApiUrlCreate, HttpMethod
from ctscommon.urls.service import api_auth_service



@router.get("/urls/{service}", operation_id="all-service-urls", name="Get all URLs for a given service",
            response_model=List[ApiUrl], status_code=200)
async def get_service_urls(service: str) -> List[ApiUrl]:
    return api_auth_service.get_api_urls(service)


@router.get("/urls", operation_id="get-all-urls", name="Get all URLs", response_model=List[ApiUrl],
            status_code=200)
async def get_all_urls() -> List[ApiUrl]:
    return api_auth_service.get_api_urls(None)


@router.post("/urls/{service}/batch-create", operation_id="create-service-urls", response_model=List[ApiUrl],
             status_code=201, name="Creates URLs for a given service")
async def batch_create_service_urls(service: str, api_urls: List[ApiUrlCreate]) -> List[ApiUrl]:
    return api_auth_service.create_service_api_urls(service, api_urls)