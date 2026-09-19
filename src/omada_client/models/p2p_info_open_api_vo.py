from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="P2PInfoOpenApiVO")


@_attrs_define
class P2PInfoOpenApiVO:
    """Child aps info

    Attributes:
        device_mac (str | Unset): Device MAC.
        device_name (str | Unset): Device name.
    """

    device_mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        device_name = self.device_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_mac = d.pop("deviceMac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        p2p_info_open_api_vo = cls(
            device_mac=device_mac,
            device_name=device_name,
        )

        p2p_info_open_api_vo.additional_properties = d
        return p2p_info_open_api_vo

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
