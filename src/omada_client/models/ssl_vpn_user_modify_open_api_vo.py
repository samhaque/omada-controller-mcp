from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslVpnUserModifyOpenApiVO")


@_attrs_define
class SslVpnUserModifyOpenApiVO:
    """
    Attributes:
        status (bool): Status of the SSL VPN user
        password (str): Password of the SSL VPN user should contain 1 to 64 characters.
        validity (str): Validity of the SSL VPN user. The format is Month/Day/Year, for example 08/20/2022
        concurrent_number (int): Concurrent number of the SSL VPN user. It should be within the range of 1–100.
        group_id (str | Unset): Group ID of the SSL VPN user. User group can be created using 'Create SSL VPN user
            group' interface, and User Group ID can be obtained from 'Get user group list for SSL VPN server' interface.
    """

    status: bool
    password: str
    validity: str
    concurrent_number: int
    group_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        password = self.password

        validity = self.validity

        concurrent_number = self.concurrent_number

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "password": password,
                "validity": validity,
                "concurrentNumber": concurrent_number,
            }
        )
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        password = d.pop("password")

        validity = d.pop("validity")

        concurrent_number = d.pop("concurrentNumber")

        group_id = d.pop("groupId", UNSET)

        ssl_vpn_user_modify_open_api_vo = cls(
            status=status,
            password=password,
            validity=validity,
            concurrent_number=concurrent_number,
            group_id=group_id,
        )

        ssl_vpn_user_modify_open_api_vo.additional_properties = d
        return ssl_vpn_user_modify_open_api_vo

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
