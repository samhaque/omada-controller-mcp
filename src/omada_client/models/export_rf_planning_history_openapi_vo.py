from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportRFPlanningHistoryOpenapiVO")


@_attrs_define
class ExportRFPlanningHistoryOpenapiVO:
    """
    Attributes:
        export_format (int): Export file format, should be a value as follows: 0: csv, 1: xlsx
        type_ (str | Unset): Export policy, type should be a value as follows:, all: export all history, include: export
            history in ids, exclude: exclude history in ids.
        history_ids (list[str] | Unset): RfPlanningHistoryId list
        start (int | Unset): Start time of history to export (millisecond timestamp)
        end (int | Unset): End time of history to export (millisecond timestamp)
        filter_mode (int | Unset): filtermode should be a value as follows: 1: rfPlanningHistory mode is manual;
            2:rfPlanningHistory mode is adaptive
    """

    export_format: int
    type_: str | Unset = UNSET
    history_ids: list[str] | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    filter_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_format = self.export_format

        type_ = self.type_

        history_ids: list[str] | Unset = UNSET
        if not isinstance(self.history_ids, Unset):
            history_ids = self.history_ids

        start = self.start

        end = self.end

        filter_mode = self.filter_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "export_format": export_format,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if history_ids is not UNSET:
            field_dict["history_ids"] = history_ids
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if filter_mode is not UNSET:
            field_dict["filter_mode"] = filter_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        export_format = d.pop("export_format")

        type_ = d.pop("type", UNSET)

        history_ids = cast(list[str], d.pop("history_ids", UNSET))

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        filter_mode = d.pop("filter_mode", UNSET)

        export_rf_planning_history_openapi_vo = cls(
            export_format=export_format,
            type_=type_,
            history_ids=history_ids,
            start=start,
            end=end,
            filter_mode=filter_mode,
        )

        export_rf_planning_history_openapi_vo.additional_properties = d
        return export_rf_planning_history_openapi_vo

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
