from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocateResultVO")


@_attrs_define
class LocateResultVO:
    """
    Attributes:
        mac (str | Unset): Mac
        locate_enable (bool | Unset): Indicates whether the locate function is enabled
        rest_time (int | Unset): The remaining time that the device locate switch is valid
    """

    mac: str | Unset = UNSET
    locate_enable: bool | Unset = UNSET
    rest_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        locate_enable = self.locate_enable

        rest_time = self.rest_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if locate_enable is not UNSET:
            field_dict["locateEnable"] = locate_enable
        if rest_time is not UNSET:
            field_dict["restTime"] = rest_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        locate_enable = d.pop("locateEnable", UNSET)

        rest_time = d.pop("restTime", UNSET)

        locate_result_vo = cls(
            mac=mac,
            locate_enable=locate_enable,
            rest_time=rest_time,
        )

        locate_result_vo.additional_properties = d
        return locate_result_vo

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
