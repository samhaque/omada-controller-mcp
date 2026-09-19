from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.port_param_vo import PortParamVO


T = TypeVar("T", bound="ClearCountersVO")


@_attrs_define
class ClearCountersVO:
    """
    Attributes:
        port_list (list[PortParamVO]):
    """

    port_list: list[PortParamVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_list = []
        for port_list_item_data in self.port_list:
            port_list_item = port_list_item_data.to_dict()
            port_list.append(port_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portList": port_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_param_vo import PortParamVO

        d = dict(src_dict)
        port_list = []
        _port_list = d.pop("portList")
        for port_list_item_data in _port_list:
            port_list_item = PortParamVO.from_dict(port_list_item_data)

            port_list.append(port_list_item)

        clear_counters_vo = cls(
            port_list=port_list,
        )

        clear_counters_vo.additional_properties = d
        return clear_counters_vo

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
