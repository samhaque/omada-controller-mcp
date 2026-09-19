from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.reactive_pon_port_dto_reactive_status import (
    ReactivePonPortDTOReactiveStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReactivePonPortDTO")


@_attrs_define
class ReactivePonPortDTO:
    """Device configuration information.If the type of data is 'Object',ignore this field

    Attributes:
        reactive_status (ReactivePonPortDTOReactiveStatus | Unset): Whether there are ports that need to be
            reactivated.ReactiveStatus should be a value as follows:DISABLE:Indicates that there are no ports that need to
            be reactivated;ENABLE:Reading the port data indicates which ports need to be activated.
        pon_ports (list[str] | Unset): Port list to be activated
    """

    reactive_status: ReactivePonPortDTOReactiveStatus | Unset = UNSET
    pon_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reactive_status: str | Unset = UNSET
        if not isinstance(self.reactive_status, Unset):
            reactive_status = self.reactive_status.value

        pon_ports: list[str] | Unset = UNSET
        if not isinstance(self.pon_ports, Unset):
            pon_ports = self.pon_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reactive_status is not UNSET:
            field_dict["reactiveStatus"] = reactive_status
        if pon_ports is not UNSET:
            field_dict["ponPorts"] = pon_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _reactive_status = d.pop("reactiveStatus", UNSET)
        reactive_status: ReactivePonPortDTOReactiveStatus | Unset
        if isinstance(_reactive_status, Unset):
            reactive_status = UNSET
        else:
            reactive_status = ReactivePonPortDTOReactiveStatus(_reactive_status)

        pon_ports = cast(list[str], d.pop("ponPorts", UNSET))

        reactive_pon_port_dto = cls(
            reactive_status=reactive_status,
            pon_ports=pon_ports,
        )

        reactive_pon_port_dto.additional_properties = d
        return reactive_pon_port_dto

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
