from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherUnitPriceDistributionOpenApiVO")


@_attrs_define
class VoucherUnitPriceDistributionOpenApiVO:
    """
    Attributes:
        unit_price (str | Unset): Price of single voucher. It should be within the range of 1–999999999
        total_amount (str | Unset): Total amount of vouchers
        used_count (int | Unset): Used count of vouchers
        currency (str | Unset): Currency Short Code of voucher. For the values of Currency Short Code, refer to section
            5.4.2 of the Open API Access Guide.
    """

    unit_price: str | Unset = UNSET
    total_amount: str | Unset = UNSET
    used_count: int | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit_price = self.unit_price

        total_amount = self.total_amount

        used_count = self.used_count

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if used_count is not UNSET:
            field_dict["usedCount"] = used_count
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unit_price = d.pop("unitPrice", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        used_count = d.pop("usedCount", UNSET)

        currency = d.pop("currency", UNSET)

        voucher_unit_price_distribution_open_api_vo = cls(
            unit_price=unit_price,
            total_amount=total_amount,
            used_count=used_count,
            currency=currency,
        )

        voucher_unit_price_distribution_open_api_vo.additional_properties = d
        return voucher_unit_price_distribution_open_api_vo

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
