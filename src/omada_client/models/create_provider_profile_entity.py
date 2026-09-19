from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.provider_setting_vo import ProviderSettingVO


T = TypeVar("T", bound="CreateProviderProfileEntity")


@_attrs_define
class CreateProviderProfileEntity:
    """
    Attributes:
        profile_name (str): Provider profile name
        provider_settings (ProviderSettingVO): Telephony provider settings
    """

    profile_name: str
    provider_settings: ProviderSettingVO
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        provider_settings = self.provider_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileName": profile_name,
                "providerSettings": provider_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.provider_setting_vo import ProviderSettingVO

        d = dict(src_dict)
        profile_name = d.pop("profileName")

        provider_settings = ProviderSettingVO.from_dict(d.pop("providerSettings"))

        create_provider_profile_entity = cls(
            profile_name=profile_name,
            provider_settings=provider_settings,
        )

        create_provider_profile_entity.additional_properties = d
        return create_provider_profile_entity

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
