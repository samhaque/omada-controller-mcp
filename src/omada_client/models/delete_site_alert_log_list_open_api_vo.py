from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSiteAlertLogListOpenApiVO")


@_attrs_define
class DeleteSiteAlertLogListOpenApiVO:
    """
    Attributes:
        select_type (str): Select type of logs. include: include selected logs, exclude: all but exclude selected logs,
            all: include all logs(Parameter [logs] need input '[]').
        start_time (int): The start timeStamp of the delete site alert log, unit: MS.
        end_time (int): The end timeStamp of the delete site alert log, unit: MS.
        logs (list[str] | Unset): Select the logs to delete; Log ID list can be obtained from 'Get site alert log list'
            interface.
        filter_module (str | Unset): The module of the delete site alert log; It is required when [selectType] is 'all',
            filterModule should be a value as follows: 'System' or 'Device'.
    """

    select_type: str
    start_time: int
    end_time: int
    logs: list[str] | Unset = UNSET
    filter_module: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_type = self.select_type

        start_time = self.start_time

        end_time = self.end_time

        logs: list[str] | Unset = UNSET
        if not isinstance(self.logs, Unset):
            logs = self.logs

        filter_module = self.filter_module

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selectType": select_type,
                "startTime": start_time,
                "endTime": end_time,
            }
        )
        if logs is not UNSET:
            field_dict["logs"] = logs
        if filter_module is not UNSET:
            field_dict["filterModule"] = filter_module

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        select_type = d.pop("selectType")

        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        logs = cast(list[str], d.pop("logs", UNSET))

        filter_module = d.pop("filterModule", UNSET)

        delete_site_alert_log_list_open_api_vo = cls(
            select_type=select_type,
            start_time=start_time,
            end_time=end_time,
            logs=logs,
            filter_module=filter_module,
        )

        delete_site_alert_log_list_open_api_vo.additional_properties = d
        return delete_site_alert_log_list_open_api_vo

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
