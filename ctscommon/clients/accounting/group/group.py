from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.group.models import GroupCreate, GroupGet, GroupUpdate
from typing import List


class AccountingGroup(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "ACCOUNTING", "/api/groups")

    def read_groups(self) -> List[GroupGet]:
        response = self._get_url("/")
        if response.status_code == 201:
            return response.payload
        else:
            return response.payload['message']

    def create_group(self, group_in: GroupCreate) -> GroupGet:
        response = self._post_url("/", group_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            return response.payload['message']

    def read_group(self, code: str) -> GroupGet:
        response = self._get_url(f"/{code}")
        if response.status_code == 201:
            return response.payload
        else:
            return response.payload['message']

    def update_group(self, code: str, group_in: GroupUpdate) -> GroupGet:
        response = self._put_url(f"/{code}", group_in.dict())
        if response.status_code == 201:
            return response.payload
        else:
            return response.payload['message']

    def delete_group(self, code: str):
        response = self._delete_url(f"/{code}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            return response.payload['message']
