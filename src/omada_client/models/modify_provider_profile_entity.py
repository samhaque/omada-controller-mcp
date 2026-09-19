from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.modify_provider_setting_open_api_vo import (
        ModifyProviderSettingOpenApiVO,
    )


T = TypeVar("T", bound="ModifyProviderProfileEntity")


@_attrs_define
class ModifyProviderProfileEntity:
    """
    Attributes:
        profile_name (str | Unset): Provider profile name
        provider_settings (ModifyProviderSettingOpenApiVO | Unset): Telephony provider settings
    """

    profile_name: str | Unset = UNSET
    provider_settings: ModifyProviderSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        provider_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_settings, Unset):
            provider_settings = self.provider_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if provider_settings is not UNSET:
            field_dict["providerSettings"] = provider_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.modify_provider_setting_open_api_vo import (
            ModifyProviderSettingOpenApiVO,
        )

        d = dict(src_dict)
        profile_name = d.pop("profileName", UNSET)

        _provider_settings = d.pop("providerSettings", UNSET)
        provider_settings: ModifyProviderSettingOpenApiVO | Unset
        if isinstance(_provider_settings, Unset):
            provider_settings = UNSET
        else:
            provider_settings = ModifyProviderSettingOpenApiVO.from_dict(
                _provider_settings
            )

        modify_provider_profile_entity = cls(
            profile_name=profile_name,
            provider_settings=provider_settings,
        )

        modify_provider_profile_entity.additional_properties = d
        return modify_provider_profile_entity

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
