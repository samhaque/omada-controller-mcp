from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswLanMulticastVO")


@_attrs_define
class OswLanMulticastVO:
    """
    Attributes:
        report_suppression_enable (bool | Unset): Whether report suppression is enabled
        fast_leave_enable (bool | Unset): Whether fast leave is enabled
    """

    report_suppression_enable: bool | Unset = UNSET
    fast_leave_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_suppression_enable = self.report_suppression_enable

        fast_leave_enable = self.fast_leave_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report_suppression_enable is not UNSET:
            field_dict["reportSuppressionEnable"] = report_suppression_enable
        if fast_leave_enable is not UNSET:
            field_dict["fastLeaveEnable"] = fast_leave_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        report_suppression_enable = d.pop("reportSuppressionEnable", UNSET)

        fast_leave_enable = d.pop("fastLeaveEnable", UNSET)

        osw_lan_multicast_vo = cls(
            report_suppression_enable=report_suppression_enable,
            fast_leave_enable=fast_leave_enable,
        )

        osw_lan_multicast_vo.additional_properties = d
        return osw_lan_multicast_vo

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
