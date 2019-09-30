from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import Profiles,  Permissions
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
    
    def add_permissions_to_user(self, login: str, permissions: Permissions):
        return self._post_url("/{login}/user", permissions)

    def create_customer_permissions(self, customer: str, permissions: Permissions):
        return self._post_url(f"/{customer}/customer", permissions)

    def remove_customer_permissions(self, customer: str, permissions: Permissions):
        return self._delete_url(f"/{customer}/customer", permissions)

    def get_permissions_by_customer(self, customer: str):
        return self._get_url(f"/{cutomer}/customer")

