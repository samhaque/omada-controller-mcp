from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSummaryVO")


@_attrs_define
class AlertSummaryVO:
    """Alert summary

    Attributes:
        total_grade_alerts (int | Unset): Number of alerts: sum by alert level
        total_type_alerts (int | Unset): Number of alerts: sum by alert type
        info_alerts (int | Unset): Number of info alerts
        error_alerts (int | Unset): Number of error alerts
        warning_alerts (int | Unset): Number of warning alerts
        client_alerts (int | Unset): Number of client alerts
        operation_alerts (int | Unset): Number of operation alerts
        device_alerts (int | Unset): Number of device alerts
        system_alerts (int | Unset): Number of system alerts
        critical_alerts (int | Unset): Number of critical alerts
    """

    total_grade_alerts: int | Unset = UNSET
    total_type_alerts: int | Unset = UNSET
    info_alerts: int | Unset = UNSET
    error_alerts: int | Unset = UNSET
    warning_alerts: int | Unset = UNSET
    client_alerts: int | Unset = UNSET
    operation_alerts: int | Unset = UNSET
    device_alerts: int | Unset = UNSET
    system_alerts: int | Unset = UNSET
    critical_alerts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_grade_alerts = self.total_grade_alerts

        total_type_alerts = self.total_type_alerts

        info_alerts = self.info_alerts

        error_alerts = self.error_alerts

        warning_alerts = self.warning_alerts

        client_alerts = self.client_alerts

        operation_alerts = self.operation_alerts

        device_alerts = self.device_alerts

        system_alerts = self.system_alerts

        critical_alerts = self.critical_alerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_grade_alerts is not UNSET:
            field_dict["totalGradeAlerts"] = total_grade_alerts
        if total_type_alerts is not UNSET:
            field_dict["totalTypeAlerts"] = total_type_alerts
        if info_alerts is not UNSET:
            field_dict["infoAlerts"] = info_alerts
        if error_alerts is not UNSET:
            field_dict["errorAlerts"] = error_alerts
        if warning_alerts is not UNSET:
            field_dict["warningAlerts"] = warning_alerts
        if client_alerts is not UNSET:
            field_dict["clientAlerts"] = client_alerts
        if operation_alerts is not UNSET:
            field_dict["operationAlerts"] = operation_alerts
        if device_alerts is not UNSET:
            field_dict["deviceAlerts"] = device_alerts
        if system_alerts is not UNSET:
            field_dict["systemAlerts"] = system_alerts
        if critical_alerts is not UNSET:
            field_dict["criticalAlerts"] = critical_alerts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_grade_alerts = d.pop("totalGradeAlerts", UNSET)

        total_type_alerts = d.pop("totalTypeAlerts", UNSET)

        info_alerts = d.pop("infoAlerts", UNSET)

        error_alerts = d.pop("errorAlerts", UNSET)

        warning_alerts = d.pop("warningAlerts", UNSET)

        client_alerts = d.pop("clientAlerts", UNSET)

        operation_alerts = d.pop("operationAlerts", UNSET)

        device_alerts = d.pop("deviceAlerts", UNSET)

        system_alerts = d.pop("systemAlerts", UNSET)

        critical_alerts = d.pop("criticalAlerts", UNSET)

        alert_summary_vo = cls(
            total_grade_alerts=total_grade_alerts,
            total_type_alerts=total_type_alerts,
            info_alerts=info_alerts,
            error_alerts=error_alerts,
            warning_alerts=warning_alerts,
            client_alerts=client_alerts,
            operation_alerts=operation_alerts,
            device_alerts=device_alerts,
            system_alerts=system_alerts,
            critical_alerts=critical_alerts,
        )

        alert_summary_vo.additional_properties = d
        return alert_summary_vo

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
