from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.group.models import GroupCreate, GroupGet, GroupUpdate, Group, GroupDelete
from typing import List


class AccountingGroup(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "ACCOUNTING", "/api/contracts")

    def get_all_groups(self) -> List[Group]:
        return self._get_url("/")

    def create_group(self, group: GroupCreate) -> Group:
        response = self._post_url("/", group.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def get_group(self, group:GroupGet) -> Group:
        return self._get_url(f"/{group}")

    def update_group(self, group:GroupUpdate) -> Group:
        return self._put_url(f"/{group}")

    def remove_group(self, group: GroupDelete):
        return self._delete_url(f"/{group}")