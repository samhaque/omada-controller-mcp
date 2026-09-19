from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainOpenApiVO")


@_attrs_define
class DomainOpenApiVO:
    """Domain info. Handle situations where there are ports, [type] value of 7 is required

    Attributes:
        address (str): Domain address, should be a valid domain address
        port (str | Unset): Domain port, port should be within the range of 0-65535 or empty, e.g. 80,80-100
        description (str | Unset): Domain description, description should contain 1 to 512 characters.
    """

    address: str
    port: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        port = self.port

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("address")

        port = d.pop("port", UNSET)

        description = d.pop("description", UNSET)

        domain_open_api_vo = cls(
            address=address,
            port=port,
            description=description,
        )

        domain_open_api_vo.additional_properties = d
        return domain_open_api_vo

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
