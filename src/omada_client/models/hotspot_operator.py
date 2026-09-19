from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="HotspotOperator")


@_attrs_define
class HotspotOperator:
    """
    Attributes:
        name (str): Operator name should contain 1 to 128 ASCII characters.
        password (str): Operator password should contain 1 to 128 ASCII characters.
        selected_sites (list[str]): Selected site ID list should contain at least one site for each operator.
        note (str | Unset): Operator note should contain 1 to 256 ASCII characters.
        operator_role_type (int | Unset): Operator role type should be a value as follows: 0: Administrator; 1: Viewer.
        last_site (str | Unset): Last Site ID
    """

    name: str
    password: str
    selected_sites: list[str]
    note: str | Unset = UNSET
    operator_role_type: int | Unset = UNSET
    last_site: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        password = self.password

        selected_sites = self.selected_sites

        note = self.note

        operator_role_type = self.operator_role_type

        last_site = self.last_site

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "password": password,
                "selectedSites": selected_sites,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if operator_role_type is not UNSET:
            field_dict["operatorRoleType"] = operator_role_type
        if last_site is not UNSET:
            field_dict["lastSite"] = last_site

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        password = d.pop("password")

        selected_sites = cast(list[str], d.pop("selectedSites"))

        note = d.pop("note", UNSET)

        operator_role_type = d.pop("operatorRoleType", UNSET)

        last_site = d.pop("lastSite", UNSET)

        hotspot_operator = cls(
            name=name,
            password=password,
            selected_sites=selected_sites,
            note=note,
            operator_role_type=operator_role_type,
            last_site=last_site,
        )

        hotspot_operator.additional_properties = d
        return hotspot_operator

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
