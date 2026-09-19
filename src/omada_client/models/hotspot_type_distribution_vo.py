from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotspotTypeDistributionVO")


@_attrs_define
class HotspotTypeDistributionVO:
    """
    Attributes:
        total (int | Unset):
        voucher (int | Unset):
        local_user (int | Unset):
        sms (int | Unset):
        form (int | Unset):
        hotspot_radius (int | Unset):
    """

    total: int | Unset = UNSET
    voucher: int | Unset = UNSET
    local_user: int | Unset = UNSET
    sms: int | Unset = UNSET
    form: int | Unset = UNSET
    hotspot_radius: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        voucher = self.voucher

        local_user = self.local_user

        sms = self.sms

        form = self.form

        hotspot_radius = self.hotspot_radius

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if voucher is not UNSET:
            field_dict["voucher"] = voucher
        if local_user is not UNSET:
            field_dict["localUser"] = local_user
        if sms is not UNSET:
            field_dict["sms"] = sms
        if form is not UNSET:
            field_dict["form"] = form
        if hotspot_radius is not UNSET:
            field_dict["hotspotRadius"] = hotspot_radius

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        voucher = d.pop("voucher", UNSET)

        local_user = d.pop("localUser", UNSET)

        sms = d.pop("sms", UNSET)

        form = d.pop("form", UNSET)

        hotspot_radius = d.pop("hotspotRadius", UNSET)

        hotspot_type_distribution_vo = cls(
            total=total,
            voucher=voucher,
            local_user=local_user,
            sms=sms,
            form=form,
            hotspot_radius=hotspot_radius,
        )

        hotspot_type_distribution_vo.additional_properties = d
        return hotspot_type_distribution_vo

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
