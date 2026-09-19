from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_state_vo import AnomalyStateVO
    from ..models.health_statistics_score_vo import HealthStatisticsScoreVO
    from ..models.site_device_sub_health_score_vo import SiteDeviceSubHealthScoreVO
    from ..models.wan_health_list_vo import WanHealthListVO


T = TypeVar("T", bound="SiteSubHealthScoreVO")


@_attrs_define
class SiteSubHealthScoreVO:
    """Sub dimension health score Detail, such as device health、client health、wan health

    Attributes:
        device_health_score_detail (SiteDeviceSubHealthScoreVO | Unset): Device health score detail
        client_health_score_detail (HealthStatisticsScoreVO | Unset): Client health score detail
        wan_score_detail (WanHealthListVO | Unset): WAN health score detail
        incident_detail (AnomalyStateVO | Unset): Incident counts of different severity levels
    """

    device_health_score_detail: SiteDeviceSubHealthScoreVO | Unset = UNSET
    client_health_score_detail: HealthStatisticsScoreVO | Unset = UNSET
    wan_score_detail: WanHealthListVO | Unset = UNSET
    incident_detail: AnomalyStateVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_health_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_health_score_detail, Unset):
            device_health_score_detail = self.device_health_score_detail.to_dict()

        client_health_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_health_score_detail, Unset):
            client_health_score_detail = self.client_health_score_detail.to_dict()

        wan_score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_score_detail, Unset):
            wan_score_detail = self.wan_score_detail.to_dict()

        incident_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_detail, Unset):
            incident_detail = self.incident_detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_health_score_detail is not UNSET:
            field_dict["deviceHealthScoreDetail"] = device_health_score_detail
        if client_health_score_detail is not UNSET:
            field_dict["clientHealthScoreDetail"] = client_health_score_detail
        if wan_score_detail is not UNSET:
            field_dict["wanScoreDetail"] = wan_score_detail
        if incident_detail is not UNSET:
            field_dict["incidentDetail"] = incident_detail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_state_vo import AnomalyStateVO
        from ..models.health_statistics_score_vo import (
            HealthStatisticsScoreVO,
        )
        from ..models.site_device_sub_health_score_vo import (
            SiteDeviceSubHealthScoreVO,
        )
        from ..models.wan_health_list_vo import WanHealthListVO

        d = dict(src_dict)
        _device_health_score_detail = d.pop("deviceHealthScoreDetail", UNSET)
        device_health_score_detail: SiteDeviceSubHealthScoreVO | Unset
        if isinstance(_device_health_score_detail, Unset):
            device_health_score_detail = UNSET
        else:
            device_health_score_detail = SiteDeviceSubHealthScoreVO.from_dict(
                _device_health_score_detail
            )

        _client_health_score_detail = d.pop("clientHealthScoreDetail", UNSET)
        client_health_score_detail: HealthStatisticsScoreVO | Unset
        if isinstance(_client_health_score_detail, Unset):
            client_health_score_detail = UNSET
        else:
            client_health_score_detail = HealthStatisticsScoreVO.from_dict(
                _client_health_score_detail
            )

        _wan_score_detail = d.pop("wanScoreDetail", UNSET)
        wan_score_detail: WanHealthListVO | Unset
        if isinstance(_wan_score_detail, Unset):
            wan_score_detail = UNSET
        else:
            wan_score_detail = WanHealthListVO.from_dict(_wan_score_detail)

        _incident_detail = d.pop("incidentDetail", UNSET)
        incident_detail: AnomalyStateVO | Unset
        if isinstance(_incident_detail, Unset):
            incident_detail = UNSET
        else:
            incident_detail = AnomalyStateVO.from_dict(_incident_detail)

        site_sub_health_score_vo = cls(
            device_health_score_detail=device_health_score_detail,
            client_health_score_detail=client_health_score_detail,
            wan_score_detail=wan_score_detail,
            incident_detail=incident_detail,
        )

        site_sub_health_score_vo.additional_properties = d
        return site_sub_health_score_vo

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
