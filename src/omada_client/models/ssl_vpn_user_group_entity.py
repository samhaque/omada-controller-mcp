from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssl_vpn_resource_group_brief_info import SslVpnResourceGroupBriefInfo


T = TypeVar("T", bound="SslVpnUserGroupEntity")


@_attrs_define
class SslVpnUserGroupEntity:
    """
    Attributes:
        name (str): Name of the SSL VPN user group
        id (str | Unset): ID of the SSL VPN user group
        radius_attribute (str | Unset): Attribute value used for radius authentication
        ldap_attribute (str | Unset): Attribute value used for LDAP authentication
        resource_group_list (list[SslVpnResourceGroupBriefInfo] | Unset): Resource group list of the SSL VPN user group
        user_list (list[str] | Unset): User list of the SSL VPN user group
        user_number (int | Unset): User number of the SSL VPN user group
    """

    name: str
    id: str | Unset = UNSET
    radius_attribute: str | Unset = UNSET
    ldap_attribute: str | Unset = UNSET
    resource_group_list: list[SslVpnResourceGroupBriefInfo] | Unset = UNSET
    user_list: list[str] | Unset = UNSET
    user_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        radius_attribute = self.radius_attribute

        ldap_attribute = self.ldap_attribute

        resource_group_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resource_group_list, Unset):
            resource_group_list = []
            for resource_group_list_item_data in self.resource_group_list:
                resource_group_list_item = resource_group_list_item_data.to_dict()
                resource_group_list.append(resource_group_list_item)

        user_list: list[str] | Unset = UNSET
        if not isinstance(self.user_list, Unset):
            user_list = self.user_list

        user_number = self.user_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if radius_attribute is not UNSET:
            field_dict["radiusAttribute"] = radius_attribute
        if ldap_attribute is not UNSET:
            field_dict["ldapAttribute"] = ldap_attribute
        if resource_group_list is not UNSET:
            field_dict["resourceGroupList"] = resource_group_list
        if user_list is not UNSET:
            field_dict["userList"] = user_list
        if user_number is not UNSET:
            field_dict["userNumber"] = user_number

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssl_vpn_resource_group_brief_info import (
            SslVpnResourceGroupBriefInfo,
        )

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        radius_attribute = d.pop("radiusAttribute", UNSET)

        ldap_attribute = d.pop("ldapAttribute", UNSET)

        _resource_group_list = d.pop("resourceGroupList", UNSET)
        resource_group_list: list[SslVpnResourceGroupBriefInfo] | Unset = UNSET
        if _resource_group_list is not UNSET:
            resource_group_list = []
            for resource_group_list_item_data in _resource_group_list:
                resource_group_list_item = SslVpnResourceGroupBriefInfo.from_dict(
                    resource_group_list_item_data
                )

                resource_group_list.append(resource_group_list_item)

        user_list = cast(list[str], d.pop("userList", UNSET))

        user_number = d.pop("userNumber", UNSET)

        ssl_vpn_user_group_entity = cls(
            name=name,
            id=id,
            radius_attribute=radius_attribute,
            ldap_attribute=ldap_attribute,
            resource_group_list=resource_group_list,
            user_list=user_list,
            user_number=user_number,
        )

        ssl_vpn_user_group_entity.additional_properties = d
        return ssl_vpn_user_group_entity

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
