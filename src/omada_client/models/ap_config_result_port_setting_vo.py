from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_port_config_result_settings_vo import ApPortConfigResultSettingsVO


T = TypeVar("T", bound="ApConfigResultPortSettingVO")


@_attrs_define
class ApConfigResultPortSettingVO:
    """port setting config result list

    Attributes:
        error_code (int | Unset): error code.
        msg (str | Unset): error msg
        lan_port (str | Unset): lanPort
        ap_port_config_result_settings (ApPortConfigResultSettingsVO | Unset): ap port config result detail setting.
    """

    error_code: int | Unset = UNSET
    msg: str | Unset = UNSET
    lan_port: str | Unset = UNSET
    ap_port_config_result_settings: ApPortConfigResultSettingsVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_code = self.error_code

        msg = self.msg

        lan_port = self.lan_port

        ap_port_config_result_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ap_port_config_result_settings, Unset):
            ap_port_config_result_settings = (
                self.ap_port_config_result_settings.to_dict()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if msg is not UNSET:
            field_dict["msg"] = msg
        if lan_port is not UNSET:
            field_dict["lanPort"] = lan_port
        if ap_port_config_result_settings is not UNSET:
            field_dict["apPortConfigResultSettings"] = ap_port_config_result_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_port_config_result_settings_vo import (
            ApPortConfigResultSettingsVO,
        )

        d = dict(src_dict)
        error_code = d.pop("errorCode", UNSET)

        msg = d.pop("msg", UNSET)

        lan_port = d.pop("lanPort", UNSET)

        _ap_port_config_result_settings = d.pop("apPortConfigResultSettings", UNSET)
        ap_port_config_result_settings: ApPortConfigResultSettingsVO | Unset
        if isinstance(_ap_port_config_result_settings, Unset):
            ap_port_config_result_settings = UNSET
        else:
            ap_port_config_result_settings = ApPortConfigResultSettingsVO.from_dict(
                _ap_port_config_result_settings
            )

        ap_config_result_port_setting_vo = cls(
            error_code=error_code,
            msg=msg,
            lan_port=lan_port,
            ap_port_config_result_settings=ap_port_config_result_settings,
        )

        ap_config_result_port_setting_vo.additional_properties = d
        return ap_config_result_port_setting_vo

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
