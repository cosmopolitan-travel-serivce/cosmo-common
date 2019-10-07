from typing import List

from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import UserCreation, User, UserUpdate, PasswordChange, Customers, PasswordResetEnd,Profiles,  Offices, Permissions


class UserClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "AUTH", "/api/users")

    def get_all_users(self) -> List[User]:
        return self._get_url("/")

    def get_current_user(self) -> User:
        return self._get_url("/me")

    def create_user(self, user: UserCreation) -> User:

        response = self._post_url("/", user.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def get_user(self, login: str) -> User:
        return self._get_url(f"/{login}")

    def update_user(self, login: str, user: UserUpdate) -> User:
        response = self._put_url(f"/{login}", user.dict(skip_defaults=True))
        print(f"status code: {response.status_code}")
        if response.status_code == 202:
            return response.payload
        else:
            return {} 

    def activate_user(self, login: str) -> bool:
        return self._put_url(f"/{login}/activate", None)

    def deactivate_user(self, login: str) -> bool:
        return self._put_url(f"/{login}/deactivate", None)

    def reset_user_password(self, login: str) -> bool:
        return self._get_url(f"/{login}/passwordreset")

    def validate_user_password_reset(self, login: str, token: str, new_password: str, new_password_confirm: str) -> bool:
        data = {"token": token, "new_password": new_password, "confirm_new_password": new_password_confirm}
        response = self._put_url(f"/{login}/passwordreset", data)
        if response.status_code == 202:
            return response.payload
        else:
            return False

    def change_password(self, login: str, change_data: PasswordChange) -> bool:
        response = self._put_url("/passwordchange", change_data.dict(skip_defaults=True))
        print(f"response.status_code: {response.status_code}")
        if response.status_code == 202:
            return response.payload
        else:
            return {}

    def validate_user(self, login: str) -> bool:
        return self._put_url(f"/{login}/validate", None)

    def search_user(self, login: str)  -> User:
        return self._get_url("/search", None)

    def rest_user_password_init(self, login: str) -> bool:
        return self._get_url(f"/{login}/passwordreset", None)

    def rest_user_password_end(self, login: str, reset_data: PasswordResetEnd) -> bool:
        return self._put_url(f"/{login}/passwordreset", reset_data.dict(skip_defaults=True))

    def add_managed_customers(self, login: str, managed_customers: Customers):
        return self._post_url(f"/{login}/managed-customers", managed_customers)

    def remove_managed_customers(self, login: str, stale_customers: Customers):
        return self._delete_url(f"/{login}/managed-customers", stale_customers)

    def update_managed_customer(self, login: str, customers: Customers):
        return self._put_url(f"/{login}/managed-customers", customers)

    def add_permissions_to_user(self, login: str, permissions: Permissions):
        return self._post_url(f"/{login}/managed-customers", permissions)

    def remove_permissions_to_user(self, login: str, permissions: Permissions):
        return self._delete_url(f"/{login}/permissions", permissions)

    def update_user_permissions(self,login: str, permissions: Permissions):
        return self._put_url(f"/{login}/permissions", permissions)

    def create_user_profile(self, login: str, profiles: Profiles):
        return self._post_url(f"/{login}/profiles", profiles)

    def remove_user_profile(self, login: str, profiles: Profiles):
        return self._delete_url(f"/{login}/profiles", profiles)

    def add_offices(self, login: str, offices: Offices):
        return self._post_url(f"/{login}/offices", offices)

    def remove_offices(self, login: str, stale_offices: Offices):
        return self._delete_url(f"/{login}/offices", stale_offices)

    def update_user_office(self, login: str, offices: Offices):
        return self._put_url(f"/{login}/offices", offices)