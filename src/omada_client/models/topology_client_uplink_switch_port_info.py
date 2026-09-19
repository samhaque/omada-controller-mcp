from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyClientUplinkSwitchPortInfo")


@_attrs_define
class TopologyClientUplinkSwitchPortInfo:
    """Uplink Port Information while Uplink Device is Switch.

    Attributes:
        port (int | Unset): Real Port Number or Port Number of Lag.
        standard_port (str | Unset): Standard Port of Stack, for Uplink Device is Stack.
        lag_id (int | Unset): Lag Id.
        lag_port (list[int] | Unset): Lag Ports.
    """

    port: int | Unset = UNSET
    standard_port: str | Unset = UNSET
    lag_id: int | Unset = UNSET
    lag_port: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port = self.standard_port

        lag_id = self.lag_id

        lag_port: list[int] | Unset = UNSET
        if not isinstance(self.lag_port, Unset):
            lag_port = self.lag_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if lag_port is not UNSET:
            field_dict["lagPort"] = lag_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        lag_id = d.pop("lagId", UNSET)

        lag_port = cast(list[int], d.pop("lagPort", UNSET))

        topology_client_uplink_switch_port_info = cls(
            port=port,
            standard_port=standard_port,
            lag_id=lag_id,
            lag_port=lag_port,
        )

        topology_client_uplink_switch_port_info.additional_properties = d
        return topology_client_uplink_switch_port_info

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
