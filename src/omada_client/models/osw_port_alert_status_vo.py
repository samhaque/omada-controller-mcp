from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswPortAlertStatusVO")


@_attrs_define
class OswPortAlertStatusVO:
    """
    Attributes:
        power (str | Unset):
        status (int | Unset):
        voltage (float | Unset):
    """

    power: str | Unset = UNSET
    status: int | Unset = UNSET
    voltage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        power = self.power

        status = self.status

        voltage = self.voltage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if power is not UNSET:
            field_dict["power"] = power
        if status is not UNSET:
            field_dict["status"] = status
        if voltage is not UNSET:
            field_dict["voltage"] = voltage

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        power = d.pop("power", UNSET)

        status = d.pop("status", UNSET)

        voltage = d.pop("voltage", UNSET)

        osw_port_alert_status_vo = cls(
            power=power,
            status=status,
            voltage=voltage,
        )

        osw_port_alert_status_vo.additional_properties = d
        return osw_port_alert_status_vo

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
