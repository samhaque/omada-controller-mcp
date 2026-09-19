from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CciTrendItemOpenApiOpenApiVO")


@_attrs_define
class CciTrendItemOpenApiOpenApiVO:
    """The trend of CCI metrics displayed on the WIFI Dashboard page.

    Attributes:
        time (int | Unset): Time(unit:ms)
        strong_interference_ap_num (int | Unset): The number of strong Interference Ap.
        strong_interference_ap_percent (int | Unset): The percent of strong Interference Ap.
        moderate_interference_ap_num (int | Unset): The number of moderate Interference Ap.
        moderate_interference_ap_percent (int | Unset): The percent of moderate Interference Ap.
        weak_interference_ap_num (int | Unset): The number of weak Interference Ap.
        weak_interference_ap_percent (int | Unset): The percent of weak Interference Ap.
    """

    time: int | Unset = UNSET
    strong_interference_ap_num: int | Unset = UNSET
    strong_interference_ap_percent: int | Unset = UNSET
    moderate_interference_ap_num: int | Unset = UNSET
    moderate_interference_ap_percent: int | Unset = UNSET
    weak_interference_ap_num: int | Unset = UNSET
    weak_interference_ap_percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        strong_interference_ap_num = self.strong_interference_ap_num

        strong_interference_ap_percent = self.strong_interference_ap_percent

        moderate_interference_ap_num = self.moderate_interference_ap_num

        moderate_interference_ap_percent = self.moderate_interference_ap_percent

        weak_interference_ap_num = self.weak_interference_ap_num

        weak_interference_ap_percent = self.weak_interference_ap_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if strong_interference_ap_num is not UNSET:
            field_dict["strongInterferenceApNum"] = strong_interference_ap_num
        if strong_interference_ap_percent is not UNSET:
            field_dict["strongInterferenceApPercent"] = strong_interference_ap_percent
        if moderate_interference_ap_num is not UNSET:
            field_dict["moderateInterferenceApNum"] = moderate_interference_ap_num
        if moderate_interference_ap_percent is not UNSET:
            field_dict["moderateInterferenceApPercent"] = (
                moderate_interference_ap_percent
            )
        if weak_interference_ap_num is not UNSET:
            field_dict["weakInterferenceApNum"] = weak_interference_ap_num
        if weak_interference_ap_percent is not UNSET:
            field_dict["weakInterferenceApPercent"] = weak_interference_ap_percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        strong_interference_ap_num = d.pop("strongInterferenceApNum", UNSET)

        strong_interference_ap_percent = d.pop("strongInterferenceApPercent", UNSET)

        moderate_interference_ap_num = d.pop("moderateInterferenceApNum", UNSET)

        moderate_interference_ap_percent = d.pop("moderateInterferenceApPercent", UNSET)

        weak_interference_ap_num = d.pop("weakInterferenceApNum", UNSET)

        weak_interference_ap_percent = d.pop("weakInterferenceApPercent", UNSET)

        cci_trend_item_open_api_open_api_vo = cls(
            time=time,
            strong_interference_ap_num=strong_interference_ap_num,
            strong_interference_ap_percent=strong_interference_ap_percent,
            moderate_interference_ap_num=moderate_interference_ap_num,
            moderate_interference_ap_percent=moderate_interference_ap_percent,
            weak_interference_ap_num=weak_interference_ap_num,
            weak_interference_ap_percent=weak_interference_ap_percent,
        )

        cci_trend_item_open_api_open_api_vo.additional_properties = d
        return cci_trend_item_open_api_open_api_vo

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
