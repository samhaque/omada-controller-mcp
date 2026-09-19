from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologySSID")


@_attrs_define
class TopologySSID:
    """SSID.

    Attributes:
        id (str | Unset): SSID ID.
        name (str | Unset): SSID Name.
        wlan_name (str | Unset): WLAN group name
        vlan_enable (bool | Unset): Whether enable vlan.
        vlan_ids (list[int] | Unset): Vlan IDs.
        configuring (bool | Unset): Whether SSID is configuring.
        client_num (int | Unset): Client Num.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    wlan_name: str | Unset = UNSET
    vlan_enable: bool | Unset = UNSET
    vlan_ids: list[int] | Unset = UNSET
    configuring: bool | Unset = UNSET
    client_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        wlan_name = self.wlan_name

        vlan_enable = self.vlan_enable

        vlan_ids: list[int] | Unset = UNSET
        if not isinstance(self.vlan_ids, Unset):
            vlan_ids = self.vlan_ids

        configuring = self.configuring

        client_num = self.client_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if wlan_name is not UNSET:
            field_dict["wlanName"] = wlan_name
        if vlan_enable is not UNSET:
            field_dict["vlanEnable"] = vlan_enable
        if vlan_ids is not UNSET:
            field_dict["vlanIds"] = vlan_ids
        if configuring is not UNSET:
            field_dict["configuring"] = configuring
        if client_num is not UNSET:
            field_dict["clientNum"] = client_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        wlan_name = d.pop("wlanName", UNSET)

        vlan_enable = d.pop("vlanEnable", UNSET)

        vlan_ids = cast(list[int], d.pop("vlanIds", UNSET))

        configuring = d.pop("configuring", UNSET)

        client_num = d.pop("clientNum", UNSET)

        topology_ssid = cls(
            id=id,
            name=name,
            wlan_name=wlan_name,
            vlan_enable=vlan_enable,
            vlan_ids=vlan_ids,
            configuring=configuring,
            client_num=client_num,
        )

        topology_ssid.additional_properties = d
        return topology_ssid

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
