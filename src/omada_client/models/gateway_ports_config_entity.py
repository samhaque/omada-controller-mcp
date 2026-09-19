from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_port_config import GatewayPortConfig


T = TypeVar("T", bound="GatewayPortsConfigEntity")


@_attrs_define
class GatewayPortsConfigEntity:
    """
    Attributes:
        ports_config (list[GatewayPortConfig] | Unset): gateway port config entity
    """

    ports_config: list[GatewayPortConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ports_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports_config, Unset):
            ports_config = []
            for ports_config_item_data in self.ports_config:
                ports_config_item = ports_config_item_data.to_dict()
                ports_config.append(ports_config_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ports_config is not UNSET:
            field_dict["portsConfig"] = ports_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.gateway_port_config import GatewayPortConfig

        d = dict(src_dict)
        _ports_config = d.pop("portsConfig", UNSET)
        ports_config: list[GatewayPortConfig] | Unset = UNSET
        if _ports_config is not UNSET:
            ports_config = []
            for ports_config_item_data in _ports_config:
                ports_config_item = GatewayPortConfig.from_dict(ports_config_item_data)

                ports_config.append(ports_config_item)

        gateway_ports_config_entity = cls(
            ports_config=ports_config,
        )

        gateway_ports_config_entity.additional_properties = d
        return gateway_ports_config_entity

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
