from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslVpnUserGroupModifyOpenApiVO")


@_attrs_define
class SslVpnUserGroupModifyOpenApiVO:
    """
    Attributes:
        radius_attribute (str | Unset): Attribute value used for radius authentication. It should contain 1 to 20
            characters.
        ldap_attribute (str | Unset): Attribute value used for LDAP authentication. It should contain 1 to 20
            characters.
        resource_group_list (list[str] | Unset): Resource group ID list of the SSL VPN user group. Resource group can be
            created using 'Create SSL VPN resource group' interface, and Resource group ID can be obtained from 'Get
            resource group list for SSL VPN server' interface.
    """

    radius_attribute: str | Unset = UNSET
    ldap_attribute: str | Unset = UNSET
    resource_group_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius_attribute = self.radius_attribute

        ldap_attribute = self.ldap_attribute

        resource_group_list: list[str] | Unset = UNSET
        if not isinstance(self.resource_group_list, Unset):
            resource_group_list = self.resource_group_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radius_attribute is not UNSET:
            field_dict["radiusAttribute"] = radius_attribute
        if ldap_attribute is not UNSET:
            field_dict["ldapAttribute"] = ldap_attribute
        if resource_group_list is not UNSET:
            field_dict["resourceGroupList"] = resource_group_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radius_attribute = d.pop("radiusAttribute", UNSET)

        ldap_attribute = d.pop("ldapAttribute", UNSET)

        resource_group_list = cast(list[str], d.pop("resourceGroupList", UNSET))

        ssl_vpn_user_group_modify_open_api_vo = cls(
            radius_attribute=radius_attribute,
            ldap_attribute=ldap_attribute,
            resource_group_list=resource_group_list,
        )

        ssl_vpn_user_group_modify_open_api_vo.additional_properties = d
        return ssl_vpn_user_group_modify_open_api_vo

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
