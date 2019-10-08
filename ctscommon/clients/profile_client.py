from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import Profile, ProfileUpdate, Permissions
from typing import List
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class ProfileClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "AUTH", "/api/profiles")

    def get_all_profiles(self) -> List[Profile]:
        return self._get_url("/")

    def get_profile_by_code(self, code: str) -> List[Profile]:
        return self._get_url(f"/{code}/")

    def create_profile(self, profile: Profile) -> Profile:
        response = self._post_url("/", profile.dict(skip_defaults=True))
        print(f"status code: {response.status_code}")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on created Profile")

    def update_profile(self, code: str, profile_update: ProfileUpdate) -> Profile:
        response = self._put_url(f"/{code}", profile_update.dict(skip_defaults=True))
        print(f"status code: {response.status_code}")
        if response.status_code == 202:
            return response.payload
        else:
            raise HTTPException(
                status_code=HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Error on update Profile")

    def remove_profile(self, code: str):
        profile = self.get_profile_by_code(code)
        return self._delete_url(f"/{code}", profile)

    def add_permissions_to_profile(self, code: str, permissions: Permissions):
        return self._post_url(f"/{code}/permissions", permissions)

    def remove_profile_role(self, code: str, permissions: Permissions):
        return self._delete_url(f"/{code}/permissions", permissions)

    def get_permissions_by_profile(self, code: str) -> List[str]:
        return self._get_url(f"/{code}/")

    def update_profile_role(self, code: str, permissions: Permissions):
        return self._put_url(f"/{code}/permissions", permissions)
