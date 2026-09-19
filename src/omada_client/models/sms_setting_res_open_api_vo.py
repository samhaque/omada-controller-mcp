from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO


T = TypeVar("T", bound="SmsSettingResOpenApiVO")


@_attrs_define
class SmsSettingResOpenApiVO:
    """Hotspot: SMS Portal setting, required when [authType] is 11 and hotspot [enabledTypes] contains 6.

    Attributes:
        sid (str | Unset): Twilio SID
        auth_token (str | Unset): Twilio auth token
        phone_num (str | Unset): Twilio phone number. String value, should contain at least 6 digits such as "+123456".
        max_verification_code_enable (bool | Unset): Whether to control the limit of authentication for the same phone
            number.
        max_verification_code_times (int | Unset): User limit with the same phone number, should be within the range of
            1–10. Required when parameter [maxVerificationCodeEnable] is true.
        auth_timeout (AuthTimeOpenApiVO | Unset): Authentication timeout time. Display when enabled, otherwise no
            display.
        country_code (str | Unset): Preset Contry code. String value such as "+86".
    """

    sid: str | Unset = UNSET
    auth_token: str | Unset = UNSET
    phone_num: str | Unset = UNSET
    max_verification_code_enable: bool | Unset = UNSET
    max_verification_code_times: int | Unset = UNSET
    auth_timeout: AuthTimeOpenApiVO | Unset = UNSET
    country_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sid = self.sid

        auth_token = self.auth_token

        phone_num = self.phone_num

        max_verification_code_enable = self.max_verification_code_enable

        max_verification_code_times = self.max_verification_code_times

        auth_timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_timeout, Unset):
            auth_timeout = self.auth_timeout.to_dict()

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sid is not UNSET:
            field_dict["sid"] = sid
        if auth_token is not UNSET:
            field_dict["authToken"] = auth_token
        if phone_num is not UNSET:
            field_dict["phoneNum"] = phone_num
        if max_verification_code_enable is not UNSET:
            field_dict["maxVerificationCodeEnable"] = max_verification_code_enable
        if max_verification_code_times is not UNSET:
            field_dict["maxVerificationCodeTimes"] = max_verification_code_times
        if auth_timeout is not UNSET:
            field_dict["authTimeout"] = auth_timeout
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO

        d = dict(src_dict)
        sid = d.pop("sid", UNSET)

        auth_token = d.pop("authToken", UNSET)

        phone_num = d.pop("phoneNum", UNSET)

        max_verification_code_enable = d.pop("maxVerificationCodeEnable", UNSET)

        max_verification_code_times = d.pop("maxVerificationCodeTimes", UNSET)

        _auth_timeout = d.pop("authTimeout", UNSET)
        auth_timeout: AuthTimeOpenApiVO | Unset
        if isinstance(_auth_timeout, Unset):
            auth_timeout = UNSET
        else:
            auth_timeout = AuthTimeOpenApiVO.from_dict(_auth_timeout)

        country_code = d.pop("countryCode", UNSET)

        sms_setting_res_open_api_vo = cls(
            sid=sid,
            auth_token=auth_token,
            phone_num=phone_num,
            max_verification_code_enable=max_verification_code_enable,
            max_verification_code_times=max_verification_code_times,
            auth_timeout=auth_timeout,
            country_code=country_code,
        )

        sms_setting_res_open_api_vo.additional_properties = d
        return sms_setting_res_open_api_vo

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
