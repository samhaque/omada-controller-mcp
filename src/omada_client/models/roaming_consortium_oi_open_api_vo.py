from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoamingConsortiumOiOpenApiVO")


@_attrs_define
class RoamingConsortiumOiOpenApiVO:
    """Roaming Consortium Oi list, enter the 802.11u roaming organization identifiers.<br />Note: Up to 3 entries are
    allowed for the Roaming Consortium Oi list.

        Attributes:
            value (str | Unset): Roaming Consortium Operator Identifier.<br />Note: Roaming Consortium Oi should conform to
                XX-XX-XX or XX-XX-XX-XX-XX format(Hexadecimal).
    """

    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        roaming_consortium_oi_open_api_vo = cls(
            value=value,
        )

        roaming_consortium_oi_open_api_vo.additional_properties = d
        return roaming_consortium_oi_open_api_vo

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
