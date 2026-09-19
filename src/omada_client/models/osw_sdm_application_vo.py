from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswSdmApplicationVO")


@_attrs_define
class OswSdmApplicationVO:
    """Application

    Attributes:
        category (int | Unset): It should be a value as follows: 0: ACL&Qos(IPv4); 1:ACL&Qos(IPv6); 3:IP Source Guard;
            4:IPv6 Source Guard.
        num (int | Unset): Maximum number of entries allowed by the feature.
    """

    category: int | Unset = UNSET
    num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        num = self.num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if num is not UNSET:
            field_dict["num"] = num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        num = d.pop("num", UNSET)

        osw_sdm_application_vo = cls(
            category=category,
            num=num,
        )

        osw_sdm_application_vo.additional_properties = d
        return osw_sdm_application_vo

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
