from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologySplitWiredNetwork")


@_attrs_define
class TopologySplitWiredNetwork:
    """Network split by vlan.

    Attributes:
        id (str | Unset): Network ID.
        name (str | Unset): Network Name.
        vlan_id (int | Unset): Vlan ID.
        default_network (bool | Unset): Whether network is default.
        configuring (bool | Unset): Whether network is configuring.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    vlan_id: int | Unset = UNSET
    default_network: bool | Unset = UNSET
    configuring: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        vlan_id = self.vlan_id

        default_network = self.default_network

        configuring = self.configuring

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if default_network is not UNSET:
            field_dict["defaultNetwork"] = default_network
        if configuring is not UNSET:
            field_dict["configuring"] = configuring

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        default_network = d.pop("defaultNetwork", UNSET)

        configuring = d.pop("configuring", UNSET)

        topology_split_wired_network = cls(
            id=id,
            name=name,
            vlan_id=vlan_id,
            default_network=default_network,
            configuring=configuring,
        )

        topology_split_wired_network.additional_properties = d
        return topology_split_wired_network

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
