from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_event_setting_open_api_vo import AnomalyEventSettingOpenApiVO
    from ..models.anomaly_setting_stat_open_api_vo import AnomalySettingStatOpenApiVO


T = TypeVar("T", bound="AnomalySettingGridVOAnomalyEventSettingOpenApiVO")


@_attrs_define
class AnomalySettingGridVOAnomalyEventSettingOpenApiVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[AnomalyEventSettingOpenApiVO] | Unset):
        resource (int | Unset): The anomaly event setting creation resource, such as: 0: new created, 1: from template,
            2: override
        statistic (AnomalySettingStatOpenApiVO | Unset): Anomaly setting statistic summary
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[AnomalyEventSettingOpenApiVO] | Unset = UNSET
    resource: int | Unset = UNSET
    statistic: AnomalySettingStatOpenApiVO | Unset = UNSET
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

        resource = self.resource

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
        if resource is not UNSET:
            field_dict["resource"] = resource
        if statistic is not UNSET:
            field_dict["statistic"] = statistic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_event_setting_open_api_vo import (
            AnomalyEventSettingOpenApiVO,
        )
        from ..models.anomaly_setting_stat_open_api_vo import (
            AnomalySettingStatOpenApiVO,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[AnomalyEventSettingOpenApiVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = AnomalyEventSettingOpenApiVO.from_dict(data_item_data)

                data.append(data_item)

        resource = d.pop("resource", UNSET)

        _statistic = d.pop("statistic", UNSET)
        statistic: AnomalySettingStatOpenApiVO | Unset
        if isinstance(_statistic, Unset):
            statistic = UNSET
        else:
            statistic = AnomalySettingStatOpenApiVO.from_dict(_statistic)

        anomaly_setting_grid_vo_anomaly_event_setting_open_api_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            resource=resource,
            statistic=statistic,
        )

        anomaly_setting_grid_vo_anomaly_event_setting_open_api_vo.additional_properties = d
        return anomaly_setting_grid_vo_anomaly_event_setting_open_api_vo

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
