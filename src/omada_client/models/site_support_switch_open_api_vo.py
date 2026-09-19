from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteSupportSwitchOpenApiVO")


@_attrs_define
class SiteSupportSwitchOpenApiVO:
    """
    Attributes:
        support_es (bool | Unset): Whether the site supports adopting Agile Series Switches
        support_l2 (bool | Unset): Whether the site supports adopting Non-Agile Series Switches
    """

    support_es: bool | Unset = UNSET
    support_l2: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_es = self.support_es

        support_l2 = self.support_l2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support_es is not UNSET:
            field_dict["supportES"] = support_es
        if support_l2 is not UNSET:
            field_dict["supportL2"] = support_l2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        support_es = d.pop("supportES", UNSET)

        support_l2 = d.pop("supportL2", UNSET)

        site_support_switch_open_api_vo = cls(
            support_es=support_es,
            support_l2=support_l2,
        )

        site_support_switch_open_api_vo.additional_properties = d
        return site_support_switch_open_api_vo

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
