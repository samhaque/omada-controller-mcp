from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgLtePinSettingVO")


@_attrs_define
class OsgLtePinSettingVO:
    """
    Attributes:
        card_status (int | Unset):
        pin_lock (bool | Unset):
        auto_un_lock (bool | Unset):
        sim_card_used (int | Unset):
    """

    card_status: int | Unset = UNSET
    pin_lock: bool | Unset = UNSET
    auto_un_lock: bool | Unset = UNSET
    sim_card_used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_status = self.card_status

        pin_lock = self.pin_lock

        auto_un_lock = self.auto_un_lock

        sim_card_used = self.sim_card_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_status is not UNSET:
            field_dict["cardStatus"] = card_status
        if pin_lock is not UNSET:
            field_dict["pinLock"] = pin_lock
        if auto_un_lock is not UNSET:
            field_dict["autoUnLock"] = auto_un_lock
        if sim_card_used is not UNSET:
            field_dict["simCardUsed"] = sim_card_used

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        card_status = d.pop("cardStatus", UNSET)

        pin_lock = d.pop("pinLock", UNSET)

        auto_un_lock = d.pop("autoUnLock", UNSET)

        sim_card_used = d.pop("simCardUsed", UNSET)

        osg_lte_pin_setting_vo = cls(
            card_status=card_status,
            pin_lock=pin_lock,
            auto_un_lock=auto_un_lock,
            sim_card_used=sim_card_used,
        )

        osg_lte_pin_setting_vo.additional_properties = d
        return osg_lte_pin_setting_vo

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
