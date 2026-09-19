from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelephoneNumberAdvancedSettingApOpenApiVO")


@_attrs_define
class TelephoneNumberAdvancedSettingApOpenApiVO:
    """Advanced settings.

    Attributes:
        locale (int | Unset): The country code of telephone number.
        dscp_for_sip (int | Unset): The dscp For Sip of telephone number.
        dscp_for_rtp (int | Unset): The dscp For Rtp of telephone number.
        dtmf_relay_setting (int | Unset): The dtmf relay setting of telephone number.
        expiration_time (int | Unset): The expiration time of telephone number.
        retry_interval (int | Unset): The retry interval of telephone number.
        t_38_support (bool | Unset): Whether to enable t38 Support.
        end_with_number_sign (bool | Unset): Whether the telephone number setting end with number sign.
    """

    locale: int | Unset = UNSET
    dscp_for_sip: int | Unset = UNSET
    dscp_for_rtp: int | Unset = UNSET
    dtmf_relay_setting: int | Unset = UNSET
    expiration_time: int | Unset = UNSET
    retry_interval: int | Unset = UNSET
    t_38_support: bool | Unset = UNSET
    end_with_number_sign: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        dscp_for_sip = self.dscp_for_sip

        dscp_for_rtp = self.dscp_for_rtp

        dtmf_relay_setting = self.dtmf_relay_setting

        expiration_time = self.expiration_time

        retry_interval = self.retry_interval

        t_38_support = self.t_38_support

        end_with_number_sign = self.end_with_number_sign

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if dscp_for_sip is not UNSET:
            field_dict["dscpForSip"] = dscp_for_sip
        if dscp_for_rtp is not UNSET:
            field_dict["dscpForRtp"] = dscp_for_rtp
        if dtmf_relay_setting is not UNSET:
            field_dict["dtmfRelaySetting"] = dtmf_relay_setting
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if retry_interval is not UNSET:
            field_dict["retryInterval"] = retry_interval
        if t_38_support is not UNSET:
            field_dict["t38Support"] = t_38_support
        if end_with_number_sign is not UNSET:
            field_dict["endWithNumberSign"] = end_with_number_sign

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

        dscp_for_sip = d.pop("dscpForSip", UNSET)

        dscp_for_rtp = d.pop("dscpForRtp", UNSET)

        dtmf_relay_setting = d.pop("dtmfRelaySetting", UNSET)

        expiration_time = d.pop("expirationTime", UNSET)

        retry_interval = d.pop("retryInterval", UNSET)

        t_38_support = d.pop("t38Support", UNSET)

        end_with_number_sign = d.pop("endWithNumberSign", UNSET)

        telephone_number_advanced_setting_ap_open_api_vo = cls(
            locale=locale,
            dscp_for_sip=dscp_for_sip,
            dscp_for_rtp=dscp_for_rtp,
            dtmf_relay_setting=dtmf_relay_setting,
            expiration_time=expiration_time,
            retry_interval=retry_interval,
            t_38_support=t_38_support,
            end_with_number_sign=end_with_number_sign,
        )

        telephone_number_advanced_setting_ap_open_api_vo.additional_properties = d
        return telephone_number_advanced_setting_ap_open_api_vo

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
