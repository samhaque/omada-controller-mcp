from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mac_time_score_list_vo import MacTimeScoreListVO


T = TypeVar("T", bound="HealthTimeLineVO")


@_attrs_define
class HealthTimeLineVO:
    """
    Attributes:
        timeline (list[MacTimeScoreListVO] | Unset): Health timeline
    """

    timeline: list[MacTimeScoreListVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timeline: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.timeline, Unset):
            timeline = []
            for timeline_item_data in self.timeline:
                timeline_item = timeline_item_data.to_dict()
                timeline.append(timeline_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timeline is not UNSET:
            field_dict["timeline"] = timeline

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mac_time_score_list_vo import MacTimeScoreListVO

        d = dict(src_dict)
        _timeline = d.pop("timeline", UNSET)
        timeline: list[MacTimeScoreListVO] | Unset = UNSET
        if _timeline is not UNSET:
            timeline = []
            for timeline_item_data in _timeline:
                timeline_item = MacTimeScoreListVO.from_dict(timeline_item_data)

                timeline.append(timeline_item)

        health_time_line_vo = cls(
            timeline=timeline,
        )

        health_time_line_vo.additional_properties = d
        return health_time_line_vo

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
