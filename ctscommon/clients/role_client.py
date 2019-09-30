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
        return self._post_url("/", role)

    def update_role(self, code: str, role_update: RoleUpdate) -> Role:
        return self._put_url(f"/{code}", role_update)

    def remove_role(self, role: Role):
        return self._delete_url("/", role)

    