from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortTagOpenApiVO")


@_attrs_define
class PortTagOpenApiVO:
    """
    Attributes:
        tag_id (str): Port label ID
        name (str): Port label name should contain 1 to 128 ASCII characters.
        resource (int | Unset): Data Source. Resource should be a value as follows: 0: new created; 1: from template; 2:
            override
    """

    tag_id: str
    name: str
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_id = self.tag_id

        name = self.name

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tagId": tag_id,
                "name": name,
            }
        )
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tag_id = d.pop("tagId")

        name = d.pop("name")

        resource = d.pop("resource", UNSET)

        port_tag_open_api_vo = cls(
            tag_id=tag_id,
            name=name,
            resource=resource,
        )

        port_tag_open_api_vo.additional_properties = d
        return port_tag_open_api_vo

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
