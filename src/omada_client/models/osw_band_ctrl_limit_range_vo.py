from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswBandCtrlLimitRangeVO")


@_attrs_define
class OswBandCtrlLimitRangeVO:
    """The limit range of the bandwidth control

    Attributes:
        unit (int | Unset): unit: 1: kbps, 2: mbps
        min_ingress_rate (int | Unset): min ingress rate
        max_ingress_rate (int | Unset): max ingress rate
        min_egress_rate (int | Unset): min egress rate
        max_egress_rate (int | Unset): max egress rate
    """

    unit: int | Unset = UNSET
    min_ingress_rate: int | Unset = UNSET
    max_ingress_rate: int | Unset = UNSET
    min_egress_rate: int | Unset = UNSET
    max_egress_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        min_ingress_rate = self.min_ingress_rate

        max_ingress_rate = self.max_ingress_rate

        min_egress_rate = self.min_egress_rate

        max_egress_rate = self.max_egress_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit is not UNSET:
            field_dict["unit"] = unit
        if min_ingress_rate is not UNSET:
            field_dict["minIngressRate"] = min_ingress_rate
        if max_ingress_rate is not UNSET:
            field_dict["maxIngressRate"] = max_ingress_rate
        if min_egress_rate is not UNSET:
            field_dict["minEgressRate"] = min_egress_rate
        if max_egress_rate is not UNSET:
            field_dict["maxEgressRate"] = max_egress_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unit = d.pop("unit", UNSET)

        min_ingress_rate = d.pop("minIngressRate", UNSET)

        max_ingress_rate = d.pop("maxIngressRate", UNSET)

        min_egress_rate = d.pop("minEgressRate", UNSET)

        max_egress_rate = d.pop("maxEgressRate", UNSET)

        osw_band_ctrl_limit_range_vo = cls(
            unit=unit,
            min_ingress_rate=min_ingress_rate,
            max_ingress_rate=max_ingress_rate,
            min_egress_rate=min_egress_rate,
            max_egress_rate=max_egress_rate,
        )

        osw_band_ctrl_limit_range_vo.additional_properties = d
        return osw_band_ctrl_limit_range_vo

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
