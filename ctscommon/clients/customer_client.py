from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import Profiles, Permissions
from typing import List


class CustomerClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "AUTH", "/api/customers")

    def create_customer_profile(self, customer_code: str, profiles: Profiles):
        return self._post_url(f"/{customer_code}/profile", profiles)

    def remove_customer_profile(self, customer_code: str, profiles: Profiles):
        return self._delete_url(f"/{customer_code}/profile", profiles)

    def get_customer_profiles(self, customer_code: str) -> List[str]:
        return self._get_url(f"/{customer_code}/profile")

    def create_customer_permissions(self, customer: str, permissions: Permissions):
        return self._post_url(f"/{customer}/customer", permissions)

    def update_customer_role(self, customer: str, permissions: Permissions):
        return self._put_url(f"/{customer}/permissions", permissions)

    def remove_customer_permissions(self, customer: str, permissions: Permissions):
        return self._delete_url(f"/{customer}/customer", permissions)

    def get_permissions_by_customer(self, customer: str):
        return self._get_url(f"/{customer}/permissions", None)

    def get_roles_and_profiles_by_customer(self, customer: str):
        return self._get_url(f"/{customer}/permissions-and-profiles", None)

    def get_users_by_customer(self, customer_code: str):
        return self._get_url(f"/{customer_code}/users", None)
