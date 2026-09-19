from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WifiHealthVO")


@_attrs_define
class WifiHealthVO:
    """
    Attributes:
        access_time_score (int | Unset): Wireless client association time score
        channel_util_score (int | Unset): AP channel utility score
        channel_inter_util_score (int | Unset): AP channel interference score
        access_capacity_score (int | Unset): AP Access capacity score
        rssi_score (int | Unset): RSSI score
        support_access_capacity (bool | Unset): support AP Access capacity score
        wireless_client_quality_score (int | Unset): Wireless client quality score (onboarding time)
    """

    access_time_score: int | Unset = UNSET
    channel_util_score: int | Unset = UNSET
    channel_inter_util_score: int | Unset = UNSET
    access_capacity_score: int | Unset = UNSET
    rssi_score: int | Unset = UNSET
    support_access_capacity: bool | Unset = UNSET
    wireless_client_quality_score: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_time_score = self.access_time_score

        channel_util_score = self.channel_util_score

        channel_inter_util_score = self.channel_inter_util_score

        access_capacity_score = self.access_capacity_score

        rssi_score = self.rssi_score

        support_access_capacity = self.support_access_capacity

        wireless_client_quality_score = self.wireless_client_quality_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_time_score is not UNSET:
            field_dict["accessTimeScore"] = access_time_score
        if channel_util_score is not UNSET:
            field_dict["channelUtilScore"] = channel_util_score
        if channel_inter_util_score is not UNSET:
            field_dict["channelInterUtilScore"] = channel_inter_util_score
        if access_capacity_score is not UNSET:
            field_dict["accessCapacityScore"] = access_capacity_score
        if rssi_score is not UNSET:
            field_dict["rssiScore"] = rssi_score
        if support_access_capacity is not UNSET:
            field_dict["supportAccessCapacity"] = support_access_capacity
        if wireless_client_quality_score is not UNSET:
            field_dict["wirelessClientQualityScore"] = wireless_client_quality_score

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        access_time_score = d.pop("accessTimeScore", UNSET)

        channel_util_score = d.pop("channelUtilScore", UNSET)

        channel_inter_util_score = d.pop("channelInterUtilScore", UNSET)

        access_capacity_score = d.pop("accessCapacityScore", UNSET)

        rssi_score = d.pop("rssiScore", UNSET)

        support_access_capacity = d.pop("supportAccessCapacity", UNSET)

        wireless_client_quality_score = d.pop("wirelessClientQualityScore", UNSET)

        wifi_health_vo = cls(
            access_time_score=access_time_score,
            channel_util_score=channel_util_score,
            channel_inter_util_score=channel_inter_util_score,
            access_capacity_score=access_capacity_score,
            rssi_score=rssi_score,
            support_access_capacity=support_access_capacity,
            wireless_client_quality_score=wireless_client_quality_score,
        )

        wifi_health_vo.additional_properties = d
        return wifi_health_vo

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
