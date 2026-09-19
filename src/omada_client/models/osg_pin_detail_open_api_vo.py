from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgPinDetailOpenApiVO")


@_attrs_define
class OsgPinDetailOpenApiVO:
    """
    Attributes:
        card_status (int | Unset): cardStatus: 0:no_sim, 1:unknown, 2:pin_lock, 3:pin_verified, 4:ready, 5:puk_lock,
            6:blocked
        pin_lock (bool | Unset): Whether the PIN has a lock or not.
        auto_un_lock (bool | Unset): Whether or not PIN is automatically unlocked.
        try_pin_limit (int | Unset): The number of times the PIN can be entered incorrectly.
        try_puk_limit (int | Unset): The number of times the PUK can be entered incorrectly.
        sim_card_used (int | Unset): When the device supports Dual-SIM card, parameter [simCardUsed] should not be
            null.1: SIM1; 2: SIM2.
    """

    card_status: int | Unset = UNSET
    pin_lock: bool | Unset = UNSET
    auto_un_lock: bool | Unset = UNSET
    try_pin_limit: int | Unset = UNSET
    try_puk_limit: int | Unset = UNSET
    sim_card_used: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_status = self.card_status

        pin_lock = self.pin_lock

        auto_un_lock = self.auto_un_lock

        try_pin_limit = self.try_pin_limit

        try_puk_limit = self.try_puk_limit

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
        if try_pin_limit is not UNSET:
            field_dict["tryPinLimit"] = try_pin_limit
        if try_puk_limit is not UNSET:
            field_dict["tryPukLimit"] = try_puk_limit
        if sim_card_used is not UNSET:
            field_dict["simCardUsed"] = sim_card_used

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        card_status = d.pop("cardStatus", UNSET)

        pin_lock = d.pop("pinLock", UNSET)

        auto_un_lock = d.pop("autoUnLock", UNSET)

        try_pin_limit = d.pop("tryPinLimit", UNSET)

        try_puk_limit = d.pop("tryPukLimit", UNSET)

        sim_card_used = d.pop("simCardUsed", UNSET)

        osg_pin_detail_open_api_vo = cls(
            card_status=card_status,
            pin_lock=pin_lock,
            auto_un_lock=auto_un_lock,
            try_pin_limit=try_pin_limit,
            try_puk_limit=try_puk_limit,
            sim_card_used=sim_card_used,
        )

        osg_pin_detail_open_api_vo.additional_properties = d
        return osg_pin_detail_open_api_vo

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
