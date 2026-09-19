from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpticalLinkDetailConfigDTO")


@_attrs_define
class OpticalLinkDetailConfigDTO:
    """
    Attributes:
        received_optical_power (float | Unset): ONU's received power, in dBm.
        transmitted_optical_power (float | Unset): ONU's transmission power, in dBm.
        bias_current (float | Unset): ONU's bias current, in mA.
        working_voltage (int | Unset): ONU's working voltage, in mV.
        working_temperature (float | Unset): ONU's operating temperature, in °C.
    """

    received_optical_power: float | Unset = UNSET
    transmitted_optical_power: float | Unset = UNSET
    bias_current: float | Unset = UNSET
    working_voltage: int | Unset = UNSET
    working_temperature: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        received_optical_power = self.received_optical_power

        transmitted_optical_power = self.transmitted_optical_power

        bias_current = self.bias_current

        working_voltage = self.working_voltage

        working_temperature = self.working_temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if received_optical_power is not UNSET:
            field_dict["receivedOpticalPower"] = received_optical_power
        if transmitted_optical_power is not UNSET:
            field_dict["transmittedOpticalPower"] = transmitted_optical_power
        if bias_current is not UNSET:
            field_dict["biasCurrent"] = bias_current
        if working_voltage is not UNSET:
            field_dict["workingVoltage"] = working_voltage
        if working_temperature is not UNSET:
            field_dict["workingTemperature"] = working_temperature

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        received_optical_power = d.pop("receivedOpticalPower", UNSET)

        transmitted_optical_power = d.pop("transmittedOpticalPower", UNSET)

        bias_current = d.pop("biasCurrent", UNSET)

        working_voltage = d.pop("workingVoltage", UNSET)

        working_temperature = d.pop("workingTemperature", UNSET)

        optical_link_detail_config_dto = cls(
            received_optical_power=received_optical_power,
            transmitted_optical_power=transmitted_optical_power,
            bias_current=bias_current,
            working_voltage=working_voltage,
            working_temperature=working_temperature,
        )

        optical_link_detail_config_dto.additional_properties = d
        return optical_link_detail_config_dto

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
