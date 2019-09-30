from typing import List

from pydantic import BaseModel

from datetime import date
class Address(BaseModel):
    country: str
    state: str
    city: str
    street: str
    zip_code: str

    def __str__(self):
        return f"{self.street}, {self.city} {self.zip_code} {self.state}, {self.country}"

    @classmethod
    def from_str(cls, address: str):
        if not address:
            return None
        s = address.split(", ")
        if len(s) == 3:
            second = s[1].split(" ")
            return Address(street=s[0], city=second[0], zip_code=second[1], state=second[2], country=s[2])


class UserCreation(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    customer: str
    email: str
    phone: str
    address: Address


class User(UserCreation):
    username: str
    managed_customers: List[str]
    groups: List[str]
    permissions: List[str]


class Group(BaseModel):
    code: str
    name: str


class PasswordChange(BaseModel):
    old_password: str
    new_password: str
    confirm_new_password: str


class PasswordResetEnd(BaseModel):
    token: str
    new_password: str
    confirm_new_password: str


class PccCredential(BaseModel):
    pcc: str
    username: str
    password: str
    gds: str
    


class PccCredentialUpdate(BaseModel):
    pcc: str = None
    username: str = None
    password: str = None
    gds: str = None


class Role(BaseModel):
    code: str
    name: str
    context: str


class RoleUpdate(BaseModel):
    code: str = None
    name: str = None
    context: str = None


class Permissions(BaseModel):
    permissions: List[str]


class Profile(BaseModel):
    code: str
    name: str
    customer : str


class AddPermissionsToProfile(BaseModel):
    permissions: str


class RemoveProfileRole(BaseModel):
    permissions: str


class ProfileUpdate(BaseModel):
    code: str = None
    name: str = None
    customer: str = None


class Profiles(BaseModel):
    profiles: List[str]
