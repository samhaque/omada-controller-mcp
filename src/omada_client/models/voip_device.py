from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telephone_number_advanced_setting_open_api_vo import (
        TelephoneNumberAdvancedSettingOpenApiVO,
    )
    from ..models.voip_device_ap_configuration_open_api_vo import (
        VoipDeviceApConfigurationOpenApiVO,
    )
    from ..models.voip_device_osg_configuration_open_api_vo import (
        VoipDeviceOsgConfigurationOpenApiVO,
    )


T = TypeVar("T", bound="VoipDevice")


@_attrs_define
class VoipDevice:
    """
    Attributes:
        added_in_advanced (bool): Whether the device is added in advanced.
        wireless_linked (bool): Whether to enable wireless linked.
        id (str | Unset): The ID of voip device.
        mac (str | Unset): The mac of voip device.
        name (str | Unset): The name of voip device.
        model (str | Unset): The model of voip device.
        model_version (str | Unset): The model version of voip device.
        type_ (str | Unset): The type of voip device.
        ip (str | Unset): The IP of voip device.
        status_category (int | Unset): The status category of voip device.
        status (int | Unset): The status of voip device.
        voip_device_ap_configuration (VoipDeviceApConfigurationOpenApiVO | Unset): Telephony settings.
        voip_device_osg_configuration (VoipDeviceOsgConfigurationOpenApiVO | Unset): Telephony settings.
        telephone_number_advanced_setting (TelephoneNumberAdvancedSettingOpenApiVO | Unset): The telephone number
            advanced setting of voip device.
        voip_vlan_ip (str | Unset): IP address of VoIP VLAN.
    """

    added_in_advanced: bool
    wireless_linked: bool
    id: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    ip: str | Unset = UNSET
    status_category: int | Unset = UNSET
    status: int | Unset = UNSET
    voip_device_ap_configuration: VoipDeviceApConfigurationOpenApiVO | Unset = UNSET
    voip_device_osg_configuration: VoipDeviceOsgConfigurationOpenApiVO | Unset = UNSET
    telephone_number_advanced_setting: (
        TelephoneNumberAdvancedSettingOpenApiVO | Unset
    ) = UNSET
    voip_vlan_ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        added_in_advanced = self.added_in_advanced

        wireless_linked = self.wireless_linked

        id = self.id

        mac = self.mac

        name = self.name

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        ip = self.ip

        status_category = self.status_category

        status = self.status

        voip_device_ap_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voip_device_ap_configuration, Unset):
            voip_device_ap_configuration = self.voip_device_ap_configuration.to_dict()

        voip_device_osg_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voip_device_osg_configuration, Unset):
            voip_device_osg_configuration = self.voip_device_osg_configuration.to_dict()

        telephone_number_advanced_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.telephone_number_advanced_setting, Unset):
            telephone_number_advanced_setting = (
                self.telephone_number_advanced_setting.to_dict()
            )

        voip_vlan_ip = self.voip_vlan_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addedInAdvanced": added_in_advanced,
                "wirelessLinked": wireless_linked,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ip is not UNSET:
            field_dict["ip"] = ip
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if status is not UNSET:
            field_dict["status"] = status
        if voip_device_ap_configuration is not UNSET:
            field_dict["voipDeviceApConfiguration"] = voip_device_ap_configuration
        if voip_device_osg_configuration is not UNSET:
            field_dict["voipDeviceOsgConfiguration"] = voip_device_osg_configuration
        if telephone_number_advanced_setting is not UNSET:
            field_dict["telephoneNumberAdvancedSetting"] = (
                telephone_number_advanced_setting
            )
        if voip_vlan_ip is not UNSET:
            field_dict["voipVlanIp"] = voip_vlan_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telephone_number_advanced_setting_open_api_vo import (
            TelephoneNumberAdvancedSettingOpenApiVO,
        )
        from ..models.voip_device_ap_configuration_open_api_vo import (
            VoipDeviceApConfigurationOpenApiVO,
        )
        from ..models.voip_device_osg_configuration_open_api_vo import (
            VoipDeviceOsgConfigurationOpenApiVO,
        )

        d = dict(src_dict)
        added_in_advanced = d.pop("addedInAdvanced")

        wireless_linked = d.pop("wirelessLinked")

        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        ip = d.pop("ip", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        status = d.pop("status", UNSET)

        _voip_device_ap_configuration = d.pop("voipDeviceApConfiguration", UNSET)
        voip_device_ap_configuration: VoipDeviceApConfigurationOpenApiVO | Unset
        if isinstance(_voip_device_ap_configuration, Unset):
            voip_device_ap_configuration = UNSET
        else:
            voip_device_ap_configuration = VoipDeviceApConfigurationOpenApiVO.from_dict(
                _voip_device_ap_configuration
            )

        _voip_device_osg_configuration = d.pop("voipDeviceOsgConfiguration", UNSET)
        voip_device_osg_configuration: VoipDeviceOsgConfigurationOpenApiVO | Unset
        if isinstance(_voip_device_osg_configuration, Unset):
            voip_device_osg_configuration = UNSET
        else:
            voip_device_osg_configuration = (
                VoipDeviceOsgConfigurationOpenApiVO.from_dict(
                    _voip_device_osg_configuration
                )
            )

        _telephone_number_advanced_setting = d.pop(
            "telephoneNumberAdvancedSetting", UNSET
        )
        telephone_number_advanced_setting: (
            TelephoneNumberAdvancedSettingOpenApiVO | Unset
        )
        if isinstance(_telephone_number_advanced_setting, Unset):
            telephone_number_advanced_setting = UNSET
        else:
            telephone_number_advanced_setting = (
                TelephoneNumberAdvancedSettingOpenApiVO.from_dict(
                    _telephone_number_advanced_setting
                )
            )

        voip_vlan_ip = d.pop("voipVlanIp", UNSET)

        voip_device = cls(
            added_in_advanced=added_in_advanced,
            wireless_linked=wireless_linked,
            id=id,
            mac=mac,
            name=name,
            model=model,
            model_version=model_version,
            type_=type_,
            ip=ip,
            status_category=status_category,
            status=status,
            voip_device_ap_configuration=voip_device_ap_configuration,
            voip_device_osg_configuration=voip_device_osg_configuration,
            telephone_number_advanced_setting=telephone_number_advanced_setting,
            voip_vlan_ip=voip_vlan_ip,
        )

        voip_device.additional_properties = d
        return voip_device

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
