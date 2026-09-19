from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DDMStatusResultVO")


@_attrs_define
class DDMStatusResultVO:
    """
    Attributes:
        port (str | Unset): OLT optical ports, including Ethernet optical ports and PON ports.
        temperature (str | Unset): Temperature of the port optical module.
        temperature_fahrenheit (float | Unset): Temperature(Fahrenheit) of the port optical module.
        temperature_flag (int | Unset): Port optical module temperature alert information.
        voltage (str | Unset): Port optical module voltage.
        voltage_flag (int | Unset): Port optical module voltage alert information.
        bias_current (str | Unset): Port optical module bias current.
        bias_current_flag (int | Unset): Port optical module bias current alert information.
        tx_powerdbm (str | Unset): Port optical module transmission power(dbm).
        tx_powerm_w (float | Unset): Port optical module transmission power(mW).
        tx_power_flag (int | Unset): Port optical module transmission power alert information.
        rx_powerdbm (str | Unset): Port optical module received power(dbm).
        rx_powerm_w (float | Unset): Port optical module received power(mW).
        rx_power_flag (int | Unset): Port optical module received power alert information.
        transmit_fault (int | Unset): Weather the signal from the remote optical module is distorted
        loss_of_signal (bool | Unset): Whether the local optical module signal is distorted.
        data_ready (bool | Unset): Whether the port optical module is in an available state.
    """

    port: str | Unset = UNSET
    temperature: str | Unset = UNSET
    temperature_fahrenheit: float | Unset = UNSET
    temperature_flag: int | Unset = UNSET
    voltage: str | Unset = UNSET
    voltage_flag: int | Unset = UNSET
    bias_current: str | Unset = UNSET
    bias_current_flag: int | Unset = UNSET
    tx_powerdbm: str | Unset = UNSET
    tx_powerm_w: float | Unset = UNSET
    tx_power_flag: int | Unset = UNSET
    rx_powerdbm: str | Unset = UNSET
    rx_powerm_w: float | Unset = UNSET
    rx_power_flag: int | Unset = UNSET
    transmit_fault: int | Unset = UNSET
    loss_of_signal: bool | Unset = UNSET
    data_ready: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        temperature = self.temperature

        temperature_fahrenheit = self.temperature_fahrenheit

        temperature_flag = self.temperature_flag

        voltage = self.voltage

        voltage_flag = self.voltage_flag

        bias_current = self.bias_current

        bias_current_flag = self.bias_current_flag

        tx_powerdbm = self.tx_powerdbm

        tx_powerm_w = self.tx_powerm_w

        tx_power_flag = self.tx_power_flag

        rx_powerdbm = self.rx_powerdbm

        rx_powerm_w = self.rx_powerm_w

        rx_power_flag = self.rx_power_flag

        transmit_fault = self.transmit_fault

        loss_of_signal = self.loss_of_signal

        data_ready = self.data_ready

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if temperature_fahrenheit is not UNSET:
            field_dict["temperature(Fahrenheit)"] = temperature_fahrenheit
        if temperature_flag is not UNSET:
            field_dict["temperatureFlag"] = temperature_flag
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if voltage_flag is not UNSET:
            field_dict["voltageFlag"] = voltage_flag
        if bias_current is not UNSET:
            field_dict["biasCurrent"] = bias_current
        if bias_current_flag is not UNSET:
            field_dict["biasCurrentFlag"] = bias_current_flag
        if tx_powerdbm is not UNSET:
            field_dict["txPower(dbm)"] = tx_powerdbm
        if tx_powerm_w is not UNSET:
            field_dict["txPower(mW)"] = tx_powerm_w
        if tx_power_flag is not UNSET:
            field_dict["txPowerFlag"] = tx_power_flag
        if rx_powerdbm is not UNSET:
            field_dict["rxPower(dbm)"] = rx_powerdbm
        if rx_powerm_w is not UNSET:
            field_dict["rxPower(mW)"] = rx_powerm_w
        if rx_power_flag is not UNSET:
            field_dict["rxPowerFlag"] = rx_power_flag
        if transmit_fault is not UNSET:
            field_dict["transmitFault"] = transmit_fault
        if loss_of_signal is not UNSET:
            field_dict["lossOfSignal"] = loss_of_signal
        if data_ready is not UNSET:
            field_dict["dataReady"] = data_ready

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        temperature = d.pop("temperature", UNSET)

        temperature_fahrenheit = d.pop("temperature(Fahrenheit)", UNSET)

        temperature_flag = d.pop("temperatureFlag", UNSET)

        voltage = d.pop("voltage", UNSET)

        voltage_flag = d.pop("voltageFlag", UNSET)

        bias_current = d.pop("biasCurrent", UNSET)

        bias_current_flag = d.pop("biasCurrentFlag", UNSET)

        tx_powerdbm = d.pop("txPower(dbm)", UNSET)

        tx_powerm_w = d.pop("txPower(mW)", UNSET)

        tx_power_flag = d.pop("txPowerFlag", UNSET)

        rx_powerdbm = d.pop("rxPower(dbm)", UNSET)

        rx_powerm_w = d.pop("rxPower(mW)", UNSET)

        rx_power_flag = d.pop("rxPowerFlag", UNSET)

        transmit_fault = d.pop("transmitFault", UNSET)

        loss_of_signal = d.pop("lossOfSignal", UNSET)

        data_ready = d.pop("dataReady", UNSET)

        ddm_status_result_vo = cls(
            port=port,
            temperature=temperature,
            temperature_fahrenheit=temperature_fahrenheit,
            temperature_flag=temperature_flag,
            voltage=voltage,
            voltage_flag=voltage_flag,
            bias_current=bias_current,
            bias_current_flag=bias_current_flag,
            tx_powerdbm=tx_powerdbm,
            tx_powerm_w=tx_powerm_w,
            tx_power_flag=tx_power_flag,
            rx_powerdbm=rx_powerdbm,
            rx_powerm_w=rx_powerm_w,
            rx_power_flag=rx_power_flag,
            transmit_fault=transmit_fault,
            loss_of_signal=loss_of_signal,
            data_ready=data_ready,
        )

        ddm_status_result_vo.additional_properties = d
        return ddm_status_result_vo

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
