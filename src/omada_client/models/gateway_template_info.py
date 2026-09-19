from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_port_config import GatewayPortConfig


T = TypeVar("T", bound="GatewayTemplateInfo")


@_attrs_define
class GatewayTemplateInfo:
    """
    Attributes:
        id (str | Unset): The ID of gateway template
        show_model (str | Unset): Gateway model description
        port_configs (list[GatewayPortConfig] | Unset): Gateway port configs
    """

    id: str | Unset = UNSET
    show_model: str | Unset = UNSET
    port_configs: list[GatewayPortConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        show_model = self.show_model

        port_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_configs, Unset):
            port_configs = []
            for port_configs_item_data in self.port_configs:
                port_configs_item = port_configs_item_data.to_dict()
                port_configs.append(port_configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if port_configs is not UNSET:
            field_dict["portConfigs"] = port_configs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.gateway_port_config import GatewayPortConfig

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        show_model = d.pop("showModel", UNSET)

        _port_configs = d.pop("portConfigs", UNSET)
        port_configs: list[GatewayPortConfig] | Unset = UNSET
        if _port_configs is not UNSET:
            port_configs = []
            for port_configs_item_data in _port_configs:
                port_configs_item = GatewayPortConfig.from_dict(port_configs_item_data)

                port_configs.append(port_configs_item)

        gateway_template_info = cls(
            id=id,
            show_model=show_model,
            port_configs=port_configs,
        )

        gateway_template_info.additional_properties = d
        return gateway_template_info

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
