from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswDDMInfoOpenApiVO")


@_attrs_define
class OswDDMInfoOpenApiVO:
    """
    Attributes:
        port (int | Unset): Switch portId.
        standard_port (str | Unset): Switch stack portId(unit/slot/port).
        rx_power (float | Unset): The received optical power(mW) of the optical module.
        rx_power_dbm (float | Unset): The received optical power(dbm) of the optical module.
        bias_current (float | Unset): The biasCurrent(mA) of the optical module.
        data_ready (int | Unset): Whether the DDM data is valid(0:invalid, 1:valid).
        voltage (float | Unset): The voltage(V) of the optical module.
        transmit_fault (int | Unset): Whether the optical module is in the Transmission Fault state(0:false, 1:true).
        tx_power (float | Unset): The transmitted optical power(mW) of the optical module.
        tx_power_dbm (float | Unset): The transmitted optical power(dbm) of the optical module.
        loss_of_signal (int | Unset): Whether the optical module is in the Loss Of Signal state(0:false, 1:true).
        temperature (float | Unset): The temperature(Celsius) of the optical module.
        temperature_fah (float | Unset): The temperature(Fahrenheit) of the optical module.
    """

    port: int | Unset = UNSET
    standard_port: str | Unset = UNSET
    rx_power: float | Unset = UNSET
    rx_power_dbm: float | Unset = UNSET
    bias_current: float | Unset = UNSET
    data_ready: int | Unset = UNSET
    voltage: float | Unset = UNSET
    transmit_fault: int | Unset = UNSET
    tx_power: float | Unset = UNSET
    tx_power_dbm: float | Unset = UNSET
    loss_of_signal: int | Unset = UNSET
    temperature: float | Unset = UNSET
    temperature_fah: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port = self.standard_port

        rx_power = self.rx_power

        rx_power_dbm = self.rx_power_dbm

        bias_current = self.bias_current

        data_ready = self.data_ready

        voltage = self.voltage

        transmit_fault = self.transmit_fault

        tx_power = self.tx_power

        tx_power_dbm = self.tx_power_dbm

        loss_of_signal = self.loss_of_signal

        temperature = self.temperature

        temperature_fah = self.temperature_fah

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if rx_power is not UNSET:
            field_dict["rxPower"] = rx_power
        if rx_power_dbm is not UNSET:
            field_dict["rxPowerDbm"] = rx_power_dbm
        if bias_current is not UNSET:
            field_dict["biasCurrent"] = bias_current
        if data_ready is not UNSET:
            field_dict["dataReady"] = data_ready
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if transmit_fault is not UNSET:
            field_dict["transmitFault"] = transmit_fault
        if tx_power is not UNSET:
            field_dict["txPower"] = tx_power
        if tx_power_dbm is not UNSET:
            field_dict["txPowerDbm"] = tx_power_dbm
        if loss_of_signal is not UNSET:
            field_dict["lossOfSignal"] = loss_of_signal
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if temperature_fah is not UNSET:
            field_dict["temperatureFah"] = temperature_fah

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        rx_power = d.pop("rxPower", UNSET)

        rx_power_dbm = d.pop("rxPowerDbm", UNSET)

        bias_current = d.pop("biasCurrent", UNSET)

        data_ready = d.pop("dataReady", UNSET)

        voltage = d.pop("voltage", UNSET)

        transmit_fault = d.pop("transmitFault", UNSET)

        tx_power = d.pop("txPower", UNSET)

        tx_power_dbm = d.pop("txPowerDbm", UNSET)

        loss_of_signal = d.pop("lossOfSignal", UNSET)

        temperature = d.pop("temperature", UNSET)

        temperature_fah = d.pop("temperatureFah", UNSET)

        osw_ddm_info_open_api_vo = cls(
            port=port,
            standard_port=standard_port,
            rx_power=rx_power,
            rx_power_dbm=rx_power_dbm,
            bias_current=bias_current,
            data_ready=data_ready,
            voltage=voltage,
            transmit_fault=transmit_fault,
            tx_power=tx_power,
            tx_power_dbm=tx_power_dbm,
            loss_of_signal=loss_of_signal,
            temperature=temperature,
            temperature_fah=temperature_fah,
        )

        osw_ddm_info_open_api_vo.additional_properties = d
        return osw_ddm_info_open_api_vo

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
