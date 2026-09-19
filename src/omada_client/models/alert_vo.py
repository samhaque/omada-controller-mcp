from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertVO")


@_attrs_define
class AlertVO:
    """Gateway alert

    Attributes:
        total_alerts (int | Unset): Total number of alerts
        info_alerts (int | Unset): Total number of info alerts
        warning_alerts (int | Unset): Total number of warning alerts
        error_alerts (int | Unset): Total number of error alerts
        critical_alerts (int | Unset): Total number of critical alerts
    """

    total_alerts: int | Unset = UNSET
    info_alerts: int | Unset = UNSET
    warning_alerts: int | Unset = UNSET
    error_alerts: int | Unset = UNSET
    critical_alerts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_alerts = self.total_alerts

        info_alerts = self.info_alerts

        warning_alerts = self.warning_alerts

        error_alerts = self.error_alerts

        critical_alerts = self.critical_alerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_alerts is not UNSET:
            field_dict["totalAlerts"] = total_alerts
        if info_alerts is not UNSET:
            field_dict["infoAlerts"] = info_alerts
        if warning_alerts is not UNSET:
            field_dict["warningAlerts"] = warning_alerts
        if error_alerts is not UNSET:
            field_dict["errorAlerts"] = error_alerts
        if critical_alerts is not UNSET:
            field_dict["criticalAlerts"] = critical_alerts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_alerts = d.pop("totalAlerts", UNSET)

        info_alerts = d.pop("infoAlerts", UNSET)

        warning_alerts = d.pop("warningAlerts", UNSET)

        error_alerts = d.pop("errorAlerts", UNSET)

        critical_alerts = d.pop("criticalAlerts", UNSET)

        alert_vo = cls(
            total_alerts=total_alerts,
            info_alerts=info_alerts,
            warning_alerts=warning_alerts,
            error_alerts=error_alerts,
            critical_alerts=critical_alerts,
        )

        alert_vo.additional_properties = d
        return alert_vo

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
