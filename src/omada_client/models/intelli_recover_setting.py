from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntelliRecoverSetting")


@_attrs_define
class IntelliRecoverSetting:
    """
    Attributes:
        id (str | Unset): The intelli recover setting Id.
        auto_flag (bool | Unset): Auto recovering flag
        first_reboot_poe_interval (int | Unset): First reboot uplinkDevice poe interval
        limit_num (int | Unset): The limit reboot uplinkDevice poe number
        reboot_poe_interval (int | Unset): Retry reboot uplinkDevice poe interval
    """

    id: str | Unset = UNSET
    auto_flag: bool | Unset = UNSET
    first_reboot_poe_interval: int | Unset = UNSET
    limit_num: int | Unset = UNSET
    reboot_poe_interval: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        auto_flag = self.auto_flag

        first_reboot_poe_interval = self.first_reboot_poe_interval

        limit_num = self.limit_num

        reboot_poe_interval = self.reboot_poe_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if auto_flag is not UNSET:
            field_dict["autoFlag"] = auto_flag
        if first_reboot_poe_interval is not UNSET:
            field_dict["firstRebootPoeInterval"] = first_reboot_poe_interval
        if limit_num is not UNSET:
            field_dict["limitNum"] = limit_num
        if reboot_poe_interval is not UNSET:
            field_dict["rebootPoeInterval"] = reboot_poe_interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        auto_flag = d.pop("autoFlag", UNSET)

        first_reboot_poe_interval = d.pop("firstRebootPoeInterval", UNSET)

        limit_num = d.pop("limitNum", UNSET)

        reboot_poe_interval = d.pop("rebootPoeInterval", UNSET)

        intelli_recover_setting = cls(
            id=id,
            auto_flag=auto_flag,
            first_reboot_poe_interval=first_reboot_poe_interval,
            limit_num=limit_num,
            reboot_poe_interval=reboot_poe_interval,
        )

        intelli_recover_setting.additional_properties = d
        return intelli_recover_setting

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
