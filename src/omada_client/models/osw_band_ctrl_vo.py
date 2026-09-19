from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_band_ctrl_limit_range_vo import OswBandCtrlLimitRangeVO


T = TypeVar("T", bound="OswBandCtrlVO")


@_attrs_define
class OswBandCtrlVO:
    """Speed Limit

    Attributes:
        egress_enable (bool): Indicates whether egress is enabled
        ingress_enable (bool): Indicates whether egress is enabled
        egress_limit (int | Unset): Egress Limit, when the user-configured value is much larger than the actual maximum
            value, the device will process it at the maximum value
        egress_unit (int | Unset): Egress Unit should be a value as follows: 1: Kbps; 2: Mbps
        ingress_limit (int | Unset): Ingress Limit, when the user-configured value is much larger than the actual
            maximum value, the device will process it at the maximum value
        ingress_unit (int | Unset): Ingress Unit should be a value as follows: 1: Kbps; 2: Mbps
        limit_range (list[OswBandCtrlLimitRangeVO] | Unset): The limit range of the bandwidth control
        unit_support (list[int] | Unset): The supported units of the bandwidth control, 1: Kbps; 2: Mbps
    """

    egress_enable: bool
    ingress_enable: bool
    egress_limit: int | Unset = UNSET
    egress_unit: int | Unset = UNSET
    ingress_limit: int | Unset = UNSET
    ingress_unit: int | Unset = UNSET
    limit_range: list[OswBandCtrlLimitRangeVO] | Unset = UNSET
    unit_support: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        egress_enable = self.egress_enable

        ingress_enable = self.ingress_enable

        egress_limit = self.egress_limit

        egress_unit = self.egress_unit

        ingress_limit = self.ingress_limit

        ingress_unit = self.ingress_unit

        limit_range: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limit_range, Unset):
            limit_range = []
            for limit_range_item_data in self.limit_range:
                limit_range_item = limit_range_item_data.to_dict()
                limit_range.append(limit_range_item)

        unit_support: list[int] | Unset = UNSET
        if not isinstance(self.unit_support, Unset):
            unit_support = self.unit_support

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "egressEnable": egress_enable,
                "ingressEnable": ingress_enable,
            }
        )
        if egress_limit is not UNSET:
            field_dict["egressLimit"] = egress_limit
        if egress_unit is not UNSET:
            field_dict["egressUnit"] = egress_unit
        if ingress_limit is not UNSET:
            field_dict["ingressLimit"] = ingress_limit
        if ingress_unit is not UNSET:
            field_dict["ingressUnit"] = ingress_unit
        if limit_range is not UNSET:
            field_dict["limitRange"] = limit_range
        if unit_support is not UNSET:
            field_dict["unitSupport"] = unit_support

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_band_ctrl_limit_range_vo import (
            OswBandCtrlLimitRangeVO,
        )

        d = dict(src_dict)
        egress_enable = d.pop("egressEnable")

        ingress_enable = d.pop("ingressEnable")

        egress_limit = d.pop("egressLimit", UNSET)

        egress_unit = d.pop("egressUnit", UNSET)

        ingress_limit = d.pop("ingressLimit", UNSET)

        ingress_unit = d.pop("ingressUnit", UNSET)

        _limit_range = d.pop("limitRange", UNSET)
        limit_range: list[OswBandCtrlLimitRangeVO] | Unset = UNSET
        if _limit_range is not UNSET:
            limit_range = []
            for limit_range_item_data in _limit_range:
                limit_range_item = OswBandCtrlLimitRangeVO.from_dict(
                    limit_range_item_data
                )

                limit_range.append(limit_range_item)

        unit_support = cast(list[int], d.pop("unitSupport", UNSET))

        osw_band_ctrl_vo = cls(
            egress_enable=egress_enable,
            ingress_enable=ingress_enable,
            egress_limit=egress_limit,
            egress_unit=egress_unit,
            ingress_limit=ingress_limit,
            ingress_unit=ingress_unit,
            limit_range=limit_range,
            unit_support=unit_support,
        )

        osw_band_ctrl_vo.additional_properties = d
        return osw_band_ctrl_vo

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
