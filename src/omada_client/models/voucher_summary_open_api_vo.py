from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherSummaryOpenApiVO")


@_attrs_define
class VoucherSummaryOpenApiVO:
    """Summary of all created vouchers, including deleted vouchers

    Attributes:
        count (int | Unset): Count of vouchers
        amount (str | Unset): Amount of single voucher
        duration (int | Unset): Duration of vouchers, unit: minutes
        currency (str | Unset): Currency Short Code of voucher. For the values of Currency Short Code, refer to section
            5.4.2 of the Open API Access Guide.
    """

    count: int | Unset = UNSET
    amount: str | Unset = UNSET
    duration: int | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        amount = self.amount

        duration = self.duration

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if amount is not UNSET:
            field_dict["amount"] = amount
        if duration is not UNSET:
            field_dict["duration"] = duration
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        amount = d.pop("amount", UNSET)

        duration = d.pop("duration", UNSET)

        currency = d.pop("currency", UNSET)

        voucher_summary_open_api_vo = cls(
            count=count,
            amount=amount,
            duration=duration,
            currency=currency,
        )

        voucher_summary_open_api_vo.additional_properties = d
        return voucher_summary_open_api_vo

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
