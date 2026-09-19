from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_vo import AlertVO
    from ..models.gateway_cpu_mem_util_list_vo import GatewayCpuMemUtilListVO


T = TypeVar("T", bound="GatewaySummaryVO")


@_attrs_define
class GatewaySummaryVO:
    """Gateway summary

    Attributes:
        gateway_alert (AlertVO | Unset): Gateway alert
        gateway_ultilization (list[GatewayCpuMemUtilListVO] | Unset): Gateway CPU and memory utilization
    """

    gateway_alert: AlertVO | Unset = UNSET
    gateway_ultilization: list[GatewayCpuMemUtilListVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gateway_alert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gateway_alert, Unset):
            gateway_alert = self.gateway_alert.to_dict()

        gateway_ultilization: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gateway_ultilization, Unset):
            gateway_ultilization = []
            for gateway_ultilization_item_data in self.gateway_ultilization:
                gateway_ultilization_item = gateway_ultilization_item_data.to_dict()
                gateway_ultilization.append(gateway_ultilization_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gateway_alert is not UNSET:
            field_dict["gatewayAlert"] = gateway_alert
        if gateway_ultilization is not UNSET:
            field_dict["gatewayUltilization"] = gateway_ultilization

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_vo import AlertVO
        from ..models.gateway_cpu_mem_util_list_vo import (
            GatewayCpuMemUtilListVO,
        )

        d = dict(src_dict)
        _gateway_alert = d.pop("gatewayAlert", UNSET)
        gateway_alert: AlertVO | Unset
        if isinstance(_gateway_alert, Unset):
            gateway_alert = UNSET
        else:
            gateway_alert = AlertVO.from_dict(_gateway_alert)

        _gateway_ultilization = d.pop("gatewayUltilization", UNSET)
        gateway_ultilization: list[GatewayCpuMemUtilListVO] | Unset = UNSET
        if _gateway_ultilization is not UNSET:
            gateway_ultilization = []
            for gateway_ultilization_item_data in _gateway_ultilization:
                gateway_ultilization_item = GatewayCpuMemUtilListVO.from_dict(
                    gateway_ultilization_item_data
                )

                gateway_ultilization.append(gateway_ultilization_item)

        gateway_summary_vo = cls(
            gateway_alert=gateway_alert,
            gateway_ultilization=gateway_ultilization,
        )

        gateway_summary_vo.additional_properties = d
        return gateway_summary_vo

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
