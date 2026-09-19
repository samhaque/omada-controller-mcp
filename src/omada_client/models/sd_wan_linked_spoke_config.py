from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SdWanLinkedSpokeConfig")


@_attrs_define
class SdWanLinkedSpokeConfig:
    """A list of linked-spokes of the SD-WAN group

    Attributes:
        device_mac_1 (str | Unset): The device MAC of one of the two linked-spokes
        device_mac_2 (str | Unset): Another device MAC of the two linked-spokes
    """

    device_mac_1: str | Unset = UNSET
    device_mac_2: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac_1 = self.device_mac_1

        device_mac_2 = self.device_mac_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_mac_1 is not UNSET:
            field_dict["deviceMac1"] = device_mac_1
        if device_mac_2 is not UNSET:
            field_dict["deviceMac2"] = device_mac_2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_mac_1 = d.pop("deviceMac1", UNSET)

        device_mac_2 = d.pop("deviceMac2", UNSET)

        sd_wan_linked_spoke_config = cls(
            device_mac_1=device_mac_1,
            device_mac_2=device_mac_2,
        )

        sd_wan_linked_spoke_config.additional_properties = d
        return sd_wan_linked_spoke_config

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
