from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_channel_stat import ApChannelStat


T = TypeVar("T", bound="ApChannelStats")


@_attrs_define
class ApChannelStats:
    """
    Attributes:
        field_2g_channel_stat (list[ApChannelStat] | Unset): 2g channel stat
        field_5g_channel_stat (list[ApChannelStat] | Unset): 5g channel stat
        field_6g_channel_stat (list[ApChannelStat] | Unset): 6g channel stat
    """

    field_2g_channel_stat: list[ApChannelStat] | Unset = UNSET
    field_5g_channel_stat: list[ApChannelStat] | Unset = UNSET
    field_6g_channel_stat: list[ApChannelStat] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_2g_channel_stat: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_2g_channel_stat, Unset):
            field_2g_channel_stat = []
            for field_2g_channel_stat_item_data in self.field_2g_channel_stat:
                field_2g_channel_stat_item = field_2g_channel_stat_item_data.to_dict()
                field_2g_channel_stat.append(field_2g_channel_stat_item)

        field_5g_channel_stat: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_5g_channel_stat, Unset):
            field_5g_channel_stat = []
            for field_5g_channel_stat_item_data in self.field_5g_channel_stat:
                field_5g_channel_stat_item = field_5g_channel_stat_item_data.to_dict()
                field_5g_channel_stat.append(field_5g_channel_stat_item)

        field_6g_channel_stat: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_6g_channel_stat, Unset):
            field_6g_channel_stat = []
            for field_6g_channel_stat_item_data in self.field_6g_channel_stat:
                field_6g_channel_stat_item = field_6g_channel_stat_item_data.to_dict()
                field_6g_channel_stat.append(field_6g_channel_stat_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_2g_channel_stat is not UNSET:
            field_dict["2g channel stat"] = field_2g_channel_stat
        if field_5g_channel_stat is not UNSET:
            field_dict["5g channel stat"] = field_5g_channel_stat
        if field_6g_channel_stat is not UNSET:
            field_dict["6g channel stat"] = field_6g_channel_stat

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_channel_stat import ApChannelStat

        d = dict(src_dict)
        _field_2g_channel_stat = d.pop("2g channel stat", UNSET)
        field_2g_channel_stat: list[ApChannelStat] | Unset = UNSET
        if _field_2g_channel_stat is not UNSET:
            field_2g_channel_stat = []
            for field_2g_channel_stat_item_data in _field_2g_channel_stat:
                field_2g_channel_stat_item = ApChannelStat.from_dict(
                    field_2g_channel_stat_item_data
                )

                field_2g_channel_stat.append(field_2g_channel_stat_item)

        _field_5g_channel_stat = d.pop("5g channel stat", UNSET)
        field_5g_channel_stat: list[ApChannelStat] | Unset = UNSET
        if _field_5g_channel_stat is not UNSET:
            field_5g_channel_stat = []
            for field_5g_channel_stat_item_data in _field_5g_channel_stat:
                field_5g_channel_stat_item = ApChannelStat.from_dict(
                    field_5g_channel_stat_item_data
                )

                field_5g_channel_stat.append(field_5g_channel_stat_item)

        _field_6g_channel_stat = d.pop("6g channel stat", UNSET)
        field_6g_channel_stat: list[ApChannelStat] | Unset = UNSET
        if _field_6g_channel_stat is not UNSET:
            field_6g_channel_stat = []
            for field_6g_channel_stat_item_data in _field_6g_channel_stat:
                field_6g_channel_stat_item = ApChannelStat.from_dict(
                    field_6g_channel_stat_item_data
                )

                field_6g_channel_stat.append(field_6g_channel_stat_item)

        ap_channel_stats = cls(
            field_2g_channel_stat=field_2g_channel_stat,
            field_5g_channel_stat=field_5g_channel_stat,
            field_6g_channel_stat=field_6g_channel_stat,
        )

        ap_channel_stats.additional_properties = d
        return ap_channel_stats

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
