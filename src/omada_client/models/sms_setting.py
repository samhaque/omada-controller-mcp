from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_timeout_setting import AuthTimeoutSetting


T = TypeVar("T", bound="SmsSetting")


@_attrs_define
class SmsSetting:
    """Sms Portal Setting.

    Attributes:
        sid (str): Twilio SID
        auth_token (str): Twilio auth token
        phone_num (str): Twilio phone number. String value, should contain at least 6 digits such as "+123456".
        user_limit_enable (bool): Whether to control the limit of authentication for the same phone number.
        auth_timeout (AuthTimeoutSetting): Auth Timeout Setting.
        user_limit (int | Unset): User limit with the same phone number, should be within the range of 1–10. Required
            when parameter [userLimitEnable] is true.
        country_code (str | Unset): Preset Contry code. String value such as "+86".
    """

    sid: str
    auth_token: str
    phone_num: str
    user_limit_enable: bool
    auth_timeout: AuthTimeoutSetting
    user_limit: int | Unset = UNSET
    country_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sid = self.sid

        auth_token = self.auth_token

        phone_num = self.phone_num

        user_limit_enable = self.user_limit_enable

        auth_timeout = self.auth_timeout.to_dict()

        user_limit = self.user_limit

        country_code = self.country_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sid": sid,
                "authToken": auth_token,
                "phoneNum": phone_num,
                "userLimitEnable": user_limit_enable,
                "authTimeout": auth_timeout,
            }
        )
        if user_limit is not UNSET:
            field_dict["userLimit"] = user_limit
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_timeout_setting import AuthTimeoutSetting

        d = dict(src_dict)
        sid = d.pop("sid")

        auth_token = d.pop("authToken")

        phone_num = d.pop("phoneNum")

        user_limit_enable = d.pop("userLimitEnable")

        auth_timeout = AuthTimeoutSetting.from_dict(d.pop("authTimeout"))

        user_limit = d.pop("userLimit", UNSET)

        country_code = d.pop("countryCode", UNSET)

        sms_setting = cls(
            sid=sid,
            auth_token=auth_token,
            phone_num=phone_num,
            user_limit_enable=user_limit_enable,
            auth_timeout=auth_timeout,
            user_limit=user_limit,
            country_code=country_code,
        )

        sms_setting.additional_properties = d
        return sms_setting

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
