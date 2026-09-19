from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_suppression_config_vo import ReportSuppressionConfigVO


T = TypeVar("T", bound="SnoopConfigVO")


@_attrs_define
class SnoopConfigVO:
    """The snoop config model.

    Attributes:
        report_suppression_enable (bool | Unset): Indicates whether to enable message suppression.
        report_suppression_except_device (ReportSuppressionConfigVO | Unset): reportSuppressionExceptDevice
        member_port_aging_time (int | Unset): The aging time of member ports (unit: s).
        router_port_aging_time (int | Unset): The aging time of the routing port (unit: s).
        leave_time (int | Unset): The time it takes to remove the port from the group after receiving the outbound
            message (unit: s).
    """

    report_suppression_enable: bool | Unset = UNSET
    report_suppression_except_device: ReportSuppressionConfigVO | Unset = UNSET
    member_port_aging_time: int | Unset = UNSET
    router_port_aging_time: int | Unset = UNSET
    leave_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_suppression_enable = self.report_suppression_enable

        report_suppression_except_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.report_suppression_except_device, Unset):
            report_suppression_except_device = (
                self.report_suppression_except_device.to_dict()
            )

        member_port_aging_time = self.member_port_aging_time

        router_port_aging_time = self.router_port_aging_time

        leave_time = self.leave_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if report_suppression_enable is not UNSET:
            field_dict["reportSuppressionEnable"] = report_suppression_enable
        if report_suppression_except_device is not UNSET:
            field_dict["reportSuppressionExceptDevice"] = (
                report_suppression_except_device
            )
        if member_port_aging_time is not UNSET:
            field_dict["memberPortAgingTime"] = member_port_aging_time
        if router_port_aging_time is not UNSET:
            field_dict["routerPortAgingTime"] = router_port_aging_time
        if leave_time is not UNSET:
            field_dict["leaveTime"] = leave_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.report_suppression_config_vo import (
            ReportSuppressionConfigVO,
        )

        d = dict(src_dict)
        report_suppression_enable = d.pop("reportSuppressionEnable", UNSET)

        _report_suppression_except_device = d.pop(
            "reportSuppressionExceptDevice", UNSET
        )
        report_suppression_except_device: ReportSuppressionConfigVO | Unset
        if isinstance(_report_suppression_except_device, Unset):
            report_suppression_except_device = UNSET
        else:
            report_suppression_except_device = ReportSuppressionConfigVO.from_dict(
                _report_suppression_except_device
            )

        member_port_aging_time = d.pop("memberPortAgingTime", UNSET)

        router_port_aging_time = d.pop("routerPortAgingTime", UNSET)

        leave_time = d.pop("leaveTime", UNSET)

        snoop_config_vo = cls(
            report_suppression_enable=report_suppression_enable,
            report_suppression_except_device=report_suppression_except_device,
            member_port_aging_time=member_port_aging_time,
            router_port_aging_time=router_port_aging_time,
            leave_time=leave_time,
        )

        snoop_config_vo.additional_properties = d
        return snoop_config_vo

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
