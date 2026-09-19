from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dst_time_open_api_dto import DstTimeOpenApiDTO


T = TypeVar("T", bound="ModifyDstDTO")


@_attrs_define
class ModifyDstDTO:
    """Daylight Saving Time config of the site

    Attributes:
        enable (bool | Unset): DST config status; If false, other parameters are not required. Deprecated, use mode
            instead.
        mode (int | Unset): DST config mode; If disable, other parameters are not required. 0: disable, 1: auto, 2:
            manually
        start (DstTimeOpenApiDTO | Unset): DST end time config
        end (DstTimeOpenApiDTO | Unset): DST end time config
        offset (int | Unset): DST offset config(Unit: ms); It should be a value as follows: [1800000, 3600000, 5400000,
            7200000]. When DST mode is 2(manually), offset is required.
    """

    enable: bool | Unset = UNSET
    mode: int | Unset = UNSET
    start: DstTimeOpenApiDTO | Unset = UNSET
    end: DstTimeOpenApiDTO | Unset = UNSET
    offset: int | Unset = UNSET
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

        offset = self.offset

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
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dst_time_open_api_dto import DstTimeOpenApiDTO

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        mode = d.pop("mode", UNSET)

        _start = d.pop("start", UNSET)
        start: DstTimeOpenApiDTO | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = DstTimeOpenApiDTO.from_dict(_start)

        _end = d.pop("end", UNSET)
        end: DstTimeOpenApiDTO | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = DstTimeOpenApiDTO.from_dict(_end)

        offset = d.pop("offset", UNSET)

        modify_dst_dto = cls(
            enable=enable,
            mode=mode,
            start=start,
            end=end,
            offset=offset,
        )

        modify_dst_dto.additional_properties = d
        return modify_dst_dto

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
