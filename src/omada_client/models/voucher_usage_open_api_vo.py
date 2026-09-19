from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherUsageOpenApiVO")


@_attrs_define
class VoucherUsageOpenApiVO:
    """Data points of vouchers

    Attributes:
        amount (str | Unset): Amount of vouchers
        currency (str | Unset): Currency Short Code of voucher. For the values of Currency Short Code, refer to section
            5.4.2 of the Open API Access Guide.
        count (int | Unset): Count of vouchers
        time_interval (int | Unset): Time interval of each data point
        time (int | Unset): Timestamp of the data point, unit: MS
    """

    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    count: int | Unset = UNSET
    time_interval: int | Unset = UNSET
    time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency

        count = self.count

        time_interval = self.time_interval

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if count is not UNSET:
            field_dict["count"] = count
        if time_interval is not UNSET:
            field_dict["timeInterval"] = time_interval
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        count = d.pop("count", UNSET)

        time_interval = d.pop("timeInterval", UNSET)

        time = d.pop("time", UNSET)

        voucher_usage_open_api_vo = cls(
            amount=amount,
            currency=currency,
            count=count,
            time_interval=time_interval,
            time=time,
        )

        voucher_usage_open_api_vo.additional_properties = d
        return voucher_usage_open_api_vo

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
