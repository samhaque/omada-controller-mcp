from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgPortGeneralConfigVO")


@_attrs_define
class OsgPortGeneralConfigVO:
    """
    Attributes:
        port (int | Unset):
        tag_set (list[str] | Unset):
        resource (int | Unset):
    """

    port: int | Unset = UNSET
    tag_set: list[str] | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        tag_set: list[str] | Unset = UNSET
        if not isinstance(self.tag_set, Unset):
            tag_set = self.tag_set

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if tag_set is not UNSET:
            field_dict["tagSet"] = tag_set
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        tag_set = cast(list[str], d.pop("tagSet", UNSET))

        resource = d.pop("resource", UNSET)

        osg_port_general_config_vo = cls(
            port=port,
            tag_set=tag_set,
            resource=resource,
        )

        osg_port_general_config_vo.additional_properties = d
        return osg_port_general_config_vo

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
