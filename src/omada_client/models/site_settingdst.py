from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dst_time_dto import DstTimeDTO


T = TypeVar("T", bound="SiteSettingdst")


@_attrs_define
class SiteSettingdst:
    """Daylight Saving Time.

    Attributes:
        enable (bool | Unset): DST config status; If false, other parameters are not required.
        mode (int | Unset): DST config mode; If disable, other parameters are not required. 0: disable, 1: auto, 2:
            manually
        offset (int | Unset): DST offset config(Unit: ms); It should be a value as follows: [1800000, 3600000, 5400000,
            7200000].
        start (DstTimeDTO | Unset): DST end time config
        end (DstTimeDTO | Unset): DST end time config
    """

    enable: bool | Unset = UNSET
    mode: int | Unset = UNSET
    offset: int | Unset = UNSET
    start: DstTimeDTO | Unset = UNSET
    end: DstTimeDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        mode = self.mode

        offset = self.offset

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if mode is not UNSET:
            field_dict["mode"] = mode
        if offset is not UNSET:
            field_dict["offset"] = offset
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dst_time_dto import DstTimeDTO

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        mode = d.pop("mode", UNSET)

        offset = d.pop("offset", UNSET)

        _start = d.pop("start", UNSET)
        start: DstTimeDTO | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = DstTimeDTO.from_dict(_start)

        _end = d.pop("end", UNSET)
        end: DstTimeDTO | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = DstTimeDTO.from_dict(_end)

        site_settingdst = cls(
            enable=enable,
            mode=mode,
            offset=offset,
            start=start,
            end=end,
        )

        site_settingdst.additional_properties = d
        return site_settingdst

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
