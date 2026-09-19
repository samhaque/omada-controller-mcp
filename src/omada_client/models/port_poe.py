from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortPoe")


@_attrs_define
class PortPoe:
    """Device PoE Ports

    Attributes:
        port_id (int | Unset): Switch port ID
        poe_supported (bool | Unset): Switch port supported
        poe_enabled (bool | Unset): Switch port enable
        poe_power (int | Unset): Switch port power
        poe_percent (int | Unset): Switch port percent
    """

    port_id: int | Unset = UNSET
    poe_supported: bool | Unset = UNSET
    poe_enabled: bool | Unset = UNSET
    poe_power: int | Unset = UNSET
    poe_percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        poe_supported = self.poe_supported

        poe_enabled = self.poe_enabled

        poe_power = self.poe_power

        poe_percent = self.poe_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if poe_supported is not UNSET:
            field_dict["poeSupported"] = poe_supported
        if poe_enabled is not UNSET:
            field_dict["poeEnabled"] = poe_enabled
        if poe_power is not UNSET:
            field_dict["poePower"] = poe_power
        if poe_percent is not UNSET:
            field_dict["poePercent"] = poe_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        poe_supported = d.pop("poeSupported", UNSET)

        poe_enabled = d.pop("poeEnabled", UNSET)

        poe_power = d.pop("poePower", UNSET)

        poe_percent = d.pop("poePercent", UNSET)

        port_poe = cls(
            port_id=port_id,
            poe_supported=poe_supported,
            poe_enabled=poe_enabled,
            poe_power=poe_power,
            poe_percent=poe_percent,
        )

        port_poe.additional_properties = d
        return port_poe

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
