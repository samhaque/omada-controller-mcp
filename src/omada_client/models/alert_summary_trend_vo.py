from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_summary_vo import AlertSummaryVO
    from ..models.trend_base_vo import TrendBaseVO


T = TypeVar("T", bound="AlertSummaryTrendVO")


@_attrs_define
class AlertSummaryTrendVO:
    """
    Attributes:
        alert_summary (AlertSummaryVO | Unset): Alert summary
        alert_trend (list[TrendBaseVO] | Unset): Alert trend
    """

    alert_summary: AlertSummaryVO | Unset = UNSET
    alert_trend: list[TrendBaseVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_summary, Unset):
            alert_summary = self.alert_summary.to_dict()

        alert_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alert_trend, Unset):
            alert_trend = []
            for alert_trend_item_data in self.alert_trend:
                alert_trend_item = alert_trend_item_data.to_dict()
                alert_trend.append(alert_trend_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_summary is not UNSET:
            field_dict["alertSummary"] = alert_summary
        if alert_trend is not UNSET:
            field_dict["alertTrend"] = alert_trend

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_summary_vo import AlertSummaryVO
        from ..models.trend_base_vo import TrendBaseVO

        d = dict(src_dict)
        _alert_summary = d.pop("alertSummary", UNSET)
        alert_summary: AlertSummaryVO | Unset
        if isinstance(_alert_summary, Unset):
            alert_summary = UNSET
        else:
            alert_summary = AlertSummaryVO.from_dict(_alert_summary)

        _alert_trend = d.pop("alertTrend", UNSET)
        alert_trend: list[TrendBaseVO] | Unset = UNSET
        if _alert_trend is not UNSET:
            alert_trend = []
            for alert_trend_item_data in _alert_trend:
                alert_trend_item = TrendBaseVO.from_dict(alert_trend_item_data)

                alert_trend.append(alert_trend_item)

        alert_summary_trend_vo = cls(
            alert_summary=alert_summary,
            alert_trend=alert_trend,
        )

        alert_summary_trend_vo.additional_properties = d
        return alert_summary_trend_vo

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
