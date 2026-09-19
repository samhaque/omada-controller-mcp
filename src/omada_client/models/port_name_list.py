from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.switch_multi_port_name import SwitchMultiPortName


T = TypeVar("T", bound="PortNameList")


@_attrs_define
class PortNameList:
    """
    Attributes:
        port_name_list (list[SwitchMultiPortName]): Port name list
    """

    port_name_list: list[SwitchMultiPortName]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_name_list = []
        for port_name_list_item_data in self.port_name_list:
            port_name_list_item = port_name_list_item_data.to_dict()
            port_name_list.append(port_name_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portNameList": port_name_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.switch_multi_port_name import SwitchMultiPortName

        d = dict(src_dict)
        port_name_list = []
        _port_name_list = d.pop("portNameList")
        for port_name_list_item_data in _port_name_list:
            port_name_list_item = SwitchMultiPortName.from_dict(
                port_name_list_item_data
            )

            port_name_list.append(port_name_list_item)

        port_name_list = cls(
            port_name_list=port_name_list,
        )

        port_name_list.additional_properties = d
        return port_name_list

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
