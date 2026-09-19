from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortalResOpenApiVO")


@_attrs_define
class PortalResOpenApiVO:
    """
    Attributes:
        id (str | Unset): Portal ID
        name (str | Unset): Portal name
        enable (bool | Unset): Is the portal enable.
        ssid_list (list[str] | Unset): The ssid list of the portal binding.
        network_list (list[str] | Unset): The network ID list of the portal binding.
        auth_type (int | Unset): The type of authentication should be a value as follows: 0: No Auth; 1: Simple
            Password; 2: External Radius; 4: External Portal Server; 11: Hotspot; 15: Ldap; 16: Social Login
        hotspot_types (list[int] | Unset): The enable types of hotspot should be a value as follows: 3: Voucher; 5:
            Local user 6: SMS; 8: Hotspot Radius; 12: Form Auth
        social_login_types (list[int] | Unset): The enable types of social login should be a value as follows: 17:
            Google
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    enable: bool | Unset = UNSET
    ssid_list: list[str] | Unset = UNSET
    network_list: list[str] | Unset = UNSET
    auth_type: int | Unset = UNSET
    hotspot_types: list[int] | Unset = UNSET
    social_login_types: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        enable = self.enable

        ssid_list: list[str] | Unset = UNSET
        if not isinstance(self.ssid_list, Unset):
            ssid_list = self.ssid_list

        network_list: list[str] | Unset = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = self.network_list

        auth_type = self.auth_type

        hotspot_types: list[int] | Unset = UNSET
        if not isinstance(self.hotspot_types, Unset):
            hotspot_types = self.hotspot_types

        social_login_types: list[int] | Unset = UNSET
        if not isinstance(self.social_login_types, Unset):
            social_login_types = self.social_login_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if enable is not UNSET:
            field_dict["enable"] = enable
        if ssid_list is not UNSET:
            field_dict["ssidList"] = ssid_list
        if network_list is not UNSET:
            field_dict["networkList"] = network_list
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if hotspot_types is not UNSET:
            field_dict["hotspotTypes"] = hotspot_types
        if social_login_types is not UNSET:
            field_dict["socialLoginTypes"] = social_login_types

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        enable = d.pop("enable", UNSET)

        ssid_list = cast(list[str], d.pop("ssidList", UNSET))

        network_list = cast(list[str], d.pop("networkList", UNSET))

        auth_type = d.pop("authType", UNSET)

        hotspot_types = cast(list[int], d.pop("hotspotTypes", UNSET))

        social_login_types = cast(list[int], d.pop("socialLoginTypes", UNSET))

        portal_res_open_api_vo = cls(
            id=id,
            name=name,
            enable=enable,
            ssid_list=ssid_list,
            network_list=network_list,
            auth_type=auth_type,
            hotspot_types=hotspot_types,
            social_login_types=social_login_types,
        )

        portal_res_open_api_vo.additional_properties = d
        return portal_res_open_api_vo

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
