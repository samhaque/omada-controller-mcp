from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoSelectWanPortResult")


@_attrs_define
class AutoSelectWanPortResult:
    """A list of the auto select Wan port result.

    Attributes:
        device_mac (str | Unset): The device MAC of the sdWan member.
        recommend_wan_id (str | Unset): Recommend Wan ID.
    """

    device_mac: str | Unset = UNSET
    recommend_wan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        recommend_wan_id = self.recommend_wan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if recommend_wan_id is not UNSET:
            field_dict["recommendWanId"] = recommend_wan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_mac = d.pop("deviceMac", UNSET)

        recommend_wan_id = d.pop("recommendWanId", UNSET)

        auto_select_wan_port_result = cls(
            device_mac=device_mac,
            recommend_wan_id=recommend_wan_id,
        )

        auto_select_wan_port_result.additional_properties = d
        return auto_select_wan_port_result

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
