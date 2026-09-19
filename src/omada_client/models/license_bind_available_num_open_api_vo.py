from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseBindAvailableNumOpenApiVO")


@_attrs_define
class LicenseBindAvailableNumOpenApiVO:
    """
    Attributes:
        trial (int | Unset): trial license num
        others (int | Unset): Used license num
        permanent (int | Unset):
        field_1year (int | Unset): 1year license num
        field_2years (int | Unset): 2years license num
        field_3years (int | Unset): 3years license num
        field_4years (int | Unset): 4years license num
        field_5years (int | Unset): 5years license num
        field_7years (int | Unset): 7years license num
        field_1month (int | Unset): 1month license num
    """

    trial: int | Unset = UNSET
    others: int | Unset = UNSET
    permanent: int | Unset = UNSET
    field_1year: int | Unset = UNSET
    field_2years: int | Unset = UNSET
    field_3years: int | Unset = UNSET
    field_4years: int | Unset = UNSET
    field_5years: int | Unset = UNSET
    field_7years: int | Unset = UNSET
    field_1month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trial = self.trial

        others = self.others

        permanent = self.permanent

        field_1year = self.field_1year

        field_2years = self.field_2years

        field_3years = self.field_3years

        field_4years = self.field_4years

        field_5years = self.field_5years

        field_7years = self.field_7years

        field_1month = self.field_1month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trial is not UNSET:
            field_dict["trial"] = trial
        if others is not UNSET:
            field_dict["others"] = others
        if permanent is not UNSET:
            field_dict["permanent"] = permanent
        if field_1year is not UNSET:
            field_dict["1year"] = field_1year
        if field_2years is not UNSET:
            field_dict["2years"] = field_2years
        if field_3years is not UNSET:
            field_dict["3years"] = field_3years
        if field_4years is not UNSET:
            field_dict["4years"] = field_4years
        if field_5years is not UNSET:
            field_dict["5years"] = field_5years
        if field_7years is not UNSET:
            field_dict["7years"] = field_7years
        if field_1month is not UNSET:
            field_dict["1month"] = field_1month

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        trial = d.pop("trial", UNSET)

        others = d.pop("others", UNSET)

        permanent = d.pop("permanent", UNSET)

        field_1year = d.pop("1year", UNSET)

        field_2years = d.pop("2years", UNSET)

        field_3years = d.pop("3years", UNSET)

        field_4years = d.pop("4years", UNSET)

        field_5years = d.pop("5years", UNSET)

        field_7years = d.pop("7years", UNSET)

        field_1month = d.pop("1month", UNSET)

        license_bind_available_num_open_api_vo = cls(
            trial=trial,
            others=others,
            permanent=permanent,
            field_1year=field_1year,
            field_2years=field_2years,
            field_3years=field_3years,
            field_4years=field_4years,
            field_5years=field_5years,
            field_7years=field_7years,
            field_1month=field_1month,
        )

        license_bind_available_num_open_api_vo.additional_properties = d
        return license_bind_available_num_open_api_vo

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
