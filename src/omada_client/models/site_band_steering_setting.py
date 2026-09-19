from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.band_steering_multi_band_vo import BandSteeringMultiBandVO


T = TypeVar("T", bound="SiteBandSteeringSetting")


@_attrs_define
class SiteBandSteeringSetting:
    """Site band steering setting.

    Attributes:
        band_steering_for_multi_band (BandSteeringMultiBandVO | Unset): Site band steering.
    """

    band_steering_for_multi_band: BandSteeringMultiBandVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        band_steering_for_multi_band: dict[str, Any] | Unset = UNSET
        if not isinstance(self.band_steering_for_multi_band, Unset):
            band_steering_for_multi_band = self.band_steering_for_multi_band.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if band_steering_for_multi_band is not UNSET:
            field_dict["bandSteeringForMultiBand"] = band_steering_for_multi_band

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.band_steering_multi_band_vo import (
            BandSteeringMultiBandVO,
        )

        d = dict(src_dict)
        _band_steering_for_multi_band = d.pop("bandSteeringForMultiBand", UNSET)
        band_steering_for_multi_band: BandSteeringMultiBandVO | Unset
        if isinstance(_band_steering_for_multi_band, Unset):
            band_steering_for_multi_band = UNSET
        else:
            band_steering_for_multi_band = BandSteeringMultiBandVO.from_dict(
                _band_steering_for_multi_band
            )

        site_band_steering_setting = cls(
            band_steering_for_multi_band=band_steering_for_multi_band,
        )

        site_band_steering_setting.additional_properties = d
        return site_band_steering_setting

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
