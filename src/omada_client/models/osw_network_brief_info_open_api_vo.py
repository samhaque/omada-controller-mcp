from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswNetworkBriefInfoOpenApiVO")


@_attrs_define
class OswNetworkBriefInfoOpenApiVO:
    """OswNetworkBriefInfoOpenApiVO

    Attributes:
        id (str | Unset): Network's ID
        name (str | Unset): Network's name
        vlan (int | Unset): VLAN ID
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        vlan = d.pop("vlan", UNSET)

        osw_network_brief_info_open_api_vo = cls(
            id=id,
            name=name,
            vlan=vlan,
        )

        osw_network_brief_info_open_api_vo.additional_properties = d
        return osw_network_brief_info_open_api_vo

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
