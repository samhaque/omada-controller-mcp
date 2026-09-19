from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswStackUnitVO")


@_attrs_define
class OswStackUnitVO:
    """Unit List

    Attributes:
        mac (str): Device mac
        unit (int): Unit
        port_list (list[OswStandPortVO]): Port List
    """

    mac: str
    unit: int
    port_list: list[OswStandPortVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        unit = self.unit

        port_list = []
        for port_list_item_data in self.port_list:
            port_list_item = port_list_item_data.to_dict()
            port_list.append(port_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "unit": unit,
                "portList": port_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        mac = d.pop("mac")

        unit = d.pop("unit")

        port_list = []
        _port_list = d.pop("portList")
        for port_list_item_data in _port_list:
            port_list_item = OswStandPortVO.from_dict(port_list_item_data)

            port_list.append(port_list_item)

        osw_stack_unit_vo = cls(
            mac=mac,
            unit=unit,
            port_list=port_list,
        )

        osw_stack_unit_vo.additional_properties = d
        return osw_stack_unit_vo

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
