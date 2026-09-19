from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ppsk_expiration_vo import PPSKExpirationVO
    from ..models.ppsk_rate_limit_setting_vo import PPSKRateLimitSettingVO
    from ..models.ppsk_setting_v2 import PpskSettingV2


T = TypeVar("T", bound="PpskProfileV2")


@_attrs_define
class PpskProfileV2:
    """PPSK Profile Setting.

    Attributes:
        profile_name (str): PPSK Profile Name, should contain 1 to 64 characters.
        auto_create_psks (bool): Whether to enable auto create psks
        ppsk (list[PpskSettingV2] | Unset): This field is required when Parameter [autoCreatePsks] is false; PPSK List
            In the PPSK Profile
        number (int | Unset): This field is required when Parameter [autoCreatePsks] is true; Generate Number, should be
            within the range of 1-1024.
        prefix (str | Unset): This field is required when Parameter [autoCreatePsks] is true; PSK Name Prefix, should
            contain 1 to 60 visible ASCII characters.
        length (int | Unset): This field is required when Parameter [autoCreatePsks] is true; PSK Password Length,
            should be within the range of 8-63.
        vlan (int | Unset): This field is required when Parameter [autoCreatePsks] is true; PSK Bound Vlan, should be
            within the range of 1-4094.
        vlan_pool (str | Unset): This field is required when Parameter [autoCreatePsks] is true; PSK Bound Vlan range,
            should be like: 10-1000.
        vlan_interval (int | Unset): This field is required when Parameter [autoCreatePsks] is true; The interval of
            vlan when auto creating psk
        rate_limit (PPSKRateLimitSettingVO | Unset): PPSK Profile Rate Limit config.
        expiration (PPSKExpirationVO | Unset): PPSK Profile expiration time config.
    """

    profile_name: str
    auto_create_psks: bool
    ppsk: list[PpskSettingV2] | Unset = UNSET
    number: int | Unset = UNSET
    prefix: str | Unset = UNSET
    length: int | Unset = UNSET
    vlan: int | Unset = UNSET
    vlan_pool: str | Unset = UNSET
    vlan_interval: int | Unset = UNSET
    rate_limit: PPSKRateLimitSettingVO | Unset = UNSET
    expiration: PPSKExpirationVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        auto_create_psks = self.auto_create_psks

        ppsk: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ppsk, Unset):
            ppsk = []
            for ppsk_item_data in self.ppsk:
                ppsk_item = ppsk_item_data.to_dict()
                ppsk.append(ppsk_item)

        number = self.number

        prefix = self.prefix

        length = self.length

        vlan = self.vlan

        vlan_pool = self.vlan_pool

        vlan_interval = self.vlan_interval

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        expiration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileName": profile_name,
                "autoCreatePsks": auto_create_psks,
            }
        )
        if ppsk is not UNSET:
            field_dict["ppsk"] = ppsk
        if number is not UNSET:
            field_dict["number"] = number
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if length is not UNSET:
            field_dict["length"] = length
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if vlan_pool is not UNSET:
            field_dict["vlanPool"] = vlan_pool
        if vlan_interval is not UNSET:
            field_dict["vlanInterval"] = vlan_interval
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if expiration is not UNSET:
            field_dict["expiration"] = expiration

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ppsk_expiration_vo import PPSKExpirationVO
        from ..models.ppsk_rate_limit_setting_vo import (
            PPSKRateLimitSettingVO,
        )
        from ..models.ppsk_setting_v2 import PpskSettingV2

        d = dict(src_dict)
        profile_name = d.pop("profileName")

        auto_create_psks = d.pop("autoCreatePsks")

        _ppsk = d.pop("ppsk", UNSET)
        ppsk: list[PpskSettingV2] | Unset = UNSET
        if _ppsk is not UNSET:
            ppsk = []
            for ppsk_item_data in _ppsk:
                ppsk_item = PpskSettingV2.from_dict(ppsk_item_data)

                ppsk.append(ppsk_item)

        number = d.pop("number", UNSET)

        prefix = d.pop("prefix", UNSET)

        length = d.pop("length", UNSET)

        vlan = d.pop("vlan", UNSET)

        vlan_pool = d.pop("vlanPool", UNSET)

        vlan_interval = d.pop("vlanInterval", UNSET)

        _rate_limit = d.pop("rateLimit", UNSET)
        rate_limit: PPSKRateLimitSettingVO | Unset
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = PPSKRateLimitSettingVO.from_dict(_rate_limit)

        _expiration = d.pop("expiration", UNSET)
        expiration: PPSKExpirationVO | Unset
        if isinstance(_expiration, Unset):
            expiration = UNSET
        else:
            expiration = PPSKExpirationVO.from_dict(_expiration)

        ppsk_profile_v2 = cls(
            profile_name=profile_name,
            auto_create_psks=auto_create_psks,
            ppsk=ppsk,
            number=number,
            prefix=prefix,
            length=length,
            vlan=vlan,
            vlan_pool=vlan_pool,
            vlan_interval=vlan_interval,
            rate_limit=rate_limit,
            expiration=expiration,
        )

        ppsk_profile_v2.additional_properties = d
        return ppsk_profile_v2

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
