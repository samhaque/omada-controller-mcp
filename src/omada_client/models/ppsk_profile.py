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
    from ..models.ppsk_setting import PpskSetting


T = TypeVar("T", bound="PpskProfile")


@_attrs_define
class PpskProfile:
    """PPSK Profile Setting.

    Attributes:
        profile_name (str): PPSK Profile Name, should contain 1 to 64 characters.
        ppsk (list[PpskSetting]): PPSK List In the PPSK Profile
        type_ (int | Unset): This field has been deprecated since version 6.1. PPSK Profile type: 0：PPSK Without
            RADIUS;Cloud Based Controller only support PPSK Without RADIUS.
        rate_limit (PPSKRateLimitSettingVO | Unset): PPSK Profile Rate Limit config.
        expiration (PPSKExpirationVO | Unset): PPSK Profile expiration time config.
    """

    profile_name: str
    ppsk: list[PpskSetting]
    type_: int | Unset = UNSET
    rate_limit: PPSKRateLimitSettingVO | Unset = UNSET
    expiration: PPSKExpirationVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        ppsk = []
        for ppsk_item_data in self.ppsk:
            ppsk_item = ppsk_item_data.to_dict()
            ppsk.append(ppsk_item)

        type_ = self.type_

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
                "ppsk": ppsk,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
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
        from ..models.ppsk_setting import PpskSetting

        d = dict(src_dict)
        profile_name = d.pop("profileName")

        ppsk = []
        _ppsk = d.pop("ppsk")
        for ppsk_item_data in _ppsk:
            ppsk_item = PpskSetting.from_dict(ppsk_item_data)

            ppsk.append(ppsk_item)

        type_ = d.pop("type", UNSET)

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

        ppsk_profile = cls(
            profile_name=profile_name,
            ppsk=ppsk,
            type_=type_,
            rate_limit=rate_limit,
            expiration=expiration,
        )

        ppsk_profile.additional_properties = d
        return ppsk_profile

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
