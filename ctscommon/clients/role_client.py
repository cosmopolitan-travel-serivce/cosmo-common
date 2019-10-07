from ctscommon.clients import MicroServiceClient
from ctscommon.clients.models import Role, RoleUpdate, Permissions
from typing import List


class RoleClient(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "AUTH", "/api/permissions")

    def get_all_roles(self) -> List[Role]:
        return self._get_url("/")

    def get_role_by_code(self, code: str) -> List[Role]:
        return self._get_url(f"/{code}/")

    def create_role(self, role: Role) -> Role:
        response = self._post_url("/", role.dict(skip_defaults=True))
        print(f"status code: {response.status_code}")
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def update_role(self, code: str, role_update: RoleUpdate) -> Role:
        response = self._put_url(f"/{code}", role_update.dict(skip_defaults=True))
        print(f"status code: {response.status_code}")
        if response.status_code == 202:
            return response.payload
        else:
            return {}
        
    def remove_role(self, code: str):
        role = self.get_role_by_code(code)
        return self._delete_url(f"/{code}", role)
