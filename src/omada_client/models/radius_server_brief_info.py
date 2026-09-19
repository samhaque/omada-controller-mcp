from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusServerBriefInfo")


@_attrs_define
class RadiusServerBriefInfo:
    """
    Attributes:
        id (str): radius server id.
        name (str): radius server name.
        over_num_limit (bool | Unset): Is the number of authentication/accounting Servers greater than 2.
        built_in_server (bool | Unset): Is this RADIUS server a built-in server
    """

    id: str
    name: str
    over_num_limit: bool | Unset = UNSET
    built_in_server: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        over_num_limit = self.over_num_limit

        built_in_server = self.built_in_server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if over_num_limit is not UNSET:
            field_dict["overNumLimit"] = over_num_limit
        if built_in_server is not UNSET:
            field_dict["builtInServer"] = built_in_server

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        over_num_limit = d.pop("overNumLimit", UNSET)

        built_in_server = d.pop("builtInServer", UNSET)

        radius_server_brief_info = cls(
            id=id,
            name=name,
            over_num_limit=over_num_limit,
            built_in_server=built_in_server,
        )

        radius_server_brief_info.additional_properties = d
        return radius_server_brief_info

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
