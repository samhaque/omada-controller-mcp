from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientAggHealthDTO")


@_attrs_define
class ClientAggHealthDTO:
    """Client Health

    Attributes:
        good (int | Unset): The Quantity of Good Clients
        fair (int | Unset): The Quantity of Fair Clients
        poor (int | Unset): The Quantity of Poor Clients
        no_data (int | Unset): The Quantity of noData Clients
    """

    good: int | Unset = UNSET
    fair: int | Unset = UNSET
    poor: int | Unset = UNSET
    no_data: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        good = self.good

        fair = self.fair

        poor = self.poor

        no_data = self.no_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if good is not UNSET:
            field_dict["good"] = good
        if fair is not UNSET:
            field_dict["fair"] = fair
        if poor is not UNSET:
            field_dict["poor"] = poor
        if no_data is not UNSET:
            field_dict["noData"] = no_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        good = d.pop("good", UNSET)

        fair = d.pop("fair", UNSET)

        poor = d.pop("poor", UNSET)

        no_data = d.pop("noData", UNSET)

        client_agg_health_dto = cls(
            good=good,
            fair=fair,
            poor=poor,
            no_data=no_data,
        )

        client_agg_health_dto.additional_properties = d
        return client_agg_health_dto

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
