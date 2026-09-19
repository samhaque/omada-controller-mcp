from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportExportV2")


@_attrs_define
class ReportExportV2:
    """
    Attributes:
        start (int): The report start time
        end (int): The report end time
        report_name (str): The report name
        report_type (int): The report type. 0 : pdf, 1 : csv.
        tab_id_list (list[str]): The tab need to export
        email_list (list[str] | Unset): The email list to send report
    """

    start: int
    end: int
    report_name: str
    report_type: int
    tab_id_list: list[str]
    email_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        report_name = self.report_name

        report_type = self.report_type

        tab_id_list = self.tab_id_list

        email_list: list[str] | Unset = UNSET
        if not isinstance(self.email_list, Unset):
            email_list = self.email_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "reportName": report_name,
                "reportType": report_type,
                "tabIdList": tab_id_list,
            }
        )
        if email_list is not UNSET:
            field_dict["emailList"] = email_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        report_name = d.pop("reportName")

        report_type = d.pop("reportType")

        tab_id_list = cast(list[str], d.pop("tabIdList"))

        email_list = cast(list[str], d.pop("emailList", UNSET))

        report_export_v2 = cls(
            start=start,
            end=end,
            report_name=report_name,
            report_type=report_type,
            tab_id_list=tab_id_list,
            email_list=email_list,
        )

        report_export_v2.additional_properties = d
        return report_export_v2

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
