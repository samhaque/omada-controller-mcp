from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WiredPortV3DTO")


@_attrs_define
class WiredPortV3DTO:
    """Downlink Port

    Attributes:
        port (str | Unset): Port Id
        standard_port (str | Unset): Standard Port of Stack
        lag_id (str | Unset): Lag Id
        mlag_id (str | Unset): Mlag Id
        poe_power (int | Unset): Poe Power
        poe_power_decimal (float | Unset): Poe Power In Decimal
        lag_ports (list[int] | Unset): Lag Ports
        mlag_ports (list[int] | Unset): Mlag Ports
        standard_lag_ports (list[str] | Unset): Standard Lag Ports of Stack
        standard_mlag_ports (list[str] | Unset): Standard Mlag Ports of Stack
        name (str | Unset): Name of the port
        multi_switch_num (int | Unset): Multi Switch Num
        uplink_name (str | Unset): Uplink Name
        multi_switch_role (int | Unset): Multi Switch Role
    """

    port: str | Unset = UNSET
    standard_port: str | Unset = UNSET
    lag_id: str | Unset = UNSET
    mlag_id: str | Unset = UNSET
    poe_power: int | Unset = UNSET
    poe_power_decimal: float | Unset = UNSET
    lag_ports: list[int] | Unset = UNSET
    mlag_ports: list[int] | Unset = UNSET
    standard_lag_ports: list[str] | Unset = UNSET
    standard_mlag_ports: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    multi_switch_num: int | Unset = UNSET
    uplink_name: str | Unset = UNSET
    multi_switch_role: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port = self.standard_port

        lag_id = self.lag_id

        mlag_id = self.mlag_id

        poe_power = self.poe_power

        poe_power_decimal = self.poe_power_decimal

        lag_ports: list[int] | Unset = UNSET
        if not isinstance(self.lag_ports, Unset):
            lag_ports = self.lag_ports

        mlag_ports: list[int] | Unset = UNSET
        if not isinstance(self.mlag_ports, Unset):
            mlag_ports = self.mlag_ports

        standard_lag_ports: list[str] | Unset = UNSET
        if not isinstance(self.standard_lag_ports, Unset):
            standard_lag_ports = self.standard_lag_ports

        standard_mlag_ports: list[str] | Unset = UNSET
        if not isinstance(self.standard_mlag_ports, Unset):
            standard_mlag_ports = self.standard_mlag_ports

        name = self.name

        multi_switch_num = self.multi_switch_num

        uplink_name = self.uplink_name

        multi_switch_role = self.multi_switch_role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if mlag_id is not UNSET:
            field_dict["mlagId"] = mlag_id
        if poe_power is not UNSET:
            field_dict["poePower"] = poe_power
        if poe_power_decimal is not UNSET:
            field_dict["poePowerDecimal"] = poe_power_decimal
        if lag_ports is not UNSET:
            field_dict["lagPorts"] = lag_ports
        if mlag_ports is not UNSET:
            field_dict["mlagPorts"] = mlag_ports
        if standard_lag_ports is not UNSET:
            field_dict["standardLagPorts"] = standard_lag_ports
        if standard_mlag_ports is not UNSET:
            field_dict["standardMlagPorts"] = standard_mlag_ports
        if name is not UNSET:
            field_dict["name"] = name
        if multi_switch_num is not UNSET:
            field_dict["multiSwitchNum"] = multi_switch_num
        if uplink_name is not UNSET:
            field_dict["uplinkName"] = uplink_name
        if multi_switch_role is not UNSET:
            field_dict["multiSwitchRole"] = multi_switch_role

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        lag_id = d.pop("lagId", UNSET)

        mlag_id = d.pop("mlagId", UNSET)

        poe_power = d.pop("poePower", UNSET)

        poe_power_decimal = d.pop("poePowerDecimal", UNSET)

        lag_ports = cast(list[int], d.pop("lagPorts", UNSET))

        mlag_ports = cast(list[int], d.pop("mlagPorts", UNSET))

        standard_lag_ports = cast(list[str], d.pop("standardLagPorts", UNSET))

        standard_mlag_ports = cast(list[str], d.pop("standardMlagPorts", UNSET))

        name = d.pop("name", UNSET)

        multi_switch_num = d.pop("multiSwitchNum", UNSET)

        uplink_name = d.pop("uplinkName", UNSET)

        multi_switch_role = d.pop("multiSwitchRole", UNSET)

        wired_port_v3dto = cls(
            port=port,
            standard_port=standard_port,
            lag_id=lag_id,
            mlag_id=mlag_id,
            poe_power=poe_power,
            poe_power_decimal=poe_power_decimal,
            lag_ports=lag_ports,
            mlag_ports=mlag_ports,
            standard_lag_ports=standard_lag_ports,
            standard_mlag_ports=standard_mlag_ports,
            name=name,
            multi_switch_num=multi_switch_num,
            uplink_name=uplink_name,
            multi_switch_role=multi_switch_role,
        )

        wired_port_v3dto.additional_properties = d
        return wired_port_v3dto

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
