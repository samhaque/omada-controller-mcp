from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswNormalPortListVO")


@_attrs_define
class OswNormalPortListVO:
    """List of Switch MAC and ports.

    Attributes:
        mac (str | Unset): Switch MAC Address
        port_list (list[int] | Unset): Switch port list.
    """

    mac: str | Unset = UNSET
    port_list: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        port_list: list[int] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if port_list is not UNSET:
            field_dict["portList"] = port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        port_list = cast(list[int], d.pop("portList", UNSET))

        osw_normal_port_list_vo = cls(
            mac=mac,
            port_list=port_list,
        )

        osw_normal_port_list_vo.additional_properties = d
        return osw_normal_port_list_vo

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
