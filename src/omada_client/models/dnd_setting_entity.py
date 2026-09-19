from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DndSettingEntity")


@_attrs_define
class DndSettingEntity:
    """
    Attributes:
        enable (bool): Enable DND or not
        omadac_id (str | Unset): Omadac ID
        site_id (str | Unset): Site ID
        day_mode (int | Unset): The days you want to block the incoming calls. 1-daily，2-weekend，3-weekday
        time_begin (int | Unset): The start time of the DND period you want to block incoming calls. It should be an
            integer value between 0 and 1438.
        time_end (int | Unset): The end time of the DND period you want to block incoming calls. It should be an integer
            value between 1 and 1439.
    """

    enable: bool
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    day_mode: int | Unset = UNSET
    time_begin: int | Unset = UNSET
    time_end: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        omadac_id = self.omadac_id

        site_id = self.site_id

        day_mode = self.day_mode

        time_begin = self.time_begin

        time_end = self.time_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if day_mode is not UNSET:
            field_dict["dayMode"] = day_mode
        if time_begin is not UNSET:
            field_dict["timeBegin"] = time_begin
        if time_end is not UNSET:
            field_dict["timeEnd"] = time_end

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        day_mode = d.pop("dayMode", UNSET)

        time_begin = d.pop("timeBegin", UNSET)

        time_end = d.pop("timeEnd", UNSET)

        dnd_setting_entity = cls(
            enable=enable,
            omadac_id=omadac_id,
            site_id=site_id,
            day_mode=day_mode,
            time_begin=time_begin,
            time_end=time_end,
        )

        dnd_setting_entity.additional_properties = d
        return dnd_setting_entity

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
