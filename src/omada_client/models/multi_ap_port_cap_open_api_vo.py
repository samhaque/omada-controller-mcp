from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="MultiApPortCapOpenApiVO")


@_attrs_define
class MultiApPortCapOpenApiVO:
    """
    Attributes:
        ap_mac_list (list[str]): AP mac list
    """

    ap_mac_list: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ap_mac_list = self.ap_mac_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apMacList": ap_mac_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ap_mac_list = cast(list[str], d.pop("apMacList"))

        multi_ap_port_cap_open_api_vo = cls(
            ap_mac_list=ap_mac_list,
        )

        multi_ap_port_cap_open_api_vo.additional_properties = d
        return multi_ap_port_cap_open_api_vo

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
