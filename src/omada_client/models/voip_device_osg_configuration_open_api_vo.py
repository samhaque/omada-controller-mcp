from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voip_device_port_setting_open_api_vo import (
        VoipDevicePortSettingOpenApiVO,
    )


T = TypeVar("T", bound="VoipDeviceOsgConfigurationOpenApiVO")


@_attrs_define
class VoipDeviceOsgConfigurationOpenApiVO:
    """Telephony settings.

    Attributes:
        port_settings (list[VoipDevicePortSettingOpenApiVO] | Unset): VOIP device port setting.
        call_blocking_enable (bool | Unset): Whether to enable callBlocking.
        call_blocking_profile_id (str | Unset): The call blocking profile ID of voip device.When callBlockingEnable is
            true, it can not be null.
        call_blocking_profile_name (str | Unset): The call blocking profile name of voip device.
        via_ipv_6 (bool | Unset): Whether via IPv6.
    """

    port_settings: list[VoipDevicePortSettingOpenApiVO] | Unset = UNSET
    call_blocking_enable: bool | Unset = UNSET
    call_blocking_profile_id: str | Unset = UNSET
    call_blocking_profile_name: str | Unset = UNSET
    via_ipv_6: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_settings, Unset):
            port_settings = []
            for port_settings_item_data in self.port_settings:
                port_settings_item = port_settings_item_data.to_dict()
                port_settings.append(port_settings_item)

        call_blocking_enable = self.call_blocking_enable

        call_blocking_profile_id = self.call_blocking_profile_id

        call_blocking_profile_name = self.call_blocking_profile_name

        via_ipv_6 = self.via_ipv_6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_settings is not UNSET:
            field_dict["portSettings"] = port_settings
        if call_blocking_enable is not UNSET:
            field_dict["callBlockingEnable"] = call_blocking_enable
        if call_blocking_profile_id is not UNSET:
            field_dict["callBlockingProfileId"] = call_blocking_profile_id
        if call_blocking_profile_name is not UNSET:
            field_dict["callBlockingProfileName"] = call_blocking_profile_name
        if via_ipv_6 is not UNSET:
            field_dict["viaIpv6"] = via_ipv_6

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.voip_device_port_setting_open_api_vo import (
            VoipDevicePortSettingOpenApiVO,
        )

        d = dict(src_dict)
        _port_settings = d.pop("portSettings", UNSET)
        port_settings: list[VoipDevicePortSettingOpenApiVO] | Unset = UNSET
        if _port_settings is not UNSET:
            port_settings = []
            for port_settings_item_data in _port_settings:
                port_settings_item = VoipDevicePortSettingOpenApiVO.from_dict(
                    port_settings_item_data
                )

                port_settings.append(port_settings_item)

        call_blocking_enable = d.pop("callBlockingEnable", UNSET)

        call_blocking_profile_id = d.pop("callBlockingProfileId", UNSET)

        call_blocking_profile_name = d.pop("callBlockingProfileName", UNSET)

        via_ipv_6 = d.pop("viaIpv6", UNSET)

        voip_device_osg_configuration_open_api_vo = cls(
            port_settings=port_settings,
            call_blocking_enable=call_blocking_enable,
            call_blocking_profile_id=call_blocking_profile_id,
            call_blocking_profile_name=call_blocking_profile_name,
            via_ipv_6=via_ipv_6,
        )

        voip_device_osg_configuration_open_api_vo.additional_properties = d
        return voip_device_osg_configuration_open_api_vo

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
