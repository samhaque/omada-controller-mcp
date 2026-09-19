from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BonjourServiceDetailOpenApiVO")


@_attrs_define
class BonjourServiceDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): The id of Bonjour Service.
        name (str | Unset): The name of Bonjour Service should contain 1 to 64 characters.
        service_ids (list[str] | Unset): The Service ID list of Bonjour Service. Service ID is a string in "_A._B.local"
            format, where "A" can be lowercase letters/numbers/hyphens (-)/underscore (_), and "B" should be lowercase
            letters. For example: _a1._b.local.Up to 3 entries are allowed for the serviceIds list.
        default_profile (bool | Unset): Indicating that this profile is default which can not be modified.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    service_ids: list[str] | Unset = UNSET
    default_profile: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        service_ids: list[str] | Unset = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        default_profile = self.default_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if service_ids is not UNSET:
            field_dict["serviceIds"] = service_ids
        if default_profile is not UNSET:
            field_dict["defaultProfile"] = default_profile

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        service_ids = cast(list[str], d.pop("serviceIds", UNSET))

        default_profile = d.pop("defaultProfile", UNSET)

        bonjour_service_detail_open_api_vo = cls(
            id=id,
            name=name,
            service_ids=service_ids,
            default_profile=default_profile,
        )

        bonjour_service_detail_open_api_vo.additional_properties = d
        return bonjour_service_detail_open_api_vo

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
