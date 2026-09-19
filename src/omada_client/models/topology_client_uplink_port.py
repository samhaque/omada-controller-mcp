from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyClientUplinkPort")


@_attrs_define
class TopologyClientUplinkPort:
    """Uplink port information while connection is wired.

    Attributes:
        port (int | Unset): Real Port Number or Port Number of Lag.
        name (str | Unset): Name of the Port.
        standard_port (str | Unset): Standard Port of Stack, for Uplink Device is Stack.
        lag_id (int | Unset): Lag Id.
        poe_power (float | Unset): Poe power, unit: W.
        poe_power_decimal (float | Unset): Poe Power Decimal, unit: W.
        lag_ports (list[int] | Unset): Lag Ports.
        standard_lag_ports (list[str] | Unset): Standard Lag Ports.
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    standard_port: str | Unset = UNSET
    lag_id: int | Unset = UNSET
    poe_power: float | Unset = UNSET
    poe_power_decimal: float | Unset = UNSET
    lag_ports: list[int] | Unset = UNSET
    standard_lag_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        standard_port = self.standard_port

        lag_id = self.lag_id

        poe_power = self.poe_power

        poe_power_decimal = self.poe_power_decimal

        lag_ports: list[int] | Unset = UNSET
        if not isinstance(self.lag_ports, Unset):
            lag_ports = self.lag_ports

        standard_lag_ports: list[str] | Unset = UNSET
        if not isinstance(self.standard_lag_ports, Unset):
            standard_lag_ports = self.standard_lag_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if poe_power is not UNSET:
            field_dict["poePower"] = poe_power
        if poe_power_decimal is not UNSET:
            field_dict["poePowerDecimal"] = poe_power_decimal
        if lag_ports is not UNSET:
            field_dict["lagPorts"] = lag_ports
        if standard_lag_ports is not UNSET:
            field_dict["standardLagPorts"] = standard_lag_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        lag_id = d.pop("lagId", UNSET)

        poe_power = d.pop("poePower", UNSET)

        poe_power_decimal = d.pop("poePowerDecimal", UNSET)

        lag_ports = cast(list[int], d.pop("lagPorts", UNSET))

        standard_lag_ports = cast(list[str], d.pop("standardLagPorts", UNSET))

        topology_client_uplink_port = cls(
            port=port,
            name=name,
            standard_port=standard_port,
            lag_id=lag_id,
            poe_power=poe_power,
            poe_power_decimal=poe_power_decimal,
            lag_ports=lag_ports,
            standard_lag_ports=standard_lag_ports,
        )

        topology_client_uplink_port.additional_properties = d
        return topology_client_uplink_port

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
