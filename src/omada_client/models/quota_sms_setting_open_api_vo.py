from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuotaSmsSettingOpenApiVO")


@_attrs_define
class QuotaSmsSettingOpenApiVO:
    """SMS quota setting.

    Attributes:
        type_ (int): Billing cycle type should be a value as follows: 0:total; 1:monthly.
        limit (bool): Quota limit is enabled/disabled.
        used (int | Unset): The amount of SMS in current billing cycle.
        start_date (int | Unset): Start date of monthly billing cycle type, valid date should be within the range of
            1–31.
        credit (int | Unset): The amount of data allowance in current billing cycle, valid date should be within the
            range of 0–100000.
        alert (bool | Unset): SMS alert for usage is enabled/disabled.
        usage (int | Unset): SMS alert for usage when reach percentage of allowance, valid date should be within the
            range of 0–100.
        country_code (str | Unset): Country code should contain 2 characters. Country code must be entered when entering
            the calling code. For the values of Country code, refer to section 5.4.1 of the Open API Access Guide.
        calling_code (str | Unset): Calling code should contain 2 to 5 characters. Calling code must be entered when
            entering the country code. For the values of Calling code, refer to section 5.4.1 of the Open API Access Guide.
        phone (str | Unset): The phone number to receive SMS alerts.
    """

    type_: int
    limit: bool
    used: int | Unset = UNSET
    start_date: int | Unset = UNSET
    credit: int | Unset = UNSET
    alert: bool | Unset = UNSET
    usage: int | Unset = UNSET
    country_code: str | Unset = UNSET
    calling_code: str | Unset = UNSET
    phone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        limit = self.limit

        used = self.used

        start_date = self.start_date

        credit = self.credit

        alert = self.alert

        usage = self.usage

        country_code = self.country_code

        calling_code = self.calling_code

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "limit": limit,
            }
        )
        if used is not UNSET:
            field_dict["used"] = used
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if credit is not UNSET:
            field_dict["credit"] = credit
        if alert is not UNSET:
            field_dict["alert"] = alert
        if usage is not UNSET:
            field_dict["usage"] = usage
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if calling_code is not UNSET:
            field_dict["callingCode"] = calling_code
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        limit = d.pop("limit")

        used = d.pop("used", UNSET)

        start_date = d.pop("startDate", UNSET)

        credit = d.pop("credit", UNSET)

        alert = d.pop("alert", UNSET)

        usage = d.pop("usage", UNSET)

        country_code = d.pop("countryCode", UNSET)

        calling_code = d.pop("callingCode", UNSET)

        phone = d.pop("phone", UNSET)

        quota_sms_setting_open_api_vo = cls(
            type_=type_,
            limit=limit,
            used=used,
            start_date=start_date,
            credit=credit,
            alert=alert,
            usage=usage,
            country_code=country_code,
            calling_code=calling_code,
            phone=phone,
        )

        quota_sms_setting_open_api_vo.additional_properties = d
        return quota_sms_setting_open_api_vo

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
