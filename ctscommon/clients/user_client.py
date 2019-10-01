from typing import List

from ctscommon.clients import MicroServiceClient
<<<<<<< HEAD
from ctscommon.clients.models import UserCreation, User, UserUpdate
=======
from ctscommon.clients.models import UserCreation, User, UserUpdate, PasswordChange
>>>>>>> 878a63d192ccf27ecdc98cc8f71bce538468a7d7


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

    def change_password(self, login: str, change_data: PasswordChange):
        response = self._put_url("/passwordchange", change_data.dict(skip_defaults=True))
        print(f"response.status_code: {response.status_code}")
        if response.status_code == 202:
            return response.payload
        else:
            return {}

    def validate_user(self, login: str) -> bool:
        return self._put_url(f"/{login}/validate", None)
