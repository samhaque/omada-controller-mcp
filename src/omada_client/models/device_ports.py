from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DevicePorts")


@_attrs_define
class DevicePorts:
    """Device ports info.

    Attributes:
        port_num (int | Unset): Device total ports number.
        port_ids (list[int] | Unset): List of device ports supporting port schedule.
    """

    port_num: int | Unset = UNSET
    port_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_num = self.port_num

        port_ids: list[int] | Unset = UNSET
        if not isinstance(self.port_ids, Unset):
            port_ids = self.port_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_num is not UNSET:
            field_dict["portNum"] = port_num
        if port_ids is not UNSET:
            field_dict["portIds"] = port_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_num = d.pop("portNum", UNSET)

        port_ids = cast(list[int], d.pop("portIds", UNSET))

        device_ports = cls(
            port_num=port_num,
            port_ids=port_ids,
        )

        device_ports.additional_properties = d
        return device_ports

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
