from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_aggregate_vo import AnomalyAggregateVO
    from ..models.insight_anomaly_stat_vo import InsightAnomalyStatVO


T = TypeVar("T", bound="AnomalyGridVOAnomalyAggregateVO")


@_attrs_define
class AnomalyGridVOAnomalyAggregateVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[AnomalyAggregateVO] | Unset):
        statistic (InsightAnomalyStatVO | Unset): Statistics of incidents.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[AnomalyAggregateVO] | Unset = UNSET
    statistic: InsightAnomalyStatVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rows = self.total_rows

        current_page = self.current_page

        current_size = self.current_size

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        statistic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.statistic, Unset):
            statistic = self.statistic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data
        if statistic is not UNSET:
            field_dict["statistic"] = statistic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_aggregate_vo import AnomalyAggregateVO
        from ..models.insight_anomaly_stat_vo import (
            InsightAnomalyStatVO,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[AnomalyAggregateVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = AnomalyAggregateVO.from_dict(data_item_data)

                data.append(data_item)

        _statistic = d.pop("statistic", UNSET)
        statistic: InsightAnomalyStatVO | Unset
        if isinstance(_statistic, Unset):
            statistic = UNSET
        else:
            statistic = InsightAnomalyStatVO.from_dict(_statistic)

        anomaly_grid_vo_anomaly_aggregate_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            statistic=statistic,
        )

        anomaly_grid_vo_anomaly_aggregate_vo.additional_properties = d
        return anomaly_grid_vo_anomaly_aggregate_vo

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
