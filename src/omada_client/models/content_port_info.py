from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentPortInfo")


@_attrs_define
class ContentPortInfo:
    """
    Attributes:
        id (str): Port Uuid.
        ip (bool): Whether to query the port IP.
        usage (bool): Whether to query the port data usage.
        name (str | Unset): Port name.
    """

    id: str
    ip: bool
    usage: bool
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ip = self.ip

        usage = self.usage

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ip": ip,
                "usage": usage,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        ip = d.pop("ip")

        usage = d.pop("usage")

        name = d.pop("name", UNSET)

        content_port_info = cls(
            id=id,
            ip=ip,
            usage=usage,
            name=name,
        )

        content_port_info.additional_properties = d
        return content_port_info

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
