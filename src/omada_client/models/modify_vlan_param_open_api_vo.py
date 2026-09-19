from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_network_open_api_v3vo import LanNetworkOpenApiV3VO
    from ..models.select_port_binding_brief_vo import SelectPortBindingBriefVO


T = TypeVar("T", bound="ModifyVlanParamOpenApiVO")


@_attrs_define
class ModifyVlanParamOpenApiVO:
    """ModifyVlanParamOpenApiVO

    Attributes:
        lan_network (LanNetworkOpenApiV3VO): LANNetworkOpenApiVO
        device_config (SelectPortBindingBriefVO): Devcie config.
        skip_enable (bool | Unset): Whether skip the second step when modify vlan
    """

    lan_network: LanNetworkOpenApiV3VO
    device_config: SelectPortBindingBriefVO
    skip_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lan_network = self.lan_network.to_dict()

        device_config = self.device_config.to_dict()

        skip_enable = self.skip_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lanNetwork": lan_network,
                "deviceConfig": device_config,
            }
        )
        if skip_enable is not UNSET:
            field_dict["skipEnable"] = skip_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_open_api_v3vo import (
            LanNetworkOpenApiV3VO,
        )
        from ..models.select_port_binding_brief_vo import (
            SelectPortBindingBriefVO,
        )

        d = dict(src_dict)
        lan_network = LanNetworkOpenApiV3VO.from_dict(d.pop("lanNetwork"))

        device_config = SelectPortBindingBriefVO.from_dict(d.pop("deviceConfig"))

        skip_enable = d.pop("skipEnable", UNSET)

        modify_vlan_param_open_api_vo = cls(
            lan_network=lan_network,
            device_config=device_config,
            skip_enable=skip_enable,
        )

        modify_vlan_param_open_api_vo.additional_properties = d
        return modify_vlan_param_open_api_vo

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
