from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.occurrence import Occurrence


T = TypeVar("T", bound="RFPlanningScheduleConfigOpenApiVO")


@_attrs_define
class RFPlanningScheduleConfigOpenApiVO:
    """
    Attributes:
        schedule_enable (bool): Whether by WLAN Optimization schedule. The optimization schedule function is temporarily
            offline.
        occurrence (Occurrence): The optimization schedule function is temporarily offline.
    """

    schedule_enable: bool
    occurrence: Occurrence
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_enable = self.schedule_enable

        occurrence = self.occurrence.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduleEnable": schedule_enable,
                "occurrence": occurrence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.occurrence import Occurrence

        d = dict(src_dict)
        schedule_enable = d.pop("scheduleEnable")

        occurrence = Occurrence.from_dict(d.pop("occurrence"))

        rf_planning_schedule_config_open_api_vo = cls(
            schedule_enable=schedule_enable,
            occurrence=occurrence,
        )

        rf_planning_schedule_config_open_api_vo.additional_properties = d
        return rf_planning_schedule_config_open_api_vo

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
