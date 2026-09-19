from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="BonjourServiceOpenApiVO")


@_attrs_define
class BonjourServiceOpenApiVO:
    """
    Attributes:
        name (str): The name of Bonjour Service should contain 1 to 64 characters.
        service_ids (list[str]): The Service ID list of Bonjour Service. Service ID is a string in "_A._B.local" format,
            where "A" can be lowercase letters/numbers/hyphens (-)/underscore (_), and "B" should be lowercase letters. For
            example: _a1._b.local.Up to 3 entries are allowed for the serviceIds list.
    """

    name: str
    service_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        service_ids = self.service_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "serviceIds": service_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        service_ids = cast(list[str], d.pop("serviceIds"))

        bonjour_service_open_api_vo = cls(
            name=name,
            service_ids=service_ids,
        )

        bonjour_service_open_api_vo.additional_properties = d
        return bonjour_service_open_api_vo

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
