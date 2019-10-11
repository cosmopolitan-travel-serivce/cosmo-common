from ctscommon.clients import MicroServiceClient
from ctscommon.clients.crm.groups.models import GroupUpdate, GroupGet, GroupCreate, Group, GroupDelete
from typing import List


class CRMGroup(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "CRM", "/api/groups")

    def read_groups(self) -> List[Group]:
        return self._get_url("/")

    def add_group(self, group: GroupCreate) -> Group:
        response = self._post_url("/", group.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return {}

    def read_group(self, group: GroupGet) -> Group:
        return self._get_url(f"/{group}")

    def update_group(self, group: GroupUpdate) -> Group:
        return self._put_url(f"/{group}")

    def delete_group(self, group: GroupDelete):
        return self._delete_url(f"/{group}")
