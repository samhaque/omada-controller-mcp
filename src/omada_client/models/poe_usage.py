from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_poe import PortPoe


T = TypeVar("T", bound="PoeUsage")


@_attrs_define
class PoeUsage:
    """
    Attributes:
        mac (str | Unset): Device MAC
        name (str | Unset): Device name
        port_num (int | Unset): Device port Number
        total_power_used (int | Unset): Total power used (in watts)
        total_percent_used (float | Unset): Percentage of total power used (integer reserved)
        total_power (int | Unset): The total power of the switch port's POE (in watts)
        poe_ports (list[PortPoe] | Unset): Device PoE Ports
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    port_num: int | Unset = UNSET
    total_power_used: int | Unset = UNSET
    total_percent_used: float | Unset = UNSET
    total_power: int | Unset = UNSET
    poe_ports: list[PortPoe] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        port_num = self.port_num

        total_power_used = self.total_power_used

        total_percent_used = self.total_percent_used

        total_power = self.total_power

        poe_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.poe_ports, Unset):
            poe_ports = []
            for poe_ports_item_data in self.poe_ports:
                poe_ports_item = poe_ports_item_data.to_dict()
                poe_ports.append(poe_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if port_num is not UNSET:
            field_dict["portNum"] = port_num
        if total_power_used is not UNSET:
            field_dict["totalPowerUsed"] = total_power_used
        if total_percent_used is not UNSET:
            field_dict["totalPercentUsed"] = total_percent_used
        if total_power is not UNSET:
            field_dict["totalPower"] = total_power
        if poe_ports is not UNSET:
            field_dict["poePorts"] = poe_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_poe import PortPoe

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        port_num = d.pop("portNum", UNSET)

        total_power_used = d.pop("totalPowerUsed", UNSET)

        total_percent_used = d.pop("totalPercentUsed", UNSET)

        total_power = d.pop("totalPower", UNSET)

        _poe_ports = d.pop("poePorts", UNSET)
        poe_ports: list[PortPoe] | Unset = UNSET
        if _poe_ports is not UNSET:
            poe_ports = []
            for poe_ports_item_data in _poe_ports:
                poe_ports_item = PortPoe.from_dict(poe_ports_item_data)

                poe_ports.append(poe_ports_item)

        poe_usage = cls(
            mac=mac,
            name=name,
            port_num=port_num,
            total_power_used=total_power_used,
            total_percent_used=total_percent_used,
            total_power=total_power,
            poe_ports=poe_ports,
        )

        poe_usage.additional_properties = d
        return poe_usage

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
