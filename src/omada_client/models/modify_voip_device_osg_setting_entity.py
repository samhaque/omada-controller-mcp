from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.telephone_number_advanced_setting_osg_open_api_vo import (
        TelephoneNumberAdvancedSettingOsgOpenApiVO,
    )
    from ..models.voip_device_osg_configuration_open_api_vo import (
        VoipDeviceOsgConfigurationOpenApiVO,
    )


T = TypeVar("T", bound="ModifyVoipDeviceOsgSettingEntity")


@_attrs_define
class ModifyVoipDeviceOsgSettingEntity:
    """
    Attributes:
        skip_confirm (bool): skipConfirm indicates whether to skip the query of "#'s conflict" of voip device settings.
            false: Not to skip the query. true: Skip the query and the device will give priority to the "end with #"
            configuration.
        voip_device_osg_configuration (VoipDeviceOsgConfigurationOpenApiVO | Unset): Telephony settings.
        telephone_number_advanced_setting (TelephoneNumberAdvancedSettingOsgOpenApiVO | Unset): Advanced settings.
    """

    skip_confirm: bool
    voip_device_osg_configuration: VoipDeviceOsgConfigurationOpenApiVO | Unset = UNSET
    telephone_number_advanced_setting: (
        TelephoneNumberAdvancedSettingOsgOpenApiVO | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip_confirm = self.skip_confirm

        voip_device_osg_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voip_device_osg_configuration, Unset):
            voip_device_osg_configuration = self.voip_device_osg_configuration.to_dict()

        telephone_number_advanced_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.telephone_number_advanced_setting, Unset):
            telephone_number_advanced_setting = (
                self.telephone_number_advanced_setting.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "skipConfirm": skip_confirm,
            }
        )
        if voip_device_osg_configuration is not UNSET:
            field_dict["voipDeviceOsgConfiguration"] = voip_device_osg_configuration
        if telephone_number_advanced_setting is not UNSET:
            field_dict["telephoneNumberAdvancedSetting"] = (
                telephone_number_advanced_setting
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.telephone_number_advanced_setting_osg_open_api_vo import (
            TelephoneNumberAdvancedSettingOsgOpenApiVO,
        )
        from ..models.voip_device_osg_configuration_open_api_vo import (
            VoipDeviceOsgConfigurationOpenApiVO,
        )

        d = dict(src_dict)
        skip_confirm = d.pop("skipConfirm")

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
            TelephoneNumberAdvancedSettingOsgOpenApiVO | Unset
        )
        if isinstance(_telephone_number_advanced_setting, Unset):
            telephone_number_advanced_setting = UNSET
        else:
            telephone_number_advanced_setting = (
                TelephoneNumberAdvancedSettingOsgOpenApiVO.from_dict(
                    _telephone_number_advanced_setting
                )
            )

        modify_voip_device_osg_setting_entity = cls(
            skip_confirm=skip_confirm,
            voip_device_osg_configuration=voip_device_osg_configuration,
            telephone_number_advanced_setting=telephone_number_advanced_setting,
        )

        modify_voip_device_osg_setting_entity.additional_properties = d
        return modify_voip_device_osg_setting_entity

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
