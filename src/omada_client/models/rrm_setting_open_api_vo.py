from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RrmSettingOpenApiVO")


@_attrs_define
class RrmSettingOpenApiVO:
    """
    Attributes:
        mode (int): The mode of Auto WLAN Optimization, such as: 0: disable, 1: adaptive
        time_range_enable (bool): Whether the Time Range is enabled. True: enable, false: disable.
        resource (int | Unset): The anomaly event setting creation resource, such as: 0: new created, 1: from template,
            2: override
        time_range_id (str | Unset): This field represents Time Range Profile ID. Time Range Profile can be created
            using Create time range profile interface, and Time Range Profile ID can be obtained from Get time range profile
            list interface.
        time_range_action (int | Unset): The Time Range Action, such as: 0: out of range, 1: in range
    """

    mode: int
    time_range_enable: bool
    resource: int | Unset = UNSET
    time_range_id: str | Unset = UNSET
    time_range_action: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        time_range_enable = self.time_range_enable

        resource = self.resource

        time_range_id = self.time_range_id

        time_range_action = self.time_range_action

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "timeRangeEnable": time_range_enable,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource
        if time_range_id is not UNSET:
            field_dict["timeRangeId"] = time_range_id
        if time_range_action is not UNSET:
            field_dict["timeRangeAction"] = time_range_action

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        time_range_enable = d.pop("timeRangeEnable")

        resource = d.pop("resource", UNSET)

        time_range_id = d.pop("timeRangeId", UNSET)

        time_range_action = d.pop("timeRangeAction", UNSET)

        rrm_setting_open_api_vo = cls(
            mode=mode,
            time_range_enable=time_range_enable,
            resource=resource,
            time_range_id=time_range_id,
            time_range_action=time_range_action,
        )

        rrm_setting_open_api_vo.additional_properties = d
        return rrm_setting_open_api_vo

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
