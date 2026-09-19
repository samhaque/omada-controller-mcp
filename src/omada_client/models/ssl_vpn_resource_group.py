from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssl_vpn_resource_brief_info import SslVpnResourceBriefInfo


T = TypeVar("T", bound="SslVpnResourceGroup")


@_attrs_define
class SslVpnResourceGroup:
    """
    Attributes:
        name (str): Name of the SSL VPN resource group
        id (str | Unset): ID of the SSL VPN resource group
        resources_list (list[SslVpnResourceBriefInfo] | Unset): Resources list of the SSL VPN resource group
    """

    name: str
    id: str | Unset = UNSET
    resources_list: list[SslVpnResourceBriefInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        resources_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources_list, Unset):
            resources_list = []
            for resources_list_item_data in self.resources_list:
                resources_list_item = resources_list_item_data.to_dict()
                resources_list.append(resources_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if resources_list is not UNSET:
            field_dict["resourcesList"] = resources_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssl_vpn_resource_brief_info import (
            SslVpnResourceBriefInfo,
        )

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        _resources_list = d.pop("resourcesList", UNSET)
        resources_list: list[SslVpnResourceBriefInfo] | Unset = UNSET
        if _resources_list is not UNSET:
            resources_list = []
            for resources_list_item_data in _resources_list:
                resources_list_item = SslVpnResourceBriefInfo.from_dict(
                    resources_list_item_data
                )

                resources_list.append(resources_list_item)

        ssl_vpn_resource_group = cls(
            name=name,
            id=id,
            resources_list=resources_list,
        )

        ssl_vpn_resource_group.additional_properties = d
        return ssl_vpn_resource_group

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
