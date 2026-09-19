from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ModifyOswVrfOpenApiVO")


@_attrs_define
class ModifyOswVrfOpenApiVO:
    """
    Attributes:
        ipv_6_enable (bool): Whether to enable ipv6
    """

    ipv_6_enable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_6_enable = self.ipv_6_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv6Enable": ipv_6_enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ipv_6_enable = d.pop("ipv6Enable")

        modify_osw_vrf_open_api_vo = cls(
            ipv_6_enable=ipv_6_enable,
        )

        modify_osw_vrf_open_api_vo.additional_properties = d
        return modify_osw_vrf_open_api_vo

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
