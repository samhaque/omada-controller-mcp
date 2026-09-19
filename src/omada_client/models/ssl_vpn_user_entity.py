from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslVpnUserEntity")


@_attrs_define
class SslVpnUserEntity:
    """
    Attributes:
        name (str): Name of the SSL VPN user
        status (bool): Status of the SSL VPN user
        password (str): Password of the SSL VPN user
        validity (str): Validity of the SSL VPN user
        concurrent_number (int): Concurrent number of the SSL VPN user
        id (str | Unset): ID of the SSL VPN user
        group_id (str | Unset): Group ID of the SSL VPN user. User group can be created using 'Create SSL VPN user
            group' interface, and User Group ID can be obtained from 'Get user group list for SSL VPN server' interface.
        group_name (str | Unset): Group name of the SSL VPN user
        available (bool | Unset): Available of the SSL VPN user
    """

    name: str
    status: bool
    password: str
    validity: str
    concurrent_number: int
    id: str | Unset = UNSET
    group_id: str | Unset = UNSET
    group_name: str | Unset = UNSET
    available: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        password = self.password

        validity = self.validity

        concurrent_number = self.concurrent_number

        id = self.id

        group_id = self.group_id

        group_name = self.group_name

        available = self.available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "password": password,
                "validity": validity,
                "concurrentNumber": concurrent_number,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if available is not UNSET:
            field_dict["available"] = available

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        password = d.pop("password")

        validity = d.pop("validity")

        concurrent_number = d.pop("concurrentNumber")

        id = d.pop("id", UNSET)

        group_id = d.pop("groupId", UNSET)

        group_name = d.pop("groupName", UNSET)

        available = d.pop("available", UNSET)

        ssl_vpn_user_entity = cls(
            name=name,
            status=status,
            password=password,
            validity=validity,
            concurrent_number=concurrent_number,
            id=id,
            group_id=group_id,
            group_name=group_name,
            available=available,
        )

        ssl_vpn_user_entity.additional_properties = d
        return ssl_vpn_user_entity

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
