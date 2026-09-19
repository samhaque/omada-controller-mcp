from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="OswStandPortVO")


@_attrs_define
class OswStandPortVO:
    """Stack port aggregation group member port

    Attributes:
        unit (int): Unit
        slot (int): Slot
        port (int): Port
    """

    unit: int
    slot: int
    port: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        slot = self.slot

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unit": unit,
                "slot": slot,
                "port": port,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unit = d.pop("unit")

        slot = d.pop("slot")

        port = d.pop("port")

        osw_stand_port_vo = cls(
            unit=unit,
            slot=slot,
            port=port,
        )

        osw_stand_port_vo.additional_properties = d
        return osw_stand_port_vo

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
