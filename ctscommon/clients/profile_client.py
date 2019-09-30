from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import Profile, ProfileUpdate, Permissions
from typing import List


class ProfileClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "AUTH", "/api/profiles")

    def get_all_profiles(self) -> List[Profile]:
        return self._get_url("/")

    def get_profile_by_code(self, code: str) -> List[Profile]:
        return self._get_url(f"/{code}/")

    def create_profile(self, profile: Profile) -> Profile:
        return self._post_url("/", profile)

    def update_profile(self, code: str, profile_update: ProfileUpdate) -> Profile:
        return self._put_url(f"/{code}", profile_update)

    def remove_profile(self, code : str, profile: Profile):
        return self._delete_url("/", profile)

    def add_permissions_to_user(self, login: str, permissions: Permissions):
        return self._post_url("/{login}/user", permissions)

    def add_permissions_to_profile(self, code: str, permissions: Permissions):
        return self._post_url(f"/{code}/permissions", permissions)

    def remove_profile_role(self, code: str, permissions: Permissions):
        return self._delete_url(f"/{code}/permissions", permissions)

    def get_permissions_by_profile(self, code: str) -> List[str]:
        return self._get_url(f"/{code}/")
