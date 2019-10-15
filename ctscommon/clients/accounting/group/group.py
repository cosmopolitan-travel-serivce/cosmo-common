from ctscommon.clients import MicroServiceClient
from ctscommon.clients.accounting.group.models import GroupCreate, GroupGet, GroupUpdate
from typing import List
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


class AccountingGroup(MicroServiceClient):
    def __init__(self):
        MicroServiceClient.__init__(self, "ACCOUNTING", "/api/groups")

    def read_groups(self) -> List[GroupGet]:
        """
        This router retrives groups
        :return json list
        """
        response = self._get_url("/")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read all groups")

    def create_group(self, group_in: GroupCreate) -> GroupGet:
        """
        This router create a new group
        :param group_in Group schemas
        :return json object
        """
        response = self._post_url("/", group_in.dict(skip_defaults=True))
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on create group")

    def read_group(self, code: str) -> GroupGet:
        """
        Read_group is used to get a
        office object.
        :param code: code of the group
        :return json object
        """
        response = self._get_url(f"/{code}")
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on read group")

    def update_group(self, code: str, group_in: GroupUpdate) -> GroupGet:
        """
        This router is used to update group
        :param code  of group to update
        :return json object
        """
        response = self._put_url(f"/{code}", group_in.dict())
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on update group")

    def delete_group(self, code: str):
        """
        Delete Group router remove a
        group given in param
        :param code of group to delete
        :return 204 status code
        """
        response = self._delete_url(f"/{code}", data=None)
        if response.status_code == 201:
            return response.payload
        else:
            raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Error on delete group")
