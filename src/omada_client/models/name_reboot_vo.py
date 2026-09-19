from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameRebootVO")


@_attrs_define
class NameRebootVO:
    """
    Attributes:
        name (str | Unset): Switch name
        reboot_times (int | Unset): Reboot times
    """

    name: str | Unset = UNSET
    reboot_times: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        reboot_times = self.reboot_times

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if reboot_times is not UNSET:
            field_dict["rebootTimes"] = reboot_times

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        reboot_times = d.pop("rebootTimes", UNSET)

        name_reboot_vo = cls(
            name=name,
            reboot_times=reboot_times,
        )

        name_reboot_vo.additional_properties = d
        return name_reboot_vo

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
