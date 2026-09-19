from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_statistics_score_vo import HealthStatisticsScoreVO


T = TypeVar("T", bound="SiteDeviceSubHealthScoreVO")


@_attrs_define
class SiteDeviceSubHealthScoreVO:
    """Device health score detail

    Attributes:
        osg_health_score_detail (HealthStatisticsScoreVO | Unset): Client health score detail
        osw_health_score_detail (HealthStatisticsScoreVO | Unset): Client health score detail
        ap_health_score_detail (HealthStatisticsScoreVO | Unset): Client health score detail
    """

    osg_health_score_detail: HealthStatisticsScoreVO | Unset = UNSET
    osw_health_score_detail: HealthStatisticsScoreVO | Unset = UNSET
    ap_health_score_detail: HealthStatisticsScoreVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        osg_health_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osg_health_score_detail, Unset):
            osg_health_score_detail = self.osg_health_score_detail.to_dict()

        osw_health_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osw_health_score_detail, Unset):
            osw_health_score_detail = self.osw_health_score_detail.to_dict()

        ap_health_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap_health_score_detail, Unset):
            ap_health_score_detail = self.ap_health_score_detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if osg_health_score_detail is not UNSET:
            field_dict["osgHealthScoreDetail"] = osg_health_score_detail
        if osw_health_score_detail is not UNSET:
            field_dict["oswHealthScoreDetail"] = osw_health_score_detail
        if ap_health_score_detail is not UNSET:
            field_dict["apHealthScoreDetail"] = ap_health_score_detail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.health_statistics_score_vo import (
            HealthStatisticsScoreVO,
        )

        d = dict(src_dict)
        _osg_health_score_detail = d.pop("osgHealthScoreDetail", UNSET)
        osg_health_score_detail: HealthStatisticsScoreVO | Unset
        if isinstance(_osg_health_score_detail, Unset):
            osg_health_score_detail = UNSET
        else:
            osg_health_score_detail = HealthStatisticsScoreVO.from_dict(
                _osg_health_score_detail
            )

        _osw_health_score_detail = d.pop("oswHealthScoreDetail", UNSET)
        osw_health_score_detail: HealthStatisticsScoreVO | Unset
        if isinstance(_osw_health_score_detail, Unset):
            osw_health_score_detail = UNSET
        else:
            osw_health_score_detail = HealthStatisticsScoreVO.from_dict(
                _osw_health_score_detail
            )

        _ap_health_score_detail = d.pop("apHealthScoreDetail", UNSET)
        ap_health_score_detail: HealthStatisticsScoreVO | Unset
        if isinstance(_ap_health_score_detail, Unset):
            ap_health_score_detail = UNSET
        else:
            ap_health_score_detail = HealthStatisticsScoreVO.from_dict(
                _ap_health_score_detail
            )

        site_device_sub_health_score_vo = cls(
            osg_health_score_detail=osg_health_score_detail,
            osw_health_score_detail=osw_health_score_detail,
            ap_health_score_detail=ap_health_score_detail,
        )

        site_device_sub_health_score_vo.additional_properties = d
        return site_device_sub_health_score_vo

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
