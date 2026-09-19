from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_setting_vo import ProviderSettingVO


T = TypeVar("T", bound="ProviderProfileEntity")


@_attrs_define
class ProviderProfileEntity:
    """
    Attributes:
        profile_id (str | Unset): Provider profile ID
        omadac_id (str | Unset): Omadac ID
        site_id (str | Unset): Site ID
        profile_name (str | Unset): Provider profile name
        provider_settings (ProviderSettingVO | Unset): Telephony provider settings
    """

    profile_id: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    profile_name: str | Unset = UNSET
    provider_settings: ProviderSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        omadac_id = self.omadac_id

        site_id = self.site_id

        profile_name = self.profile_name

        provider_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_settings, Unset):
            provider_settings = self.provider_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if provider_settings is not UNSET:
            field_dict["providerSettings"] = provider_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.provider_setting_vo import ProviderSettingVO

        d = dict(src_dict)
        profile_id = d.pop("profileId", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        profile_name = d.pop("profileName", UNSET)

        _provider_settings = d.pop("providerSettings", UNSET)
        provider_settings: ProviderSettingVO | Unset
        if isinstance(_provider_settings, Unset):
            provider_settings = UNSET
        else:
            provider_settings = ProviderSettingVO.from_dict(_provider_settings)

        provider_profile_entity = cls(
            profile_id=profile_id,
            omadac_id=omadac_id,
            site_id=site_id,
            profile_name=profile_name,
            provider_settings=provider_settings,
        )

        provider_profile_entity.additional_properties = d
        return provider_profile_entity

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
