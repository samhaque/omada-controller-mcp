from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_vo import PortVO


T = TypeVar("T", bound="DhcpSnoopImbpVO")


@_attrs_define
class DhcpSnoopImbpVO:
    """
    Attributes:
        mac (str | Unset): The mac of the general device.
        stack_id (str | Unset): The stack of the stack device.
        ports (list[PortVO] | Unset): The ports selected.
    """

    mac: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    ports: list[PortVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        stack_id = self.stack_id

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_vo import PortVO

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        stack_id = d.pop("stackId", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[PortVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = PortVO.from_dict(ports_item_data)

                ports.append(ports_item)

        dhcp_snoop_imbp_vo = cls(
            mac=mac,
            stack_id=stack_id,
            ports=ports,
        )

        dhcp_snoop_imbp_vo.additional_properties = d
        return dhcp_snoop_imbp_vo

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
