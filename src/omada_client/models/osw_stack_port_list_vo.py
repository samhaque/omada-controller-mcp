from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStackPortListVO")


@_attrs_define
class OswStackPortListVO:
    """List of Stack ID and Standard Ports.

    Attributes:
        stack_id (str | Unset): Stack Id
        standard_ports (list[str] | Unset): Standard port should be in the format of unit/slot/portId. e.g. 1/0/1
    """

    stack_id: str | Unset = UNSET
    standard_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        standard_ports: list[str] | Unset = UNSET
        if not isinstance(self.standard_ports, Unset):
            standard_ports = self.standard_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if standard_ports is not UNSET:
            field_dict["standardPorts"] = standard_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        standard_ports = cast(list[str], d.pop("standardPorts", UNSET))

        osw_stack_port_list_vo = cls(
            stack_id=stack_id,
            standard_ports=standard_ports,
        )

        osw_stack_port_list_vo.additional_properties = d
        return osw_stack_port_list_vo

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
