from typing import List

from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import UserCreation, User, UserUpdate


class UserClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "AUTH", "/api/users")

    def get_all_users(self) -> List[User]:
        return self._get_url("/")

    def get_current_user(self) -> User:
        return self._get_url("/me")

    def create_user(self, user: UserCreation) -> User:

        response = self._post_url("/", user.dict(skip_defaults=True))
        print(f"status code: {response.status_code}")
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
        return self._put_url(f"/{login}/passwordreset", data)

    def change_password(self, old_password: str, new_password: str, new_password_confirm: str):
        data = {"old_password": old_password, "new_password": new_password,
                "confirm_new_password": new_password_confirm}
        return self._post_url("/passwordchange", data)

    def validate_user(self, login: str) -> bool:
        return self._put_url(f"/{login}/validate", None)
