from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_config_open_api_vo import AutoConfigOpenApiVO
    from ..models.dns_config_open_api_vo import DnsConfigOpenApiVO
    from ..models.manually_config_open_api_vo import ManuallyConfigOpenApiVO
    from ..models.wan_dhcp_option_open_api_vo import WanDhcpOptionOpenApiVO


T = TypeVar("T", bound="UsbLteSettingConfigOpenApiVO")


@_attrs_define
class UsbLteSettingConfigOpenApiVO:
    """USB LTE ports config

    Attributes:
        port_id (str): Port ID
        config_type (int): 0: Auto; 1：Manually
        connection_mode (int): 1: Connect Automatically, 2: Connect Manually.
        auth_type (int): 0:Auto; 1:PAP; 2:CHAP.
        mtu_size (int): MTU ranges from 576 ~ 1500.
        dns_enable (bool): 0:off,1:on.
        port_description (str | Unset): Port description should contain 1 to 32 characters.
        auto_config (AutoConfigOpenApiVO | Unset): It is required when [configType] is 0.
        manually_config (ManuallyConfigOpenApiVO | Unset): It is required when [configType] is 1.
        pin (str | Unset): It is required when [usbModemMsgId] is 1 or 3.
        dhcp_options (list[WanDhcpOptionOpenApiVO] | Unset):
        dns_config (DnsConfigOpenApiVO | Unset): It is required when [dnsEnable] is true.
    """

    port_id: str
    config_type: int
    connection_mode: int
    auth_type: int
    mtu_size: int
    dns_enable: bool
    port_description: str | Unset = UNSET
    auto_config: AutoConfigOpenApiVO | Unset = UNSET
    manually_config: ManuallyConfigOpenApiVO | Unset = UNSET
    pin: str | Unset = UNSET
    dhcp_options: list[WanDhcpOptionOpenApiVO] | Unset = UNSET
    dns_config: DnsConfigOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        config_type = self.config_type

        connection_mode = self.connection_mode

        auth_type = self.auth_type

        mtu_size = self.mtu_size

        dns_enable = self.dns_enable

        port_description = self.port_description

        auto_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_config, Unset):
            auto_config = self.auto_config.to_dict()

        manually_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manually_config, Unset):
            manually_config = self.manually_config.to_dict()

        pin = self.pin

        dhcp_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dhcp_options, Unset):
            dhcp_options = []
            for dhcp_options_item_data in self.dhcp_options:
                dhcp_options_item = dhcp_options_item_data.to_dict()
                dhcp_options.append(dhcp_options_item)

        dns_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dns_config, Unset):
            dns_config = self.dns_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portId": port_id,
                "configType": config_type,
                "connectionMode": connection_mode,
                "authType": auth_type,
                "mtuSize": mtu_size,
                "dnsEnable": dns_enable,
            }
        )
        if port_description is not UNSET:
            field_dict["portDescription"] = port_description
        if auto_config is not UNSET:
            field_dict["autoConfig"] = auto_config
        if manually_config is not UNSET:
            field_dict["manuallyConfig"] = manually_config
        if pin is not UNSET:
            field_dict["pin"] = pin
        if dhcp_options is not UNSET:
            field_dict["dhcpOptions"] = dhcp_options
        if dns_config is not UNSET:
            field_dict["dnsConfig"] = dns_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auto_config_open_api_vo import (
            AutoConfigOpenApiVO,
        )
        from ..models.dns_config_open_api_vo import DnsConfigOpenApiVO
        from ..models.manually_config_open_api_vo import (
            ManuallyConfigOpenApiVO,
        )
        from ..models.wan_dhcp_option_open_api_vo import (
            WanDhcpOptionOpenApiVO,
        )

        d = dict(src_dict)
        port_id = d.pop("portId")

        config_type = d.pop("configType")

        connection_mode = d.pop("connectionMode")

        auth_type = d.pop("authType")

        mtu_size = d.pop("mtuSize")

        dns_enable = d.pop("dnsEnable")

        port_description = d.pop("portDescription", UNSET)

        _auto_config = d.pop("autoConfig", UNSET)
        auto_config: AutoConfigOpenApiVO | Unset
        if isinstance(_auto_config, Unset):
            auto_config = UNSET
        else:
            auto_config = AutoConfigOpenApiVO.from_dict(_auto_config)

        _manually_config = d.pop("manuallyConfig", UNSET)
        manually_config: ManuallyConfigOpenApiVO | Unset
        if isinstance(_manually_config, Unset):
            manually_config = UNSET
        else:
            manually_config = ManuallyConfigOpenApiVO.from_dict(_manually_config)

        pin = d.pop("pin", UNSET)

        _dhcp_options = d.pop("dhcpOptions", UNSET)
        dhcp_options: list[WanDhcpOptionOpenApiVO] | Unset = UNSET
        if _dhcp_options is not UNSET:
            dhcp_options = []
            for dhcp_options_item_data in _dhcp_options:
                dhcp_options_item = WanDhcpOptionOpenApiVO.from_dict(
                    dhcp_options_item_data
                )

                dhcp_options.append(dhcp_options_item)

        _dns_config = d.pop("dnsConfig", UNSET)
        dns_config: DnsConfigOpenApiVO | Unset
        if isinstance(_dns_config, Unset):
            dns_config = UNSET
        else:
            dns_config = DnsConfigOpenApiVO.from_dict(_dns_config)

        usb_lte_setting_config_open_api_vo = cls(
            port_id=port_id,
            config_type=config_type,
            connection_mode=connection_mode,
            auth_type=auth_type,
            mtu_size=mtu_size,
            dns_enable=dns_enable,
            port_description=port_description,
            auto_config=auto_config,
            manually_config=manually_config,
            pin=pin,
            dhcp_options=dhcp_options,
            dns_config=dns_config,
        )

        usb_lte_setting_config_open_api_vo.additional_properties = d
        return usb_lte_setting_config_open_api_vo

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
