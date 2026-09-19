from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientTrafficFilterOpenApiVO")


@_attrs_define
class ClientTrafficFilterOpenApiVO:
    """Client traffic filtering condition

    Attributes:
        network (str | Unset): Network name
        vlan_id (str | Unset): VLAN ID. The VLAN ID range is 1–4096 or Untag.
    """

    network: str | Unset = UNSET
    vlan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network = self.network

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network is not UNSET:
            field_dict["network"] = network
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network = d.pop("network", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        client_traffic_filter_open_api_vo = cls(
            network=network,
            vlan_id=vlan_id,
        )

        client_traffic_filter_open_api_vo.additional_properties = d
        return client_traffic_filter_open_api_vo

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
