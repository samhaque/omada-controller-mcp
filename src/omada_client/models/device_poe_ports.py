from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DevicePoePorts")


@_attrs_define
class DevicePoePorts:
    """Device poe ports info.

    Attributes:
        port_num (int | Unset): Total port num.
        poe_port_ids (list[int] | Unset): List of ports supporting Poe.
    """

    port_num: int | Unset = UNSET
    poe_port_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_num = self.port_num

        poe_port_ids: list[int] | Unset = UNSET
        if not isinstance(self.poe_port_ids, Unset):
            poe_port_ids = self.poe_port_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_num is not UNSET:
            field_dict["portNum"] = port_num
        if poe_port_ids is not UNSET:
            field_dict["poePortIds"] = poe_port_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_num = d.pop("portNum", UNSET)

        poe_port_ids = cast(list[int], d.pop("poePortIds", UNSET))

        device_poe_ports = cls(
            port_num=port_num,
            poe_port_ids=poe_port_ids,
        )

        device_poe_ports.additional_properties = d
        return device_poe_ports

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
