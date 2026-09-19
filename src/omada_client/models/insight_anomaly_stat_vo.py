from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InsightAnomalyStatVO")


@_attrs_define
class InsightAnomalyStatVO:
    """Statistics of incidents.

    Attributes:
        all_ (int | Unset): Total number of incidents.
        all_status (int | Unset): Total number of incidents in status.
        all_level (int | Unset): Total number of incidents in level.
        critical (int | Unset): Number of critical level incidents.
        error (int | Unset): Number of error level incidents.
        warning (int | Unset): Number of warning level incidents.
        info (int | Unset): Number of info level incidents.
        unresolved (int | Unset): Number of unresolved incidents.
        resolved (int | Unset): Number of resolved incidents.
        ignored (int | Unset): Number of ignored incidents.
        ongoing (int | Unset): Number of ongoing incidents.
    """

    all_: int | Unset = UNSET
    all_status: int | Unset = UNSET
    all_level: int | Unset = UNSET
    critical: int | Unset = UNSET
    error: int | Unset = UNSET
    warning: int | Unset = UNSET
    info: int | Unset = UNSET
    unresolved: int | Unset = UNSET
    resolved: int | Unset = UNSET
    ignored: int | Unset = UNSET
    ongoing: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        all_status = self.all_status

        all_level = self.all_level

        critical = self.critical

        error = self.error

        warning = self.warning

        info = self.info

        unresolved = self.unresolved

        resolved = self.resolved

        ignored = self.ignored

        ongoing = self.ongoing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if all_status is not UNSET:
            field_dict["allStatus"] = all_status
        if all_level is not UNSET:
            field_dict["allLevel"] = all_level
        if critical is not UNSET:
            field_dict["critical"] = critical
        if error is not UNSET:
            field_dict["error"] = error
        if warning is not UNSET:
            field_dict["warning"] = warning
        if info is not UNSET:
            field_dict["info"] = info
        if unresolved is not UNSET:
            field_dict["unresolved"] = unresolved
        if resolved is not UNSET:
            field_dict["resolved"] = resolved
        if ignored is not UNSET:
            field_dict["ignored"] = ignored
        if ongoing is not UNSET:
            field_dict["ongoing"] = ongoing

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        all_status = d.pop("allStatus", UNSET)

        all_level = d.pop("allLevel", UNSET)

        critical = d.pop("critical", UNSET)

        error = d.pop("error", UNSET)

        warning = d.pop("warning", UNSET)

        info = d.pop("info", UNSET)

        unresolved = d.pop("unresolved", UNSET)

        resolved = d.pop("resolved", UNSET)

        ignored = d.pop("ignored", UNSET)

        ongoing = d.pop("ongoing", UNSET)

        insight_anomaly_stat_vo = cls(
            all_=all_,
            all_status=all_status,
            all_level=all_level,
            critical=critical,
            error=error,
            warning=warning,
            info=info,
            unresolved=unresolved,
            resolved=resolved,
            ignored=ignored,
            ongoing=ongoing,
        )

        insight_anomaly_stat_vo.additional_properties = d
        return insight_anomaly_stat_vo

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
