from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ppsk_expiration_vo import PPSKExpirationVO
    from ..models.ppsk_rate_limit_setting_vo import PPSKRateLimitSettingVO
    from ..models.pskvo import PSKVO


T = TypeVar("T", bound="PPSKProfileVO")


@_attrs_define
class PPSKProfileVO:
    """
    Attributes:
        profile_name (str): PPSK Profile Name
        ppsk (list[PSKVO]): PSK List In the PPSK Profile
        id (str | Unset): PPSK Profile ID
        ssid (list[str] | Unset): Ssid List Bound With PPSK Profile
        type_ (int | Unset): PPSK Profile type: 0：PPSK Without RADIUS; 1: PPSK With Built-In RADIUS.
        rate_limit (PPSKRateLimitSettingVO | Unset): PPSK Profile Rate Limit config.
        expiration (PPSKExpirationVO | Unset): PPSK Profile expiration time config.
        resource (int | Unset):
    """

    profile_name: str
    ppsk: list[PSKVO]
    id: str | Unset = UNSET
    ssid: list[str] | Unset = UNSET
    type_: int | Unset = UNSET
    rate_limit: PPSKRateLimitSettingVO | Unset = UNSET
    expiration: PPSKExpirationVO | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        ppsk = []
        for ppsk_item_data in self.ppsk:
            ppsk_item = ppsk_item_data.to_dict()
            ppsk.append(ppsk_item)

        id = self.id

        ssid: list[str] | Unset = UNSET
        if not isinstance(self.ssid, Unset):
            ssid = self.ssid

        type_ = self.type_

        rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        expiration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration, Unset):
            expiration = self.expiration.to_dict()

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileName": profile_name,
                "ppsk": ppsk,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if type_ is not UNSET:
            field_dict["type"] = type_
        if rate_limit is not UNSET:
            field_dict["rateLimit"] = rate_limit
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ppsk_expiration_vo import PPSKExpirationVO
        from ..models.ppsk_rate_limit_setting_vo import (
            PPSKRateLimitSettingVO,
        )
        from ..models.pskvo import PSKVO

        d = dict(src_dict)
        profile_name = d.pop("profileName")

        ppsk = []
        _ppsk = d.pop("ppsk")
        for ppsk_item_data in _ppsk:
            ppsk_item = PSKVO.from_dict(ppsk_item_data)

            ppsk.append(ppsk_item)

        id = d.pop("id", UNSET)

        ssid = cast(list[str], d.pop("ssid", UNSET))

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

        resource = d.pop("resource", UNSET)

        ppsk_profile_vo = cls(
            profile_name=profile_name,
            ppsk=ppsk,
            id=id,
            ssid=ssid,
            type_=type_,
            rate_limit=rate_limit,
            expiration=expiration,
            resource=resource,
        )

        ppsk_profile_vo.additional_properties = d
        return ppsk_profile_vo

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
