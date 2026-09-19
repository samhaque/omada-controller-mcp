from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iptv_custom_open_api_vo import IptvCustomOpenApiVO
    from ..models.iptv_dsl_open_api_vo import IptvDslOpenApiVO
    from ..models.iptv_port_config_open_api_vo import IptvPortConfigOpenApiVO


T = TypeVar("T", bound="IptvConfigOpenApiVO")


@_attrs_define
class IptvConfigOpenApiVO:
    """
    Attributes:
        enable (bool):
        wan_port_id (str): WAN port ID can be obtained from 'Get internet basic info' interface.
        mode (int): Mode should be a value as follows: 0:Bridge; 1:Custom
        port_config (list[IptvPortConfigOpenApiVO]): All available ports need to be configured. The list of port ID is
            the same as that returned by "Get IPTV setting"
        custom_config (IptvCustomOpenApiVO | Unset): Required when parameter[mode] is 1
        dsl_config (IptvDslOpenApiVO | Unset): Configurations that appear only when DSL WAN port is selected.
    """

    enable: bool
    wan_port_id: str
    mode: int
    port_config: list[IptvPortConfigOpenApiVO]
    custom_config: IptvCustomOpenApiVO | Unset = UNSET
    dsl_config: IptvDslOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        wan_port_id = self.wan_port_id

        mode = self.mode

        port_config = []
        for port_config_item_data in self.port_config:
            port_config_item = port_config_item_data.to_dict()
            port_config.append(port_config_item)

        custom_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_config, Unset):
            custom_config = self.custom_config.to_dict()

        dsl_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dsl_config, Unset):
            dsl_config = self.dsl_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "wanPortId": wan_port_id,
                "mode": mode,
                "portConfig": port_config,
            }
        )
        if custom_config is not UNSET:
            field_dict["customConfig"] = custom_config
        if dsl_config is not UNSET:
            field_dict["dslConfig"] = dsl_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.iptv_custom_open_api_vo import (
            IptvCustomOpenApiVO,
        )
        from ..models.iptv_dsl_open_api_vo import IptvDslOpenApiVO
        from ..models.iptv_port_config_open_api_vo import (
            IptvPortConfigOpenApiVO,
        )

        d = dict(src_dict)
        enable = d.pop("enable")

        wan_port_id = d.pop("wanPortId")

        mode = d.pop("mode")

        port_config = []
        _port_config = d.pop("portConfig")
        for port_config_item_data in _port_config:
            port_config_item = IptvPortConfigOpenApiVO.from_dict(port_config_item_data)

            port_config.append(port_config_item)

        _custom_config = d.pop("customConfig", UNSET)
        custom_config: IptvCustomOpenApiVO | Unset
        if isinstance(_custom_config, Unset):
            custom_config = UNSET
        else:
            custom_config = IptvCustomOpenApiVO.from_dict(_custom_config)

        _dsl_config = d.pop("dslConfig", UNSET)
        dsl_config: IptvDslOpenApiVO | Unset
        if isinstance(_dsl_config, Unset):
            dsl_config = UNSET
        else:
            dsl_config = IptvDslOpenApiVO.from_dict(_dsl_config)

        iptv_config_open_api_vo = cls(
            enable=enable,
            wan_port_id=wan_port_id,
            mode=mode,
            port_config=port_config,
            custom_config=custom_config,
            dsl_config=dsl_config,
        )

        iptv_config_open_api_vo.additional_properties = d
        return iptv_config_open_api_vo

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
