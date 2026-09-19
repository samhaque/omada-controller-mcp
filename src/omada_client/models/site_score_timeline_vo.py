from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_sub_health_score_vo import SiteSubHealthScoreVO


T = TypeVar("T", bound="SiteScoreTimelineVO")


@_attrs_define
class SiteScoreTimelineVO:
    """
    Attributes:
        time (int | Unset): Time(unit:ms)
        site_health_score (int | Unset): Site health score
        device_health_score (int | Unset): Device health score
        client_health_score (int | Unset): Client health score
        wifi_health_score (int | Unset): Wifi health score
        wan_health_score (int | Unset): WAN health score
        score_detail (SiteSubHealthScoreVO | Unset): Sub dimension health score Detail, such as device health、client
            health、wan health
    """

    time: int | Unset = UNSET
    site_health_score: int | Unset = UNSET
    device_health_score: int | Unset = UNSET
    client_health_score: int | Unset = UNSET
    wifi_health_score: int | Unset = UNSET
    wan_health_score: int | Unset = UNSET
    score_detail: SiteSubHealthScoreVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        site_health_score = self.site_health_score

        device_health_score = self.device_health_score

        client_health_score = self.client_health_score

        wifi_health_score = self.wifi_health_score

        wan_health_score = self.wan_health_score

        score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.score_detail, Unset):
            score_detail = self.score_detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if site_health_score is not UNSET:
            field_dict["siteHealthScore"] = site_health_score
        if device_health_score is not UNSET:
            field_dict["deviceHealthScore"] = device_health_score
        if client_health_score is not UNSET:
            field_dict["clientHealthScore"] = client_health_score
        if wifi_health_score is not UNSET:
            field_dict["wifiHealthScore"] = wifi_health_score
        if wan_health_score is not UNSET:
            field_dict["wanHealthScore"] = wan_health_score
        if score_detail is not UNSET:
            field_dict["scoreDetail"] = score_detail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_sub_health_score_vo import (
            SiteSubHealthScoreVO,
        )

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        site_health_score = d.pop("siteHealthScore", UNSET)

        device_health_score = d.pop("deviceHealthScore", UNSET)

        client_health_score = d.pop("clientHealthScore", UNSET)

        wifi_health_score = d.pop("wifiHealthScore", UNSET)

        wan_health_score = d.pop("wanHealthScore", UNSET)

        _score_detail = d.pop("scoreDetail", UNSET)
        score_detail: SiteSubHealthScoreVO | Unset
        if isinstance(_score_detail, Unset):
            score_detail = UNSET
        else:
            score_detail = SiteSubHealthScoreVO.from_dict(_score_detail)

        site_score_timeline_vo = cls(
            time=time,
            site_health_score=site_health_score,
            device_health_score=device_health_score,
            client_health_score=client_health_score,
            wifi_health_score=wifi_health_score,
            wan_health_score=wan_health_score,
            score_detail=score_detail,
        )

        site_score_timeline_vo.additional_properties = d
        return site_score_timeline_vo

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
