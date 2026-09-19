from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_radio_setting import ApRadioSetting


T = TypeVar("T", bound="ApRadiosConfig")


@_attrs_define
class ApRadiosConfig:
    """
    Attributes:
        radio_setting_2_g (ApRadioSetting | Unset): Radio Setting
        radio_setting_5_g (ApRadioSetting | Unset): Radio Setting
        radio_setting_5_g_1 (ApRadioSetting | Unset): Radio Setting
        radio_setting_5_g_2 (ApRadioSetting | Unset): Radio Setting
        radio_setting_6_g (ApRadioSetting | Unset): Radio Setting
    """

    radio_setting_2_g: ApRadioSetting | Unset = UNSET
    radio_setting_5_g: ApRadioSetting | Unset = UNSET
    radio_setting_5_g_1: ApRadioSetting | Unset = UNSET
    radio_setting_5_g_2: ApRadioSetting | Unset = UNSET
    radio_setting_6_g: ApRadioSetting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_setting_2_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_2_g, Unset):
            radio_setting_2_g = self.radio_setting_2_g.to_dict()

        radio_setting_5_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_5_g, Unset):
            radio_setting_5_g = self.radio_setting_5_g.to_dict()

        radio_setting_5_g_1: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_5_g_1, Unset):
            radio_setting_5_g_1 = self.radio_setting_5_g_1.to_dict()

        radio_setting_5_g_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_5_g_2, Unset):
            radio_setting_5_g_2 = self.radio_setting_5_g_2.to_dict()

        radio_setting_6_g: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radio_setting_6_g, Unset):
            radio_setting_6_g = self.radio_setting_6_g.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_setting_2_g is not UNSET:
            field_dict["radioSetting2g"] = radio_setting_2_g
        if radio_setting_5_g is not UNSET:
            field_dict["radioSetting5g"] = radio_setting_5_g
        if radio_setting_5_g_1 is not UNSET:
            field_dict["radioSetting5g1"] = radio_setting_5_g_1
        if radio_setting_5_g_2 is not UNSET:
            field_dict["radioSetting5g2"] = radio_setting_5_g_2
        if radio_setting_6_g is not UNSET:
            field_dict["radioSetting6g"] = radio_setting_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_radio_setting import ApRadioSetting

        d = dict(src_dict)
        _radio_setting_2_g = d.pop("radioSetting2g", UNSET)
        radio_setting_2_g: ApRadioSetting | Unset
        if isinstance(_radio_setting_2_g, Unset):
            radio_setting_2_g = UNSET
        else:
            radio_setting_2_g = ApRadioSetting.from_dict(_radio_setting_2_g)

        _radio_setting_5_g = d.pop("radioSetting5g", UNSET)
        radio_setting_5_g: ApRadioSetting | Unset
        if isinstance(_radio_setting_5_g, Unset):
            radio_setting_5_g = UNSET
        else:
            radio_setting_5_g = ApRadioSetting.from_dict(_radio_setting_5_g)

        _radio_setting_5_g_1 = d.pop("radioSetting5g1", UNSET)
        radio_setting_5_g_1: ApRadioSetting | Unset
        if isinstance(_radio_setting_5_g_1, Unset):
            radio_setting_5_g_1 = UNSET
        else:
            radio_setting_5_g_1 = ApRadioSetting.from_dict(_radio_setting_5_g_1)

        _radio_setting_5_g_2 = d.pop("radioSetting5g2", UNSET)
        radio_setting_5_g_2: ApRadioSetting | Unset
        if isinstance(_radio_setting_5_g_2, Unset):
            radio_setting_5_g_2 = UNSET
        else:
            radio_setting_5_g_2 = ApRadioSetting.from_dict(_radio_setting_5_g_2)

        _radio_setting_6_g = d.pop("radioSetting6g", UNSET)
        radio_setting_6_g: ApRadioSetting | Unset
        if isinstance(_radio_setting_6_g, Unset):
            radio_setting_6_g = UNSET
        else:
            radio_setting_6_g = ApRadioSetting.from_dict(_radio_setting_6_g)

        ap_radios_config = cls(
            radio_setting_2_g=radio_setting_2_g,
            radio_setting_5_g=radio_setting_5_g,
            radio_setting_5_g_1=radio_setting_5_g_1,
            radio_setting_5_g_2=radio_setting_5_g_2,
            radio_setting_6_g=radio_setting_6_g,
        )

        ap_radios_config.additional_properties = d
        return ap_radios_config

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
