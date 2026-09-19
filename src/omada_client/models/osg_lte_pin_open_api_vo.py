from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_lte_pin_setting_open_api_vo import OsgLtePinSettingOpenApiVO


T = TypeVar("T", bound="OsgLtePinOpenApiVO")


@_attrs_define
class OsgLtePinOpenApiVO:
    """
    Attributes:
        type_ (int | Unset): Type of change: 1: Changing the PIN setting, 2: Changing the PIN code.
        first_try (bool | Unset): Whether the first attempt was successful.
        pin_code (str | Unset): PIN code.
        puk_code (str | Unset): PUK code.
        new_pin_code (str | Unset): New PIN code
        pin_setting (OsgLtePinSettingOpenApiVO | Unset): PIN settings.
        sim_card (int | Unset): When the device supports Dual-SIM card, parameter [simCard] should not be null.1: SIM1;
            2: SIM2.
    """

    type_: int | Unset = UNSET
    first_try: bool | Unset = UNSET
    pin_code: str | Unset = UNSET
    puk_code: str | Unset = UNSET
    new_pin_code: str | Unset = UNSET
    pin_setting: OsgLtePinSettingOpenApiVO | Unset = UNSET
    sim_card: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        first_try = self.first_try

        pin_code = self.pin_code

        puk_code = self.puk_code

        new_pin_code = self.new_pin_code

        pin_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pin_setting, Unset):
            pin_setting = self.pin_setting.to_dict()

        sim_card = self.sim_card

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if first_try is not UNSET:
            field_dict["firstTry"] = first_try
        if pin_code is not UNSET:
            field_dict["pinCode"] = pin_code
        if puk_code is not UNSET:
            field_dict["pukCode"] = puk_code
        if new_pin_code is not UNSET:
            field_dict["newPinCode"] = new_pin_code
        if pin_setting is not UNSET:
            field_dict["pinSetting"] = pin_setting
        if sim_card is not UNSET:
            field_dict["simCard"] = sim_card

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_lte_pin_setting_open_api_vo import (
            OsgLtePinSettingOpenApiVO,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        first_try = d.pop("firstTry", UNSET)

        pin_code = d.pop("pinCode", UNSET)

        puk_code = d.pop("pukCode", UNSET)

        new_pin_code = d.pop("newPinCode", UNSET)

        _pin_setting = d.pop("pinSetting", UNSET)
        pin_setting: OsgLtePinSettingOpenApiVO | Unset
        if isinstance(_pin_setting, Unset):
            pin_setting = UNSET
        else:
            pin_setting = OsgLtePinSettingOpenApiVO.from_dict(_pin_setting)

        sim_card = d.pop("simCard", UNSET)

        osg_lte_pin_open_api_vo = cls(
            type_=type_,
            first_try=first_try,
            pin_code=pin_code,
            puk_code=puk_code,
            new_pin_code=new_pin_code,
            pin_setting=pin_setting,
            sim_card=sim_card,
        )

        osg_lte_pin_open_api_vo.additional_properties = d
        return osg_lte_pin_open_api_vo

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
