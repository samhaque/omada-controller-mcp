from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lte_wan_port_setting_open_api_vo import LteWanPortSettingOpenApiVO


T = TypeVar("T", bound="LteWanSettingOpenApiVO")


@_attrs_define
class LteWanSettingOpenApiVO:
    """The setting of the WAN lte.

    Attributes:
        port_uuid (str): LTE WAN port uuid
        port_name (str | Unset): LTE WAN port name
        port_desc (str | Unset): LTE WAN port description
        lte_wan_ports_config (list[LteWanPortSettingOpenApiVO] | Unset): LTE WAN ports config
    """

    port_uuid: str
    port_name: str | Unset = UNSET
    port_desc: str | Unset = UNSET
    lte_wan_ports_config: list[LteWanPortSettingOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_uuid = self.port_uuid

        port_name = self.port_name

        port_desc = self.port_desc

        lte_wan_ports_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lte_wan_ports_config, Unset):
            lte_wan_ports_config = []
            for lte_wan_ports_config_item_data in self.lte_wan_ports_config:
                lte_wan_ports_config_item = lte_wan_ports_config_item_data.to_dict()
                lte_wan_ports_config.append(lte_wan_ports_config_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portUuid": port_uuid,
            }
        )
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if port_desc is not UNSET:
            field_dict["portDesc"] = port_desc
        if lte_wan_ports_config is not UNSET:
            field_dict["lteWanPortsConfig"] = lte_wan_ports_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lte_wan_port_setting_open_api_vo import (
            LteWanPortSettingOpenApiVO,
        )

        d = dict(src_dict)
        port_uuid = d.pop("portUuid")

        port_name = d.pop("portName", UNSET)

        port_desc = d.pop("portDesc", UNSET)

        _lte_wan_ports_config = d.pop("lteWanPortsConfig", UNSET)
        lte_wan_ports_config: list[LteWanPortSettingOpenApiVO] | Unset = UNSET
        if _lte_wan_ports_config is not UNSET:
            lte_wan_ports_config = []
            for lte_wan_ports_config_item_data in _lte_wan_ports_config:
                lte_wan_ports_config_item = LteWanPortSettingOpenApiVO.from_dict(
                    lte_wan_ports_config_item_data
                )

                lte_wan_ports_config.append(lte_wan_ports_config_item)

        lte_wan_setting_open_api_vo = cls(
            port_uuid=port_uuid,
            port_name=port_name,
            port_desc=port_desc,
            lte_wan_ports_config=lte_wan_ports_config,
        )

        lte_wan_setting_open_api_vo.additional_properties = d
        return lte_wan_setting_open_api_vo

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
