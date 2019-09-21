from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import Profiles
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
