from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPv6SubnetsOpenApiVO")


@_attrs_define
class IPv6SubnetsOpenApiVO:
    """IPv6 subnet info list. [type] value of 3 or 4 is required

    Attributes:
        ip (str): IPv6 address, should be a valid IPv6 format
        prefix (int): IPv6 prefix, prefix should be within the range of 1-128
        description (str | Unset): IPv6 description, description should contain 1 to 512 characters.
    """

    ip: str
    prefix: int
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip = self.ip

        prefix = self.prefix

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip": ip,
                "prefix": prefix,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ip = d.pop("ip")

        prefix = d.pop("prefix")

        description = d.pop("description", UNSET)

        i_pv_6_subnets_open_api_vo = cls(
            ip=ip,
            prefix=prefix,
            description=description,
        )

        i_pv_6_subnets_open_api_vo.additional_properties = d
        return i_pv_6_subnets_open_api_vo

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
