from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_interference_sub_health_info_vo import (
        ChannelInterferenceSubHealthInfoVO,
    )
    from ..models.on_boarding_time_sub_health_detail_vo import (
        OnBoardingTimeSubHealthDetailVO,
    )
    from ..models.sub_single_health_info_detail_vo import SubSingleHealthInfoDetailVO


T = TypeVar("T", bound="WifiHealthDetailVO")


@_attrs_define
class WifiHealthDetailVO:
    """
    Attributes:
        wifi_health_score (int | Unset): Wifi health score
        access_time_score_detail (SubSingleHealthInfoDetailVO | Unset): Rssi score detail info
        wireless_client_quality_detail (OnBoardingTimeSubHealthDetailVO | Unset): Onboarding time health info and score
        channel_util_score_detail (SubSingleHealthInfoDetailVO | Unset): Rssi score detail info
        channel_inter_util_detail (ChannelInterferenceSubHealthInfoVO | Unset): Channel interference rate score detail
            info
        access_capacity_score_detail (SubSingleHealthInfoDetailVO | Unset): Rssi score detail info
        rssi_score_detail (SubSingleHealthInfoDetailVO | Unset): Rssi score detail info
    """

    wifi_health_score: int | Unset = UNSET
    access_time_score_detail: SubSingleHealthInfoDetailVO | Unset = UNSET
    wireless_client_quality_detail: OnBoardingTimeSubHealthDetailVO | Unset = UNSET
    channel_util_score_detail: SubSingleHealthInfoDetailVO | Unset = UNSET
    channel_inter_util_detail: ChannelInterferenceSubHealthInfoVO | Unset = UNSET
    access_capacity_score_detail: SubSingleHealthInfoDetailVO | Unset = UNSET
    rssi_score_detail: SubSingleHealthInfoDetailVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wifi_health_score = self.wifi_health_score

        access_time_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access_time_score_detail, Unset):
            access_time_score_detail = self.access_time_score_detail.to_dict()

        wireless_client_quality_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_client_quality_detail, Unset):
            wireless_client_quality_detail = (
                self.wireless_client_quality_detail.to_dict()
            )

        channel_util_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_util_score_detail, Unset):
            channel_util_score_detail = self.channel_util_score_detail.to_dict()

        channel_inter_util_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_inter_util_detail, Unset):
            channel_inter_util_detail = self.channel_inter_util_detail.to_dict()

        access_capacity_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access_capacity_score_detail, Unset):
            access_capacity_score_detail = self.access_capacity_score_detail.to_dict()

        rssi_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rssi_score_detail, Unset):
            rssi_score_detail = self.rssi_score_detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wifi_health_score is not UNSET:
            field_dict["wifiHealthScore"] = wifi_health_score
        if access_time_score_detail is not UNSET:
            field_dict["accessTimeScoreDetail"] = access_time_score_detail
        if wireless_client_quality_detail is not UNSET:
            field_dict["wirelessClientQualityDetail"] = wireless_client_quality_detail
        if channel_util_score_detail is not UNSET:
            field_dict["channelUtilScoreDetail"] = channel_util_score_detail
        if channel_inter_util_detail is not UNSET:
            field_dict["channelInterUtilDetail"] = channel_inter_util_detail
        if access_capacity_score_detail is not UNSET:
            field_dict["accessCapacityScoreDetail"] = access_capacity_score_detail
        if rssi_score_detail is not UNSET:
            field_dict["rssiScoreDetail"] = rssi_score_detail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.channel_interference_sub_health_info_vo import (
            ChannelInterferenceSubHealthInfoVO,
        )
        from ..models.on_boarding_time_sub_health_detail_vo import (
            OnBoardingTimeSubHealthDetailVO,
        )
        from ..models.sub_single_health_info_detail_vo import (
            SubSingleHealthInfoDetailVO,
        )

        d = dict(src_dict)
        wifi_health_score = d.pop("wifiHealthScore", UNSET)

        _access_time_score_detail = d.pop("accessTimeScoreDetail", UNSET)
        access_time_score_detail: SubSingleHealthInfoDetailVO | Unset
        if isinstance(_access_time_score_detail, Unset):
            access_time_score_detail = UNSET
        else:
            access_time_score_detail = SubSingleHealthInfoDetailVO.from_dict(
                _access_time_score_detail
            )

        _wireless_client_quality_detail = d.pop("wirelessClientQualityDetail", UNSET)
        wireless_client_quality_detail: OnBoardingTimeSubHealthDetailVO | Unset
        if isinstance(_wireless_client_quality_detail, Unset):
            wireless_client_quality_detail = UNSET
        else:
            wireless_client_quality_detail = OnBoardingTimeSubHealthDetailVO.from_dict(
                _wireless_client_quality_detail
            )

        _channel_util_score_detail = d.pop("channelUtilScoreDetail", UNSET)
        channel_util_score_detail: SubSingleHealthInfoDetailVO | Unset
        if isinstance(_channel_util_score_detail, Unset):
            channel_util_score_detail = UNSET
        else:
            channel_util_score_detail = SubSingleHealthInfoDetailVO.from_dict(
                _channel_util_score_detail
            )

        _channel_inter_util_detail = d.pop("channelInterUtilDetail", UNSET)
        channel_inter_util_detail: ChannelInterferenceSubHealthInfoVO | Unset
        if isinstance(_channel_inter_util_detail, Unset):
            channel_inter_util_detail = UNSET
        else:
            channel_inter_util_detail = ChannelInterferenceSubHealthInfoVO.from_dict(
                _channel_inter_util_detail
            )

        _access_capacity_score_detail = d.pop("accessCapacityScoreDetail", UNSET)
        access_capacity_score_detail: SubSingleHealthInfoDetailVO | Unset
        if isinstance(_access_capacity_score_detail, Unset):
            access_capacity_score_detail = UNSET
        else:
            access_capacity_score_detail = SubSingleHealthInfoDetailVO.from_dict(
                _access_capacity_score_detail
            )

        _rssi_score_detail = d.pop("rssiScoreDetail", UNSET)
        rssi_score_detail: SubSingleHealthInfoDetailVO | Unset
        if isinstance(_rssi_score_detail, Unset):
            rssi_score_detail = UNSET
        else:
            rssi_score_detail = SubSingleHealthInfoDetailVO.from_dict(
                _rssi_score_detail
            )

        wifi_health_detail_vo = cls(
            wifi_health_score=wifi_health_score,
            access_time_score_detail=access_time_score_detail,
            wireless_client_quality_detail=wireless_client_quality_detail,
            channel_util_score_detail=channel_util_score_detail,
            channel_inter_util_detail=channel_inter_util_detail,
            access_capacity_score_detail=access_capacity_score_detail,
            rssi_score_detail=rssi_score_detail,
        )

        wifi_health_detail_vo.additional_properties = d
        return wifi_health_detail_vo

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
