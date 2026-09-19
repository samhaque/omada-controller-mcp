from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnomalySettingStatOpenApiVO")


@_attrs_define
class AnomalySettingStatOpenApiVO:
    """Anomaly setting statistic summary

    Attributes:
        all_ (int | Unset): Total number of anomaly event settings
        enable (int | Unset): Number of enabled anomaly event settings
        disable (int | Unset): Number of disabled anomaly event settings
        all_level (int | Unset): Total number of level statistics
        critical (int | Unset): Number of critical level anomaly event settings
        error (int | Unset): Number of error level anomaly event settings
        warning (int | Unset): Number of warning level anomaly event settings
        info (int | Unset): Number of info level anomaly event settings
    """

    all_: int | Unset = UNSET
    enable: int | Unset = UNSET
    disable: int | Unset = UNSET
    all_level: int | Unset = UNSET
    critical: int | Unset = UNSET
    error: int | Unset = UNSET
    warning: int | Unset = UNSET
    info: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        enable = self.enable

        disable = self.disable

        all_level = self.all_level

        critical = self.critical

        error = self.error

        warning = self.warning

        info = self.info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if enable is not UNSET:
            field_dict["enable"] = enable
        if disable is not UNSET:
            field_dict["disable"] = disable
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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        enable = d.pop("enable", UNSET)

        disable = d.pop("disable", UNSET)

        all_level = d.pop("allLevel", UNSET)

        critical = d.pop("critical", UNSET)

        error = d.pop("error", UNSET)

        warning = d.pop("warning", UNSET)

        info = d.pop("info", UNSET)

        anomaly_setting_stat_open_api_vo = cls(
            all_=all_,
            enable=enable,
            disable=disable,
            all_level=all_level,
            critical=critical,
            error=error,
            warning=warning,
            info=info,
        )

        anomaly_setting_stat_open_api_vo.additional_properties = d
        return anomaly_setting_stat_open_api_vo

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
