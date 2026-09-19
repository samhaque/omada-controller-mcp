from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dst_time_dto import DstTimeDTO


T = TypeVar("T", bound="DstDTO")


@_attrs_define
class DstDTO:
    """Daylight Saving Time config of the site

    Attributes:
        enable (bool | Unset): DST config status; If false, other parameters are not required.
        mode (int | Unset): DST config mode; If disable, other parameters are not required. 0: disable, 1: auto, 2:
            manually
        start (DstTimeDTO | Unset): DST end time config
        end (DstTimeDTO | Unset): DST end time config
        status (bool | Unset): DST available status
        start_time (int | Unset): The timeStamp of the DST available start time
        end_time (int | Unset): The timeStamp of the DST available end time
        offset (int | Unset): DST offset config(Unit: ms); It should be a value as follows: [1800000, 3600000, 5400000,
            7200000].
        next_start (int | Unset): The timeStamp of the DST start time of the next year(Unit: ms)
        next_end (int | Unset): The timeStamp of the DST end time of the next year(Unit: ms)
        time_zone (str | Unset): Timezone of the site
        last_start (int | Unset): The timeStamp of the DST start time of the last year(Unit: ms)
        last_end (int | Unset): The timeStamp of the DST end time of the last year(Unit: ms)
    """

    enable: bool | Unset = UNSET
    mode: int | Unset = UNSET
    start: DstTimeDTO | Unset = UNSET
    end: DstTimeDTO | Unset = UNSET
    status: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    offset: int | Unset = UNSET
    next_start: int | Unset = UNSET
    next_end: int | Unset = UNSET
    time_zone: str | Unset = UNSET
    last_start: int | Unset = UNSET
    last_end: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        mode = self.mode

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        status = self.status

        start_time = self.start_time

        end_time = self.end_time

        offset = self.offset

        next_start = self.next_start

        next_end = self.next_end

        time_zone = self.time_zone

        last_start = self.last_start

        last_end = self.last_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if mode is not UNSET:
            field_dict["mode"] = mode
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if status is not UNSET:
            field_dict["status"] = status
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if offset is not UNSET:
            field_dict["offset"] = offset
        if next_start is not UNSET:
            field_dict["nextStart"] = next_start
        if next_end is not UNSET:
            field_dict["nextEnd"] = next_end
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if last_start is not UNSET:
            field_dict["lastStart"] = last_start
        if last_end is not UNSET:
            field_dict["lastEnd"] = last_end

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dst_time_dto import DstTimeDTO

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        mode = d.pop("mode", UNSET)

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

        status = d.pop("status", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        offset = d.pop("offset", UNSET)

        next_start = d.pop("nextStart", UNSET)

        next_end = d.pop("nextEnd", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        last_start = d.pop("lastStart", UNSET)

        last_end = d.pop("lastEnd", UNSET)

        dst_dto = cls(
            enable=enable,
            mode=mode,
            start=start,
            end=end,
            status=status,
            start_time=start_time,
            end_time=end_time,
            offset=offset,
            next_start=next_start,
            next_end=next_end,
            time_zone=time_zone,
            last_start=last_start,
            last_end=last_end,
        )

        dst_dto.additional_properties = d
        return dst_dto

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
