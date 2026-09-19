from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternetBasicInfo")


@_attrs_define
class InternetBasicInfo:
    """Port info list

    Attributes:
        port_id (str | Unset): Port ID
        port_name (str | Unset): Port name
        port_mode (int | Unset): Port mode should be a value as follows: 0: WAN; 1: LAN.
        port_type (int | Unset): Port type should be a value as follows: 0: WAN; 1: WAN/LAN.
    """

    port_id: str | Unset = UNSET
    port_name: str | Unset = UNSET
    port_mode: int | Unset = UNSET
    port_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        port_name = self.port_name

        port_mode = self.port_mode

        port_type = self.port_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if port_mode is not UNSET:
            field_dict["portMode"] = port_mode
        if port_type is not UNSET:
            field_dict["portType"] = port_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        port_name = d.pop("portName", UNSET)

        port_mode = d.pop("portMode", UNSET)

        port_type = d.pop("portType", UNSET)

        internet_basic_info = cls(
            port_id=port_id,
            port_name=port_name,
            port_mode=port_mode,
            port_type=port_type,
        )

        internet_basic_info.additional_properties = d
        return internet_basic_info

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
