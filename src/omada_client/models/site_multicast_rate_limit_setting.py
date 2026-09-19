from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcast_rate_limit_setting_vo import McastRateLimitSettingVO


T = TypeVar("T", bound="SiteMulticastRateLimitSetting")


@_attrs_define
class SiteMulticastRateLimitSetting:
    """Site multicast rate limit setting

    Attributes:
        mcast_rate_limit (McastRateLimitSettingVO | Unset):
    """

    mcast_rate_limit: McastRateLimitSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mcast_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcast_rate_limit, Unset):
            mcast_rate_limit = self.mcast_rate_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mcast_rate_limit is not UNSET:
            field_dict["mcastRateLimit"] = mcast_rate_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcast_rate_limit_setting_vo import (
            McastRateLimitSettingVO,
        )

        d = dict(src_dict)
        _mcast_rate_limit = d.pop("mcastRateLimit", UNSET)
        mcast_rate_limit: McastRateLimitSettingVO | Unset
        if isinstance(_mcast_rate_limit, Unset):
            mcast_rate_limit = UNSET
        else:
            mcast_rate_limit = McastRateLimitSettingVO.from_dict(_mcast_rate_limit)

        site_multicast_rate_limit_setting = cls(
            mcast_rate_limit=mcast_rate_limit,
        )

        site_multicast_rate_limit_setting.additional_properties = d
        return site_multicast_rate_limit_setting

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
