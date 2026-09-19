from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_server_changed_config_open_api_vo import (
        DhcpServerChangedConfigOpenApiVO,
    )
    from ..models.portal_logout_config_open_api_vo import PortalLogoutConfigOpenApiVO
    from ..models.remember_device_setting import RememberDeviceSetting
    from ..models.remote_log_setting_open_api_vo import RemoteLogSettingOpenApiVO
    from ..models.site_led_setting import SiteLedSetting


T = TypeVar("T", bound="SiteServiceGeneralConfigOpenApiVO")


@_attrs_define
class SiteServiceGeneralConfigOpenApiVO:
    """
    Attributes:
        led (SiteLedSetting | Unset): Site led setting
        remote_log (RemoteLogSettingOpenApiVO | Unset): Site remote logging setting.
        remember_device (RememberDeviceSetting | Unset): Site remember device setting
        dhcp_srv_changed (DhcpServerChangedConfigOpenApiVO | Unset): Site DHCP server changed setting
        portal_logout_config (PortalLogoutConfigOpenApiVO | Unset):
    """

    led: SiteLedSetting | Unset = UNSET
    remote_log: RemoteLogSettingOpenApiVO | Unset = UNSET
    remember_device: RememberDeviceSetting | Unset = UNSET
    dhcp_srv_changed: DhcpServerChangedConfigOpenApiVO | Unset = UNSET
    portal_logout_config: PortalLogoutConfigOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        led: dict[str, Any] | Unset = UNSET
        if not isinstance(self.led, Unset):
            led = self.led.to_dict()

        remote_log: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remote_log, Unset):
            remote_log = self.remote_log.to_dict()

        remember_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remember_device, Unset):
            remember_device = self.remember_device.to_dict()

        dhcp_srv_changed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_srv_changed, Unset):
            dhcp_srv_changed = self.dhcp_srv_changed.to_dict()

        portal_logout_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.portal_logout_config, Unset):
            portal_logout_config = self.portal_logout_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if led is not UNSET:
            field_dict["led"] = led
        if remote_log is not UNSET:
            field_dict["remoteLog"] = remote_log
        if remember_device is not UNSET:
            field_dict["rememberDevice"] = remember_device
        if dhcp_srv_changed is not UNSET:
            field_dict["dhcpSrvChanged"] = dhcp_srv_changed
        if portal_logout_config is not UNSET:
            field_dict["portalLogoutConfig"] = portal_logout_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_server_changed_config_open_api_vo import (
            DhcpServerChangedConfigOpenApiVO,
        )
        from ..models.portal_logout_config_open_api_vo import (
            PortalLogoutConfigOpenApiVO,
        )
        from ..models.remember_device_setting import (
            RememberDeviceSetting,
        )
        from ..models.remote_log_setting_open_api_vo import (
            RemoteLogSettingOpenApiVO,
        )
        from ..models.site_led_setting import SiteLedSetting

        d = dict(src_dict)
        _led = d.pop("led", UNSET)
        led: SiteLedSetting | Unset
        if isinstance(_led, Unset):
            led = UNSET
        else:
            led = SiteLedSetting.from_dict(_led)

        _remote_log = d.pop("remoteLog", UNSET)
        remote_log: RemoteLogSettingOpenApiVO | Unset
        if isinstance(_remote_log, Unset):
            remote_log = UNSET
        else:
            remote_log = RemoteLogSettingOpenApiVO.from_dict(_remote_log)

        _remember_device = d.pop("rememberDevice", UNSET)
        remember_device: RememberDeviceSetting | Unset
        if isinstance(_remember_device, Unset):
            remember_device = UNSET
        else:
            remember_device = RememberDeviceSetting.from_dict(_remember_device)

        _dhcp_srv_changed = d.pop("dhcpSrvChanged", UNSET)
        dhcp_srv_changed: DhcpServerChangedConfigOpenApiVO | Unset
        if isinstance(_dhcp_srv_changed, Unset):
            dhcp_srv_changed = UNSET
        else:
            dhcp_srv_changed = DhcpServerChangedConfigOpenApiVO.from_dict(
                _dhcp_srv_changed
            )

        _portal_logout_config = d.pop("portalLogoutConfig", UNSET)
        portal_logout_config: PortalLogoutConfigOpenApiVO | Unset
        if isinstance(_portal_logout_config, Unset):
            portal_logout_config = UNSET
        else:
            portal_logout_config = PortalLogoutConfigOpenApiVO.from_dict(
                _portal_logout_config
            )

        site_service_general_config_open_api_vo = cls(
            led=led,
            remote_log=remote_log,
            remember_device=remember_device,
            dhcp_srv_changed=dhcp_srv_changed,
            portal_logout_config=portal_logout_config,
        )

        site_service_general_config_open_api_vo.additional_properties = d
        return site_service_general_config_open_api_vo

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
