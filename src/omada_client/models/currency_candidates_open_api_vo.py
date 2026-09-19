from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrencyCandidatesOpenApiVO")


@_attrs_define
class CurrencyCandidatesOpenApiVO:
    """
    Attributes:
        currency_list (list[str] | Unset): All currency Short Code list. For the values of Currency Short Code, refer to
            section 5.4.2 of the Open API Access Guide.
        selected_currency (str | Unset): The currency selected for the site
    """

    currency_list: list[str] | Unset = UNSET
    selected_currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_list: list[str] | Unset = UNSET
        if not isinstance(self.currency_list, Unset):
            currency_list = self.currency_list

        selected_currency = self.selected_currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_list is not UNSET:
            field_dict["currencyList"] = currency_list
        if selected_currency is not UNSET:
            field_dict["selectedCurrency"] = selected_currency

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        currency_list = cast(list[str], d.pop("currencyList", UNSET))

        selected_currency = d.pop("selectedCurrency", UNSET)

        currency_candidates_open_api_vo = cls(
            currency_list=currency_list,
            selected_currency=selected_currency,
        )

        currency_candidates_open_api_vo.additional_properties = d
        return currency_candidates_open_api_vo

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
