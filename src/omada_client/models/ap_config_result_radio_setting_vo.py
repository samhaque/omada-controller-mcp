from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_radio_config_result_settings_vo import (
        ApRadioConfigResultSettingsVO,
    )


T = TypeVar("T", bound="ApConfigResultRadioSettingVO")


@_attrs_define
class ApConfigResultRadioSettingVO:
    """radio 6g setting config result

    Attributes:
        error_code (int | Unset): error code.
        msg (str | Unset): error msg
        ap_radio_config_result_setting (ApRadioConfigResultSettingsVO | Unset): ap radio config result detail setting.
    """

    error_code: int | Unset = UNSET
    msg: str | Unset = UNSET
    ap_radio_config_result_setting: ApRadioConfigResultSettingsVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        msg = self.msg

        ap_radio_config_result_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap_radio_config_result_setting, Unset):
            ap_radio_config_result_setting = (
                self.ap_radio_config_result_setting.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if msg is not UNSET:
            field_dict["msg"] = msg
        if ap_radio_config_result_setting is not UNSET:
            field_dict["apRadioConfigResultSetting"] = ap_radio_config_result_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_radio_config_result_settings_vo import (
            ApRadioConfigResultSettingsVO,
        )

        d = dict(src_dict)
        error_code = d.pop("errorCode", UNSET)

        msg = d.pop("msg", UNSET)

        _ap_radio_config_result_setting = d.pop("apRadioConfigResultSetting", UNSET)
        ap_radio_config_result_setting: ApRadioConfigResultSettingsVO | Unset
        if isinstance(_ap_radio_config_result_setting, Unset):
            ap_radio_config_result_setting = UNSET
        else:
            ap_radio_config_result_setting = ApRadioConfigResultSettingsVO.from_dict(
                _ap_radio_config_result_setting
            )

        ap_config_result_radio_setting_vo = cls(
            error_code=error_code,
            msg=msg,
            ap_radio_config_result_setting=ap_radio_config_result_setting,
        )

        ap_config_result_radio_setting_vo.additional_properties = d
        return ap_config_result_radio_setting_vo

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
