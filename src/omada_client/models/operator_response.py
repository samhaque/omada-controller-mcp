from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_info_open_api_vo import SiteInfoOpenApiVO


T = TypeVar("T", bound="OperatorResponse")


@_attrs_define
class OperatorResponse:
    """
    Attributes:
        name (str): Operator name should contain 1 to 128 ASCII characters.
        password (str): Operator password should contain 1 to 128 ASCII characters.
        selected_sites (list[str]): Selected site ID list should contain at least one site for each operator.
        id (str | Unset): Operator ID
        note (str | Unset): Operator note should contain 1 to 256 ASCII characters.
        operator_role_type (int | Unset): Operator role type should be a value as follows: 0: Administrator; 1: Viewer.
        sites (list[SiteInfoOpenApiVO] | Unset): Site ID List
    """

    name: str
    password: str
    selected_sites: list[str]
    id: str | Unset = UNSET
    note: str | Unset = UNSET
    operator_role_type: int | Unset = UNSET
    sites: list[SiteInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        password = self.password

        selected_sites = self.selected_sites

        id = self.id

        note = self.note

        operator_role_type = self.operator_role_type

        sites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "password": password,
                "selectedSites": selected_sites,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if operator_role_type is not UNSET:
            field_dict["operatorRoleType"] = operator_role_type
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_info_open_api_vo import SiteInfoOpenApiVO

        d = dict(src_dict)
        name = d.pop("name")

        password = d.pop("password")

        selected_sites = cast(list[str], d.pop("selectedSites"))

        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        operator_role_type = d.pop("operatorRoleType", UNSET)

        _sites = d.pop("sites", UNSET)
        sites: list[SiteInfoOpenApiVO] | Unset = UNSET
        if _sites is not UNSET:
            sites = []
            for sites_item_data in _sites:
                sites_item = SiteInfoOpenApiVO.from_dict(sites_item_data)

                sites.append(sites_item)

        operator_response = cls(
            name=name,
            password=password,
            selected_sites=selected_sites,
            id=id,
            note=note,
            operator_role_type=operator_role_type,
            sites=sites,
        )

        operator_response.additional_properties = d
        return operator_response

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
