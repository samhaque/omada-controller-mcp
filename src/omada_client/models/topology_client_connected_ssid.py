from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyClientConnectedSsid")


@_attrs_define
class TopologyClientConnectedSsid:
    """SSID that client connected.

    Attributes:
        id (str | Unset): SSID ID.
        name (str | Unset): SSID Name.
        vlan_enable (bool | Unset): Whether the SSID enable vlan.
        vlan_ids (list[int] | Unset): Vlan ID while SSID enable vlan.
        client_vlan_id (int | Unset): Client Report Vlan Id.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    vlan_enable: bool | Unset = UNSET
    vlan_ids: list[int] | Unset = UNSET
    client_vlan_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        vlan_enable = self.vlan_enable

        vlan_ids: list[int] | Unset = UNSET
        if not isinstance(self.vlan_ids, Unset):
            vlan_ids = self.vlan_ids

        client_vlan_id = self.client_vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if vlan_enable is not UNSET:
            field_dict["vlanEnable"] = vlan_enable
        if vlan_ids is not UNSET:
            field_dict["vlanIds"] = vlan_ids
        if client_vlan_id is not UNSET:
            field_dict["clientVlanId"] = client_vlan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        vlan_enable = d.pop("vlanEnable", UNSET)

        vlan_ids = cast(list[int], d.pop("vlanIds", UNSET))

        client_vlan_id = d.pop("clientVlanId", UNSET)

        topology_client_connected_ssid = cls(
            id=id,
            name=name,
            vlan_enable=vlan_enable,
            vlan_ids=vlan_ids,
            client_vlan_id=client_vlan_id,
        )

        topology_client_connected_ssid.additional_properties = d
        return topology_client_connected_ssid

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
