from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertLogStatOpenApiVO")


@_attrs_define
class AlertLogStatOpenApiVO:
    """Alert log statistic.

    Attributes:
        total_log_num (int | Unset): Total log number.
        un_resolved_log_num (int | Unset): Unresolved alert log number.
        resolved_log_num (int | Unset): Resolved alert log number.
        system_log_num (int | Unset): System alert log number.
        device_log_num (int | Unset): Device alert log number.
    """

    total_log_num: int | Unset = UNSET
    un_resolved_log_num: int | Unset = UNSET
    resolved_log_num: int | Unset = UNSET
    system_log_num: int | Unset = UNSET
    device_log_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_log_num = self.total_log_num

        un_resolved_log_num = self.un_resolved_log_num

        resolved_log_num = self.resolved_log_num

        system_log_num = self.system_log_num

        device_log_num = self.device_log_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_log_num is not UNSET:
            field_dict["totalLogNum"] = total_log_num
        if un_resolved_log_num is not UNSET:
            field_dict["unResolvedLogNum"] = un_resolved_log_num
        if resolved_log_num is not UNSET:
            field_dict["resolvedLogNum"] = resolved_log_num
        if system_log_num is not UNSET:
            field_dict["systemLogNum"] = system_log_num
        if device_log_num is not UNSET:
            field_dict["deviceLogNum"] = device_log_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_log_num = d.pop("totalLogNum", UNSET)

        un_resolved_log_num = d.pop("unResolvedLogNum", UNSET)

        resolved_log_num = d.pop("resolvedLogNum", UNSET)

        system_log_num = d.pop("systemLogNum", UNSET)

        device_log_num = d.pop("deviceLogNum", UNSET)

        alert_log_stat_open_api_vo = cls(
            total_log_num=total_log_num,
            un_resolved_log_num=un_resolved_log_num,
            resolved_log_num=resolved_log_num,
            system_log_num=system_log_num,
            device_log_num=device_log_num,
        )

        alert_log_stat_open_api_vo.additional_properties = d
        return alert_log_stat_open_api_vo

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
