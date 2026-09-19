from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApRssiThresholdOpenApiVO")


@_attrs_define
class ApRssiThresholdOpenApiVO:
    """Rssi Threshold setting of 6 GHz.

    Attributes:
        rssi_enable (bool | Unset): Rssi Threshold enabled or not.
        threshold (int | Unset): Value of rssi threshold.
    """

    rssi_enable: bool | Unset = UNSET
    threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rssi_enable = self.rssi_enable

        threshold = self.threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rssi_enable is not UNSET:
            field_dict["rssiEnable"] = rssi_enable
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rssi_enable = d.pop("rssiEnable", UNSET)

        threshold = d.pop("threshold", UNSET)

        ap_rssi_threshold_open_api_vo = cls(
            rssi_enable=rssi_enable,
            threshold=threshold,
        )

        ap_rssi_threshold_open_api_vo.additional_properties = d
        return ap_rssi_threshold_open_api_vo

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
